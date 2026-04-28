#!/bin/bash
#SBATCH --job-name=clm_pretrain
#SBATCH --partition=amperenodes
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --gres=gpu:1
#SBATCH --time=08:00:00
#SBATCH --output=logs/clm_pretrain_%j.out
#SBATCH --error=logs/clm_pretrain_%j.err

set -euo pipefail
echo "[pretrain] start $(date -u +%FT%TZ) on $(hostname) jobid=$SLURM_JOB_ID"
nvidia-smi || true

DATA=/data/user/$USER/aim4_clm
DATAFILE=$DATA/bioactives.smi
RUN=$DATA/runs/$SLURM_JOB_ID
mkdir -p "$RUN"
[ -f "$DATAFILE" ] || { echo "[pretrain] FAIL: $DATAFILE missing"; exit 2; }

# A100 I/O discipline: stage data to local SSD
LOCAL=/local/$USER/$SLURM_JOB_ID
mkdir -p "$LOCAL"
cp "$DATAFILE" "$LOCAL/bioactives.smi"

module reset
module load Miniforge3/latest
source activate clm-lstm

python -c "import torch; print(\"[pretrain] torch\", torch.__version__, \"cuda=\", torch.cuda.is_available()); print(\"[pretrain] gpu\", torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"NONE\")"

python pretrain_lstm.py \
  --data "$LOCAL/bioactives.smi" \
  --out "$RUN" \
  --epochs 30 --batch 256 --workers 4 \
  --hidden 512 --embed 128 --layers 3 --dropout 0.2 \
  --lr 1e-3 --weight-decay 1e-5

echo "[pretrain] artifacts in $RUN:"
ls -la "$RUN"
echo "[pretrain] done $(date -u +%FT%TZ)"
