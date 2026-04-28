#!/bin/bash
#SBATCH --job-name=clm_r5_dock
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=01:30:00
#SBATCH --output=logs/clm_r5_dock_%A_%a.out
#SBATCH --error=logs/clm_r5_dock_%A_%a.err
#SBATCH --array=0-24

set -euo pipefail
echo "[r5d] start $(date -u +%FT%TZ) on $(hostname) job=$SLURM_JOB_ID array=$SLURM_ARRAY_TASK_ID"

# Auto-discover the latest Round 5 RL output dir
DATA=/data/user/$USER/aim4_clm
ROUND_DIR=$(ls -dt $DATA/runs/round5_rl_* 2>/dev/null | head -1)
if [ -z "$ROUND_DIR" ]; then
  echo "FAIL: no round5_rl_* dir found"; exit 2
fi
echo "[r5d] using $ROUND_DIR"
[ -f "$ROUND_DIR/rl_candidates.csv" ] || { echo "FAIL: no rl_candidates.csv"; exit 3; }
RECEPTORS=$DATA/receptors
mkdir -p "$ROUND_DIR/dock_results"

CHUNK_SIZE=40
module reset
module load Miniforge3/latest
source activate vina-py

cd "$HOME/jobs/aim4_clm"

python vina_dock_chunk.py \
  --candidates "$ROUND_DIR/rl_candidates.csv" \
  --receptor "$RECEPTORS/6rih_chainA_protein.pdbqt" \
  --pocket-config "$RECEPTORS/pocket_config.json" \
  --out "$ROUND_DIR/dock_results/chunk_${SLURM_ARRAY_TASK_ID}.csv" \
  --task-id "$SLURM_ARRAY_TASK_ID" \
  --chunk-size $CHUNK_SIZE \
  --exhaustiveness 8 \
  --n-poses 5 \
  --cpu 2

echo "[r5d] task $SLURM_ARRAY_TASK_ID done $(date -u +%FT%TZ)"
