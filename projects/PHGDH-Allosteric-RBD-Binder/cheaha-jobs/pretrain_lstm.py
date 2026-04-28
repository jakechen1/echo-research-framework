#!/usr/bin/env python
"""LSTM character-level pretrain for SMILES (Fan Li 2026 CLM).

Reads SMILES (one per line, optionally tab-suffix metadata which is ignored)
and trains an autoregressive LSTM predicting next char. Saves best-val
checkpoint, vocab, config, and per-epoch loss CSV. Resumable.

Usage:
  pretrain_lstm.py --data bioactives.smi --out runs/<jobid> [--limit N] [--epochs E]

Designed to run identically on CPU (smoke) and GPU (full); auto-detects.
"""
from __future__ import annotations
import argparse, csv, json, math, os, random, sys, time
from pathlib import Path

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

PAD, START, END = " ", "^", "$"


def load_smiles(path: Path, limit: int = 0) -> list[str]:
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


def build_vocab(smiles: list[str]) -> tuple[list[str], dict]:
    chars = set()
    for s in smiles:
        chars.update(s)
    vocab = [PAD, START, END] + sorted(chars - {PAD, START, END})
    ch2i = {c: i for i, c in enumerate(vocab)}
    return vocab, ch2i


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


def run_epoch(model, loader, loss_fn, optim, device, train: bool):
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
        total_loss += loss.item() * tok
        total_tok += tok
    return total_loss / max(total_tok, 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--epochs", type=int, default=30)
    ap.add_argument("--batch", type=int, default=256)
    ap.add_argument("--max-len", type=int, default=110)
    ap.add_argument("--hidden", type=int, default=512)
    ap.add_argument("--embed", type=int, default=128)
    ap.add_argument("--layers", type=int, default=3)
    ap.add_argument("--dropout", type=float, default=0.2)
    ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--weight-decay", type=float, default=1e-5)
    ap.add_argument("--val-frac", type=float, default=0.05)
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--workers", type=int, default=2)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    args.out.mkdir(parents=True, exist_ok=True)
    random.seed(args.seed); torch.manual_seed(args.seed)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[pretrain] device={device} cuda={torch.cuda.is_available()}", flush=True)
    if device == "cuda":
        print(f"[pretrain] gpu={torch.cuda.get_device_name(0)}", flush=True)

    smiles = load_smiles(args.data, args.limit)
    if not smiles:
        sys.exit("no SMILES loaded")
    smiles = [s for s in smiles if 1 < len(s) < args.max_len - 2]
    random.shuffle(smiles)
    n_val = max(1, int(len(smiles) * args.val_frac))
    val, train = smiles[:n_val], smiles[n_val:]
    print(f"[pretrain] n_train={len(train)} n_val={len(val)}", flush=True)

    vocab_path = args.out / "vocab.json"
    if args.resume and vocab_path.exists():
        vocab = json.loads(vocab_path.read_text())["vocab"]
        ch2i = {c: i for i, c in enumerate(vocab)}
    else:
        vocab, ch2i = build_vocab(train + val)
        vocab_path.write_text(json.dumps({"vocab": vocab, "max_len": args.max_len}))
    print(f"[pretrain] vocab={len(vocab)}", flush=True)

    config = {k: (str(v) if isinstance(v, Path) else v) for k, v in vars(args).items()}
    config["vocab_size"] = len(vocab)
    (args.out / "config.json").write_text(json.dumps(config, indent=2))

    ds_train = SMILESDataset(train, ch2i, args.max_len)
    ds_val = SMILESDataset(val, ch2i, args.max_len)
    dl_train = DataLoader(
        ds_train, batch_size=args.batch, shuffle=True,
        num_workers=args.workers, pin_memory=(device == "cuda"),
    )
    dl_val = DataLoader(
        ds_val, batch_size=args.batch, shuffle=False,
        num_workers=args.workers, pin_memory=(device == "cuda"),
    )

    model = CharLSTM(len(vocab), args.embed, args.hidden, args.layers, args.dropout).to(device)
    n_params = sum(p.numel() for p in model.parameters())
    print(f"[pretrain] params={n_params:,}", flush=True)
    optim = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    loss_fn = nn.CrossEntropyLoss(ignore_index=0)

    start_epoch = 0
    best_val = float("inf")
    last_ckpt = args.out / "last.pt"
    if args.resume and last_ckpt.exists():
        ck = torch.load(last_ckpt, map_location=device)
        model.load_state_dict(ck["model"])
        optim.load_state_dict(ck["optim"])
        start_epoch = ck["epoch"] + 1
        best_val = ck.get("best_val", best_val)
        print(f"[pretrain] resumed epoch={start_epoch} best_val={best_val:.4f}", flush=True)

    loss_csv = args.out / "loss.csv"
    write_header = not loss_csv.exists()
    with loss_csv.open("a") as fcsv:
        w = csv.writer(fcsv)
        if write_header:
            w.writerow(["epoch", "train_loss", "val_loss", "train_ppl", "val_ppl", "secs"])
        for ep in range(start_epoch, args.epochs):
            t0 = time.time()
            tr = run_epoch(model, dl_train, loss_fn, optim, device, train=True)
            vl = run_epoch(model, dl_val, loss_fn, optim, device, train=False)
            dt = time.time() - t0
            tr_ppl, vl_ppl = math.exp(min(tr, 30)), math.exp(min(vl, 30))
            print(
                f"[pretrain] ep={ep} train={tr:.4f} val={vl:.4f} "
                f"ppl_train={tr_ppl:.2f} ppl_val={vl_ppl:.2f} secs={dt:.1f}",
                flush=True,
            )
            w.writerow([ep, f"{tr:.4f}", f"{vl:.4f}", f"{tr_ppl:.2f}", f"{vl_ppl:.2f}", f"{dt:.1f}"])
            fcsv.flush()
            ckpt = {
                "model": model.state_dict(), "optim": optim.state_dict(),
                "epoch": ep, "best_val": best_val, "config": config,
            }
            torch.save(ckpt, last_ckpt)
            if vl < best_val:
                best_val = vl
                ckpt["best_val"] = best_val
                torch.save(ckpt, args.out / "best.pt")
                print(f"[pretrain] new best val={vl:.4f}", flush=True)

    print(f"[pretrain] done; best_val={best_val:.4f}", flush=True)


if __name__ == "__main__":
    main()
