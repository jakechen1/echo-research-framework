# PLEASER Stage Codes

The 7-phase PLEASER iteration uses single-character codes in
`project-state/iteration_state.json`. Because **Execution** and **Expense**
both begin with E, the 6th stage is coded **`X`** (eXpense) to disambiguate.

| Code | Full Name   | Purpose                                               |
|------|-------------|-------------------------------------------------------|
| `P`  | Plan        | Define goal, done criteria, budget                   |
| `L`  | Learning    | Read prior art (wiki, papers, past iterations)       |
| `E`  | Execution   | Run the task — compute, writing, experimentation     |
| `A`  | Assessment  | Score via AGE (1-9 reverse NIH), capture metrics     |
| `S`  | Sharing     | Emit artifacts (wiki drafts, figures, reports)       |
| `X`  | **eXpense** | Log wall-time, tokens, GPU-hours, \$ vs budget        |
| `R`  | Resolver    | Close iteration or escalate; hand off to next task    |

**Codes are canonical.** All scripts (`advance_stage.sh`, `post_r_watchdog.py`,
`liveness.py`, `auto_resolver.py`, `report_builder.py`) match on these.

Never rename `X` back to `E` — two stages with code `E` would break the
state machine.

## Stage durations

Liveness flags `iteration` RED when the current stage has been unchanged for:

| Stage | RED threshold |
|-------|---------------|
| P / L / S / X | > 1 h   |
| E / A | > 6 h (long tasks OK) |
| R     | > 10 min (Resolver should flip immediately) |
