#!/bin/bash
#SBATCH --job-name=clm_setup
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=01:30:00
#SBATCH --output=logs/clm_setup_%j.out
#SBATCH --error=logs/clm_setup_%j.err

set -euo pipefail
echo "[setup] start $(date -u +%FT%TZ) on $(hostname)"

CHEMBL_VERSION="${CHEMBL_VERSION:-35}"
DATA=/data/user/$USER/aim4_clm
CHEMBL_DIR=$DATA/chembl
mkdir -p $DATA $CHEMBL_DIR

module reset
module load Miniforge3/latest

# 1) Build conda env (idempotent)
if ! conda env list | grep -q "^clm-lstm "; then
  echo "[setup] creating env clm-lstm"
  mamba create -n clm-lstm -y -c conda-forge \
      python=3.11 numpy tqdm rdkit
  source activate clm-lstm
  pip install --quiet --extra-index-url https://download.pytorch.org/whl/cu121 \
      "torch==2.4.*"
else
  echo "[setup] env clm-lstm already exists"
  source activate clm-lstm
fi

python -c "import torch, rdkit, sys; print('torch=', torch.__version__, 'cuda=', torch.cuda.is_available()); print('rdkit=', rdkit.__version__); print('py=', sys.version.split()[0])"

# 2) Download ChEMBL SQLite bulk (skip if present)
TARBALL=$CHEMBL_DIR/chembl_${CHEMBL_VERSION}_sqlite.tar.gz
DB=$CHEMBL_DIR/chembl_${CHEMBL_VERSION}/chembl_${CHEMBL_VERSION}_sqlite/chembl_${CHEMBL_VERSION}.db
if [ ! -f "$DB" ]; then
  if [ ! -f "$TARBALL" ]; then
    URL="https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_${CHEMBL_VERSION}/chembl_${CHEMBL_VERSION}_sqlite.tar.gz"
    echo "[setup] downloading $URL"
    curl -sSfL --retry 3 -o "$TARBALL" "$URL"
  fi
  echo "[setup] extracting $TARBALL"
  tar -xzf "$TARBALL" -C "$CHEMBL_DIR"
else
  echo "[setup] db already extracted"
fi
ls -la "$DB"

# 3) Extract bioactives via SQL — optimized: PRAGMA mmap + temp table + reordered join
OUT=$DATA/bioactives.smi
if [ ! -f "$OUT" ] || [ "$(wc -l <"$OUT")" -lt 100000 ]; then
  echo "[setup] extracting bioactives -> $OUT"
  python extract_bioactives.py "$DB" "$OUT"
fi

echo "[setup] bioactives count = $(wc -l <"$OUT")"
echo "[setup] done $(date -u +%FT%TZ)"
