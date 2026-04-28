#!/bin/bash
#SBATCH --job-name=clm_r4_pretrain
#SBATCH --partition=pascalnodes
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --time=12:00:00
#SBATCH --output=logs/clm_r4_pretrain_%j.out
#SBATCH --error=logs/clm_r4_pretrain_%j.err

set -euo pipefail
echo "[r4_pretrain] start $(date -u +%FT%TZ) on $(hostname) jobid=$SLURM_JOB_ID"
nvidia-smi | head -20 || true

DATA=/data/user/$USER/aim4_clm
OUT=$DATA/runs/round4_pretrain_$SLURM_JOB_ID
mkdir -p "$OUT"

# A100 I/O discipline: stage data to local SSD
LOCAL=/local/$USER/$SLURM_JOB_ID
mkdir -p "$LOCAL"
cp "$DATA/bioactives.smi" "$LOCAL/"

module reset
module load Miniforge3/latest

# Build a fresh env with selfies + torch (extends clm-lstm)
if ! conda env list | grep -q "^clm-trans "; then
  echo "[r4_pretrain] creating env clm-trans"
  mamba create -n clm-trans -y -c conda-forge \
    python=3.11 numpy tqdm rdkit selfies
  source activate clm-trans
  pip install --quiet --extra-index-url https://download.pytorch.org/whl/cu121 \
    "torch==2.4.*"
else
  echo "[r4_pretrain] env clm-trans already exists"
  source activate clm-trans
fi

python -c "import torch, selfies, rdkit; print('torch', torch.__version__, 'cuda', torch.cuda.is_available()); print('selfies', selfies.__version__); print('rdkit', rdkit.__version__)"

cd "$HOME/jobs/aim4_clm"

python pretrain_transformer.py \
  --data "$LOCAL/bioactives.smi" \
  --out "$OUT" \
  --epochs 10 \
  --batch 128 \
  --max-len 128 \
  --d-model 512 \
  --n-heads 8 \
  --n-layers 8 \
  --ffn-dim 1024 \
  --lr 3e-4 \
  --workers 4

echo "[r4_pretrain] artifacts in $OUT:"
ls -la "$OUT"
echo "[r4_pretrain] done $(date -u +%FT%TZ)"
