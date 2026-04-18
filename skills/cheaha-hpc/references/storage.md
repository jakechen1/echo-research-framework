# Storage on Cheaha

| Path                        | Backing      | Quota | Purpose                        |
|-----------------------------|--------------|-------|--------------------------------|
| `$HOME` (`/home/$USER`)     | GPFS         | small | dotfiles, configs              |
| `/data/user/$USER`          | GPFS         | 5 TB  | **primary personal storage**   |
| `/scratch/$USER`            | GPFS (fast)  | —     | intermediate; auto-purged      |
| `/local/$USER/$SLURM_JOB_ID`| node-local SSD | — (node-size) | per-job scratch, FAST |
| `/data/project/<lab>`       | GPFS         | —     | shared lab storage             |

## Rule of thumb
- **Inputs**: `/data/user/$USER/...`
- **Job scratch**: `/local/$USER/$SLURM_JOB_ID/...` (for A100) or `/scratch/$USER/...` otherwise
- **Final outputs**: `/data/user/$USER/results/...`
- **Never write to `$HOME`** during compute — quota is small
