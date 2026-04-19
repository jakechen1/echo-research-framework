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
