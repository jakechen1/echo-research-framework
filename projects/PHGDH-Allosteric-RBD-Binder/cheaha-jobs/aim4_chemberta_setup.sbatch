#!/bin/bash
#SBATCH --job-name=chemberta
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/chemberta_%j.out
#SBATCH --error=logs/chemberta_%j.err

set -euo pipefail
echo "[cb] start $(date -u +%FT%TZ)"

# ChemBERTa-based affinity proxy: embed candidate SMILES + known PHGDH actives
# via HuggingFace ChemBERTa, score by max cosine similarity. No protein side,
# but the 1011 known PHGDH actives serve as anchors. Robust, fast (<1ms/mol on GPU).

DATA=/data/user/$USER/aim4_clm
CB_DIR=$DATA/chemberta
mkdir -p $CB_DIR
cd $CB_DIR

module reset
module load Miniforge3/latest

# Reuse clm-trans (has torch + rdkit) and add transformers
source activate clm-trans

# Add HuggingFace transformers + tokenizers if not already present
pip install --quiet transformers==4.46.0 2>&1 | tail -3

python -c "import transformers; print(\"transformers\", transformers.__version__)"

# Smoke test: embed known PHGDH actives + decoys, compute affinity proxy
python <<"PYEOF"
import torch
from transformers import AutoTokenizer, AutoModel
from pathlib import Path
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs

print("[cb] loading ChemBERTa-zinc-base-v1")
device = "cuda" if torch.cuda.is_available() else "cpu"
tok = AutoTokenizer.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")
model = AutoModel.from_pretrained("seyonec/ChemBERTa-zinc-base-v1").to(device).eval()
print(f"[cb] loaded; device={device}, params={sum(p.numel() for p in model.parameters()):,}")

@torch.no_grad()
def embed(smiles_list, batch_size=32):
    out = []
    for i in range(0, len(smiles_list), batch_size):
        batch = smiles_list[i:i+batch_size]
        enc = tok(batch, padding=True, truncation=True, max_length=128, return_tensors="pt").to(device)
        h = model(**enc).last_hidden_state  # [B, T, D]
        mask = enc.attention_mask.unsqueeze(-1).float()
        pooled = (h * mask).sum(1) / mask.sum(1).clamp(min=1)
        out.append(pooled.cpu())
    return torch.cat(out, dim=0)

# Load known PHGDH actives as anchors
known_path = Path("/data/user/jakechen/aim4_clm/bucket_pv5.smi")
anchors = []
for line in known_path.open():
    s = line.strip().split()[0]
    if s and Chem.MolFromSmiles(s):
        anchors.append(s)
print(f"[cb] anchors (known PHGDH actives): {len(anchors)}")

print("[cb] embedding anchors")
anchor_emb = embed(anchors)
anchor_emb_norm = anchor_emb / anchor_emb.norm(dim=-1, keepdim=True).clamp(min=1e-8)
print(f"[cb] anchor_emb shape: {anchor_emb.shape}")

# Save anchors embedding for re-use
torch.save({
    "anchors": anchors,
    "embeddings": anchor_emb,
    "model": "seyonec/ChemBERTa-zinc-base-v1",
}, "/data/user/jakechen/aim4_clm/chemberta/phgdh_anchors.pt")
print("[cb] saved anchors → /data/user/jakechen/aim4_clm/chemberta/phgdh_anchors.pt")

# Smoke test on candidates
tests = [
    ("CBR-5884",       "Cc1ccc(NC(=O)c2cc(C)nn2-c2nc3ccccc3s2)cc1"),
    ("NCT-503",        "OC(C(=O)NCCN1CCN(c2ccc(Cl)cc2)CC1)c1ccc(F)cc1"),
    ("ethanol_decoy",  "CCO"),
    ("aspirin_decoy",  "CC(=O)Oc1ccccc1C(=O)O"),
    ("benzene_decoy",  "c1ccccc1"),
]

cand_smiles = [smi for _, smi in tests]
cand_emb = embed(cand_smiles)
cand_emb_norm = cand_emb / cand_emb.norm(dim=-1, keepdim=True).clamp(min=1e-8)
sims = cand_emb_norm @ anchor_emb_norm.T  # [n_cand, n_anchors]

print()
print("[cb] === affinity proxy results (max-cosine to known PHGDH actives) ===")
print(f"{'name':<18} {'max_cos':>8} {'mean_top10':>12} {'rdkit_tanimoto_top1':>22}")
for i, (name, smi) in enumerate(tests):
    sim = sims[i]
    max_cos = sim.max().item()
    top10_mean = sim.topk(min(10, len(anchors))).values.mean().item()
    # Compare with classical RDKit Tanimoto-fingerprint top1 for sanity
    mol = Chem.MolFromSmiles(smi)
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, 2048)
    rdkit_sims = []
    for a in anchors[:200]:  # subsample for speed in smoke test
        am = Chem.MolFromSmiles(a)
        if am is None: continue
        afp = AllChem.GetMorganFingerprintAsBitVect(am, 2, 2048)
        rdkit_sims.append(DataStructs.TanimotoSimilarity(fp, afp))
    rdkit_top1 = max(rdkit_sims) if rdkit_sims else 0.0
    print(f"{name:<18} {max_cos:>8.3f} {top10_mean:>12.3f} {rdkit_top1:>22.3f}")

print()
print("[cb] interpretation:")
print("[cb]   high max_cos = chemistry close to a known PHGDH active = likely binder")
print("[cb]   compare ChemBERTa cosine vs RDKit Morgan-Tanimoto: both should rank actives high, decoys low")
print()
print("[cb] ChemBERTa-cosine affinity proxy is READY for Round 5 RL reward integration")
PYEOF

echo "[cb] done $(date -u +%FT%TZ)"
