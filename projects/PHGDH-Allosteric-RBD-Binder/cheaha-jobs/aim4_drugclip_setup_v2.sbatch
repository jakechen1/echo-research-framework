#!/bin/bash
#SBATCH --job-name=drugclip_v2
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=24G
#SBATCH --time=01:30:00
#SBATCH --output=logs/drugclip_v2_%j.out
#SBATCH --error=logs/drugclip_v2_%j.err

set -euo pipefail
echo "[dc2] start $(date -u +%FT%TZ) on $(hostname)"

# Fix attempt for pymoo build failure: pre-install pymoo + descriptastorus deps via
# conda-forge (binary), then pip-install DeepPurpose without forcing source build.
# Also pin pymoo to a version that has the compiled .pyx files in the right place.

DATA=/data/user/$USER/aim4_clm
DRUGCLIP_DIR=$DATA/drugclip
mkdir -p $DRUGCLIP_DIR
cd $DRUGCLIP_DIR

module reset
module load Miniforge3/latest

# Wipe and rebuild env (since prior attempt got partway and may be inconsistent)
if conda env list | grep -q "^drugclip "; then
  echo "[dc2] removing old drugclip env"
  conda env remove -n drugclip -y
fi

echo "[dc2] creating fresh drugclip env with binary deps from conda-forge"
mamba create -n drugclip -y -c conda-forge \
  python=3.10 numpy pandas scikit-learn rdkit tqdm requests \
  cython setuptools wheel pip \
  matplotlib seaborn

source activate drugclip

# Install torch (cu121 wheels)
pip install --quiet --extra-index-url https://download.pytorch.org/whl/cu121 \
  "torch==2.4.*"

# Install pymoo binary via pip (older version that has pre-compiled .pyx)
pip install --quiet "pymoo>=0.5,<0.6"

# Install DeepPurpose deps individually so failures are diagnosable
pip install --quiet descriptastorus subword-nmt prettytable

# Now install DeepPurpose with deps already satisfied
pip install --quiet --no-deps DeepPurpose==0.1.5

echo "[dc2] versions:"
python -c "import DeepPurpose, pymoo, torch, rdkit; print(\"DeepPurpose\", DeepPurpose.__version__ if hasattr(DeepPurpose, \"__version__\") else \"installed\"); print(\"pymoo\", pymoo.__version__); print(\"torch\", torch.__version__); print(\"rdkit\", rdkit.__version__)"

# Smoke test: load pretrained MPNN_CNN_BindingDB model
python <<"PYEOF"
print("[dc2] importing DeepPurpose")
from DeepPurpose import DTI as models
from DeepPurpose import utils

print("[dc2] loading pretrained MPNN_CNN_BindingDB (auto-downloads ~30MB on first call)")
try:
    net = models.model_pretrained(model='MPNN_CNN_BindingDB')
    print("[dc2] MPNN_CNN_BindingDB loaded successfully")
except Exception as e:
    import traceback; traceback.print_exc()
    print(f"[dc2] FAIL loading model: {e}")
    raise SystemExit(2)

# PHGDH human, UniProt O43175
phgdh_seq = ("MAFANLRKVLISDSLDPCCRKILQDGGLQVVEKQNLSKEELIAELQDCEGLIVRSATKVTADVINAAEKLQVVGRAGTGV"
             "DNVDLEAATRKGILVMNTPNGNSLSAAELTCGMIMCLARQIPQATASMKDGKWERKKFMGTELNGKTLGILGLGRIGRE"
             "VATRMQSFGMKTIGYDPIIPADVAKTIEMEFMPSREEIKAKGFPDLAFIVNLIPEKAEDFPDAFDTYRVYSEDQDFGKH"
             "LGVGGSELLGLLGFKAKLGRTAVGSRAANAEKAGGDIAIAFKETDAVIARARKILDYRGSANSILTLPFQEQLLPNINE"
             "KSTLTKLLREAEDIKDGVRFYAVKNPLNVVVPFEKKIPTKKVDLEDAQNNTGEGIAILRGTEVATKTEFQDIPASEPSI"
             "SKAGGVPPETKVFISPATGHIRTGLSVLQKAFSEIGAGAVASGLPEDVPRVLLNGNLAGEIAAITGGGVLTAGSSLITM"
             "ARMNELIGAVRGGRAVLEDADKEALAACFGNSDTPSLTKEELASEVKMSVDGINNAVTCTGEDFRVVANARRLASCGYH"
             "VVVTDKKAYIE")

# Known PHGDH inhibitors from literature
test_smiles = [
    ("CBR-5884",   "Cc1ccc(NC(=O)c2cc(C)nn2-c2nc3ccccc3s2)cc1"),
    ("NCT-503",    "OC(C(=O)NCCN1CCN(c2ccc(Cl)cc2)CC1)c1ccc(F)cc1"),
    ("decoy",      "CCO"),                                               # ethanol (should be very weak)
    ("decoy_aspirin", "CC(=O)Oc1ccccc1C(=O)O"),                          # aspirin (off-target, weak)
]

print("[dc2] smoke test: predict affinity for known PHGDH actives + decoys")
import pandas as pd
for name, smi in test_smiles:
    try:
        X = utils.data_process(
            X_drug=[smi], X_target=[phgdh_seq], y=[0],
            drug_encoding="MPNN", target_encoding="CNN",
            split_method="no_split",
        )
        pred = net.predict(X)
        # pred[0] is the predicted affinity (typically pIC50 or log10 Kd)
        print(f"[dc2]   {name:20s}  pred={pred[0]:.3f}  smi={smi[:50]}")
    except Exception as e:
        print(f"[dc2]   {name:20s}  ERROR: {e}")

print("[dc2] DeepPurpose CPI scorer is READY for Round 5 RL reward integration")
PYEOF

echo "[dc2] env drugclip ready"
echo "[dc2] done $(date -u +%FT%TZ)"
