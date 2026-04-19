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

## Extending: adding a new playbook

To make auto-resolver handle a new failure class:

1. **Add a channel to liveness** — in `skills/liveness-audit/scripts/liveness.py`,
   append to `channels = { ... }` with a `status: green|red|unknown`.

2. **Write a playbook function** in `skills/auto-resolver/scripts/auto_resolver.py`:
   ```python
   def pb_my_channel(details: dict) -> tuple[str, bool]:
       """Remediate my_channel. Return (action_description, success_bool)."""
       import subprocess
       r = subprocess.run([...], capture_output=True, text=True, timeout=60)
       return f"action rc={r.returncode}", r.returncode == 0
   ```

3. **Register it** in the `PLAYBOOKS` dict:
   ```python
   PLAYBOOKS = {
       ..., 
       "my_channel": pb_my_channel,
   }
   ```

4. **Smoke test**:
   ```
   python3 skills/auto-resolver/scripts/auto_resolver.py --channel my_channel
   ```

5. **Commit**. That's it — the escalation ladder (silent → notify → urgent →
   HUMAN_REQUIRED after 4 attempts) applies automatically.

### No-op playbooks are legitimate

For channels where auto-remediation isn't appropriate (e.g. `w0_cpu` idle
can be a legitimate state — the agent might simply be waiting), register
`pb_noop`. The counter still ticks, but no action is taken.

### Playbook budget

Each playbook must:
- Complete within **60 s** (timeout enforced by subprocess)
- Be **idempotent** — running twice must not cause harm
- Use `atomic_write` for any state mutation
- **Not enqueue infinite retries** — rely on the escalation ladder
- Return a short action description (≤200 chars) for the audit log

### Planned additions (future growth)

| Channel         | Proposed playbook                                |
|-----------------|--------------------------------------------------|
| `cheaha_quota`  | `sacctmgr show user`, prune old scratch files    |
| `disk_low_w0`   | prune `~/backups/project-state/` beyond 168 cap  |
| `hermes_pending`| trigger `hermes_wiki_growth.sh`                  |
| `iteration_P`   | auto-advance P → L after 2 h with no L trigger   |
| `iteration_E`   | post 🚨 if Execution > 6 h; E often needs time   |
| `telegram_queue`| if queue > 20, increase retry cadence            |
| `box_auth`      | re-run Hermes Box OAuth refresh                  |
| `gemma_slow`    | swap model to `gemma4-agent-fast` if tokens/s <5 |
