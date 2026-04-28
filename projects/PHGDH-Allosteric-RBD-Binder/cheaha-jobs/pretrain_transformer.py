#!/usr/bin/env python
"""Round 4: SELFIES + small transformer (causal LM) pretrain on bioactives.

Replaces the iter-2 char-LSTM with:
- SELFIES tokenizer (every sampled string is a valid molecule by construction)
- Decoder-only transformer (~20M params: 8 layers, 8 heads, 512 dim, 1024 ffn)
- Same data: ChEMBL bioactives (1.09M from iter 2; PubChem-BioAssay augmentation = future work)

Usage:
  pretrain_transformer.py \
    --data /local/$USER/$SLURM_JOB_ID/bioactives.smi \
    --out runs/<jobid> \
    --epochs 10 --batch 128 --max-len 128 \
    --d-model 512 --n-heads 8 --n-layers 8 --ffn-dim 1024
"""
from __future__ import annotations
import argparse, csv, json, math, os, random, sys, time
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

PAD, START, END = "[PAD]", "[BOS]", "[EOS]"


def load_smiles(path: Path, limit: int = 0):
    out = []
    with path.open() as f:
        for line in f:
            s = line.strip().split("\t")[0]
            if not s or s.startswith("#"):
                continue
            out.append(s)
            if limit and len(out) >= limit:
                break
    return out


def smiles_to_selfies_tokens(smiles_list):
    """Convert SMILES → SELFIES tokens. Returns (tokenized_list, vocab_set)."""
    import selfies as sf
    tokens = []
    vocab = set()
    n_failed = 0
    for s in smiles_list:
        try:
            sel = sf.encoder(s)
            toks = list(sf.split_selfies(sel))
            if toks:
                tokens.append(toks)
                vocab.update(toks)
            else:
                n_failed += 1
        except Exception:
            n_failed += 1
    return tokens, vocab, n_failed


class SELFIESDataset(Dataset):
    def __init__(self, tokens_list, tok2i: dict, max_len: int):
        self.tokens_list = tokens_list
        self.tok2i = tok2i
        self.max_len = max_len
        self.pad = tok2i[PAD]
        self.bos = tok2i[START]
        self.eos = tok2i[END]

    def __len__(self):
        return len(self.tokens_list)

    def __getitem__(self, i):
        toks = self.tokens_list[i]
        ids = [self.bos] + [self.tok2i.get(t, self.pad) for t in toks] + [self.eos]
        ids = ids[: self.max_len]
        ids = ids + [self.pad] * (self.max_len - len(ids))
        ids = torch.tensor(ids, dtype=torch.long)
        return ids[:-1], ids[1:]


class SmallTransformer(nn.Module):
    def __init__(self, vocab: int, d_model: int, n_heads: int, n_layers: int, ffn_dim: int, max_len: int, dropout: float = 0.1):
        super().__init__()
        self.tok_embed = nn.Embedding(vocab, d_model, padding_idx=0)
        self.pos_embed = nn.Embedding(max_len, d_model)
        layer = nn.TransformerEncoderLayer(
            d_model=d_model, nhead=n_heads, dim_feedforward=ffn_dim,
            dropout=dropout, activation="gelu", batch_first=True, norm_first=True,
        )
        self.blocks = nn.TransformerEncoder(layer, num_layers=n_layers)
        self.norm = nn.LayerNorm(d_model)
        self.head = nn.Linear(d_model, vocab, bias=False)
        self.head.weight = self.tok_embed.weight  # tied embeddings
        self.max_len = max_len

    def forward(self, x):
        B, T = x.shape
        pos = torch.arange(T, device=x.device).unsqueeze(0).expand(B, -1)
        h = self.tok_embed(x) + self.pos_embed(pos)
        # causal mask
        mask = torch.triu(torch.ones(T, T, device=x.device, dtype=torch.bool), diagonal=1)
        h = self.blocks(h, mask=mask, is_causal=True)
        h = self.norm(h)
        return self.head(h)


def warmup_cosine_lr(step, total, base, warmup_frac=0.05):
    warm = max(1, int(total * warmup_frac))
    if step < warm:
        return base * step / warm
    rem = (step - warm) / max(1, total - warm)
    return 0.5 * base * (1 + math.cos(math.pi * rem))


def run_epoch(model, loader, loss_fn, optim, device, train, sched_state=None):
    model.train(train)
    total_loss, total_tok = 0.0, 0
    for x, y in loader:
        x, y = x.to(device, non_blocking=True), y.to(device, non_blocking=True)
        with torch.set_grad_enabled(train):
            logits = model(x)
            loss = loss_fn(logits.reshape(-1, logits.size(-1)), y.reshape(-1))
            mask = (y != 0).float()
            tok = mask.sum().item()
            if train:
                optim.zero_grad(set_to_none=True)
                loss.backward()
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                optim.step()
                if sched_state is not None:
                    sched_state["step"] += 1
                    new_lr = warmup_cosine_lr(sched_state["step"], sched_state["total"], sched_state["base"])
                    for pg in optim.param_groups:
                        pg["lr"] = new_lr
        total_loss += loss.item() * tok
        total_tok += tok
    return total_loss / max(total_tok, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--epochs", type=int, default=10)
    ap.add_argument("--batch", type=int, default=128)
    ap.add_argument("--max-len", type=int, default=128)
    ap.add_argument("--d-model", type=int, default=512)
    ap.add_argument("--n-heads", type=int, default=8)
    ap.add_argument("--n-layers", type=int, default=8)
    ap.add_argument("--ffn-dim", type=int, default=1024)
    ap.add_argument("--dropout", type=float, default=0.1)
    ap.add_argument("--lr", type=float, default=3e-4)
    ap.add_argument("--weight-decay", type=float, default=0.01)
    ap.add_argument("--val-frac", type=float, default=0.02)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    random.seed(args.seed); torch.manual_seed(args.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[trans] device={device}", flush=True)
    if device == "cuda":
        print(f"[trans] gpu={torch.cuda.get_device_name(0)}", flush=True)

    print(f"[trans] loading SMILES from {args.data}", flush=True)
    smiles = load_smiles(args.data, args.limit)
    print(f"[trans] loaded {len(smiles)} SMILES", flush=True)

    print(f"[trans] tokenizing to SELFIES", flush=True)
    t0 = time.time()
    tokens, sel_vocab, n_failed = smiles_to_selfies_tokens(smiles)
    print(f"[trans] SELFIES: {len(tokens)} ok, {n_failed} failed; vocab size {len(sel_vocab)} ({time.time()-t0:.1f}s)", flush=True)

    vocab = [PAD, START, END] + sorted(sel_vocab)
    tok2i = {t: i for i, t in enumerate(vocab)}
    i2tok = {i: t for t, i in tok2i.items()}
    (args.out / "vocab.json").write_text(json.dumps({"vocab": vocab, "max_len": args.max_len}))
    print(f"[trans] total vocab {len(vocab)} -> {args.out/'vocab.json'}", flush=True)

    random.shuffle(tokens)
    n_val = max(1, int(len(tokens) * args.val_frac))
    val_toks, train_toks = tokens[:n_val], tokens[n_val:]
    print(f"[trans] n_train={len(train_toks)} n_val={len(val_toks)}", flush=True)

    config = {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()}
    config["vocab_size"] = len(vocab)
    (args.out / "config.json").write_text(json.dumps(config, indent=2))

    ds_train = SELFIESDataset(train_toks, tok2i, args.max_len)
    ds_val = SELFIESDataset(val_toks, tok2i, args.max_len)
    dl_train = DataLoader(ds_train, batch_size=args.batch, shuffle=True,
                          num_workers=args.workers, pin_memory=(device == "cuda"),
                          persistent_workers=(args.workers > 0))
    dl_val = DataLoader(ds_val, batch_size=args.batch, shuffle=False,
                        num_workers=args.workers, pin_memory=(device == "cuda"),
                        persistent_workers=(args.workers > 0))

    model = SmallTransformer(
        len(vocab), args.d_model, args.n_heads, args.n_layers, args.ffn_dim,
        max_len=args.max_len, dropout=args.dropout,
    ).to(device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"[trans] params={n_params:,}", flush=True)

    optim = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay,
                              betas=(0.9, 0.95))
    loss_fn = nn.CrossEntropyLoss(ignore_index=0)
    total_steps = max(1, len(dl_train) * args.epochs)
    sched = {"step": 0, "total": total_steps, "base": args.lr}

    start_ep = 0; best_val = float("inf")
    last = args.out / "last.pt"
    if args.resume and last.exists():
        ck = torch.load(last, map_location=device)
        model.load_state_dict(ck["model"])
        optim.load_state_dict(ck["optim"])
        start_ep = ck["epoch"] + 1
        best_val = ck.get("best_val", best_val)
        sched["step"] = ck.get("step", 0)
        print(f"[trans] resumed ep={start_ep} best_val={best_val:.4f}", flush=True)

    csv_path = args.out / "loss.csv"
    write_hdr = not csv_path.exists()
    with csv_path.open("a") as fcsv:
        w = csv.writer(fcsv)
        if write_hdr:
            w.writerow(["epoch", "train_loss", "val_loss", "train_ppl", "val_ppl", "secs"])
        for ep in range(start_ep, args.epochs):
            t0 = time.time()
            tr = run_epoch(model, dl_train, loss_fn, optim, device, train=True, sched_state=sched)
            vl = run_epoch(model, dl_val, loss_fn, optim, device, train=False)
            dt = time.time() - t0
            tr_ppl, vl_ppl = math.exp(min(tr, 30)), math.exp(min(vl, 30))
            print(f"[trans] ep={ep} train={tr:.4f} val={vl:.4f} ppl_t={tr_ppl:.2f} ppl_v={vl_ppl:.2f} secs={dt:.1f}", flush=True)
            w.writerow([ep, f"{tr:.4f}", f"{vl:.4f}", f"{tr_ppl:.2f}", f"{vl_ppl:.2f}", f"{dt:.1f}"])
            fcsv.flush()
            ck = {"model": model.state_dict(), "optim": optim.state_dict(), "epoch": ep,
                  "best_val": best_val, "step": sched["step"], "config": config}
            torch.save(ck, last)
            if vl < best_val:
                best_val = vl; ck["best_val"] = best_val
                torch.save(ck, args.out / "best.pt")
                print(f"[trans] new best val={vl:.4f}", flush=True)

    print(f"[trans] done; best_val={best_val:.4f}", flush=True)


if __name__ == "__main__":
    main()
