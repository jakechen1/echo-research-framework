#!/bin/bash
#SBATCH --job-name=vina_setup
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs/vina_setup_%j.out
#SBATCH --error=logs/vina_setup_%j.err

set -euo pipefail
echo "[vina_setup] start $(date -u +%FT%TZ) on $(hostname)"

DATA=/data/user/$USER/aim4_clm
RECEPTOR_DIR=$DATA/receptors
mkdir -p "$RECEPTOR_DIR"

module reset
module load Miniforge3/latest

# Install vina + meeko + rdkit + requests in a dedicated env (idempotent)
if ! conda env list | grep -q "^vina-py "; then
  echo "[vina_setup] creating env vina-py"
  mamba create -n vina-py -y -c conda-forge \
    python=3.11 vina meeko rdkit numpy pandas tqdm requests
else
  echo "[vina_setup] env vina-py already exists"
fi
source activate vina-py
python -c "import vina, meeko, rdkit; print('vina', vina.__version__ if hasattr(vina, '__version__') else 'ok'); print('rdkit', rdkit.__version__)"

# Download PHGDH 6RIH from RCSB (skip if cached)
PDB=$RECEPTOR_DIR/6rih.pdb
if [ ! -f "$PDB" ]; then
  echo "[vina_setup] downloading 6RIH from RCSB"
  curl -sSfL --retry 3 -o "$PDB" "https://files.rcsb.org/download/6RIH.pdb"
else
  echo "[vina_setup] 6rih.pdb already present"
fi
ls -la "$PDB"

# Extract chain A (allosteric monomer), strip waters/HETATM (keep K4T for box-center calc), save
python <<PYEOF
from pathlib import Path
src = Path("$PDB")
lines = src.read_text().splitlines()

# Keep ATOM and TER for chain A, plus K4T HETATM lines (the allosteric inhibitor)
prot_lines = []
k4t_lines = []
for line in lines:
    if line.startswith(("ATOM", "TER")) and (len(line) >= 22 and line[21] == "A"):
        prot_lines.append(line)
    elif line.startswith("HETATM") and " K4T " in line and (len(line) >= 22 and line[21] == "A"):
        k4t_lines.append(line)

# Write protein-only (no K4T, for docking)
prot_only = src.parent / "6rih_chainA_protein.pdb"
prot_only.write_text("\n".join(prot_lines + ["END"]))
print(f"[vina_setup] protein-only PDB ({len(prot_lines)} ATOM lines): {prot_only}")

# Write K4T ligand-only (used to compute pocket center)
k4t = src.parent / "6rih_K4T.pdb"
k4t.write_text("\n".join(k4t_lines + ["END"]))
print(f"[vina_setup] K4T ligand PDB ({len(k4t_lines)} HETATM lines): {k4t}")

if not k4t_lines:
    print("[vina_setup] WARN: no K4T HETATM lines found in chain A; will use whole-protein centroid as fallback")
PYEOF

# Compute pocket box center from K4T (or chain-A centroid as fallback) + define box
python <<PYEOF
import json
from pathlib import Path
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np

receptor_dir = Path("$RECEPTOR_DIR")
k4t_path = receptor_dir / "6rih_K4T.pdb"
prot_path = receptor_dir / "6rih_chainA_protein.pdb"

def centroid_from_pdb(pdb_path: Path):
    coords = []
    for line in pdb_path.read_text().splitlines():
        if line.startswith(("ATOM", "HETATM")):
            try:
                x = float(line[30:38]); y = float(line[38:46]); z = float(line[46:54])
                coords.append((x, y, z))
            except ValueError:
                pass
    if not coords:
        return None
    arr = np.array(coords)
    return arr.mean(axis=0).tolist(), arr.min(axis=0).tolist(), arr.max(axis=0).tolist()

k4t_info = centroid_from_pdb(k4t_path)
if k4t_info and k4t_info[0]:
    center, lo, hi = k4t_info
    span = [hi[i] - lo[i] for i in range(3)]
    # Pad box by ~10 Å on each axis around the K4T extent (typical Vina box)
    box_size = [max(20.0, span[i] + 10.0) for i in range(3)]
    print(f"[vina_setup] pocket center (K4T centroid): {center}")
    print(f"[vina_setup] pocket box size: {box_size}")
else:
    # Fallback: compute from full chain A (whole protein) — almost certainly wrong for allosteric, but safe
    fallback = centroid_from_pdb(prot_path)
    center = fallback[0] if fallback else [0, 0, 0]
    box_size = [25.0, 25.0, 25.0]
    print(f"[vina_setup] WARN: using fallback chain-A centroid: {center}")

config = {
    "receptor_pdb": "6rih_chainA_protein.pdb",
    "k4t_reference_pdb": "6rih_K4T.pdb",
    "pocket_center": center,
    "pocket_box_size": box_size,
    "exhaustiveness": 8,
    "n_poses": 5,
    "vina_version": "1.2.x (python lib)",
}
out = receptor_dir / "pocket_config.json"
out.write_text(json.dumps(config, indent=2))
print(f"[vina_setup] wrote {out}")
print(out.read_text())
PYEOF

# Prepare receptor PDBQT using meeko / openbabel (vina-py env has rdkit)
# Use ADFR's prepare_receptor or AutoDockTools; here we rely on meeko's CLI
echo "[vina_setup] prepare receptor PDBQT"
cd "$RECEPTOR_DIR"

# Try mk_prepare_receptor.py (meeko)
if command -v mk_prepare_receptor.py > /dev/null 2>&1; then
  mk_prepare_receptor.py -i 6rih_chainA_protein.pdb -o 6rih_chainA_protein.pdbqt --no-add-hydrogens 2>&1 || \
  mk_prepare_receptor.py -i 6rih_chainA_protein.pdb -o 6rih_chainA_protein.pdbqt 2>&1 || true
fi

# Fallback: use prepare_receptor4 from AutoDockTools if available
if [ ! -f 6rih_chainA_protein.pdbqt ] && command -v prepare_receptor4.py > /dev/null 2>&1; then
  prepare_receptor4.py -r 6rih_chainA_protein.pdb -o 6rih_chainA_protein.pdbqt -A "hydrogens" 2>&1 || true
fi

# Last resort: try vina_split / openbabel obabel
if [ ! -f 6rih_chainA_protein.pdbqt ]; then
  python <<PYEOF
# Direct conversion via meeko PDBQTReceptor (avoid CLI)
from meeko import PDBQTReceptor
from pathlib import Path
import sys
try:
    rec = PDBQTReceptor("6rih_chainA_protein.pdb")
    out = Path("6rih_chainA_protein.pdbqt")
    out.write_text(rec.write_pdbqt_string())
    print(f"[vina_setup] meeko python wrote {out}")
except Exception as e:
    print(f"[vina_setup] FALLBACK FAIL: {e}", file=sys.stderr)
    sys.exit(1)
PYEOF
fi

ls -la "$RECEPTOR_DIR"
[ -f "$RECEPTOR_DIR/6rih_chainA_protein.pdbqt" ] && echo "[vina_setup] receptor PDBQT ready" || { echo "[vina_setup] FAIL: no PDBQT receptor"; exit 3; }

echo "[vina_setup] done $(date -u +%FT%TZ)"
