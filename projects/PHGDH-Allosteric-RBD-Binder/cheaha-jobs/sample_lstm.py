#!/usr/bin/env python
"""Sample SMILES from a fine-tuned char-LSTM, validate with RDKit, rank.

Usage:
  sample_lstm.py \
    --checkpoint runs/<jobid>/ft_final.pt \
    --vocab runs/<jobid>/vocab.json \
    --out runs/<jobid>/candidates.csv \
    --n 10000 --temperatures 0.8,1.0,1.2 \
    --known-actives /data/user/jakechen/aim4_clm/bucket_pv5.smi
"""
from __future__ import annotations
import argparse, csv, json, math, sys, time
from pathlib import Path

import torch
import torch.nn as nn
import torch.nn.functional as F

PAD, START, END = " ", "^", "$"


class CharLSTM(nn.Module):
    def __init__(self, vocab: int, embed: int, hidden: int, layers: int, dropout: float = 0.0):
        super().__init__()
        self.embed = nn.Embedding(vocab, embed, padding_idx=0)
        self.lstm = nn.LSTM(embed, hidden, num_layers=layers,
                            dropout=dropout if layers > 1 else 0.0, batch_first=True)
        self.head = nn.Linear(hidden, vocab)

    def forward(self, x, h=None):
        e = self.embed(x)
        o, h = self.lstm(e, h)
        return self.head(o), h


@torch.no_grad()
def sample_batch(model, ch2i, i2ch, batch_size: int, max_len: int, temperature: float, device: str):
    """Sample batch_size SMILES sequences. Returns list of strings (without START/END/PAD)."""
    pad_id = ch2i[PAD]; start_id = ch2i[START]; end_id = ch2i[END]
    cur = torch.full((batch_size, 1), start_id, dtype=torch.long, device=device)
    h = None
    out_ids = [[] for _ in range(batch_size)]
    done = [False] * batch_size
    for _ in range(max_len):
        logits, h = model(cur, h)
        logits = logits[:, -1, :] / max(temperature, 1e-6)
        probs = F.softmax(logits, dim=-1)
        nxt = torch.multinomial(probs, num_samples=1)
        cur = nxt
        for i in range(batch_size):
            if done[i]:
                continue
            tok = int(nxt[i].item())
            if tok == end_id or tok == pad_id:
                done[i] = True
            else:
                out_ids[i].append(tok)
        if all(done):
            break
    return ["".join(i2ch[t] for t in seq) for seq in out_ids]


@torch.no_grad()
def perplexity(model, ch2i, smiles: str, max_len: int, device: str) -> float:
    """Return perplexity (lower = more confident model)."""
    pad_id = ch2i[PAD]; start_id = ch2i[START]; end_id = ch2i[END]
    s = START + smiles + END
    s = s[:max_len]
    ids = [ch2i.get(c, pad_id) for c in s]
    if len(ids) < 2:
        return float("inf")
    x = torch.tensor([ids[:-1]], dtype=torch.long, device=device)
    y = torch.tensor([ids[1:]], dtype=torch.long, device=device)
    logits, _ = model(x)
    log_probs = F.log_softmax(logits, dim=-1)
    nll = -log_probs.gather(2, y.unsqueeze(-1)).squeeze(-1)
    mask = (y != pad_id).float()
    nll_mean = (nll * mask).sum().item() / max(mask.sum().item(), 1)
    return math.exp(min(nll_mean, 30))


def try_rdkit():
    try:
        from rdkit import Chem
        from rdkit.Chem import AllChem, QED, DataStructs, Descriptors, Crippen, Lipinski
        from rdkit import RDLogger
        RDLogger.DisableLog("rdApp.*")
        return Chem, AllChem, QED, DataStructs, Descriptors, Crippen, Lipinski
    except ImportError:
        print("[sample] WARN: rdkit not available; skipping validity/QED/Lipinski/Tanimoto", flush=True)
        return (None,) * 7


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--checkpoint", required=True, type=Path)
    ap.add_argument("--vocab", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--n", type=int, default=10000, help="total samples across all temperatures")
    ap.add_argument("--temperatures", default="0.8,1.0,1.2")
    ap.add_argument("--max-len", type=int, default=110)
    ap.add_argument("--batch", type=int, default=256)
    ap.add_argument("--hidden", type=int, default=512)
    ap.add_argument("--embed", type=int, default=128)
    ap.add_argument("--layers", type=int, default=3)
    ap.add_argument("--known-actives", type=Path, default=None,
                    help="optional .smi file with known actives for novelty/Tanimoto")
    ap.add_argument("--top-k", type=int, default=1000, help="output top-K by perplexity")
    args = ap.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[sample] device={device}", flush=True)

    vocab = json.loads(args.vocab.read_text())["vocab"]
    ch2i = {c: i for i, c in enumerate(vocab)}
    i2ch = {i: c for c, i in ch2i.items()}

    model = CharLSTM(len(vocab), args.embed, args.hidden, args.layers).to(device)
    ck = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(ck["model"])
    model.eval()

    Chem, AllChem, QED, DataStructs, Descriptors, Crippen, Lipinski = try_rdkit()

    # Build Morgan fingerprints of known actives for novelty
    known_fps = []
    if args.known_actives and Chem and args.known_actives.exists():
        with args.known_actives.open() as f:
            for line in f:
                s = line.strip().split()[0]
                m = Chem.MolFromSmiles(s)
                if m:
                    known_fps.append(AllChem.GetMorganFingerprintAsBitVect(m, 2, 2048))
        print(f"[sample] loaded {len(known_fps)} known-active fingerprints for novelty", flush=True)

    # Sample
    temps = [float(t) for t in args.temperatures.split(",")]
    per_temp = max(1, args.n // len(temps))
    raw = []
    t0 = time.time()
    for T in temps:
        produced = 0
        while produced < per_temp:
            bs = min(args.batch, per_temp - produced)
            ss = sample_batch(model, ch2i, i2ch, bs, args.max_len, T, device)
            raw.extend([(s, T) for s in ss])
            produced += bs
        print(f"[sample] T={T:.2f}: {produced} samples (cum total={len(raw)}) elapsed={time.time()-t0:.1f}s", flush=True)

    # Validate with RDKit, dedup canonical, score
    rows = []
    seen_canon = set()
    valid = 0; invalid = 0
    for s, T in raw:
        if not s:
            invalid += 1; continue
        mol = Chem.MolFromSmiles(s) if Chem else None
        if Chem and mol is None:
            invalid += 1; continue
        canon = Chem.MolToSmiles(mol, canonical=True) if mol else s
        if canon in seen_canon:
            continue
        seen_canon.add(canon)
        valid += 1
        ppl = perplexity(model, ch2i, canon, args.max_len, device)
        row = {"smiles_raw": s, "smiles_canonical": canon, "temperature": T, "perplexity": ppl}
        if mol is not None:
            row["qed"] = QED.qed(mol)
            row["mw"] = Descriptors.MolWt(mol)
            row["logp"] = Crippen.MolLogP(mol)
            row["hbd"] = Lipinski.NumHDonors(mol)
            row["hba"] = Lipinski.NumHAcceptors(mol)
            row["rotbonds"] = Lipinski.NumRotatableBonds(mol)
            row["tpsa"] = Descriptors.TPSA(mol)
            # Lipinski Ro5 violations
            v = sum([row["mw"] > 500, row["logp"] > 5, row["hbd"] > 5, row["hba"] > 10])
            row["lipinski_violations"] = v
            # Novelty (max Tanimoto vs known actives = closeness; novelty = 1 - max_tanimoto)
            if known_fps:
                fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048)
                sims = DataStructs.BulkTanimotoSimilarity(fp, known_fps)
                row["max_tanimoto_known"] = max(sims) if sims else 0.0
                row["novelty"] = 1.0 - row["max_tanimoto_known"]
        rows.append(row)

    print(f"[sample] valid={valid} invalid={invalid} unique_canonical={len(seen_canon)} valid_rate={valid/(valid+invalid+1e-9):.2%}", flush=True)

    # Rank by perplexity (ascending = most confident first)
    rows.sort(key=lambda r: r["perplexity"])
    top = rows[: args.top_k]

    # Write CSV
    fieldnames = ["smiles_canonical", "smiles_raw", "temperature", "perplexity",
                  "qed", "mw", "logp", "hbd", "hba", "rotbonds", "tpsa",
                  "lipinski_violations", "max_tanimoto_known", "novelty"]
    with args.out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(top)
    print(f"[sample] wrote top {len(top)} -> {args.out}", flush=True)

    # Summary stats
    summary = {
        "total_sampled": len(raw),
        "valid": valid,
        "invalid": invalid,
        "unique_canonical": len(seen_canon),
        "valid_rate": valid / (valid + invalid + 1e-9),
        "kept_top_k": len(top),
        "ppl_top1": top[0]["perplexity"] if top else None,
        "ppl_top10_mean": (sum(r["perplexity"] for r in top[:10]) / 10) if len(top) >= 10 else None,
        "qed_top10_mean": (sum(r.get("qed", 0) for r in top[:10]) / 10) if Chem and len(top) >= 10 else None,
        "novelty_top10_mean": (sum(r.get("novelty", 0) for r in top[:10]) / 10) if known_fps and len(top) >= 10 else None,
    }
    summary_path = args.out.with_suffix(".summary.json")
    summary_path.write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2), flush=True)


if __name__ == "__main__":
    main()
