# Skill: cheaha-telemetry

Exposes Cheaha HPC workload intensity to the local AGE E-score. Prior to
this skill, E was blind to Cheaha — if local was idle while a 100-ligand
Vina array was running, E would report 10 % while the REAL effort was 90 %.

## What it measures

Every 3 min, `cheaha_status.sh` runs `sacct -u jakechen -S now-2days -X`
and extracts:

| Metric | Source | Used for |
|---|---|---|
| `rwi_pct` = actual_cpuseconds / requested_cpuseconds | `CPUTimeRAW` / `ReqCPUS × Timelimit` | **Remote Workload Intensity** — how well we packed our allocation |
| `total_actual_cpu_hours` | `CPUTimeRAW` sum | headline effort figure |
| `total_gpu_hours_est` | `TRESUsageInMax` `gres/gpu` × elapsed | GPU-hours consumed |
| `running` / `pending` / `failed_recent` | `State` counts | liveness + optimizer signals |

## Output files

- `project-state/cheaha_utilization.jsonl` — append-only, 3 min cadence
- `/tmp/phgdh_cheaha_status.json` — latest snapshot (dashboard-readable)
- Dashboard endpoint `/api/cheaha-status` (wired on W0 dashboard)

## Integration with E

`utilization_sampler.py` now emits a 4th field `cheaha_rwi_pct`. `age_score.py`
`score_effort()` picks the max of `(local_cpu, l0_gpu, cheaha_rwi)` as the
combined utilization — meaning **a 95 % Cheaha array run correctly scores
E = 9 even if W0/L0 are idle**. See `AGE_SCORING.md` v3.

## Liveness channel `cheaha_queue`

Added to `liveness.py`:
- **RED** if any job stuck in PENDING > 60 min OR `failed_recent` > 0 in last 48 h
- **GREEN** if running ≥ 1 or recent success
- **UNKNOWN** if SSH to cheaha failed

Auto-resolver playbook `cheaha_queue` (new): list failed jobs, requeue once,
then escalate. Registered in `auto_resolver.py` PLAYBOOKS.

## Cadence

Every 3 min — jobs don't end faster, sacct-over-SSH has ~500 ms overhead.

## Workload-optimizer integration

New action `W0_utilization_booster` registered: if `cheaha_rwi ≥ 80%` AND
`local_util < 20%`, spawn Gemma wiki-interlink on L0 — keeps local hot while
Cheaha crushes a screen. No more "only one tier hot at a time".
