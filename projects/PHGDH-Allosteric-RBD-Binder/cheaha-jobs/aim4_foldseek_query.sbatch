#!/bin/bash
#SBATCH --job-name=foldseek_phgdh
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --time=01:00:00
#SBATCH --output=logs/foldseek_phgdh_%j.out
#SBATCH --error=logs/foldseek_phgdh_%j.err

set -euo pipefail
echo "[fs] start $(date -u +%FT%TZ) on $(hostname)"

DATA=/data/user/$USER/aim4_clm
QUERY=$DATA/receptors/6rih_chainA_protein.pdb
WORK=$DATA/foldseek
mkdir -p $WORK
cd $WORK

module reset
module load Miniforge3/latest

# Install foldseek in dedicated env (idempotent)
if ! conda env list | grep -q "^foldseek "; then
  echo "[fs] creating env foldseek"
  mamba create -n foldseek -y -c conda-forge -c bioconda foldseek
fi
source activate foldseek
which foldseek && echo "foldseek installed"

# Download PDB database (smaller, ~5GB; afdb50 would be ~50GB and longer)
DB_DIR=$DATA/foldseek_db/pdb
if [ ! -d "$DB_DIR" ]; then
  echo "[fs] downloading PDB database"
  mkdir -p $DB_DIR
  foldseek databases PDB $DB_DIR/pdb $DATA/foldseek_db/tmp
else
  echo "[fs] PDB database already present"
fi
ls -la $DB_DIR/

# Run easy-search: 6RIH chain A (PHGDH allosteric) → PDB neighbors
echo "[fs] running easy-search"
foldseek easy-search \
  $QUERY \
  $DB_DIR/pdb \
  $WORK/6rih_pdb_hits.m8 \
  $WORK/tmp \
  --max-seqs 200 \
  --threads 8 \
  --format-output "query,target,fident,alnlen,mismatch,gapopen,qstart,qend,tstart,tend,evalue,bits,prob,alntmscore"

echo "[fs] top 50 hits ==="
sort -k14 -g -r $WORK/6rih_pdb_hits.m8 | head -50 > $WORK/6rih_top50.tsv
head -10 $WORK/6rih_top50.tsv

echo
echo "[fs] unique target chains:"
awk "{print \$2}" $WORK/6rih_top50.tsv | sort -u | wc -l
awk "{print \$2}" $WORK/6rih_top50.tsv | sort -u | head -20

echo "[fs] done $(date -u +%FT%TZ)"
