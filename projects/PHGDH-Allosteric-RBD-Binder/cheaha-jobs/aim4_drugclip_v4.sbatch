#!/bin/bash
#SBATCH --job-name=drugclip_v4
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:25:00
#SBATCH --output=logs/drugclip_v4_%j.out
#SBATCH --error=logs/drugclip_v4_%j.err

set -euo pipefail
echo "[dc4] start $(date -u +%FT%TZ)"

module reset
module load Miniforge3/latest
source activate drugclip

# v3 failed on xgboost source build (no cmake). Fix: install xgboost via conda-forge BINARY.
# Also install all other transitive deps as binaries from conda where available.
echo "[dc4] installing binary xgboost + other deps from conda-forge"
mamba install -n drugclip -y -c conda-forge \
  xgboost lifelines statsmodels scipy networkx biopython \
  prettytable seaborn matplotlib

# Verify imports BEFORE trying DeepPurpose load (catches any missing deps fast)
python <<"PYEOF"
import sys
mods = ["torch","rdkit","pymoo","xgboost","lifelines","statsmodels","scipy","networkx","biopython","prettytable","seaborn","matplotlib"]
miss = []
for m in mods:
    try: __import__(m)
    except ImportError as e: miss.append(f"{m}: {e}")
if miss:
    print("[dc4] MISSING:")
    for x in miss: print(f"  - {x}")
    sys.exit(2)
print("[dc4] all base deps importable")
PYEOF

# Try the DeepPurpose import
python <<"PYEOF"
print("[dc4] importing DeepPurpose")
from DeepPurpose import DTI as models
from DeepPurpose import utils
print("[dc4] imports OK")

print("[dc4] loading pretrained MPNN_CNN_BindingDB")
net = models.model_pretrained(model="MPNN_CNN_BindingDB")
print("[dc4] model loaded")

phgdh_seq = ("MAFANLRKVLISDSLDPCCRKILQDGGLQVVEKQNLSKEELIAELQDCEGLIVRSATKVTADVINAAEKLQVVGRAGTGV"
             "DNVDLEAATRKGILVMNTPNGNSLSAAELTCGMIMCLARQIPQATASMKDGKWERKKFMGTELNGKTLGILGLGRIGRE"
             "VATRMQSFGMKTIGYDPIIPADVAKTIEMEFMPSREEIKAKGFPDLAFIVNLIPEKAEDFPDAFDTYRVYSEDQDFGKH"
             "LGVGGSELLGLLGFKAKLGRTAVGSRAANAEKAGGDIAIAFKETDAVIARARKILDYRGSANSILTLPFQEQLLPNINE"
             "KSTLTKLLREAEDIKDGVRFYAVKNPLNVVVPFEKKIPTKKVDLEDAQNNTGEGIAILRGTEVATKTEFQDIPASEPSI"
             "SKAGGVPPETKVFISPATGHIRTGLSVLQKAFSEIGAGAVASGLPEDVPRVLLNGNLAGEIAAITGGGVLTAGSSLITM"
             "ARMNELIGAVRGGRAVLEDADKEALAACFGNSDTPSLTKEELASEVKMSVDGINNAVTCTGEDFRVVANARRLASCGYH"
             "VVVTDKKAYIE")

tests = [
    ("CBR-5884",       "Cc1ccc(NC(=O)c2cc(C)nn2-c2nc3ccccc3s2)cc1"),
    ("NCT-503",        "OC(C(=O)NCCN1CCN(c2ccc(Cl)cc2)CC1)c1ccc(F)cc1"),
    ("ethanol",        "CCO"),
    ("aspirin",        "CC(=O)Oc1ccccc1C(=O)O"),
]
for name, smi in tests:
    X = utils.data_process(X_drug=[smi], X_target=[phgdh_seq], y=[0],
                           drug_encoding="MPNN", target_encoding="CNN", split_method="no_split")
    p = net.predict(X)
    print(f"[dc4]   {name:12s}  pred={p[0]:.3f}  smi={smi[:50]}")
print("[dc4] DeepPurpose MPNN_CNN scorer READY")
PYEOF

echo "[dc4] done $(date -u +%FT%TZ)"
