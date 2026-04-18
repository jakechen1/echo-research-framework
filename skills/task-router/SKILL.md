---
name: task-router
description: Estimate the computational cost of a task (CPU seconds, RAM, GPU need) and route it to the cheapest tier that can handle it - local single-process, local parallel-10, W0 local, L0 local, or Cheaha HPC. Use when any agent needs to decide where to run a job.
---

# Task Router — where should this run?

## Tier map (cheapest first)

| Tier | Host | When |
|------|------|------|
| 0 — trivial | any | est < 1 s, no GPU, < 100 MB RAM |
| 1 — local serial | W0 OR L0 | 1 s - 60 s, < 2 GB RAM, no heavy GPU |
| 2 — local parallel×10 | W0 OR L0 | N independent subtasks each tier-1 |
| 3 — L0 GPU | L0 Apple Silicon GPU | needs small-model inference (fits in 6 GB free VRAM after Gemma) |
| 4 — Cheaha CPU | cheaha amd-hdr100 / medium | > 30 min, > 8 GB RAM, or fan-out > 100 |
| 5 — Cheaha GPU | cheaha amperenodes (A100) / pascalnodes (P100) | large-model training, large-batch docking, models > 6 GB VRAM |

## Host budgets

- **L0 (M4 Pro, 24 GB)** — runs Gemma 4 26B (17.9 GB VRAM). Free:
  ~6 GB RAM + GPU fraction + 11-14 CPU cores mostly idle.
- **W0 (M4, 16 GB)** — runs openclaw gateway, dashboard, Qwen 3.5 9B
  (6 GB VRAM on demand). Free: ~8-10 GB RAM + 8-10 cores.
- **Cheaha** — 48-128 CPU cores/node; 189-755 GB RAM/node; 2× A100 80GB
  or 4× P100 16GB GPUs. See `cheaha-hpc-skill/references/partitions.md`.

## Decision heuristic (call this first)

Before running a task, answer four questions:

1. **Parallelizable?** Can it split into N ≥ 5 independent subtasks?
   - yes, each tier-1: run with `scripts/parallel_local.sh`
   - yes, each tier-4/5: submit as array job on Cheaha
2. **Wall-clock estimate** (single-process, best-case hardware):
   - < 1 s → tier 0
   - < 60 s → tier 1 (W0 unless it'd fight openclaw)
   - 1 - 30 min → tier 2-3 locally OR tier 4 on Cheaha if it'd block iteration
   - > 30 min → tier 4-5 Cheaha
3. **Memory estimate** (peak RSS):
   - < 2 GB → local
   - 2 - 8 GB → local single-process only
   - > 8 GB → Cheaha
4. **GPU need?**
   - no → CPU tier
   - small model, < 6 GB VRAM → L0 (use residual VRAM around Gemma)
   - large model, > 6 GB VRAM → Cheaha GPU

## Estimation

See `scripts/estimate_task.sh` for a rough estimator.

Inputs:
- input size (bytes or row count)
- operation type (docking / MD / inference / preprocessing / fit-model / ...)
- per-unit cost table (kept in `scripts/cost_table.json`)

The estimator is not magic — it applies simple per-operation scaling rules
and learned constants. Over time we update the cost table from actual
observed runtimes so future estimates get better.

## Calibration loop

Every task that runs > 5 s appends a row to
`project-state/TASK_TELEMETRY.jsonl`:
```
{"ts": "...", "task": "dock_100_ligands", "host": "L0", "n_items": 100, "wall_s": 127.4, "rss_mb": 340, "gpu_util_pct": 12}
```
The estimator reads the last 100 rows for each `task` to derive a
typical cost. If we have no history for a new task, default to tier 1
(safe, cheap) on first run, then let telemetry inform the next.

## Usage

From any agent:
```bash
/Users/jakeclaw/.openclaw/workspace/skills/task-router/scripts/route.sh \
  --task "pchembl_histogram" \
  --n-items 2613 \
  --op-type preprocessing
# prints the chosen tier and the exact command to execute
```

For parallel work:
```bash
.../scripts/parallel_local.sh --host W0 --jobs 10 --cmd "process_one.py" --in items.txt
```

For remote (Cheaha) submission:
```bash
.../scripts/submit_cheaha.sh --template gpu_single --job my_dock --data data/top500.smi
# runs cheaha-hpc-skill/scripts/submit.sh under the hood
```
