# Open issues & blockers

*Entry format:*
```
## I-NNN — <one-line summary>
- **Opened:** YYYY-MM-DD
- **Severity:** [low | medium | high | blocker]
- **Context:** <2-3 lines>
- **Next action:** <who does what>
```

---

## I-001 — cheaha passwordless SSH from W0 IP (rate-limit cooldown)
- **Opened:** 2026-04-17
- **Severity:** low
- **Context:** SSHPiper rate-limited W0 IP after failed expect scripts.
  Key is installed (verified from local laptop IP). W0 IP blocked ~15 min.
- **Next action:** jakeclaw re-tests after 22:25 CDT 2026-04-17;
  confirms ssh -o BatchMode=yes jakechen@cheaha.rc.uab.edu works.

## I-002 — Box folder path unspecified
- **Opened:** 2026-04-18
- **Severity:** medium
- **Context:** Daily reports + paper drafts need to sync to Box but path
  not yet provided. Default proposed: `Box/Research/PHGDH/`.
- **Next action:** jakechen to confirm or override.
- [2026-04-19T00:11:01Z] Liveness RED: iteration
- [2026-04-19T00:15:07Z] Liveness RED: iteration
- [2026-04-19T00:20:17Z] Liveness RED: iteration
- [2026-04-19T00:25:26Z] Liveness RED: iteration
- [2026-04-19T00:30:34Z] Liveness RED: iteration
- [2026-04-19T00:35:43Z] Liveness RED: iteration
- [2026-04-19T00:40:51Z] Liveness RED: iteration
- [2026-04-19T00:45:58Z] Liveness RED: iteration
- [2026-04-19T00:50:06Z] Liveness RED: iteration
- [2026-04-19T00:55:13Z] Liveness RED: iteration
- [2026-04-19T01:00:21Z] Liveness RED: iteration
- [2026-04-19T01:05:29Z] Liveness RED: iteration
- [2026-04-19T01:10:38Z] Liveness RED: iteration
- [2026-04-19T01:15:46Z] Liveness RED: iteration
- [2026-04-19T01:20:54Z] Liveness RED: iteration
- [2026-04-19T01:25:01Z] Liveness RED: iteration
- [2026-04-19T01:30:09Z] Liveness RED: iteration
- [2026-04-19T01:35:17Z] Liveness RED: iteration
- [2026-04-19T01:40:25Z] Liveness RED: iteration
- [2026-04-19T01:45:32Z] Liveness RED: iteration
- [2026-04-19T01:50:39Z] Liveness RED: iteration
- [2026-04-19T01:55:47Z] Liveness RED: iteration
- [2026-04-19T02:00:54Z] Liveness RED: iteration
- [2026-04-19T02:05:01Z] Liveness RED: iteration
- [2026-04-19T02:10:09Z] Liveness RED: iteration
- [2026-04-19T02:15:17Z] Liveness RED: iteration
- [2026-04-19T02:20:25Z] Liveness RED: iteration
- [2026-04-19T02:25:33Z] Liveness RED: iteration
- [2026-04-19T02:30:40Z] Liveness RED: iteration
- [2026-04-19T02:35:49Z] Liveness RED: iteration
- [2026-04-19T02:40:56Z] Liveness RED: iteration
- [2026-04-19T02:45:02Z] Liveness RED: iteration
- [2026-04-19T02:50:10Z] Liveness RED: iteration
- [2026-04-19T02:55:17Z] Liveness RED: iteration
- [2026-04-19T03:00:25Z] Liveness RED: iteration
- [2026-04-19T03:05:33Z] Liveness RED: iteration
- [2026-04-19T03:10:41Z] Liveness RED: iteration
- [2026-04-19T03:15:49Z] Liveness RED: iteration
- [2026-04-19T03:20:58Z] Liveness RED: iteration
- [2026-04-19T03:25:03Z] Liveness RED: iteration
- [2026-04-19T03:30:14Z] Liveness RED: iteration
- [2026-04-18T19:30Z] RESOLVED: iteration RED (Task 4.1 R stalled 6h+).
  Root cause: Resolver stage had no auto-exit — state entered R and sat
  forever. Fixed by adding skills/resilience/scripts/post_r_watchdog.py
  to scheduler_loop (every 5 min). R > 10 min → auto-promote next task.
  State advanced: Task 4.1 → Task 4.2.
- [2026-04-19T03:35:13Z] Liveness RED: dashboard_api
- [2026-04-19T03:50:34Z] Liveness RED: dashboard_api
- [2026-04-19T04:05:08Z] Liveness RED: dashboard_api
- [2026-04-19T04:35:31Z] Liveness RED: dashboard_api
- [2026-04-19T09:01:08Z] Liveness RED: l0_gpu
- [2026-04-19T10:45:44Z] Liveness RED: iteration
- [2026-04-19T10:50:12Z] Liveness RED: iteration
- [2026-04-19T10:55:33Z] Liveness RED: iteration
- [2026-04-19T11:01:01Z] Liveness RED: iteration
- [2026-04-19T11:05:25Z] Liveness RED: iteration
- [2026-04-19T11:10:53Z] Liveness RED: iteration
- [2026-04-19T11:15:15Z] Liveness RED: iteration
- [2026-04-19T11:20:43Z] Liveness RED: iteration
- [2026-04-19T11:30:31Z] Liveness RED: iteration
- [2026-04-19T11:36:00Z] Liveness RED: iteration
- [2026-04-19T11:40:17Z] Liveness RED: iteration
- [2026-04-19T11:45:43Z] Liveness RED: iteration
- [2026-04-19T11:50:09Z] Liveness RED: iteration
- [2026-04-19T11:55:32Z] Liveness RED: iteration
- [2026-04-19T12:01:00Z] Liveness RED: iteration
- [2026-04-19T12:05:23Z] Liveness RED: iteration
- [2026-04-19T12:10:50Z] Liveness RED: iteration
- [2026-04-19T12:15:12Z] Liveness RED: iteration
- [2026-04-19T12:20:39Z] Liveness RED: iteration
- [2026-04-19T12:30:27Z] Liveness RED: iteration
- [2026-04-19T12:35:51Z] Liveness RED: iteration
- [2026-04-19T12:40:18Z] Liveness RED: iteration
- [2026-04-19T12:45:40Z] Liveness RED: iteration
- [2026-04-19T12:50:06Z] Liveness RED: iteration
- [2026-04-19T12:55:28Z] Liveness RED: iteration
- [2026-04-19T13:00:56Z] Liveness RED: iteration
- [2026-04-19T13:05:18Z] Liveness RED: iteration
- [2026-04-19T13:10:45Z] Liveness RED: iteration
- [2026-04-19T13:15:02Z] Liveness RED: iteration
- [2026-04-19T13:20:31Z] Liveness RED: iteration
- [2026-04-19T13:25:58Z] Liveness RED: iteration
- [2026-04-19T13:30:16Z] Liveness RED: iteration
- [2026-04-19T13:35:44Z] Liveness RED: iteration
- [2026-04-19T13:40:11Z] Liveness RED: iteration
- [2026-04-19T13:45:33Z] Liveness RED: iteration
- [2026-04-19T13:51:01Z] Liveness RED: iteration
