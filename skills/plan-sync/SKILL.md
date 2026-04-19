# Skill: plan-sync

Keeps BACKLOG.md statuses in sync with reality (COMPLETED.md + on-disk artifacts).
Runs hourly + at every Resolver exit. Writes `project-state/PLAN_STATUS.md`.

## Truth-source precedence

1. `project-state/COMPLETED.md` — if a task's `G-NNN` legacy ID appears as
   a `## G-NNN —` heading, it's DONE.
2. **Artifact probes** — per task, a list of files that must exist (with
   min size). Matches even if COMPLETED.md entry missing.
3. `iteration_state.json` — if current task matches, marks ACTIVE.
4. Otherwise, `pending`.

## Artifact probes

| Task | Required artifact(s) | Min bytes |
|------|----------------------|-----------|
| 1.1  | workers/data/phgdh/*.jsonl newest <30h old | 10 000 |
| 2.1  | figures/pchembl_dist.png | 10 000 |
| 2.2  | data/aim2_top20_inhibitors.csv | 1 000 |
| 2.3  | data/aim2_pdb_binding_sites.json | 1 000 |
| 3.1  | data/aim3_pubmed_phgdh_allosteric.json | 1 000 |
| 4.1  | data/aim4_docking_results/lig1_docked.pdbqt | 5 000 |
| 4.2  | data/aim4_vina_top20_ranked.csv | 500 |

## Output

- `project-state/PLAN_STATUS.md` — dashboard: per-aim totals, per-task status, artifacts found, next actionable task
- Telegram 📋 when any status flips

## Invocation

```
# On-demand:
python3 skills/plan-sync/scripts/plan_sync.py

# Automatic:
- scheduler_loop.sh: hourly at :45
- post_r_watchdog.py: after every auto-promotion
```
