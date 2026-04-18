---
title: "Six Levels of Communication & Documentation"
version: 1.0
date: 2026-04-18
authors: [jakechen]
status: canonical
---

# Six Levels of Communication & Documentation

Every project artifact Jake or any agent produces must target one of six
levels. Each level has a specific audience, cadence, and channel. Each
level's report compares **delta from the previous report of the same
level** — not from scratch, not from the project's origin. The delta is
what makes reports cheap to read.

All levels use the **same length constraint as L1** but expose more
detail as the level number rises. L1 is not shorter text; L6 is not
longer text. The density of technical content scales; the narrative
form stays concise.

## The Six Levels

| Level | Content | Cadence | Channel | Required for |
|-------|---------|---------|---------|--------------|
| **L1** | One-sentence thesis-status | **3× daily** (07:30, 13:00, 22:00) | Telegram | continuous awareness |
| **L2** | One-page, up to 4 aims | **Daily 17:00** | Telegram | daily reflection |
| **L3** | Full proposal (significance, innovation, approaches) | **Each PLEASER-ONE iteration**, on completion | Telegram + Wiki | formal iteration close |
| **L4** | Full poster (figures, tables, brief interpretations) | On-demand after successful tasks | Wiki | each shared-result version for AI+Human assessment |
| **L5** | Full paper (technical overview, repeatable detail, results interpreted into conclusions) | On-demand at milestone | Box | publication-ready drafts |
| **L6** | All logs, debug, highly technical | On-demand at project conclusion | GitHub | post-mortem, reproducibility |

## Delta rule

Every level's report MUST include a "Delta vs previous L{n}" section
that names exactly what changed since the last report of the same
level. If there is no prior report, state "baseline." If nothing
changed, state "no net change" plus a 1-line justification.

This is the whole point of the system. A report without delta is
reciting the project, not updating the reader.

## Storage

| Level | Directory | Naming |
|-------|-----------|--------|
| L1 | `project-state/reports/L1/` | `YYYY-MM-DD-HH-MM.md` |
| L2 | `project-state/reports/L2/` | `YYYY-MM-DD.md` |
| L3 | `project-state/reports/L3/` | `G-NNN-YYYY-MM-DD.md` |
| L4 | `project-state/reports/L4/` | `poster-YYYY-MM-DD-NN.md` |
| L5 | `project-state/reports/L5/` | `paper-YYYY-MM-DD.md` |
| L6 | `project-state/reports/L6/` | `debug-YYYY-MM-DD-HHMM.md` |

All levels sync to GitHub `phgdh-scavenger/project-state/reports/`.
L3+ also publish to `sdd-wiki` (Wiki channel). L5 also ships to Box
`PHGDH/paper/`.

## Triggering

### Automatic (scheduled)
- `ai.jakeclaw.report_l1_morning` at 07:30 → after qwenclaw_morning
- `ai.jakeclaw.report_l1_afternoon` at 13:00
- `ai.jakeclaw.report_l1_evening` at 22:00
- `ai.jakeclaw.report_l2_daily` at 17:00
- L3 fires inside `qwenclaw_morning.sh` whenever auto-promotion rotates a goal

### On-demand (Telegram keywords)
Jakeclaw recognizes these as report requests:
- `L1` or `status` → generate + send L1
- `L2` or `digest` → generate + send L2
- `L3` → generate + post to wiki + reply with wiki URL
- `L4` → generate poster + post to wiki
- `L5` → generate paper → save to Box/PHGDH/paper/
- `L6` → compile debug bundle → push to GitHub

## Cost awareness

L1 is cheap (short prompt, ~15s GPU). L2 is moderate. L3+ are expensive
(long prompts, minutes of GPU). Scheduled L1×3 + L2 = ~4 GPU cycles/day
beyond qwenclaw+briefing. L3-L6 fire only when there is real project
advancement — do not fire them hourly.

## Style contract (applies to all levels)

- Plain language. No emoji. No manifestos.
- Evidence-based. Every claim traces to a file or commit or measured
  number.
- Delta-first. What changed comes before what stayed the same.
- Ambiguity flagged explicitly. "Unclear whether X causes Y — needs
  next iteration" beats silent hedging.
- If a level's prompt demands results that do not yet exist (e.g., L4
  poster before any figure has been made), the report states that
  outright and fills remaining sections with "pending G-NNN."

## Quality check

A report is "working" if a reader unfamiliar with today's chat can pick
it up, understand what changed, what it means, and what's next — in the
time it takes to read it at the level's expected length (L1 = 15
seconds; L6 = half an hour).

