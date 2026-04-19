# Skill: task-executor

Continuously drives the current task through PLEASER stages
(P → L → E → A → S → X → R) without waiting for human intervention.

## Design

- Each task has a per-stage command in `project-state/task_executors/registry.json`
- `task_advancer.py` runs every 2 min from `scheduler_loop`
- Reads current `iteration_state.json`
- Looks up executor for `(task, stage)` pair
- Runs it, interprets return code:
  - **rc=0** → advance to next stage
  - **rc=2** → pending (e.g. HPC job running) → stay, retry
  - **rc!=0,2** → failure, log, retry next tick (assessor / retry-alternatives picks up)
- 4-min cooldown per (task,stage) to avoid spam
- Missing executor → auto-advance with note (for pure-bookkeeping stages)

## Registry format

```json
{
  "Task 4.2": {
    "L": "bash /Users/jakeclaw/workers/bin/task_4_2_learning.sh",
    "E": "bash /Users/jakeclaw/workers/bin/task_4_2_execute.sh",
    "A": "bash /Users/jakeclaw/workers/bin/task_4_2_assess.sh",
    "S": "bash /Users/jakeclaw/workers/bin/task_4_2_share.sh"
  }
}
```

## Convention for executors

- Idempotent (use marker files; check-and-skip if already done)
- Return 0 when stage is complete
- Return 2 when still working (e.g. HPC job pending)
- Write artifacts to `$WS/data/` or `$WS/figures/`
- Write notes to `$WS/project-state/<stage>_notes/<task>-iter<N>.md`

## What's wired now

| Task | Stages with executor |
|------|----------------------|
| 4.2  | L, E, A, S          |
| 2.4  | E                   |
| 1.2  | E                   |

Future tasks: add entry to `registry.json` + write a small bash wrapper
in `/Users/jakeclaw/workers/bin/task_X_Y_<stage>.sh`.
