---
name: cheaha-hpc
description: Submit, monitor, and manage compute jobs on UAB Cheaha (Slurm HPC cluster with CPU/GPU partitions). Use when the user wants to run CPU-intensive or GPU-intensive workloads, train models, run bioinformatics pipelines, submit batch scripts to Slurm, launch interactive sessions, or check job status on Cheaha. Cheaha is accessed via SSH to cheaha.rc.uab.edu (no VPN needed for the login gateway).
---

# Cheaha HPC — Submitting Slurm Jobs

## When to use
- User asks to run a CPU- or GPU-heavy job (training, simulation, genomics pipeline, etc.)
- User mentions "Cheaha", "UAB HPC", "slurm", "sbatch", "cluster"
- User wants to check on a previously submitted job (status, logs, efficiency)
- Task needs >24 CPU cores or a GPU and wouldn't fit on the local mac

## Never use for
- Small tasks that fit on W0/L0 — don't burn queue time for 5-minute jobs
- Data transfer without compute — use Globus/rsync directly

## Access
- SSH host: `cheaha.rc.uab.edu` (public, port 22, SSHPiper gateway)
- User alias in `~/.ssh/config`: `cheaha` (already set to `jakechen@cheaha.rc.uab.edu`)
- **No UAB VPN needed** for the login gateway itself
- VPN only needed if reaching internal UAB hosts beyond cheaha

## Golden rules
1. **Never run compute on the login node** — it's for editing + submitting only
2. **`module reset` before `module load`** in every job script
3. **Request the smallest resources that fit** — smaller requests run sooner
4. **A100 jobs: stage inputs to `/local/$USER/$SLURM_JOB_ID`** before compute; network /scratch can't keep up
5. **Always verify job state before declaring success** — `squeue -u $USER` or `sacct -j <jobid>`. Don't narrate.

## Core workflow (four mechanical steps)

### 1. Write a batch script
Use a template from `templates/`:
- `cpu_job.sbatch` — single-node CPU
- `gpu_single.sbatch` — 1 GPU
- `gpu_multi.sbatch` — 2-4 GPUs on one node
- `array_job.sbatch` — parameter sweep
- `interactive.sh` — `srun` one-liner for debugging

### 2. Copy to cheaha
```bash
scp myjob.sbatch cheaha:~/jobs/
# or use rsync for whole dirs
rsync -av ~/project/ cheaha:~/project/
```

### 3. Submit
```bash
ssh cheaha "cd ~/jobs && sbatch myjob.sbatch"
# Returns: "Submitted batch job 12345678"
```

### 4. Observe (verbs — not narrate)
```bash
ssh cheaha "squeue -u \$USER"                  # is it queued/running?
ssh cheaha "sacct -j 12345678 -o jobid,state,elapsed,maxrss,reqmem"
ssh cheaha "cat ~/jobs/<jobname>_12345678.out" # your stdout
ssh cheaha "seff 12345678"                     # post-mortem efficiency
```

## Partitions — cheat sheet

**CPU (pick by time needed, shorter = faster queue)**
| Partition    | Max time | Cores | RAM    | Use for                              |
|--------------|----------|-------|--------|--------------------------------------|
| `express`    | 2 h      | 48    | 754 GB | quick tests, smoke tests, debugging  |
| `short`      | 12 h     | 48    | 754 GB | typical day jobs                     |
| `medium`     | 50 h     | 48    | 754 GB | multi-day runs                       |
| `long`       | 150 h    | 48    | 754 GB | week-long runs (5-node limit)        |
| `amd-hdr100` | 150 h    | 128   | 504 GB | AMD nodes, more cores/node           |
| `largemem`   | 50 h     | 24    | 755 GB | memory-bound single-node jobs        |

**GPU**
| Partition              | Max time | GPUs/node | GPU type  | Use for                          |
|------------------------|----------|-----------|-----------|----------------------------------|
| `pascalnodes`          | 12 h     | 4x P100   | 16 GB VRAM| older GPU work, fits smaller models |
| `pascalnodes-medium`   | 48 h     | 4x P100   | 16 GB VRAM| longer P100 runs                 |
| `amperenodes`          | 12 h     | 2x A100   | 80 GB VRAM| training/inference on big models  |
| `amperenodes-medium`   | 48 h     | 2x A100   | 80 GB VRAM| multi-day A100 work              |

QoS limits: ~264 cores total per person, 5 nodes on `long`, limits per partition. Hit limits → jobs wait.

## GPU specifics (critical)

- Always include `--ntasks-per-socket=1` when requesting multiple GPUs
- **At least 2 CPU cores per GPU** (8 cores per A100 is a good starting point)
- Stage inputs to **`/local/$USER/$SLURM_JOB_ID`** on A100 nodes — the local SSD keeps up with A100 I/O; network storage doesn't
- CUDA modules: `module load CUDA/12.6.0` (or nearest version); for DL add `cuDNN/...`

## Verification over narration

After submitting, NEVER reply with "job is running" without proof. The truth source is:
- `squeue -u $USER` — what Slurm currently thinks
- `sacct -j <id>` — historical record, authoritative
- `.out`/`.err` files — what the job actually produced

If those don't show the claim, the claim is wrong.

## See also
- `references/partitions.md` — full partition detail
- `references/gpu_guide.md` — deeper GPU walkthrough
- `references/storage.md` — where to put data
- `templates/` — ready-to-adapt sbatch files
- `scripts/` — helper wrappers (submit, check, cancel)
