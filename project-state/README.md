# Project-state files (Tier 1)

Canonical, on-disk project state. Independent of any LLM session. All agents
read and write these files.

## Layout
- `CURRENT_GOAL.md` — the ONE active sub-goal
- `BACKLOG.md` — prioritized upcoming sub-goals
- `COMPLETED.md` — finished sub-goals (append-only)
- `ISSUES/OPEN.md` — open blockers
- `DAILY_LOG/YYYY-MM-DD.md` — per-day action log (append-only)
- `SNAPSHOTS/weekly_YYYY-WW.md` — weekly rollups

## Update rules
- **Pickers** (qwenclaw, jakechen): move one backlog item → CURRENT_GOAL
- **Executors** (jakeclaw): never edit BACKLOG/COMPLETED; only append to DAILY_LOG
- **Completers** (qwenclaw, Chrome-Claude, jakechen): after verification,
  move CURRENT_GOAL content → COMPLETED with date + artifact links, then
  promote next from BACKLOG
- **Issue-raisers** (any agent): append to ISSUES/OPEN.md with unique I-NNN

## Source of truth
These files are the project's long-term memory. Commit message changes via the
workspace git repo (`echo-research-framework`); auto-pushed every 15-45 min.
