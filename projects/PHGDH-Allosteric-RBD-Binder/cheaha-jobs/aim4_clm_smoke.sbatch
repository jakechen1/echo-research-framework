#!/bin/bash
#SBATCH --job-name=clm_smoke
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:15:00
#SBATCH --output=logs/clm_smoke_%j.out
#SBATCH --error=logs/clm_smoke_%j.err

set -euo pipefail
echo "[smoke] start $(date -u +%FT%TZ) on $(hostname) jobid=$SLURM_JOB_ID"

DATA=/data/user/$USER/aim4_clm
DATAFILE=$DATA/bioactives.smi
RUN=$DATA/runs/smoke_$SLURM_JOB_ID
mkdir -p $RUN

[ -f "$DATAFILE" ] || { echo "[smoke] FAIL: $DATAFILE missing — run setup first"; exit 2; }

module reset
module load Miniforge3/latest
source activate clm-lstm

python -c "import torch; print(\"[smoke] torch\", torch.__version__, \"cuda=\", torch.cuda.is_available())"

# 1k SMILES, 2 epochs, batch 64, no GPU. Verifies env+data+ckpt path.
python pretrain_lstm.py \
  --data "$DATAFILE" \
  --out "$RUN" \
  --limit 1000 --epochs 2 --batch 64 --workers 2

echo "[smoke] checkpoints:"
ls -la "$RUN"
[ -s "$RUN/best.pt" ] && [ -s "$RUN/vocab.json" ] && [ -s "$RUN/loss.csv" ] || { echo "[smoke] FAIL: missing artifacts"; exit 3; }
echo "[smoke] done $(date -u +%FT%TZ)"
