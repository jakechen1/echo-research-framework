# Skill: auto-resolver

Self-healing layer. When Liveness flags any channel RED, auto-resolver
consults the playbook map and runs the known remediation. Escalation
ladder prevents runaway loops and respects human-in-loop.

## Playbook map (channel → remediation)

| Channel          | Playbook                               | Notes |
|------------------|----------------------------------------|-------|
| iteration (R)    | `post_r_watchdog.py`                   | Already handles the 2026-04-18 incident class |
| iteration (P-X)  | auto-advance if no history in 2h       | Logs "auto-advance: no agent progress" |
| l0_gpu cold      | curl `/api/generate` tiny prompt       | Warms Gemma within 5 s |
| scavenger stale  | run `phgdh_scavenger.py`               | Verifies output file grew |
| git_push stale   | `phgdh_repo_sync.sh` + enqueue if fail | Retry every 2 min via resilience |
| dashboard_api    | signal `com.openclaw.jakeclaw` WD      | Triggers dashboard restart |
| wiki_interlink   | `wiki_interlink_gemma.py --top 20`     | Generates stubs for broken links |
| box_sync unknown | Hermes MCP box upload                  | Only if hermes gateway up |
| w0_cpu idle      | no-op                                  | Legitimate idle is fine |
| figures stale    | no-op                                  | Iteration choice — not fixable |

## Escalation ladder

| Attempt | Action | Notification |
|---------|--------|--------------|
| 1       | Silent remediation | None if success |
| 2       | Remediation | 🔧 normal notify |
| 3       | Remediation | 🚨 urgent notify |
| 4+      | **STOP auto-action**. Mark HUMAN_REQUIRED. Notify hourly. | 🆘 urgent |

Counter resets when channel stays green ≥ 30 min.

## Invocation

Wired into `liveness.sh --resolver`:
```
liveness.sh --resolver
  → if red: call auto_resolver.py --channels <list>
  → auto_resolver reads resolver_state.json (attempt counters)
  → runs playbook, logs action to resolver_actions.jsonl
  → updates attempt counter
```

On-demand: `python3 skills/auto-resolver/scripts/auto_resolver.py --channel iteration`

## State files

- `project-state/resolver_state.json` — per-channel attempt counter + last-green-at
- `project-state/resolver_actions.jsonl` — every remediation attempt (audit trail)
