#!/bin/bash
#SBATCH --job-name=clm_r5_pareto
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=00:20:00
#SBATCH --output=logs/clm_r5_pareto_%j.out
#SBATCH --error=logs/clm_r5_pareto_%j.err

set -euo pipefail
echo "[r5p] start $(date -u +%FT%TZ)"

DATA=/data/user/$USER/aim4_clm
ROUND_DIR=$(ls -dt $DATA/runs/round5_rl_* 2>/dev/null | head -1)
[ -z "$ROUND_DIR" ] && { echo "FAIL: no round5_rl_* dir"; exit 2; }
echo "[r5p] using $ROUND_DIR"

module reset
module load Miniforge3/latest
source activate vina-py

cd "$HOME/jobs/aim4_clm"

# Run the same Pareto rank as iter 3
python pareto_rank_round3.py \
  --candidates "$ROUND_DIR/rl_candidates.csv" \
  --dock-glob "$ROUND_DIR/dock_results/chunk_*.csv" \
  --out "$ROUND_DIR/top200.csv" \
  --top-k 200

# Also produce the novelty-floored variant (replicates the iter-3 manual re-rank)
python <<"PYEOF"
import csv, glob, json, math
from pathlib import Path
import statistics as S
from rdkit import Chem
from rdkit.Chem import FilterCatalog
from rdkit import RDLogger
RDLogger.DisableLog("rdApp.*")

import os
ROUND = Path(os.environ.get("ROUND_DIR_R5") or "$ROUND_DIR")
NOV_FLOOR = 0.3

cand = list(csv.DictReader(open(ROUND / "rl_candidates.csv")))
dock_by_smi = {}
for p in sorted(glob.glob(str(ROUND / "dock_results" / "chunk_*.csv"))):
    for r in csv.DictReader(open(p)):
        smi = r.get("smiles_canonical")
        try: vs = float(r.get("vina_score", ""))
        except (ValueError, TypeError): continue
        if smi:
            prev = dock_by_smi.get(smi)
            if prev is None or vs < prev: dock_by_smi[smi] = vs

def safe(v, d=0.0):
    try: return float(v)
    except: return d

params = FilterCatalog.FilterCatalogParams()
params.AddCatalog(FilterCatalog.FilterCatalogParams.FilterCatalogs.PAINS)
pcat = FilterCatalog.FilterCatalog(params)

merged = []
for r in cand:
    vs = dock_by_smi.get(r["smiles_canonical"])
    if vs is None: continue
    nov = safe(r.get("novelty"))
    liv = int(safe(r.get("lipinski_violations"), 0))
    if nov < NOV_FLOOR or liv > 1 or vs > -6.0: continue
    mol = Chem.MolFromSmiles(r["smiles_canonical"])
    if mol is None or pcat.HasMatch(mol): continue
    r["vina_score"] = vs
    merged.append(r)

if merged:
    aff = [-r["vina_score"] for r in merged]
    qed = [safe(r.get("qed")) for r in merged]
    nov = [safe(r.get("novelty")) for r in merged]
    def z(vals):
        m = S.mean(vals); s = S.pstdev(vals) or 1.0
        return [(v-m)/s for v in vals]
    za, zq, zn = z(aff), z(qed), z(nov)
    for i, r in enumerate(merged):
        r["composite_score"] = 2*za[i] + zq[i] + zn[i]
    merged.sort(key=lambda r: r["composite_score"], reverse=True)
    top = merged[:200]
    fields = ["smiles_canonical","vina_score","qed","novelty","mw","logp","hbd","hba","rotbonds",
              "lipinski_violations","max_tanimoto_known","temperature","composite_score"]
    out = ROUND / "top200_novel.csv"
    with out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader(); w.writerows(top)
    summary = {
        "n_survivors": len(merged),
        "n_top": len(top),
        "best_vina": min(r["vina_score"] for r in top),
        "median_vina": S.median(r["vina_score"] for r in top),
        "best_novelty": max(safe(r.get("novelty")) for r in top),
        "median_novelty": S.median(safe(r.get("novelty")) for r in top),
        "median_qed": S.median(safe(r.get("qed")) for r in top),
        "best_qed": max(safe(r.get("qed")) for r in top),
    }
    (ROUND / "top200_novel.summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))
else:
    print("[r5p] no survivors after gates")
PYEOF

echo "[r5p] done $(date -u +%FT%TZ)"
ls -la "$ROUND_DIR"
