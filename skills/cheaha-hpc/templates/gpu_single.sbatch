#!/bin/bash
#SBATCH --job-name=gpu_example
#SBATCH --partition=amperenodes          # or pascalnodes for smaller model
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8                # 2+ per GPU; 8 is healthy
#SBATCH --mem=48G
#SBATCH --gres=gpu:1
#SBATCH --time=02:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

set -euo pipefail

echo "Job $SLURM_JOB_ID on $(hostname) at $(date)"
nvidia-smi

module reset
module load CUDA/12.6.0
# module load cuDNN/8.9.2.26-CUDA-12.2.0  # uncomment if needed
# module load Anaconda3                    # or whatever your env loader is

# Stage inputs to local SSD (A100 speed discipline)
LOCAL=/local/$USER/$SLURM_JOB_ID
mkdir -p $LOCAL
# cp -r /data/user/$USER/my_inputs $LOCAL/

# ---- your training/inference command ----
python my_gpu_script.py

# Copy results off the node before exit
# cp -r $LOCAL/output /data/user/$USER/results/$SLURM_JOB_ID/

echo "Done at $(date)"
