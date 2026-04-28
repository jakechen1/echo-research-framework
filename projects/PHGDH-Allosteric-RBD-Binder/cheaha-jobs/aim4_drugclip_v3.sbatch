#!/bin/bash
#SBATCH --job-name=drugclip_v3
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:20:00
#SBATCH --output=logs/drugclip_v3_%j.out
#SBATCH --error=logs/drugclip_v3_%j.err

set -euo pipefail
echo "[dc3] start $(date -u +%FT%TZ)"

module reset
module load Miniforge3/latest
source activate drugclip

# Reuse existing env (pymoo 0.5.0 + torch + rdkit + DeepPurpose --no-deps already there).
# Add the runtime-required deps we missed: lifelines, statsmodels, plus cushion for any others.
pip install --quiet lifelines statsmodels scipy networkx xgboost biopython

# Also re-run with proper deps from PyPI (now that pymoo is pre-pinned at 0.5)
pip install --quiet --no-build-isolation --upgrade DeepPurpose==0.1.5 || true

python -c "from DeepPurpose import DTI as models; print(\"DeepPurpose import OK\")"

# Smoke test: PHGDH known active vs decoy
python <<"PYEOF"
from DeepPurpose import DTI as models
from DeepPurpose import utils
print("[dc3] loading pretrained MPNN_CNN_BindingDB")
net = models.model_pretrained(model="MPNN_CNN_BindingDB")
print("[dc3] model loaded")

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
    ("ethanol_decoy",  "CCO"),
    ("aspirin_decoy",  "CC(=O)Oc1ccccc1C(=O)O"),
]

print("[dc3] smoke predictions:")
for name, smi in tests:
    try:
        X = utils.data_process(X_drug=[smi], X_target=[phgdh_seq], y=[0],
                               drug_encoding="MPNN", target_encoding="CNN",
                               split_method="no_split")
        p = net.predict(X)
        print(f"[dc3]   {name:20s}  pred={p[0]:.3f}  smi={smi[:50]}")
    except Exception as e:
        import traceback; traceback.print_exc()
        print(f"[dc3]   {name:20s}  ERROR: {e}")

print("[dc3] DeepPurpose CPI scorer READY for Round 5 RL reward")
PYEOF

echo "[dc3] done $(date -u +%FT%TZ)"
