#!/bin/bash
#SBATCH --job-name=counter_recep
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:20:00
#SBATCH --output=logs/counter_recep_%j.out
#SBATCH --error=logs/counter_recep_%j.err

set -euo pipefail
echo "[crep] start $(date -u +%FT%TZ) on $(hostname)"

DATA=/data/user/$USER/aim4_clm
RECEPTOR_DIR=$DATA/receptors
mkdir -p $RECEPTOR_DIR
cd $RECEPTOR_DIR

module reset
module load Miniforge3/latest
source activate vina-py

# Counter-receptors:
#   PSAT1 (Phosphoserine aminotransferase) — PDB 3E77
#   PSPH  (Phosphoserine phosphatase)       — PDB 1L7M
# These are the same-pathway homologs; selectivity over them is critical.

declare -A PDBS=(
  [psat1]=3E77
  [psph]=1L7M
)

for name in "${!PDBS[@]}"; do
  pdb_id=${PDBS[$name]}
  pdb_lc=$(echo $pdb_id | tr '"'"'A-Z'"'"' '"'"'a-z'"'"')
  echo
  echo "[crep] === $name ($pdb_id) ==="

  PDB=$RECEPTOR_DIR/${pdb_lc}.pdb
  if [ ! -f "$PDB" ]; then
    curl -sSfL --retry 3 -o "$PDB" "https://files.rcsb.org/download/${pdb_id}.pdb"
  fi
  ls -la $PDB

  # Extract chain A protein-only + HET ligands separately
  python <<PYEOF
from pathlib import Path
src = Path("${pdb_lc}.pdb")
prot_lines, het_lines = [], []
for line in src.read_text().splitlines():
    if line.startswith(("ATOM", "TER")) and (len(line) >= 22 and line[21] == "A"):
        prot_lines.append(line)
    elif line.startswith("HETATM") and (len(line) >= 22 and line[21] == "A"):
        # skip waters
        if line[17:20].strip() not in ("HOH", "WAT"):
            het_lines.append(line)
prot_only = Path("${pdb_lc}_chainA_protein.pdb")
prot_only.write_text("\n".join(prot_lines + ["END"]))
het_path = Path("${pdb_lc}_chainA_het.pdb")
het_path.write_text("\n".join(het_lines + ["END"]))
print(f"[crep:${name}] protein lines={len(prot_lines)} het lines={len(het_lines)}")
PYEOF

  # PDBQT receptor via OpenBabel (we know this works from Round 3)
  if [ ! -f ${pdb_lc}_chainA_protein.pdbqt ]; then
    obabel -i pdb ${pdb_lc}_chainA_protein.pdb -o pdbqt -O ${pdb_lc}_chainA_protein.pdbqt -xr 2>&1 | tail -5
  fi
  ls -la ${pdb_lc}_chainA_protein.pdbqt

  # Pocket center: use HET ligand centroid if present; else fpocket / chain-A centroid fallback
  python <<PYEOF
import json
from pathlib import Path
import numpy as np

def centroid(pdb_path):
    coords = []
    for line in Path(pdb_path).read_text().splitlines():
        if line.startswith(("ATOM", "HETATM")):
            try:
                coords.append((float(line[30:38]), float(line[38:46]), float(line[46:54])))
            except ValueError: pass
    if not coords: return None
    arr = np.array(coords)
    return arr.mean(axis=0).tolist(), arr.min(axis=0).tolist(), arr.max(axis=0).tolist()

het = Path("${pdb_lc}_chainA_het.pdb")
prot = Path("${pdb_lc}_chainA_protein.pdb")
het_info = centroid(het)
if het_info and het_info[0]:
    center, lo, hi = het_info
    span = [hi[i] - lo[i] for i in range(3)]
    box_size = [max(20.0, span[i] + 8.0) for i in range(3)]
    src = "HET ligand centroid"
else:
    fb = centroid(prot)
    center = fb[0] if fb else [0,0,0]
    box_size = [22.0, 22.0, 22.0]
    src = "WARN chain-A centroid (no HET; review pocket)"

cfg = {
    "name": "${name}",
    "pdb_id": "${pdb_id}",
    "receptor_pdb": "${pdb_lc}_chainA_protein.pdb",
    "receptor_pdbqt": "${pdb_lc}_chainA_protein.pdbqt",
    "pocket_center": center,
    "pocket_box_size": box_size,
    "pocket_source": src,
    "exhaustiveness": 8,
    "n_poses": 5,
}
out = Path("pocket_config_${name}.json")
out.write_text(json.dumps(cfg, indent=2))
print(out.read_text())
PYEOF

  # Smoke test: load with vina
  python -c "from vina import Vina; v = Vina(sf_name='vina', verbosity=0); v.set_receptor('${pdb_lc}_chainA_protein.pdbqt'); print('[crep:${name}] vina loaded OK')"
done

echo
echo "[crep] all counter-receptors prepared:"
ls -la $RECEPTOR_DIR/*.pdbqt $RECEPTOR_DIR/pocket_config_*.json
echo "[crep] done $(date -u +%FT%TZ)"
