# Optimization Guidelines — AGE ↑ within Expense budget

*Companion to AGE_SCORING.md. How to drive each axis toward 9 without
overspending. Used by assessor (A-stage) and retry-alternatives (R-stage).*

## Goal function

For each task iteration, **maximize A subject to X (Expense) ≤ budget**.
G is tracked but not optimized per-task — grows naturally from skill/doc work.

**Target bands:**
- A ≥ 7 (SOTA in ≥50 % of declared categories) — primary goal
- E ≥ 6 (≥67 % utilization) — use hardware we already pay for
- X ≤ task.budget (wall-time × host-cost)

## Per-axis levers

### Improving A (Achievement)

| If A is … | Diagnosis | Levers |
|-----------|-----------|--------|
| 1–3 (<75 % complete) | artifacts missing | re-run with more logging; fix DoD checklist; shorter window |
| 4 (<100 % complete) | near miss | finish remaining criteria in a small iter 2 |
| 5 (par) | no SOTA wins declared | run quality probes against `benchmarks.json`; if win, declare in `_wins_<task>.json` |
| 6–8 (SOTA in some) | partial SOTA | target the unwon categories with focused tweaks (scale data, tune hyperparams) |

### Improving E (Effort / utilization)

| If E is … | Diagnosis | Levers |
|-----------|-----------|--------|
| 1–3 (<33 %) | idle compute | parallelism: fan-out subtasks; use workload-optimizer expansion actions |
| 4–5 (33–50 %) | mixed | batch more work per job; enable GPU in docking (cheaha-amperenodes) |
| 6–7 (67–80 %) | good | protect against flapping — don't chase 9 if marginal |
| 8–9 (≥90 %) | saturated | ensure A is rising; if flat, too-much-effort-for-no-gain, reduce |

### Controlling X (Expense)

- **Wall-time budget** per task (from BACKLOG ETA column)
- **Token budget** per LLM call (L1=800, L2=3000, L3=7000, L4=7000, L5=12000, L6=4000)
- **Cheaha CPU-hours** — track via `sacct`; soft-cap 200 core-hours/week
- **L0 GPU-hours** — unmetered (local) but drop if temperature rises
- **Retry budget**: max 3 alternative strategies per iteration before escalate-to-human

## Undo / redo / alternatives protocol

1. **Assessor** (A-stage) writes improvement plan to
   `project-state/assessment_notes/<task>-iter<N>.md`:
   - What went well (baseline checklist)
   - What's below target (each axis vs target band)
   - Proposed alternatives (ranked by expected ΔA / ΔX cost)

2. **If A < target**: enter **retry cycle** in R-stage:
   - Try alternative #1 (highest expected ΔA / ΔX)
   - If A improves ≥ 1 point: accept, close iteration
   - If not: try alternative #2 (up to 3 total)
   - If all 3 fail: mark `HUMAN_ESCALATION` in ISSUES/OPEN.md

3. **Undo rule**: each alternative runs against a copy of the artifacts in
   `data/retry_<task>_iterN_altM/`. Original is never overwritten.
   The winning alternative is promoted to canonical only at iteration close.

4. **Redo rule**: if first run failed with a transient error (network,
   queue-saturation, GPU thermal), retry is free (doesn't count against
   the 3-alternative budget) — logged as `transient_retry` in
   `retry_attempts.jsonl`.

## Batch processing guidance

- Docking: prefer **array-job sbatch** on Cheaha (one sbatch handles 20 ligands) over 20 individual submits
- LLM calls: batch prompts (up to 10 per call) when fine-tuning the CLM
- Wiki interlink: Gemma /api/chat with `stream:false` and `num_predict`
  matched to paragraph length (no over-generation)
- Rsync: **no --delete** on human-curated dirs (Assessment-Ledger, Molecule-Library, Research-Log)

## Parallelism guidance

- W0 CPU: 8 worker threads max (leave 2 for system)
- L0 GPU: 1 Ollama model at a time (GPU memory-bound)
- Cheaha: submit in groups of ≤10 (avoid saturating express partition)
- Fan-out rules: **never** fan-out a task whose output is the input of another (serialize); fan-out siblings only

## Cost-benefit decisions

Accept an alternative if:
```
(A_new - A_old) * 100  >  X_new * cost_per_hour_of_host
```
i.e., each AGE point is worth 100 "cost units"; anything cheaper than that
is a net win. Hosts have cost weights: L0=1, W0=1, cheaha-express=5,
cheaha-amperenodes=20, cheaha-pascalnodes=15.
