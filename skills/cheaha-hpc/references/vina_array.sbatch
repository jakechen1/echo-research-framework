#!/bin/bash
#SBATCH --job-name=phgdh-vina-top20
#SBATCH --partition=short
#SBATCH --time=00:30:00
#SBATCH --mem=3G
#SBATCH --cpus-per-task=2
#SBATCH --array=1-20
#SBATCH --output=/home/jakechen/phgdh-sbdd/logs/vina_top20_%A_%a.out
#SBATCH --error=/home/jakechen/phgdh-sbdd/logs/vina_top20_%A_%a.err

set -euo pipefail
cd /home/jakechen/phgdh-sbdd
source /etc/profile.d/modules.sh
module load AutoDock_Vina/1.1.2_linux_x86 Miniforge3/24.3.0-0
CONDA_BIN=$(which conda)
source $(dirname $(dirname $CONDA_BIN))/etc/profile.d/conda.sh
conda activate phgdh-sbdd

# CSV columns: rank, pchembl, smiles, chembl_id, assay_type, standard_type, standard_value, standard_units
# Row number = array_task_id + 1 (to skip header)
ROW=$((SLURM_ARRAY_TASK_ID + 1))
LINE=$(sed -n "${ROW}p" data/aim2_top20_inhibitors.csv)
PV=$(echo "$LINE"  | awk -F, '{print $2}')
SMI=$(echo "$LINE" | awk -F, '{print $3}')
CID=$(echo "$LINE" | awk -F, '{print $4}')
echo "[$(date)] array_id=$SLURM_ARRAY_TASK_ID row=$ROW  pv=$PV  cid=$CID  smi=$SMI"

# Prep ligand
python - "$SMI" "$CID" "$SLURM_ARRAY_TASK_ID" <<PY
import sys
from rdkit import Chem
from rdkit.Chem import AllChem
smi, cid, aid = sys.argv[1], sys.argv[2], sys.argv[3]
m = Chem.MolFromSmiles(smi)
if m is None:
    print(f"ERROR parse failed for SMILES: {smi!r}"); sys.exit(2)
m = Chem.AddHs(m)
AllChem.EmbedMolecule(m, randomSeed=42)
try: AllChem.MMFFOptimizeMolecule(m)
except Exception as e: print(f"opt warn: {e}")
Chem.MolToMolFile(m, f"data/array_lig_{aid}.mol")
print(f"ok lig_{aid} {cid} pv_handled atoms={m.GetNumAtoms()}")
PY

obabel data/array_lig_${SLURM_ARRAY_TASK_ID}.mol \
       -O data/array_lig_${SLURM_ARRAY_TASK_ID}.pdbqt \
       --partialcharge gasteiger 2>&1 | tail -1

if [ ! -f data/receptor6rih.pdbqt ]; then
  grep -E "^(ATOM|TER|END)" data/pdbs/6RIH.pdb > data/receptor6rih_clean.pdb
  obabel data/receptor6rih_clean.pdb -O data/receptor6rih.pdbqt -xr 2>&1 | tail -1
fi

vina --receptor data/receptor6rih.pdbqt \
     --ligand   data/array_lig_${SLURM_ARRAY_TASK_ID}.pdbqt \
     --center_x 14.11 --center_y 10.46 --center_z 80.98 \
     --size_x 25 --size_y 25 --size_z 25 \
     --exhaustiveness 8 --num_modes 5 \
     --out    results/array_lig_${SLURM_ARRAY_TASK_ID}.pdbqt \
     2>&1 | tee logs/vina_array_${SLURM_ARRAY_TASK_ID}.log

BEST=$(grep -E '^\s+1\s+' logs/vina_array_${SLURM_ARRAY_TASK_ID}.log | head -1 | awk '{print $2}')
(flock -x 200; echo -e "$CID\t$PV\t$BEST" >> results/top20_scores.tsv) 200>results/scores.lock
echo "[$(date)] array_id=$SLURM_ARRAY_TASK_ID done, best_dG=$BEST"
