#!/bin/bash
#SBATCH --job-name=bindingdb_parse
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/bindingdb_parse_%j.out
#SBATCH --error=logs/bindingdb_parse_%j.err

set -euo pipefail
echo "[bdbp] start $(date -u +%FT%TZ) on $(hostname)"

DATA=/data/user/$USER/aim4_clm
BDB_DIR=$DATA/bindingdb
TSV=$BDB_DIR/BindingDB_All.tsv

[ -f "$TSV" ] || { echo "FAIL: $TSV missing"; exit 2; }
ls -la "$TSV"

module reset
module load Miniforge3/latest
source activate clm-trans

# Chunked stream parse — never holds full 8.8 GB in memory
python <<"PYEOF"
import csv, sys
from pathlib import Path
from rdkit import Chem
from rdkit import RDLogger
RDLogger.DisableLog("rdApp.*")
csv.field_size_limit(sys.maxsize)

bdb = Path("/data/user/jakechen/aim4_clm/bindingdb")
tsv = bdb / "BindingDB_All.tsv"

# Detect SMILES + binding columns from header
with tsv.open(encoding="utf-8", errors="replace") as f:
    header = next(csv.reader(f, delimiter="\t"))
print(f"[bdbp] header has {len(header)} columns")
smi_idx = None
for i, c in enumerate(header):
    if "Ligand SMILES" in c:
        smi_idx = i; break
if smi_idx is None:
    for i, c in enumerate(header):
        if "smiles" in c.lower():
            smi_idx = i; break
print(f"[bdbp] SMILES column idx={smi_idx} name={header[smi_idx] if smi_idx is not None else 'NONE'}")

aff_idx = {}
for label, want in [("Ki", "Ki (nM)"), ("IC50", "IC50 (nM)"),
                     ("Kd", "Kd (nM)"), ("EC50", "EC50 (nM)")]:
    for i, c in enumerate(header):
        if c == want:
            aff_idx[label] = i; break
print(f"[bdbp] affinity columns: {aff_idx}")

if smi_idx is None or not aff_idx:
    sys.exit("required columns not found")

def parse_aff(v):
    if not v: return None
    v = v.replace(">", "").replace("<", "").strip()
    try:
        x = float(v)
        return x if x > 0 else None
    except ValueError:
        return None

# Stream through file, keep only bioactives, canonicalize, dedupe
n_total = 0; n_active = 0; n_smiles_ok = 0
seen = set()
out_path = bdb / "bindingdb_bioactives.smi"

with tsv.open(encoding="utf-8", errors="replace") as f, out_path.open("w") as out:
    reader = csv.reader(f, delimiter="\t")
    next(reader, None)  # skip header
    for row in reader:
        n_total += 1
        if n_total % 250000 == 0:
            print(f"[bdbp]   {n_total} rows, {n_active} bioactive, {n_smiles_ok} canonical written", flush=True)
        if len(row) <= max(smi_idx, *aff_idx.values()):
            continue
        # Active = any of Ki/IC50/Kd/EC50 < 10000 nM
        active = False
        for col_idx in aff_idx.values():
            v = parse_aff(row[col_idx])
            if v is not None and v < 10000:
                active = True; break
        if not active:
            continue
        n_active += 1
        smi = row[smi_idx].strip()
        if not smi:
            continue
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            continue
        canon = Chem.MolToSmiles(mol, canonical=True)
        if "." in canon:
            continue
        if not (5 <= mol.GetNumHeavyAtoms() <= 80):
            continue
        if canon in seen:
            continue
        seen.add(canon)
        out.write(canon + "\n")
        n_smiles_ok += 1

print(f"[bdbp] DONE total={n_total} active={n_active} unique_canonical={n_smiles_ok}")
print(f"[bdbp] wrote {out_path} ({n_smiles_ok} SMILES)")
PYEOF

# Merge with existing ChEMBL bioactives, dedup
echo
echo "[bdbp] merging with ChEMBL bioactives"
CHEMBL=$DATA/bioactives.smi
NEW=$BDB_DIR/bindingdb_bioactives.smi
MERGED=$DATA/bioactives_merged.smi

python <<"PYEOF"
from pathlib import Path
chembl = set()
chembl_path = Path("/data/user/jakechen/aim4_clm/bioactives.smi")
for line in chembl_path.open():
    s = line.strip().split("\t")[0]
    if s: chembl.add(s)
print(f"[bdbp] ChEMBL bioactives: {len(chembl)}")

bdb_set = set()
bdb_path = Path("/data/user/jakechen/aim4_clm/bindingdb/bindingdb_bioactives.smi")
for line in bdb_path.open():
    s = line.strip()
    if s: bdb_set.add(s)
print(f"[bdbp] BindingDB bioactives: {len(bdb_set)}")

new_only = bdb_set - chembl
print(f"[bdbp] BindingDB unique-vs-ChEMBL: {len(new_only)}")

merged_path = Path("/data/user/jakechen/aim4_clm/bioactives_merged.smi")
with merged_path.open("w") as f:
    for s in chembl: f.write(s + "\n")
    for s in new_only: f.write(s + "\n")
print(f"[bdbp] merged corpus: {len(chembl) + len(new_only)} unique SMILES -> {merged_path}")
PYEOF

wc -l $MERGED
echo "[bdbp] done $(date -u +%FT%TZ)"
