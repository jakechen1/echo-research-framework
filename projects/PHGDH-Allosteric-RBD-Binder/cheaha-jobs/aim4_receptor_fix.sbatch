#!/bin/bash
#SBATCH --job-name=receptor_fix
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=00:10:00
#SBATCH --output=logs/receptor_fix_%j.out
#SBATCH --error=logs/receptor_fix_%j.err

set -euo pipefail
echo "[recfix] start $(date -u +%FT%TZ) on $(hostname)"

DATA=/data/user/$USER/aim4_clm
RECEPTOR_DIR=$DATA/receptors
cd "$RECEPTOR_DIR"

module reset
module load Miniforge3/latest
source activate vina-py

# Newer meeko CLI: must use -p flag to actually emit PDBQT
echo "[recfix] running mk_prepare_receptor.py with -p (write_pdbqt)"
mk_prepare_receptor.py \
  -i 6rih_chainA_protein.pdb \
  -o 6rih_chainA_protein \
  -p \
  --skip_gpf 2>&1 || true

# Some meeko versions emit *.pdbqt; some emit -p flag triggers .pdbqt extension automatically
ls -la 6rih_chainA_protein* 2>&1

# If the CLI didn't produce PDBQT, fall back to AutoDockTools
if [ ! -s 6rih_chainA_protein.pdbqt ]; then
  echo "[recfix] meeko CLI did not produce PDBQT; trying ADFRsuite-style prepare_receptor"
  # Try ADFR or pdb_to_pdbqt via openbabel
  which obabel 2>&1 || mamba install -n vina-py -y -c conda-forge openbabel 2>&1 | tail -5
  source activate vina-py
  obabel -i pdb 6rih_chainA_protein.pdb -o pdbqt -O 6rih_chainA_protein.pdbqt -xr 2>&1 || true
  ls -la 6rih_chainA_protein.pdbqt 2>&1 || true
fi

# Last resort: pdb2pqr + manual PDBQT shim using prody atomtypes
if [ ! -s 6rih_chainA_protein.pdbqt ]; then
  echo "[recfix] fallback: prody-based PDBQT writer"
  python <<PYEOF
# Minimal PDBQT writer for a clean PDB. Adds AD4 atom types via simple element rules.
# Good enough for Vina if hydrogens already present; otherwise add via rdkit/prody.
from pathlib import Path
import re

src = Path("6rih_chainA_protein.pdb")
out = Path("6rih_chainA_protein.pdbqt")

# Rule-based AD4 atom-type mapping — minimal, will skip charge/Gasteiger
elem_to_ad4 = {
    "C": "C", "N": "N", "O": "OA", "S": "SA",
    "H": "HD", "P": "P", "F": "F", "Cl": "Cl", "Br": "Br", "I": "I",
}

lines_out = []
n_atoms = 0
for line in src.read_text().splitlines():
    if line.startswith("ATOM") and len(line) >= 78:
        elem = line[76:78].strip()
        ad4 = elem_to_ad4.get(elem, "C")
        # PDBQT adds charge column [70:76] and AD4 type [77:79]
        new_line = f"{line[:54]}{line[54:60]}{line[60:66]}{0.000:8.3f}{ad4:>2s}"
        lines_out.append(new_line)
        n_atoms += 1
    elif line.startswith("TER"):
        lines_out.append(line)

lines_out.append("TER")
out.write_text("\n".join(lines_out) + "\n")
print(f"[recfix] manual PDBQT: {n_atoms} atoms -> {out}")
PYEOF
fi

ls -la 6rih_chainA_protein.pdbqt
[ -s 6rih_chainA_protein.pdbqt ] && echo "[recfix] OK" || { echo "[recfix] FAIL"; exit 3; }

# Quick smoke test: load with vina
python <<PYEOF
from vina import Vina
v = Vina(sf_name="vina", verbosity=0)
v.set_receptor("6rih_chainA_protein.pdbqt")
print("[recfix] vina loaded receptor successfully")
PYEOF

echo "[recfix] done $(date -u +%FT%TZ)"
