#!/bin/bash
#SBATCH --job-name=sweep
#SBATCH --partition=short
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=02:00:00
#SBATCH --array=0-9%4                    # 10 tasks, 4 at a time
#SBATCH --output=%x_%A_%a.out
#SBATCH --error=%x_%A_%a.err

set -euo pipefail

# Each task reads its index from SLURM_ARRAY_TASK_ID
PARAMS=(0.01 0.03 0.1 0.3 1.0 3.0 10.0 30.0 100.0 300.0)
LR=${PARAMS[$SLURM_ARRAY_TASK_ID]}

echo "Task $SLURM_ARRAY_TASK_ID running with lr=$LR on $(hostname)"

module reset
module load Python/3.11
python train.py --lr $LR --out results_${SLURM_ARRAY_JOB_ID}_${SLURM_ARRAY_TASK_ID}
