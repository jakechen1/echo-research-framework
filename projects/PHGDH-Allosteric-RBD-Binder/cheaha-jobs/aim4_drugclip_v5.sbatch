#!/bin/bash
#SBATCH --job-name=drugclip_v5
#SBATCH --partition=express
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:20:00
#SBATCH --output=logs/drugclip_v5_%j.out
#SBATCH --error=logs/drugclip_v5_%j.err
set -euo pipefail
echo "[dc5] start $(date -u +%FT%TZ)"
module reset
module load Miniforge3/latest
source activate drugclip
python -c "import torch, rdkit, pymoo, xgboost, lifelines, statsmodels, scipy, networkx, prettytable, seaborn, matplotlib; import Bio; print(\"all deps importable\")"
python <<PYEOF
print("[dc5] importing DeepPurpose")
from DeepPurpose import DTI as models
from DeepPurpose import utils
print("[dc5] loading pretrained MPNN_CNN_BindingDB")
net = models.model_pretrained(model="MPNN_CNN_BindingDB")
print("[dc5] model loaded")
phgdh = ("MAFANLRKVLISDSLDPCCRKILQDGGLQVVEKQNLSKEELIAELQDCEGLIVRSATKVTADVINAAEKLQVVGRAGTGV"
         "DNVDLEAATRKGILVMNTPNGNSLSAAELTCGMIMCLARQIPQATASMKDGKWERKKFMGTELNGKTLGILGLGRIGRE"
         "VATRMQSFGMKTIGYDPIIPADVAKTIEMEFMPSREEIKAKGFPDLAFIVNLIPEKAEDFPDAFDTYRVYSEDQDFGKH"
         "LGVGGSELLGLLGFKAKLGRTAVGSRAANAEKAGGDIAIAFKETDAVIARARKILDYRGSANSILTLPFQEQLLPNINE"
         "KSTLTKLLREAEDIKDGVRFYAVKNPLNVVVPFEKKIPTKKVDLEDAQNNTGEGIAILRGTEVATKTEFQDIPASEPSI"
         "SKAGGVPPETKVFISPATGHIRTGLSVLQKAFSEIGAGAVASGLPEDVPRVLLNGNLAGEIAAITGGGVLTAGSSLITM"
         "ARMNELIGAVRGGRAVLEDADKEALAACFGNSDTPSLTKEELASEVKMSVDGINNAVTCTGEDFRVVANARRLASCGYH"
         "VVVTDKKAYIE")
tests = [("CBR-5884","Cc1ccc(NC(=O)c2cc(C)nn2-c2nc3ccccc3s2)cc1"),
         ("NCT-503","OC(C(=O)NCCN1CCN(c2ccc(Cl)cc2)CC1)c1ccc(F)cc1"),
         ("ethanol","CCO"),
         ("aspirin","CC(=O)Oc1ccccc1C(=O)O")]
for name, smi in tests:
    X = utils.data_process(X_drug=[smi], X_target=[phgdh], y=[0],
                           drug_encoding="MPNN", target_encoding="CNN", split_method="no_split")
    p = net.predict(X)
    print(f"[dc5]   {name:10s}  pred={p[0]:.3f}  smi={smi[:50]}")
print("[dc5] DeepPurpose CPI scorer READY")
PYEOF
echo "[dc5] done $(date -u +%FT%TZ)"
