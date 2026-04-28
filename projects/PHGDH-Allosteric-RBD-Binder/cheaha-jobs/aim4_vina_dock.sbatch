#!/bin/bash
#SBATCH --job-name=vina_dock_round3
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=01:30:00
#SBATCH --output=logs/vina_dock_%A_%a.out
#SBATCH --error=logs/vina_dock_%A_%a.err
#SBATCH --array=0-24

set -euo pipefail
echo "[dock] start $(date -u +%FT%TZ) on $(hostname) job=$SLURM_JOB_ID array_id=$SLURM_ARRAY_TASK_ID"

# These are set by the submitter (export ROUND_DIR=...)
ROUND_DIR=${ROUND_DIR:-/data/user/$USER/aim4_clm/runs/round3_38299884}
RECEPTORS=${RECEPTORS:-/data/user/$USER/aim4_clm/receptors}
CHUNK_SIZE=${CHUNK_SIZE:-40}

mkdir -p "$ROUND_DIR/dock_results"

module reset
module load Miniforge3/latest
source activate vina-py

cd "$HOME/jobs/aim4_clm"

python vina_dock_chunk.py \
  --candidates "$ROUND_DIR/candidates.csv" \
  --receptor "$RECEPTORS/6rih_chainA_protein.pdbqt" \
  --pocket-config "$RECEPTORS/pocket_config.json" \
  --out "$ROUND_DIR/dock_results/chunk_${SLURM_ARRAY_TASK_ID}.csv" \
  --task-id "$SLURM_ARRAY_TASK_ID" \
  --chunk-size "$CHUNK_SIZE" \
  --exhaustiveness 8 \
  --n-poses 5 \
  --cpu 2

echo "[dock] task $SLURM_ARRAY_TASK_ID done $(date -u +%FT%TZ)"
