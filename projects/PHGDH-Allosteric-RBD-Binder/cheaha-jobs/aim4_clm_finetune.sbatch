#!/bin/bash
#SBATCH --job-name=clm_ft_round3
#SBATCH --partition=amperenodes
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=48G
#SBATCH --gres=gpu:1
#SBATCH --time=02:00:00
#SBATCH --output=logs/clm_ft_round3_%j.out
#SBATCH --error=logs/clm_ft_round3_%j.err

set -euo pipefail
echo "[ft+sample] start $(date -u +%FT%TZ) on $(hostname) jobid=$SLURM_JOB_ID"
nvidia-smi | head -20 || true

DATA=/data/user/$USER/aim4_clm
PRETRAIN_RUN=$DATA/runs/38298494
OUT=$DATA/runs/round3_$SLURM_JOB_ID
mkdir -p "$OUT"

# Stage data to local SSD for A100 I/O discipline
LOCAL=/local/$USER/$SLURM_JOB_ID
mkdir -p "$LOCAL"
cp "$PRETRAIN_RUN/best.pt" "$LOCAL/"
cp "$PRETRAIN_RUN/vocab.json" "$LOCAL/"
cp "$DATA"/bucket_pv*.smi "$LOCAL/" 2>/dev/null || { echo "FAIL: bucket_pv*.smi missing on cheaha"; exit 2; }
ls -la "$LOCAL"/

module reset
module load Miniforge3/latest
source activate clm-lstm

python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available(), 'gpu', torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'NONE')"

# 1) Fine-tune (5-stage incremental)
echo "[ft+sample] === FINE-TUNE ==="
python finetune_lstm.py \
  --pretrain "$LOCAL/best.pt" \
  --vocab "$LOCAL/vocab.json" \
  --buckets "$LOCAL/bucket_pv5.smi,$LOCAL/bucket_pv6.smi,$LOCAL/bucket_pv7.smi,$LOCAL/bucket_pv8.smi,$LOCAL/bucket_pv9.smi" \
  --out "$OUT" \
  --epochs-per-stage 8 \
  --batch 64 \
  --lr 1e-4

# Copy vocab into out for downstream use
cp "$LOCAL/vocab.json" "$OUT/vocab.json"

# 2) Sample 10K, validate with RDKit, rank by perplexity
echo "[ft+sample] === SAMPLE ==="
python sample_lstm.py \
  --checkpoint "$OUT/ft_final.pt" \
  --vocab "$OUT/vocab.json" \
  --out "$OUT/candidates.csv" \
  --n 10000 \
  --temperatures 0.8,1.0,1.2 \
  --known-actives "$LOCAL/bucket_pv5.smi" \
  --top-k 1000

echo "[ft+sample] artifacts in $OUT:"
ls -la "$OUT"
echo "[ft+sample] done $(date -u +%FT%TZ)"
