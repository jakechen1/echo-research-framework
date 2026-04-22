# PHGDH Autonomous Harness — Contract

*Version: 2026-04-22. Single source of truth for which component writes what and reads what.*

## Core principle

**The Assessor writes. Everyone else reads.** No component invents its own
view of "what's happening." If a component needs to decide something, it
reads the latest Assessor entry. If the Assessor disagrees with prose, the
Assessor wins.

## Ledger: `project-state/assessor_log.jsonl`

Appended every 3 min by `skills/assessor/scripts/tick.py`. Each entry:

```json
{
  "at": "ISO-8601",
  "task": "Task X.Y", "stage": "P|L|E|A|S|X|R",
  "stage_age_min": 17.3,
  "progress":  {"verdict": "PROGRESS|IDLE|NO_WORK",
                "files_added": N, "bytes_added": N,
                "net_bytes_out": N, "commits": N, "window_min": N},
  "liveness":  {"overall": "green|red", "red_channels": [...]},
  "age":       {"task": ..., "A": n, "G": n, "E": n},
  "stalls":    ["Task X.Y/stage/no_executor", ...],
  "flags": {
    "STAGE_STALLED": bool,           # stage_age_min > 60
    "NO_WORK_THIS_WINDOW": bool,     # progress.verdict == NO_WORK
    "BLOCKED": bool,                 # any stall alerts open
    "AGE_SUBPAR": bool,              # A < 5
  }
}
```

Also mirrored at `/tmp/phgdh_assessor_latest.json` for dashboards.

## Who writes

| Component | Writes to | Cadence |
|---|---|---|
| Assessor | `assessor_log.jsonl`, `/tmp/phgdh_assessor_latest.json` | every 3 min |
| Progress-audit snapshot | `project-state/progress_snapshots/*.json`, `/tmp/phgdh_progress_latest.json` | every 5 min |
| Liveness | `project-state/liveness.json`, `/tmp/phgdh_liveness.json` | every 5 min |
| Utilization sampler | `project-state/utilization.jsonl` | every 60 s |
| Cheaha telemetry | `project-state/cheaha_utilization.jsonl`, `/tmp/phgdh_cheaha_status.json` | every 3 min |
| task_advancer | `project-state/iteration_state.json` (via atomic) | every 2 min, on executor success |
| auto-resolver | `project-state/resolver_state.json`, `resolver_actions.jsonl` | every 5 min |
| Learner | `project-state/learning_notes/*.md` | on user correction |
| Planner | `/Users/jakeclaw/workers/bin/task_*.sh.pending`, registry | on first stall |

## Who reads (and enforces the Assessor's verdict)

| Component | Reads Assessor for | Enforcement |
|---|---|---|
| `report_builder_guard.py` | Every report | Rejects (rc=3) if `NO_WORK_THIS_WINDOW` unless report leads with that fact |
| `task_advancer` | Before any advance | Refuses to advance if executor exists but `flags.NO_WORK` since last tick |
| `auto_resolver` | On every tick | Uses red_channels + BLOCKED flag to decide playbook vs escalation |
| Dashboard `/api/assessor` | UI display | Shows current flags at top of every tab |
| `jakeclaw` Telegram bot | Before composing any status reply | Must include the 4 hard numbers from latest entry; prose without numbers rejected |

## Mandatory inclusion in any "what's happening" answer

Any agent or report that answers "what's happening" or "is progress being made"
MUST include these four lines verbatim from the latest assessor entry:

```
- Task: <task> / stage <stage> (age <N> min)
- Progress: <verdict> (+<files> files, +<bytes> bytes, +<net> net, <commits> commits, <window> min)
- Liveness: <overall>  red=<list>
- Flags: <flags dict>
```

If any of STAGE_STALLED / NO_WORK_THIS_WINDOW / BLOCKED / AGE_SUBPAR is true,
the answer must name it explicitly. No prose may contradict these numbers.

## Upgrade protocol (Learner)

When user corrects the harness (e.g. "reports cannot be no change"),
`skills/learner/scripts/record.py` is called to durably capture the rule
into `project-state/learning_notes/`. Future assessor ticks reference the
learning_index. No user correction is lost to Telegram scroll.
