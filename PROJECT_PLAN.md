---
title: "PHGDH Project — Unified Plan"
version: 1.0
date: 2026-04-18
status: active
authors: [jakechen, claude-code]
---

# PHGDH Project — Unified Plan

## Executive summary

Goal: identify and characterize allosteric / RBD-site modulators of **PHGDH**
(D-3-phosphoglycerate dehydrogenase, UniProt O43175) as candidates for
neurodegenerative disease intervention, producing (a) a reproducible
data + analysis pipeline, (b) a living wiki, (c) a paper draft + slide deck,
(d) experiments run on Cheaha HPC. Operated **locally-first** (Gemma 4 26B
on L0, Qwen 3.5 9B on W0) with Claude (paid) reserved for strategic review
only. Runs autonomously until completion via LaunchDaemons + local agents.

## Project goals (from Master-Blueprint + paper-project + 2025-progress)

1. **Data**: continuous scavenge of ChEMBL/UniProt bioactivities against PHGDH
   (already deployed — `ai.jakeclaw.worker.phgdh_scavenger`, 2 AM daily).
2. **Virtual screening**: structure-based drug design (SBDD) for allosteric site;
   run on Cheaha GPU (`amperenodes`).
3. **Wiki**: living, source-validated knowledge graph of PHGDH biology,
   inhibitors, and method (~40 PHGDH pages already authored via Hermes
   wiki-builder; continue incremental growth).
4. **Paper draft**: build in Box `paper/` folder; update with each milestone.
5. **Slide deck**: auto-update in Box `slides/` folder with new figures.
6. **Monthly 2025 AI-drug-discovery digest** (see `wiki/research/drug_discovery_2025_progress.md`).

## Architecture — three tiers

### Tier 0 — OS-level persistence (free, no LLM)
- `/Library/LaunchDaemons/ai.jakeclaw.worker.phgdh_scavenger.plist` — data pull
- `/Library/LaunchDaemons/ai.jakeclaw.worker.daily_briefing.plist` — state snapshot
- `/Library/LaunchDaemons/ai.jakeclaw.session_compactor.plist` — context safety (TBD)
- `/Library/LaunchDaemons/ai.jakeclaw.qwenclaw_morning.plist` — PM orchestrator (TBD)
- `com.jakeclaw.git-autopush` — workspace → github every 15-45 min
- `com.jakeclaw.nas-mount`, `com.jakeclaw.l0-keepalive`, `com.jakeclaw.system-health`

### Tier 1 — Project state (files; canonical across all agents)
Location: `/Users/jakeclaw/workers/project-state/` (to be created):
- `CURRENT_GOAL.md` — one active sub-goal
- `BACKLOG.md` — prioritized upcoming sub-goals
- `COMPLETED.md` — finished sub-goals with dates + commit SHAs
- `DAILY_LOG/YYYY-MM-DD.md` — per-day action log
- `SNAPSHOTS/weekly_YYYY-WW.md` — weekly state rollup

Plus existing authoritative files (in place):
- Scavenger output: `/Users/jakeclaw/workers/data/phgdh/YYYY-MM-DD.jsonl`
- Wiki: `/Users/jakeclaw/wiki/` (git-backed)
- Hermes holographic memory: `/Users/jakeclaw/.hermes/memories/`
- Workspace git: auto-pushed to `github.com/jakechen1/echo-research-framework`
- Box folder: `[TO-BE-CONFIRMED]/PHGDH/` with `paper/`, `slides/`, `reports/`, `logs/`

### Tier 2 — Local agents (free; all on your hardware)

| Agent | Model | Host | Role |
|-------|-------|------|------|
| **jakeclaw** | Gemma 4 26B (Q4_K_M, 128K ctx) | L0 Ollama | Senior executor: writes, thinks, runs commands, drafts |
| **qwenclaw** (new) | Qwen 3.5 9B | W0 Ollama | Junior PM: picks daily goal, routes, audits, logs |
| **Hermes** (existing) | Gemma 4 via L0 | W0 | Wiki-builder + source-validator (already running) |

### Tier 3 — Claude (paid; consultant only)
- **Chrome-Claude (Opus)**: weekly 30-min strategic review, paper draft polish
- **Claude Code (me)**: ops fires, architectural questions, incident response

## Roles and what triggers what

| Event | Who handles | Where |
|-------|-------------|-------|
| 02:00 daily | scavenger LaunchDaemon | new JSONL file |
| 07:00 daily | qwenclaw picks goal | `CURRENT_GOAL.md` updated |
| 07:15 daily | qwenclaw → jakeclaw task | Telegram / internal API |
| 08:00 daily | daily_briefing | markdown report to Box |
| Task result arrives | qwenclaw audits, logs | `DAILY_LOG/` + `COMPLETED.md` |
| Wiki gap identified | Hermes wiki_builder | `~/wiki/general/` pages |
| Session > 80 msgs | session_compactor | archive + reset |
| Stuck 3x or ambiguous goal | escalate to human | Telegram to Jake |
| Weekly sync (Sunday) | Chrome-Claude strategic review | `SNAPSHOTS/weekly_*.md` |
| Ops incident | Claude Code (paid) | ad hoc |

## Long-term memory integration

**Built-in (all always-on):**
- `~/.openclaw/workspace/MEMORY.md`, `SOUL.md`, `IDENTITY.md` — identity
- `~/.openclaw/workspace/memory/YYYY-MM-DD.md` — daily memory entries

**Hermes holographic memory (already configured):**
- `~/.hermes/memories/` — semantic associative recall
- Driven by `hermes memory` subcommand; provider = `holographic`

**Wiki (existing, 1546+ pages):**
- `~/wiki/general/` — PHGDH biology / drug discovery (already rich)
- `~/wiki/research/` — project progress trackers
- Built + maintained by `~/.hermes/scripts/wiki_builder.py`
- Source-validated via `~/.hermes/scripts/source_validator.py`
- Git-tracked at `~/wiki/.git`

**Project state files (to be created):**
- `~/workers/project-state/` — see Tier 1 above

**Git + GitHub:**
- `~/.openclaw/workspace/` → `github.com/jakechen1/echo-research-framework`
- Auto-push every 15-45 min via `com.jakeclaw.git-autopush`

**Box (to be wired):**
- Summary paper, slide deck, monthly digests

## Success criteria

- [ ] Scavenger has ≥ 30 days of PHGDH bioactivity data in JSONL
- [ ] Wiki has ≥ 100 source-validated PHGDH pages
- [ ] At least 1 SBDD virtual-screening run completed on Cheaha
- [ ] Paper draft has introduction + methods + preliminary results sections
- [ ] Slide deck at 20+ slides summarizing findings
- [ ] System ran ≥ 30 consecutive days without human intervention (beyond Duo pushes)
- [ ] Resolution log has 0 unresolved incidents for 7+ days

## Implementation task list (build in order)

See `TASKS.md` for details. Headlines:

1. **Session auto-compactor** — prevent context overflow (URGENT; hit this tonight)
2. **Tier 1 state files** — initialize `CURRENT_GOAL.md`, `BACKLOG.md`, etc.
3. **qwenclaw agent** — second OpenClaw agent using Qwen 3.5 for PM role
4. **Morning orchestrator LaunchDaemon** — qwenclaw fires at 07:00

## Confirmed decisions (2026-04-18)

| Item | Value |
|------|-------|
| Box root | `My Projects/Current/JakeClaw/PHGDH/` (id 377424964160) |
| Box subfolders | paper / slides / reports / logs / data / figures / references — IDs in `project-state/BOX_FOLDERS.md` |
| GitHub repo | `github.com/jakechen1/phgdh-scavenger` (dedicated) — setup pending |
| Kill switch | **`STOP-CHROME-CLAUDE`** — any agent must halt on this phrase |
| Hermes memory | `holographic` (keep as-is) |
| Daily report time | 21:00 local via future daemon; morning cycle at 07:00 |

## Still open
- GitHub: empty repo needs to exist before first push. Choose:
  (a) Jake creates `jakechen1/phgdh-scavenger` via github.com web (fastest)
  (b) Provide PAT so Claude Code can `curl` the GitHub API to create it
- Old JakeClaw folder cleanup: MCP cannot move/delete; Jake does via Box UI
