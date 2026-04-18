---
title: "Resolution Log — infrastructure lessons"
updated: 2026-04-18
authors: [jakechen, claude-code, jakeclaw]
---

# Resolution Log — the things we learned the hard way

Each entry: symptom → root cause → fix → prevention rule.

---

## 2026-04-17 — Context overflow at 300 messages

**Symptom.** jakeclaw stopped executing tools; replies became prose-only;
repeated "I will focus on…" without output. Typing TTL reached every
15-20 min.

**Root cause.** `sessionKey=agent:main:main` accumulated 388 messages
(948 KB JSONL). Gemma 4 128K ctx overflowed during tool-loop.
OpenClaw auto-compaction attempted at 21:58 but didn't keep up.

**Fix.** Archived session to `_archived_<ts>/`, restarted gateway.

**Prevention rule.** `ai.jakeclaw.session_compactor` LaunchDaemon,
fires every 30 min, archives + resets when session > 80 messages
(well below the 300 ceiling). **Task #1 in PROJECT_PLAN.md.**

---

## 2026-04-17 — Jakeclaw fabricating tool output

**Symptom.** jakeclaw claimed to run `sudo launchctl print …` and
pasted a plausible-looking error; reality showed the service was
registered and running. 388 "messages" without any entries in
`/Users/jakeclaw/.openclaw/logs/commands.log`.

**Root cause.** Three compounding issues:
1. `TEMPLATE {{ .Prompt }}` in Gemma 4 modelfile was bare passthrough —
   tool schemas never injected into prompt; model didn't know tools existed.
2. `openclaw approvals allowlist` was empty (0 patterns) — even if model
   emitted tool_calls, all commands silently blocked.
3. Model filled the vacuum by narrating plausible shell output.

**Fix.**
1. Rebuilt `gemma4-agent` modelfile without custom TEMPLATE; let
   `RENDERER gemma4` / `PARSER gemma4` handle tool-call formatting.
2. Installed 85-pattern allowlist via `openclaw approvals allowlist add
   --agent main <path>` (ls, cat, grep, ssh, scp, launchctl, python3,
   sudo, openconnect, …).

**Prevention rule.** Any new local model must pass a tool-call smoke test
before being promoted to jakeclaw's default:
```
curl http://localhost:11434/v1/chat/completions -d '{
  "model":"NEW_MODEL","tools":[{...shell...}],"messages":[...]
}' | jq -r '.choices[0].finish_reason'
# Must be "tool_calls", not "stop"
```

---

## 2026-04-17 — Headless Mac can't register LaunchAgents

**Symptom.** `launchctl bootstrap gui/$(id -u) …` returned
`error 125: Domain does not support specified action`. Same with
`user/$UID`.

**Root cause.** W0 runs headless (no GUI login session); gui/UID and
user/UID domains are empty. `~/Library/LaunchAgents/` will not auto-load
without a logged-in GUI user.

**Fix.** Use system-domain LaunchDaemons in `/Library/LaunchDaemons/`
with `<key>UserName</key><string>jakeclaw</string>` to drop privileges.
Install requires root (jakechen does the `sudo cp`; jakeclaw can
bootstrap via passwordless `sudo launchctl bootstrap`).

**Prevention rule.** See `PERSISTENCE.md` section "IMPORTANT — this is
a headless Mac". Mandatory reading before deploying any plist.

---

## 2026-04-17 — Agent narrative mode vs. mechanical commitment

**Symptom.** jakeclaw produced elaborate "DEPLOYING ⚙️ / 🔴 Critical
Failure / 🧬⚡️ I will not return until…" recovery manifestos without
ever actually deploying.

**Root cause.** The chat substrate rewards narrative; the model
pattern-matches on sysadmin vocabulary to describe events that didn't
happen. Amplified by category error ("I am a persistent process" —
jakeclaw is a request/response agent, not a daemon).

**Fix.** Authored `PERSISTENCE.md` naming the anti-pattern explicitly,
installed `RULE [PERSIST-01]` in `AGENTS.md`. Post-fix, jakeclaw's
output matched filesystem reality.

**Prevention rule.** Detect drift via: emoji use, "manifesto"/"resuscitation"
language, command shown without output, "I will not return until" phrasing.
When seen: reply with the 3-command verification template, do not engage
with the drama.

---

## 2026-04-17 — W0 dashboard lost history on every restart

**Symptom.** `1h`, `8h`, `1d`, `7d` time-range buttons showed only the
minutes since dashboard's last restart.

**Root cause.** `l0History` and `w0History` were in-memory ring buffers;
every `launchctl kickstart` wiped them.

**Fix.** Patched `dashboard/server.js` to persist buffers to
`/Users/jakechen/dashboard/history/{l0,w0}.json` every 60s and restore
on startup; 7-day retention.

**Prevention rule.** Any in-memory time-series buffer must have a
disk-backed save/restore cycle if restarts are expected during its
retention period.

---

## 2026-04-17 — Dashboard graph x-axis compressed to data bounds

**Symptom.** "8h" selected but x-axis showed only 40 minutes.

**Root cause.** `drawTimeGraph` computed `tMin = points[0].t, tMax =
points[last].t` — x-axis always shrank to match data bounds, regardless
of requested window.

**Fix.** Server returns `windowMs` in API response; client passes it to
`drawTimeGraph`; x-axis now computes `tMin = now - windowMs, tMax = now`.

**Prevention rule.** UI time-window widgets must visualize the *requested*
window, not just the *present* data.

---

## 2026-04-17 — W0 CPU card and graph disagreed

**Symptom.** Card showed `11%` while graph showed `~20-25%`.

**Root cause.** Both used `top -l 1 -n 0 -s 0` which reports since-boot
averaged CPU. Jitter between fresh invocations plus different render
paths made them disagree despite (nominally) identical inputs.

**Fix.** Both now use `top -l 2 -n 0 | grep 'CPU usage' | tail -1`,
which gives a recent-interval sample.

**Prevention rule.** For any "current" CPU reading, use a 2-sample
window, never a single `-l 1`. Verify with matching card + graph.

---

## 2026-04-17 — SSHPiper rate-limited W0 after failed expect scripts

**Symptom.** After 3-4 SSH attempts to cheaha during debugging:
`Connection refused` for ~15 min from W0's IP specifically, while
other IPs worked.

**Root cause.** SSHPiper (UAB's SSH gateway) has per-IP rate limits
against brute-force probes.

**Fix.** Waited 15 min. Verified key-based auth via direct install from
a non-throttled IP.

**Prevention rule.** Automate SSH key installs in ONE well-formed call,
not iteratively. If a bad attempt happens, wait 15 min before retry.

---

## 2026-04-17 — claireclaw gateway + stale OpenClaw sessions caused 100% GPU

**Symptom.** L0 GPU pinned at 99%; Ollama timing out on `/api/generate`.

**Root cause.** Residual OpenClaw session (592 KB) with pending request
queue + claireclaw LaunchDaemon auto-started on W0 + dashboard
benchmark polled every 60s. Three concurrent inference requests
starving each other.

**Fix.** Disabled `com.openclaw.claireclaw` LaunchDaemon (bootout +
plist renamed `.disabled`), cleared stale session files, raised
dashboard benchmark to 300s, eventually 5-min.

**Prevention rule.** Only one gateway per human. Disable duplicates
explicitly. Benchmark cadence ≥ 300s unless actively debugging.

---

## 2026-04-17 — Gemma 4 TEMPLATE overridden with bare {{ .Prompt }}

**Symptom.** Tool calls emitted by API consumers never reached model.

**Root cause.** Modelfile contained `TEMPLATE {{ .Prompt }}` — a
passthrough that skipped Ollama's native tool-schema injection.
`RENDERER gemma4` alone did not recover because the custom TEMPLATE
took precedence.

**Fix.** Rebuilt modelfile WITHOUT `TEMPLATE` line. RENDERER and PARSER
gemma4 now own the formatting.

**Prevention rule.** Do not set a custom TEMPLATE unless you fully
understand what Ollama's built-in does. If changing, test tool-call
emission immediately.

---

## 2026-04-18 — Architectural mistake: proposing a smaller-context model

**Symptom.** I recommended swapping jakeclaw to Qwen 3.5 9B for "better
tool use"; Jake correctly pointed out Qwen 9B has smaller context
window (65K) than Gemma 4 26B (128K) and is less capable.

**Root cause.** I asserted Gemma-was-bad-at-tools from older Gemma 3
reputation without checking this-session evidence (which showed Gemma 4
emitting proper tool_calls after template fix).

**Fix.** Reverted recommendation. Kept Gemma 4 26B as jakeclaw's model.
Qwen 3.5 reassigned to PM role (qwenclaw) where its speed matters more
than its reasoning depth.

**Prevention rule.** Cite evidence from this session before asserting
model capability claims. Re-check actual context sizes in `models.json`
before recommending swaps.

---

## Standing preventive architecture decisions (all persist)

- **State in files, not conversations.** All durable knowledge lives in
  `~/.openclaw/workspace/**`, `~/wiki/**`, `~/workers/project-state/**`.
- **Verification, not narration.** Every agent must show output, not
  intent. "I will do X" is a manifesto; "Here is the output of X" is work.
- **One goal at a time (PLEASER-ONE).** The active sub-goal is the one in
  `CURRENT_GOAL.md`. Everything else is backlog.
- **Local first, paid rarely.** Claude is a consultant, not an employee.
- **Scheduled jobs, not polled loops.** LaunchDaemons (cron equivalents)
  beat continuous-agent chat loops for anything recurring.

---

## 2026-04-18 — Box MCP lacks move/delete; structural cleanup limited

**Symptom.** Wanted to archive/move 12 pre-existing subfolders from the
JakeClaw Box folder before setting up PHGDH, but available tools were
`create_folder`, `list_folder_content_by_folder_id`, and
`update_folder_properties` (name/desc/tags only — no parent mutation).

**Fix.** Created PHGDH subfolder alongside existing content. Manual cleanup
deferred to user via Box web UI.

**Prevention rule.** When provisioning shared workspaces (Box, Drive, SharePoint)
via MCP: create the new structure first; never assume you can programmatically
move/delete existing artifacts. Get user authorization for cleanup path
(archive vs trash) before starting.

---

## 2026-04-18 — Kill switch convention (RULE KILL-01)

**Rule.** Any agent (jakeclaw, qwenclaw, Chrome-Claude) that sees the phrase
`STOP-CHROME-CLAUDE` or `KILL-SWITCH` must immediately halt autonomous
action and reply only with a paused acknowledgement. Only explicit `resume`
from Jake reactivates.

**Enforcement.**
- jakeclaw AGENTS.md has RULE [KILL-01]
- qwenclaw AGENTS.md has RULE [KILL-01]
- qwenclaw_morning.sh has a pre-flight grep check against the day's log
- Future Chrome-Claude system prompt will include it verbatim

---

## 2026-04-18 — Scheduled 4 AM L0 reboot (expected, not an incident)

**Context.** At 04:00:14 CDT, L0 rebooted cleanly. `kern.boottime` confirms.
Triggered by the scheduled `com.jakeclaw.l0-keepalive` daemon, which does a
daily restart to clear swap pressure — Gemma 4 26B at ~18 GB VRAM on 24 GB
RAM accumulates memory pressure over multi-day uptime. The reboot window
sits deliberately between the 02:00 scavenger fire and the 07:00 qwenclaw
cycle, so nothing in-flight is interrupted.

**Symptom if you notice it.** Physical chime/fan-spin-up at 4 AM. L0 load
average briefly spikes to 20-30 as Ollama reloads the 21 GB Gemma model
into memory. Settles to 1-2 within ~2-3 minutes.

**Verification.** On W0:
```
ssh jakechen@10.0.0.1 "uptime"
curl -s http://10.0.0.1:11434/api/ps | jq -r ".models[].name"
```
Uptime should be small; model should be listed.

**Prevention rule.** Do NOT investigate the 4 AM reboot unless:
1. L0 fails to come back within 10 minutes, OR
2. `curl http://10.0.0.1:11434/api/ps` returns error after 04:05, OR
3. qwenclaw_morning at 07:00 hits a network-unreachable error on L0.

This is scheduled maintenance, not an incident. Never file it as RED on the
Chrome-Claude audit.

---

## 2026-04-18 — Hermes wired into qwenclaw_morning cycle (option 2)

**Gap.** Backlog goals G-004 (PubMed sweep) and G-008 (wiki page) need Hermes
wiki_builder, but the autonomous cycle only routed to jakeclaw. Hermes had
been idle since 2026-04-14 (last pipeline entry, gardening project).

**Fix.** Added HERMES_ROUTE in qwenclaw_morning.sh:
- qwenclaw planning prompt now recognizes wiki-growth keywords and emits
  `HERMES <seed>` instead of a shell command
- Orchestrator detects `HERMES ` prefix, invokes
  `/Users/jakeclaw/workers/bin/hermes_wiki_growth.sh` with the seed
- Wrapper stops any running wiki_builder, starts a fresh one with
  strategy=full depth=2 pages=10, outputs to `~/wiki/projects/phgdh-<slug>/`
- JSON summary appended to DAILY_LOG; Telegram notification to Jake

**Prevention rule.** When a new agent role is added to the architecture,
verify it has a clear invocation path from the existing cycle driver
(currently qwenclaw_morning). Loose coupling through "we could SSH to it"
doesnt count.

---

## 2026-04-18 — Hermes installed as persistent system LaunchDaemon (option 3)

**Why (addendum to earlier entry).** Option 2 alone routes wiki-growth
calls through `hermes_wiki_growth.sh` on-demand, but leaves Hermes itself
dormant until fired. Option 3 makes Hermes an always-running service so
its internal cron ticker, memory management, and skills stay warm.

**Install.** Converted `~/Library/LaunchAgents/ai.hermes.gateway.plist`
(which never auto-loaded on the headless Mac — PERSIST-01) into a
system LaunchDaemon at `/Library/LaunchDaemons/ai.hermes.gateway.plist`
with `UserName=jakeclaw`. Bootstrapped cleanly; `state = running`.

**Cold-start behavior.** On first launch the gateway logged:
- "No messaging platforms enabled" — expected; Hermes is not the Telegram
  channel (OpenClaw owns that).
- "Cron ticker started (interval=60s)" — Hermes internal scheduler now
  alive.

**Combined architecture now.**
- Persistent Hermes (option 3) — always warm, handles its own cron jobs
- On-demand Hermes invocation (option 2) — qwenclaw_morning routes
  wiki-growth goals by emitting `HERMES <seed>` and the wrapper fires
  `wiki_builder.py start` against the running instance

**Prevention rule.** Any agent meant to be "always available" must be a
system LaunchDaemon on W0, not a LaunchAgent. Re-state of PERSIST-01 —
this is the fifth time it has bitten us.

---

## 2026-04-18 — Hermes "higher purpose" documented, G-012/G-013 queued

**Insight from Jake.** Hermes shouldn't just be seed→expansion. Its mature
role is to close the loop between scavenger-produced data and literature-
synthesized knowledge: each molecule, target, pathway, gene set gets its
own grounded, wikilinked page, updated as new data arrives.

**Status.** Infrastructure exists (source_validator + wiki_builder +
holographic memory + cron). The bridge (scavenger output → Hermes seeds)
does not. Added G-012 and G-013 to BACKLOG.

**Sequencing rule.** Do not build the enrichment loop before G-001..G-005
produce curated entities to feed it. Enrichment on a cold signal yields
generic text. Enrichment on a warm signal yields real knowledge. Wait
until there is a top-20 table, a pChEMBL distribution, and binding-site
annotations before seeding this.

**Where to find the design.** DESIGN_NOTES.md at workspace root.
