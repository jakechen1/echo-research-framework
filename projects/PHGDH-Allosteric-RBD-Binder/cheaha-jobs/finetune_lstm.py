#!/usr/bin/env python
"""5-stage incremental fine-tune from a pretrained char-LSTM checkpoint.

Loads `best.pt` from a previous pretrain run and fine-tunes sequentially on
PHGDH potency buckets in order: pv5 -> pv6 -> pv7 -> pv8 -> pv9. Each stage
uses low LR (1e-4) with brief warmup. Saves a checkpoint after each stage.

Per Fan Li 2026: the potency staircase smoothly shifts the model distribution
from generic bioactive to PHGDH-active-at-cutoff-N, without sharp distribution
collapse.

Usage:
  finetune_lstm.py \
    --pretrain best.pt \
    --vocab vocab.json \
    --buckets bucket_pv5.smi,bucket_pv6.smi,bucket_pv7.smi,bucket_pv8.smi,bucket_pv9.smi \
    --out runs/<jobid> \
    --epochs-per-stage 8 \
    --lr 1e-4
"""
from __future__ import annotations
import argparse, csv, json, math, os, random, sys, time
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

PAD, START, END = " ", "^", "$"


def load_smiles(path: Path, vocab_chars: set) -> tuple[list[str], int]:
    """Return (kept_smiles, dropped_oov_count). Drops SMILES with chars not in vocab."""
    kept, dropped = [], 0
    with path.open() as f:
        for line in f:
            s = line.strip().split("\t")[0]
            if not s or s.startswith("#"):
                continue
            if any(c not in vocab_chars for c in s):
                dropped += 1
                continue
            kept.append(s)
    return kept, dropped


class SMILESDataset(Dataset):
    def __init__(self, smiles: list[str], ch2i: dict, max_len: int):
        self.smiles = smiles
        self.ch2i = ch2i
        self.max_len = max_len
        self.pad = ch2i[PAD]

    def __len__(self):
        return len(self.smiles)

    def __getitem__(self, i):
        s = START + self.smiles[i] + END
        s = s[: self.max_len]
        ids = [self.ch2i.get(c, self.pad) for c in s]
        ids += [self.pad] * (self.max_len - len(ids))
        ids = torch.tensor(ids, dtype=torch.long)
        return ids[:-1], ids[1:]


class CharLSTM(nn.Module):
    def __init__(self, vocab: int, embed: int, hidden: int, layers: int, dropout: float):
        super().__init__()
        self.embed = nn.Embedding(vocab, embed, padding_idx=0)
        self.lstm = nn.LSTM(
            embed, hidden, num_layers=layers,
            dropout=dropout if layers > 1 else 0.0, batch_first=True,
        )
        self.head = nn.Linear(hidden, vocab)

    def forward(self, x):
        e = self.embed(x)
        o, _ = self.lstm(e)
        return self.head(o)


def warmup_cosine_lr(step: int, total: int, base: float, warmup_frac: float = 0.1) -> float:
    warm = max(1, int(total * warmup_frac))
    if step < warm:
        return base * step / warm
    rem = (step - warm) / max(1, (total - warm))
    return 0.5 * base * (1 + math.cos(math.pi * rem))


def run_epoch(model, loader, loss_fn, optim, device, train: bool, scheduler_state=None):
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
                if scheduler_state is not None:
                    scheduler_state["step"] += 1
                    new_lr = warmup_cosine_lr(
                        scheduler_state["step"],
                        scheduler_state["total"],
                        scheduler_state["base"],
                    )
                    for pg in optim.param_groups:
                        pg["lr"] = new_lr
        total_loss += loss.item() * tok
        total_tok += tok
    return total_loss / max(total_tok, 1)


def fine_tune_stage(model, ch2i, smiles, args, device, stage_name, out_dir):
    if not smiles:
        print(f"[ft:{stage_name}] empty corpus, skipping", flush=True)
        return None
    random.shuffle(smiles)
    n_val = max(1, int(len(smiles) * 0.1))
    val, train = smiles[:n_val], smiles[n_val:]
    print(f"[ft:{stage_name}] n_train={len(train)} n_val={len(val)}", flush=True)

    ds_train = SMILESDataset(train, ch2i, args.max_len)
    ds_val = SMILESDataset(val, ch2i, args.max_len)
    dl_train = DataLoader(ds_train, batch_size=args.batch, shuffle=True,
                          num_workers=2, pin_memory=(device == "cuda"))
    dl_val = DataLoader(ds_val, batch_size=args.batch, shuffle=False,
                        num_workers=2, pin_memory=(device == "cuda"))

    optim = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    loss_fn = nn.CrossEntropyLoss(ignore_index=0)

    total_steps = max(1, len(dl_train) * args.epochs_per_stage)
    sched = {"step": 0, "total": total_steps, "base": args.lr}

    best_val = float("inf")
    log_path = out_dir / f"ft_{stage_name}_log.csv"
    with log_path.open("w") as f:
        w = csv.writer(f)
        w.writerow(["epoch", "train_loss", "val_loss", "train_ppl", "val_ppl", "secs"])
        for ep in range(args.epochs_per_stage):
            t0 = time.time()
            tr = run_epoch(model, dl_train, loss_fn, optim, device, train=True, scheduler_state=sched)
            vl = run_epoch(model, dl_val, loss_fn, optim, device, train=False)
            dt = time.time() - t0
            tr_ppl = math.exp(min(tr, 30)); vl_ppl = math.exp(min(vl, 30))
            print(f"[ft:{stage_name}] ep={ep} train={tr:.4f} val={vl:.4f} "
                  f"ppl_t={tr_ppl:.2f} ppl_v={vl_ppl:.2f} secs={dt:.1f} lr={optim.param_groups[0]['lr']:.2e}",
                  flush=True)
            w.writerow([ep, f"{tr:.4f}", f"{vl:.4f}", f"{tr_ppl:.2f}", f"{vl_ppl:.2f}", f"{dt:.1f}"])
            best_val = min(best_val, vl)

    ckpt_path = out_dir / f"ft_{stage_name}.pt"
    torch.save({"model": model.state_dict(), "stage": stage_name, "best_val": best_val}, ckpt_path)
    print(f"[ft:{stage_name}] saved {ckpt_path} (best_val={best_val:.4f})", flush=True)
    return ckpt_path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pretrain", required=True, type=Path, help="pretrain best.pt")
    ap.add_argument("--vocab", required=True, type=Path, help="vocab.json from pretrain")
    ap.add_argument("--buckets", required=True, help="comma-separated bucket .smi files")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--epochs-per-stage", type=int, default=8)
    ap.add_argument("--batch", type=int, default=128)
    ap.add_argument("--max-len", type=int, default=110)
    ap.add_argument("--hidden", type=int, default=512)
    ap.add_argument("--embed", type=int, default=128)
    ap.add_argument("--layers", type=int, default=3)
    ap.add_argument("--dropout", type=float, default=0.2)
    ap.add_argument("--lr", type=float, default=1e-4)
    ap.add_argument("--weight-decay", type=float, default=1e-5)
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    random.seed(args.seed); torch.manual_seed(args.seed)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[ft] device={device}", flush=True)
    if device == "cuda":
        print(f"[ft] gpu={torch.cuda.get_device_name(0)}", flush=True)

    vocab = json.loads(args.vocab.read_text())["vocab"]
    ch2i = {c: i for i, c in enumerate(vocab)}
    vocab_chars = set(vocab)
    print(f"[ft] vocab size={len(vocab)}", flush=True)

    model = CharLSTM(len(vocab), args.embed, args.hidden, args.layers, args.dropout).to(device)
    ck = torch.load(args.pretrain, map_location=device)
    model.load_state_dict(ck["model"])
    print(f"[ft] loaded pretrain from {args.pretrain} (best_val={ck.get('best_val', '?')})", flush=True)

    config = {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()}
    config["vocab_size"] = len(vocab)
    (args.out / "ft_config.json").write_text(json.dumps(config, indent=2))

    bucket_paths = [Path(b.strip()) for b in args.buckets.split(",") if b.strip()]
    summary = []
    for bp in bucket_paths:
        stage = bp.stem  # e.g., "bucket_pv5"
        smiles, dropped = load_smiles(bp, vocab_chars)
        print(f"[ft:{stage}] loaded {len(smiles)} (dropped {dropped} oov)", flush=True)
        ckpt = fine_tune_stage(model, ch2i, smiles, args, device, stage, args.out)
        summary.append({"stage": stage, "n_smiles": len(smiles), "dropped_oov": dropped,
                        "checkpoint": str(ckpt) if ckpt else None})

    (args.out / "ft_summary.json").write_text(json.dumps(summary, indent=2))
    # Also save the FINAL state under a stable name
    final = args.out / "ft_final.pt"
    torch.save({"model": model.state_dict(), "stage": "final", "config": config}, final)
    print(f"[ft] DONE; final ckpt -> {final}", flush=True)


if __name__ == "__main__":
    main()
