#!/bin/bash
#SBATCH --job-name=gpu_multi
#SBATCH --partition=amperenodes
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --ntasks-per-socket=1            # REQUIRED for multi-GPU
#SBATCH --cpus-per-task=8
#SBATCH --mem=96G
#SBATCH --gres=gpu:2
#SBATCH --time=04:00:00
#SBATCH --output=%x_%j.out
#SBATCH --error=%x_%j.err

set -euo pipefail

module reset
module load CUDA/12.6.0

nvidia-smi -L
echo "CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES"

# Typical DDP-style launch (PyTorch) — adjust for your framework
# torchrun --standalone --nproc_per_node=2 train.py

python my_multi_gpu_script.py
