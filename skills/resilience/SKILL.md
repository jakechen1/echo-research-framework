# Skill: resilience

Fail-safe / guaranteed-resumption layer. Survives: network outages, disk
full, power loss mid-write, partial git pushes, Telegram downtime.

## Guarantees

1. **Atomic state writes** — every critical file is written via temp+rename
   (POSIX-atomic). No partial JSON, ever. Wrapper: `atomic_write.py`.
2. **Replay queues** — failed Telegram sends, failed git pushes, failed
   wiki publishes are queued to `project-state/queues/*.jsonl` and replayed
   every 120 s by `retry_queue.py`.
3. **Hourly checkpoint** — `project-state/` is tarred with mtime-preserving
   timestamp and committed to `phgdh-scavenger` repo + cached locally in
   `~/backups/project-state/`. Last 168 hours kept (= 7 days).
4. **Boot recovery** — on W0 reboot or agent relaunch, `on_boot.sh` runs:
   - verifies every JSON/MD state file parses or rolls back to last good
   - detects iteration stuck > 1 h with no history entry
   - reruns the liveness sampler + age baseline refresh once
   - sends "🔁 Resumed from boot at T+Xs" via notifier (tagged urgent)
5. **Lock-free writes** — readers never block writers: snapshots taken
   from `/tmp/phgdh_*.json` copies, not primary files.
6. **Offline-tolerant** — all actions degrade gracefully:
   - no GitHub? commit locally, queue push
   - no Telegram? queue message
   - no L0? fall back to Ollama `/api/ps` proxy for GPU%

## Scripts

- `atomic_write.py` — Python lib + CLI. `atomic_write.sh PATH - <<<'{...}'`
- `checkpoint.sh` — hourly tarball + git commit/push
- `on_boot.sh` — startup recovery
- `retry_queue.py` — every 120 s: replay queued notify/push/publish
- `health_check.sh` — full end-to-end dry run (no side effects)

## LaunchAgents

| Agent | Interval |
|---|---|
| `ai.jakeclaw.resilience_boot` | RunAtLoad only |
| `ai.jakeclaw.resilience_checkpoint` | 3600 s |
| `ai.jakeclaw.resilience_retry` | 120 s |
