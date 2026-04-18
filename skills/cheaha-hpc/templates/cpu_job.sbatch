#!/bin/bash
#SBATCH --job-name=cpu_example
#SBATCH --partition=express              # 2h limit, fast queue
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=jakechen@uab.edu

set -euo pipefail

echo "Job $SLURM_JOB_ID on $(hostname) at $(date)"
echo "Allocated: $SLURM_CPUS_PER_TASK CPUs, ${SLURM_MEM_PER_NODE}MB RAM"

module reset
module load Python/3.11                  # example; adjust as needed

# ---- your work here ----
python -c "import os; print('hello from', os.uname().nodename)"

echo "Done at $(date)"
