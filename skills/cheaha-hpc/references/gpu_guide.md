# GPU jobs on Cheaha

## Request syntax
```
#SBATCH --partition=amperenodes     # or pascalnodes
#SBATCH --gres=gpu:2                # 1-4 GPUs on a node
#SBATCH --ntasks-per-socket=1       # REQUIRED when >1 GPU
#SBATCH --cpus-per-task=8           # >= 2 per GPU, 8 is healthy for A100
#SBATCH --mem=64G
#SBATCH --time=04:00:00
```

## CUDA modules (check with `module avail CUDA`)
```bash
module reset
module load CUDA/12.6.0
module load cuDNN/8.9.2.26-CUDA-12.2.0   # if using cuDNN
```

## A100 I/O discipline (critical)
A100s can starve on network storage. Stage inputs first:
```bash
LOCAL=/local/$USER/$SLURM_JOB_ID
mkdir -p $LOCAL
cp -r /data/user/$USER/my_dataset $LOCAL/
# run compute against $LOCAL/my_dataset
# copy results back at end:
cp -r $LOCAL/output /data/user/$USER/results/$SLURM_JOB_ID/
```

## Checking GPU inside a job
Run this inside your script to confirm GPU allocation:
```bash
nvidia-smi
echo "SLURM gave me GPUs: $CUDA_VISIBLE_DEVICES"
```

## Typical PyTorch GPU job skeleton
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU count: {torch.cuda.device_count()}")
print(f"GPU 0: {torch.cuda.get_device_name(0)}")
```
