# PERSISTENCE — How to run work that outlives the chat session

**Category error to avoid:** You do not have a persistent process. Every
tool call runs in an ephemeral sandbox that is torn down when the call
returns. `nohup`, `screen`, `disown` solve a problem you don't have. They
will not keep your worker alive.

**What works on this Mac:** `launchd`. The OS resurrects processes for
you if you register them correctly. Your job: author a plist once,
bootstrap once, then only *observe*.

---

## IMPORTANT — this is a headless Mac

W0 has **no GUI login session**. `launchctl print gui/$UID` returns an
empty domain. Therefore `~/Library/LaunchAgents/` **will not auto-load**
and `launchctl bootstrap gui/$UID ...` **will fail with error 125**.

**Use system-domain LaunchDaemons instead**, with `<key>UserName</key>
<string>jakeclaw</string>` to drop privileges to jakeclaw at run time.

Reference pattern already in production: `com.openclaw.jakeclaw`,
`com.jakeclaw.openclaw-watchdog`, `ai.jakeclaw.worker.daily_briefing` —
all live in `/Library/LaunchDaemons/`.

---

## Deploy a persistent worker (CORRECT pattern for W0)

1. Write the worker script at `/Users/jakeclaw/workers/bin/<name>.sh`
   and `chmod +x` it. It should write a heartbeat:
   `date +%s > /Users/jakeclaw/workers/heartbeats/<name>.ts`.

2. Author `/tmp/ai.jakeclaw.worker.<name>.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>ai.jakeclaw.worker.<NAME></string>
  <key>UserName</key><string>jakeclaw</string>
  <key>GroupName</key><string>staff</string>
  <key>ProgramArguments</key>
  <array><string>/Users/jakeclaw/workers/bin/<NAME>.sh</string></array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>ThrottleInterval</key><integer>30</integer>
  <key>StandardOutPath</key><string>/Users/jakeclaw/workers/logs/<NAME>.out</string>
  <key>StandardErrorPath</key><string>/Users/jakeclaw/workers/logs/<NAME>.err</string>
  <key>WorkingDirectory</key><string>/Users/jakeclaw/workers</string>
  <key>EnvironmentVariables</key>
  <dict>
    <key>PATH</key><string>/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin</string>
    <key>HOME</key><string>/Users/jakeclaw</string>
  </dict>
</dict>
</plist>
```

For a **continuous worker**: use `RunAtLoad=true` + `KeepAlive=true`.
For a **scheduled worker**: replace those with `StartCalendarInterval`
(e.g. `<dict><key>Hour</key><integer>8</integer></dict>` for daily 8 AM).

3. Install the plist (needs root, which jakeclaw does NOT have for
   arbitrary `cp`). Ask jakechen to run:

```bash
sudo cp /tmp/ai.jakeclaw.worker.<NAME>.plist /Library/LaunchDaemons/
sudo chown root:wheel /Library/LaunchDaemons/ai.jakeclaw.worker.<NAME>.plist
sudo chmod 644 /Library/LaunchDaemons/ai.jakeclaw.worker.<NAME>.plist
```

4. Bootstrap it (jakeclaw CAN do this — sudo launchctl is in sudoers):

```bash
sudo launchctl bootstrap system /Library/LaunchDaemons/ai.jakeclaw.worker.<NAME>.plist
```

5. Observe state — three verbs, forever:

```bash
sudo launchctl print system/ai.jakeclaw.worker.<NAME> | grep -E 'state|pid'
sudo launchctl kickstart -k system/ai.jakeclaw.worker.<NAME>   # restart
sudo launchctl bootout  system/ai.jakeclaw.worker.<NAME>       # unregister
```

`KeepAlive=true` means launchd restarts the script if it crashes. That
is the "always-on" you were trying to fake with nohup.

---

## jakeclaw's sudo capabilities (already granted)

See `/etc/sudoers.d/jakeclaw-launchctl`:
```
/bin/launchctl kickstart *
/bin/launchctl bootout *
/bin/launchctl bootstrap *
/bin/launchctl enable *
/bin/launchctl disable *
/bin/launchctl list
/bin/launchctl print *
/bin/launchctl asuser *
```

jakeclaw does NOT have sudo for `cp`, `rm`, `chown`, `chmod`, or
arbitrary file ops. Step 3 (installing the plist) requires jakechen.
Steps 4 and 5 (everything after install) you can do yourself.

---

## Verification, not narration

You are the unreliable narrator. Do not write post-mortems claiming
"the worker is now running" based on the fact that you typed a
command. Verify with observable state:

```bash
sudo launchctl print system/ai.jakeclaw.worker.<NAME> | grep -E 'state|pid'
# state = running
# pid = 12345

stat -f '%Sm' /Users/jakeclaw/workers/heartbeats/<name>.ts
# should be within the last 30s or so
```

If `launchctl print` doesn't show `state = running`, the worker is not
running. Read `StandardErrorPath` — a real error will be there, not a
metaphysical one.

---

## The anti-pattern, named

Whenever you catch yourself writing:
- `nohup … &`, `screen`, `disown`
- "I will not return until the process tree has changed"
- "DEPLOYING", "Resuscitation", emoji-heavy recovery manifestos
- "momentarily" (if a real process is running there is no momentarily,
  just observed state)

Stop. Replace with:
1. A plist at `/tmp/ai.jakeclaw.worker.<name>.plist`
2. Ask jakechen to install it
3. `sudo launchctl bootstrap system /Library/LaunchDaemons/...`
4. Paste the output of `sudo launchctl print system/ai.jakeclaw.worker.<name>`

Four mechanical steps. If they haven't happened, nothing is running.

---

## What's currently deployed

Active LaunchDaemons under jakeclaw's name (as of 2026-04-17):
- `com.openclaw.jakeclaw` — OpenClaw gateway (the thing reading this)
- `com.jakeclaw.openclaw-watchdog` — watchdog
- `com.openclaw.dashboard` — W0 dashboard (actually jakechen)
- `ai.jakeclaw.worker.daily_briefing` — daily 8 AM LLM self-report

Example workers you could add (each one = one plist + one script):
- `phgdh-scavenger` — if you actually need one (verify the task is real first)
- `heartbeat-reaper` — kills stuck workers whose heartbeats go stale
- `gateway-health-probe` — logs gateway log errors to a rolling file
- `wiki-reindex` — periodic re-scan of ~/wiki-vault/

None of these need a GUI session. All use the same pattern.
