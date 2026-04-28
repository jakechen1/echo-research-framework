#!/bin/bash
#SBATCH --job-name=bindingdb_dl
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=01:30:00
#SBATCH --output=logs/bindingdb_dl_%j.out
#SBATCH --error=logs/bindingdb_dl_%j.err

set -euo pipefail
echo "[bdb] start $(date -u +%FT%TZ) on $(hostname)"

DATA=/data/user/$USER/aim4_clm
BDB_DIR=$DATA/bindingdb
mkdir -p $BDB_DIR
cd $BDB_DIR

module reset
module load Miniforge3/latest
source activate clm-trans 2>/dev/null || source activate clm-lstm

# BindingDB All (~600 MB compressed, ~3 GB uncompressed; ~2.4M binding measurements)
TARBALL=$BDB_DIR/BindingDB_All_202604_tsv.zip
if [ ! -f "$TARBALL" ]; then
  echo "[bdb] downloading BindingDB All TSV"
  curl -sSfL --retry 3 -o "$TARBALL" \
    "https://www.bindingdb.org/rwd/bind/downloads/BindingDB_All_202604_tsv.zip" || \
  curl -sSfL --retry 3 -o "$TARBALL" \
    "https://www.bindingdb.org/rwd/bind/downloads/BindingDB_All_202604_tsv.zip"
fi
ls -la "$TARBALL"

# Extract
if [ ! -f "$BDB_DIR/BindingDB_All.tsv" ]; then
  echo "[bdb] extracting"
  cd $BDB_DIR && unzip -o "$TARBALL"
  ls -la $BDB_DIR/*.tsv
fi

# Filter to bioactives (Ki, Kd, IC50, EC50 columns; pchembl >= 5 equivalent → < 10000 nM)
# Also dedupe by InChIKey vs ChEMBL
python <<"PYEOF"
import pandas as pd
import sys
from pathlib import Path
from rdkit import Chem
from rdkit import RDLogger
RDLogger.DisableLog("rdApp.*")

bdb_path = Path("/data/user/jakechen/aim4_clm/bindingdb")
tsv = bdb_path / "BindingDB_All.tsv"
print(f"[bdb] reading {tsv}")
# BindingDB has many columns; key ones: 'Ligand SMILES', 'Ki (nM)', 'IC50 (nM)', 'Kd (nM)', 'EC50 (nM)'
df = pd.read_csv(tsv, sep="\t", low_memory=False, on_bad_lines="skip", quoting=3)
print(f"[bdb] rows={len(df)}")
print(f"[bdb] cols sample: {list(df.columns[:8])}")

# Find SMILES column
smi_col = None
for c in df.columns:
    if "Ligand SMILES" in c or "smiles" in c.lower():
        smi_col = c; break
if smi_col is None:
    print("[bdb] FAIL: no SMILES column found")
    sys.exit(2)
print(f"[bdb] using SMILES col: {smi_col}")

# Keep rows with any binding measurement < 10000 nM
keep_mask = pd.Series(False, index=df.index)
for col in ["Ki (nM)", "IC50 (nM)", "Kd (nM)", "EC50 (nM)"]:
    if col in df.columns:
        v = pd.to_numeric(df[col].astype(str).str.replace(">", "").str.replace("<", ""), errors="coerce")
        keep_mask |= (v.notna() & (v < 10000))
df_active = df[keep_mask].copy()
print(f"[bdb] bioactives (any of Ki/IC50/Kd/EC50 < 10 µM): {len(df_active)}")

# Deduplicate by canonical SMILES
print("[bdb] canonicalizing + deduping")
canonical = []
for s in df_active[smi_col].astype(str).tolist():
    if not s or s == "nan":
        canonical.append(None); continue
    mol = Chem.MolFromSmiles(s)
    if mol is None:
        canonical.append(None); continue
    if "." in Chem.MolToSmiles(mol):
        canonical.append(None); continue
    if not (5 <= mol.GetNumHeavyAtoms() <= 80):
        canonical.append(None); continue
    canonical.append(Chem.MolToSmiles(mol, canonical=True))

df_active["canonical_smiles"] = canonical
df_active = df_active.dropna(subset=["canonical_smiles"]).drop_duplicates(subset=["canonical_smiles"])
print(f"[bdb] unique canonical SMILES: {len(df_active)}")

# Compare against existing ChEMBL bioactives.smi
chembl_smi = set()
chembl_path = Path("/data/user/jakechen/aim4_clm/bioactives.smi")
if chembl_path.exists():
    for line in chembl_path.open():
        s = line.strip().split("\t")[0]
        if s:
            chembl_smi.add(s)
print(f"[bdb] ChEMBL bioactives loaded: {len(chembl_smi)}")

new_only = df_active[~df_active["canonical_smiles"].isin(chembl_smi)]
print(f"[bdb] BindingDB UNIQUE (not in ChEMBL): {len(new_only)}")

# Write augmented bioactives file
out_smi = bdb_path / "bindingdb_bioactives.smi"
new_only["canonical_smiles"].to_csv(out_smi, index=False, header=False)
print(f"[bdb] wrote {out_smi} ({len(new_only)} new SMILES)")

# Also write merged corpus (ChEMBL ∪ BindingDB) for Round 5+ pretrain
merged_path = bdb_path.parent / "bioactives_merged.smi"
with merged_path.open("w") as f:
    for s in chembl_smi:
        f.write(s + "\n")
    for s in new_only["canonical_smiles"]:
        f.write(s + "\n")
print(f"[bdb] merged corpus -> {merged_path}")
import subprocess
print(f"[bdb] merged size: {subprocess.run(['wc', '-l', str(merged_path)], capture_output=True, text=True).stdout.strip()}")
PYEOF

echo "[bdb] done $(date -u +%FT%TZ)"
