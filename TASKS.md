---
title: "Build Tasks — 1 through 4"
date: 2026-04-18
---

# Task 1 — Session auto-compactor (URGENT)

**Why.** Prevents the 300-message context overflow we hit 2026-04-17.

**Build.**
- Script: `/Users/jakeclaw/workers/bin/session_compactor.sh`
  - Watch every `*.jsonl` under `~/.openclaw/agents/main/sessions/`
  - When line count > 80 OR size > 500 KB: archive + extract last 10
    messages as summary into `workspace/MEMORY.md`, then restart gateway
- LaunchDaemon: `ai.jakeclaw.session_compactor` — `StartInterval: 1800` (30 min)

**Verify.** Induce 81-msg session, run manually, confirm:
- Archive created under `_archived_<ts>/`
- Gateway restarted, new PID
- Next jakeclaw message succeeds

---

# Task 2 — Tier 1 state files

**Why.** Durable project state independent of any LLM session.

**Build.**
- `~/workers/project-state/CURRENT_GOAL.md` — seeded with first goal
- `~/workers/project-state/BACKLOG.md` — 10 PHGDH sub-goals from proposal
- `~/workers/project-state/COMPLETED.md` — empty with header
- `~/workers/project-state/DAILY_LOG/` — empty dir
- `~/workers/project-state/SNAPSHOTS/` — empty dir
- `~/workers/project-state/README.md` — navigation

**Verify.** Files exist, committed to `echo-research-framework`.

---

# Task 3 — qwenclaw agent setup

**Why.** Separate PM context from executor context; free, faster routing.

**Build.**
- `openclaw agents add qwenclaw --model qwen3.5-agent --provider ollama-local`
- Workspace: `~/.openclaw/agents/qwenclaw/workspace/`
- System prompt: PM role, reads Tier 1 state, sends tasks to jakeclaw
- Bind to a new Telegram channel or internal-only (route:local)
- Add exec-approvals allowlist (lighter than jakeclaw's; PM rarely needs shell)

**Verify.** `openclaw agent --agent qwenclaw -m "summarize current goal"`
returns a sensible one-paragraph summary reading CURRENT_GOAL.md.

---

# Task 4 — Morning orchestrator LaunchDaemon

**Why.** The "forever" driver. Fires at 07:00 daily and runs one
PLEASER-ONE cycle.

**Build.**
- `/Users/jakeclaw/workers/bin/qwenclaw_morning.sh`
  - Reads Tier 1 state
  - Invokes `openclaw agent --agent qwenclaw --local -m "daily plan"`
  - Captures qwenclaw's instructions
  - Forwards ONE command to jakeclaw via internal API / Telegram
  - Waits for reply; captures output
  - Appends to `DAILY_LOG/YYYY-MM-DD.md`
  - Updates `CURRENT_GOAL.md` / `COMPLETED.md` as appropriate
  - Posts daily summary to Jake's Telegram
- LaunchDaemon: `ai.jakeclaw.qwenclaw_morning` — `StartCalendarInterval { Hour: 7, Minute: 0 }`

**Verify.** Run script manually; confirm one log entry appears with
actual tool output (not narration).
