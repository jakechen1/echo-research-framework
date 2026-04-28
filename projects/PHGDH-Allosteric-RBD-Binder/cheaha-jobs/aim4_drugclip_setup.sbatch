#!/bin/bash
#SBATCH --job-name=drugclip_setup
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=01:00:00
#SBATCH --output=logs/drugclip_setup_%j.out
#SBATCH --error=logs/drugclip_setup_%j.err

set -euo pipefail
echo "[dc] start $(date -u +%FT%TZ) on $(hostname)"

# Pragmatic Track-B path: instead of training DrugCLIP from scratch (12+h, requires
# substantial setup), install DeepPurpose — a well-maintained open-source library
# with multiple PRETRAINED CPI/DTI models (MPNN+CNN, TransformerCPI, etc.). Gives us
# a working "cheap affinity scorer" TODAY. We can wire DrugCLIP-from-scratch later
# when we want a PHGDH-pathway-tuned head.

DATA=/data/user/$USER/aim4_clm
DRUGCLIP_DIR=$DATA/drugclip
mkdir -p $DRUGCLIP_DIR
cd $DRUGCLIP_DIR

module reset
module load Miniforge3/latest

# Build env (idempotent)
if ! conda env list | grep -q "^drugclip "; then
  echo "[dc] creating env drugclip"
  mamba create -n drugclip -y -c conda-forge \
    python=3.10 numpy pandas scikit-learn rdkit tqdm requests
  source activate drugclip
  pip install --quiet --extra-index-url https://download.pytorch.org/whl/cu121 \
    "torch==2.4.*"
  pip install --quiet DeepPurpose==0.1.5 descriptastorus subword-nmt prettytable
else
  echo "[dc] env drugclip already exists"
  source activate drugclip
fi

python -c "import DeepPurpose; print('DeepPurpose OK')"
python -c "import torch; print('torch', torch.__version__, 'cuda', torch.cuda.is_available())"

# Pull DeepPurpose pretrained weights (it auto-downloads on first use; warm cache here)
python <<"PYEOF"
from DeepPurpose import DTI as models
from DeepPurpose import utils
print("[dc] loading pretrained MPNN_CNN model (auto-download if needed)")
try:
    net = models.model_pretrained(model='MPNN_CNN_BindingDB')
    print("[dc] MPNN_CNN_BindingDB loaded")
except Exception as e:
    print(f"[dc] MPNN_CNN load attempt: {e}")
PYEOF

# Quick smoke test: score one known PHGDH active vs PHGDH sequence
python <<"PYEOF"
from DeepPurpose import DTI as models
from DeepPurpose import utils

# PHGDH sequence (UniProt O43175, human, 533 aa)
phgdh_seq = "MAFANLRKVLISDSLDPCCRKILQDGGLQVVEKQNLSKEELIAELQDCEGLIVRSATKVTADVINAAEKLQVVGRAGTGVDNVDLEAATRKGILVMNTPNGNSLSAAELTCGMIMCLARQIPQATASMKDGKWERKKFMGTELNGKTLGILGLGRIGREVATRMQSFGMKTIGYDPIIPADVAKTIEMEFMPSREEIKAKGFPDLAFIVNLIPEKAEDFPDAFDTYRVYSEDQDFGKHLGVGGSELLGLLGFKAKLGRTAVGSRAANAEKAGGDIAIAFKETDAVIARARKILDYRGSANSILTLPFQEQLLPNINEKSTLTKLLREAEDIKDGVRFYAVKNPLNVVVPFEKKIPTKKVDLEDAQNNTGEGIAILRGTEVATKTEFQDIPASEPSISKAGGVPPETKVFISPATGHIRTGLSVLQKAFSEIGAGAVASGLPEDVPRVLLNGNLAGEIAAITGGGVLTAGSSLITMARMNELIGAVRGGRAVLEDADKEALAACFGNSDTPSLTKEELASEVKMSVDGINNAVTCTGEDFRVVANARRLASCGYHVVVTDKKAYIE"
# A known PHGDH-active SMILES (CBR-5884): from literature
known_active_smi = "Cc1ccc(NC(=O)c2cc(C)nn2-c2nc3ccccc3s2)cc1"

print("[dc] running smoke test: known-active vs PHGDH")
try:
    net = models.model_pretrained(model='MPNN_CNN_BindingDB')
    drug_encoding, target_encoding = 'MPNN', 'CNN'
    X_pred = utils.data_process(
        X_drug=[known_active_smi], X_target=[phgdh_seq], y=[0],
        drug_encoding=drug_encoding, target_encoding=target_encoding,
        split_method='no_split'
    )
    pred = net.predict(X_pred)
    print(f"[dc] DeepPurpose MPNN_CNN affinity prediction: {pred}")
    print(f"[dc] (interpretation: log10 IC50 nM range; lower = stronger binding)")
except Exception as e:
    import traceback; traceback.print_exc()
    print(f"[dc] smoke test ERROR: {e}")
PYEOF

echo "[dc] env drugclip ready for use"
echo "[dc] usage from RL fine-tune:"
echo "    rl_finetune.py --reward-fn drugclip_phgdh"
echo "  (after we wire DeepPurpose call into RewardFn)"
echo "[dc] done $(date -u +%FT%TZ)"
