#!/bin/bash
#SBATCH --job-name=clm_r5_rl
#SBATCH --partition=amperenodes
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --gres=gpu:1
#SBATCH --time=04:00:00
#SBATCH --output=logs/clm_r5_rl_%j.out
#SBATCH --error=logs/clm_r5_rl_%j.err

set -euo pipefail
echo "[r5] start $(date -u +%FT%TZ) on $(hostname) jobid=$SLURM_JOB_ID"
nvidia-smi | head -12 || true

# Round 5: REINFORCE fine-tune of iter-4 transformer with ChemBERTa anchored
# affinity reward + QED + novelty, KL-to-prior penalty, entropy regularization.
# Then sample 5K candidates from the RL-tuned model.

DATA=/data/user/$USER/aim4_clm
PRETRAIN_DIR=${PRETRAIN_DIR:-$DATA/runs/round4_pretrain_38302811}
ANCHORS=$DATA/chemberta/phgdh_anchors.pt
OUT=$DATA/runs/round5_rl_$SLURM_JOB_ID
mkdir -p "$OUT"

# Cancel the P100 race-loser if it's still running (we use A100 winner only)
P100_JOB=${P100_JOB:-38302357}
if squeue -j $P100_JOB -h -o "%T" 2>/dev/null | grep -q RUNNING; then
  echo "[r5] cancelling losing P100 job $P100_JOB"
  scancel $P100_JOB || true
fi

# Stage data to local SSD
LOCAL=/local/$USER/$SLURM_JOB_ID
mkdir -p "$LOCAL"
cp "$PRETRAIN_DIR/best.pt" "$LOCAL/" || cp "$PRETRAIN_DIR/last.pt" "$LOCAL/best.pt"
cp "$PRETRAIN_DIR/vocab.json" "$LOCAL/"
cp "$PRETRAIN_DIR/config.json" "$LOCAL/"
cp "$ANCHORS" "$LOCAL/anchors.pt"
ls -la "$LOCAL/"

module reset
module load Miniforge3/latest
source activate clm-trans

# Add transformers (ChemBERTa needs it; clm-trans probably already has it from chemberta job)
python -c "import transformers" 2>/dev/null || pip install --quiet transformers==4.46.0

python -c "import torch, transformers, selfies, rdkit; print(\"torch\", torch.__version__, \"cuda\", torch.cuda.is_available()); print(\"transformers\", transformers.__version__)"

cd "$HOME/jobs/aim4_clm"

# 1) RL fine-tune (1000 steps; ~1-3h on A100 depending on ChemBERTa overhead)
echo "[r5] === RL FINE-TUNE ==="
python rl_finetune.py \
  --pretrain "$LOCAL/best.pt" \
  --vocab "$LOCAL/vocab.json" \
  --known-actives "$DATA/bucket_pv5.smi" \
  --chemberta-anchors "$LOCAL/anchors.pt" \
  --reward-fn chemberta \
  --out "$OUT" \
  --batch 64 \
  --steps 1000 \
  --lr 1e-5 \
  --beta-kl 0.1 \
  --lambda-ent 0.01 \
  --w-aff 1.0 --w-dl 0.3 --w-nov 0.3 --w-inv 1.0 --w-sa 0.1 \
  --temperature 1.0 \
  --save-every 200

# 2) Sample 5K from RL-tuned model
echo "[r5] === SAMPLE ==="
# Reuse sample_lstm.py — but the model is now a SELFIES transformer not char-LSTM,
# so we need a transformer-compatible sampler. Quick inline:
python <<"PYEOF"
import json, torch, sys, csv, math, time
from pathlib import Path
sys.path.insert(0, "/home/jakechen/jobs/aim4_clm")
from pretrain_transformer import SmallTransformer, PAD, START, END

OUT = Path("$OUT")
device = "cuda" if torch.cuda.is_available() else "cpu"
cfg = json.loads((Path("$LOCAL") / "config.json").read_text())
vocab = json.loads((Path("$LOCAL") / "vocab.json").read_text())["vocab"]
tok2i = {t: i for i, t in enumerate(vocab)}
i2tok = {i: t for t, i in tok2i.items()}
pad_id = tok2i.get(PAD, 0); bos_id = tok2i.get(START, 1); eos_id = tok2i.get(END, 2)

model = SmallTransformer(
    vocab=cfg["vocab_size"], d_model=cfg["d_model"], n_heads=cfg["n_heads"],
    n_layers=cfg["n_layers"], ffn_dim=cfg["ffn_dim"],
    max_len=cfg.get("max_len", 128), dropout=0.0,
).to(device)
ck = torch.load(OUT / "rl_final.pt", map_location=device, weights_only=False)
model.load_state_dict(ck["model"])
model.eval()
print(f"[sample] loaded RL-tuned model from {OUT}/rl_final.pt", flush=True)

import selfies as sf
from rdkit import Chem
from rdkit.Chem import QED, AllChem, DataStructs, Crippen, Lipinski, Descriptors
from rdkit import RDLogger
RDLogger.DisableLog("rdApp.*")

# Load known actives for novelty
known_fps = []
for line in open("$DATA/bucket_pv5.smi"):
    s = line.strip().split()[0]
    m = Chem.MolFromSmiles(s) if s else None
    if m: known_fps.append(AllChem.GetMorganFingerprintAsBitVect(m, 2, 2048))
print(f"[sample] {len(known_fps)} anchor fps for novelty", flush=True)

@torch.no_grad()
def sample_batch(bs, max_len, T=1.0):
    cur = torch.full((bs, 1), bos_id, dtype=torch.long, device=device)
    out_ids = [[] for _ in range(bs)]
    done = [False]*bs
    for _ in range(max_len-1):
        logits = model(cur)[:, -1, :] / max(T, 1e-6)
        probs = torch.softmax(logits, dim=-1)
        nxt = torch.multinomial(probs, 1)
        cur = torch.cat([cur, nxt], dim=1)
        for i in range(bs):
            if done[i]: continue
            t = int(nxt[i].item())
            if t == eos_id or t == pad_id: done[i] = True
            else: out_ids[i].append(t)
        if all(done): break
    return ["".join(i2tok[t] for t in seq if t in i2tok) for seq in out_ids]

# Sample at multiple temperatures
N_TOTAL = 5000
temps = [0.8, 1.0, 1.2]
per_temp = N_TOTAL // len(temps)
all_smiles = []
for T in temps:
    produced = 0
    while produced < per_temp:
        bs = min(64, per_temp - produced)
        sels = sample_batch(bs, cfg.get("max_len", 128), T=T)
        for s in sels:
            try:
                smi = sf.decoder(s)
                all_smiles.append((smi, T))
            except Exception:
                pass
        produced += bs
    print(f"[sample] T={T}: ran to {produced}", flush=True)

# Validate, dedupe, score
valid = 0; invalid = 0; seen_canon = set(); rows = []
for smi, T in all_smiles:
    if not smi:
        invalid += 1; continue
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        invalid += 1; continue
    canon = Chem.MolToSmiles(mol, canonical=True)
    if canon in seen_canon: continue
    seen_canon.add(canon); valid += 1
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048)
    sims = DataStructs.BulkTanimotoSimilarity(fp, known_fps) if known_fps else [0.0]
    novelty = 1.0 - max(sims)
    rows.append({
        "smiles_canonical": canon,
        "smiles_raw": smi,
        "temperature": T,
        "qed": QED.qed(mol),
        "mw": Descriptors.MolWt(mol),
        "logp": Crippen.MolLogP(mol),
        "hbd": Lipinski.NumHDonors(mol),
        "hba": Lipinski.NumHAcceptors(mol),
        "rotbonds": Lipinski.NumRotatableBonds(mol),
        "tpsa": Descriptors.TPSA(mol),
        "lipinski_violations": sum([Descriptors.MolWt(mol)>500, Crippen.MolLogP(mol)>5,
                                    Lipinski.NumHDonors(mol)>5, Lipinski.NumHAcceptors(mol)>10]),
        "max_tanimoto_known": max(sims),
        "novelty": novelty,
    })
print(f"[sample] valid={valid} invalid={invalid} unique={len(seen_canon)} valid_rate={valid/(valid+invalid+1e-9):.2%}", flush=True)

rows.sort(key=lambda r: -r["qed"] - 0.5*r["novelty"])  # stable preliminary rank
out_csv = OUT / "rl_candidates.csv"
with out_csv.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else [], extrasaction="ignore")
    if rows: w.writeheader()
    w.writerows(rows[:2000])
print(f"[sample] wrote top 2000 -> {out_csv}", flush=True)

# Summary
import statistics as S
summary = {
    "rl_step_count": ck.get("step", "?"),
    "n_sampled": len(all_smiles),
    "valid": valid, "invalid": invalid, "unique": len(seen_canon),
    "valid_rate": valid/(valid+invalid+1e-9),
    "qed_mean": S.mean(r["qed"] for r in rows) if rows else None,
    "qed_top10": S.mean(r["qed"] for r in rows[:10]) if len(rows)>=10 else None,
    "novelty_mean": S.mean(r["novelty"] for r in rows) if rows else None,
    "novelty_top10": S.mean(r["novelty"] for r in rows[:10]) if len(rows)>=10 else None,
}
(OUT / "rl_candidates.summary.json").write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2), flush=True)
PYEOF

echo "[r5] artifacts in $OUT:"
ls -la "$OUT"
echo "[r5] done $(date -u +%FT%TZ)"
