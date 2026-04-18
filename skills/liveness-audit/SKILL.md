# Liveness / Stuck-Detector Skill

Audits every 5 min (or on-demand) whether the autonomous PHGDH project is
actually making progress. Rolls multiple signals into a per-channel status:

| Channel            | Healthy if                                         | Source |
|--------------------|----------------------------------------------------|--------|
| L0 GPU             | active_residency ≥ 5% OR last inference < 10 min   | L0 powermetrics + Ollama `/api/ps` |
| W0 CPU             | 1-min load > 0.3 OR any python>1% in last sample   | W0 `uptime` + `ps` |
| Scavenger          | newest `workers/data/phgdh/*.jsonl` < 26 h old     | mtime on W0 |
| Figures            | `figures/*.png` newest mtime change in 24 h        | mtime |
| Aim data           | `data/aim*/` per-aim newest mtime                   | mtime |
| Iteration          | `iteration_state.json` stage-change age < 6 h      | history[-1].at |
| Git push           | repo remote/HEAD sha != local, OR last push < 2 h  | `git log` |
| Dashboard          | GET /api/status returns 200 within 3 s             | curl |
| Wiki interlink     | newest `_generated_hubs/*.md` mtime                 | mtime |
| Box sync           | last BOX_FOLDERS.md sync log < 24 h                 | /Users/jakeclaw/workers/logs/box_sync.log |

Outputs `project-state/liveness.json` + appends to `liveness_history.jsonl`.
Dashboard renders a **Liveness** card showing per-channel status + "last change"
age. When any channel goes RED, the Resolver phase of PLEASER escalates:
1. qwenclaw receives a `RESOLVER_ALERT` instruction
2. L1 report is forced within 5 min
3. Telegram notification sent to user

## Invocation

- On-demand:   `bash scripts/liveness.sh`
- Scheduled:   LaunchDaemon `ai.jakeclaw.liveness_audit` every 300 s
- In PLEASER:  resolver stage calls `scripts/liveness.sh --resolver`
