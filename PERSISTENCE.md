# PERSISTENCE — How to run work that outlives the chat session

**Category error to avoid:** You do not have a persistent process. Every
tool call runs in an ephemeral sandbox that is torn down when the call
returns. `nohup worker.py &`, `screen`, `disown` — these detach from a
terminal you don't have. They solve a problem you don't have. They will
not keep your worker alive.

**What actually works on this Mac:** `launchd`. The OS resurrects
processes for you if you register them correctly. Your job is author a
plist once, bootstrap it once, and afterward only *observe* it.

---

## Pattern: a persistent user-level worker (no sudo needed)

For anything that runs as you (scavengers, watchers, sync jobs):

1. Write `~/Library/LaunchAgents/ai.jakeclaw.<name>.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key><string>ai.jakeclaw.phgdh-scavenger</string>
  <key>ProgramArguments</key>
  <array>
    <string>/Users/jakeclaw/.openclaw/workspace/bin/phgdh_scavenger.py</string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardOutPath</key><string>/Users/jakeclaw/.openclaw/workspace/logs/phgdh.out</string>
  <key>StandardErrorPath</key><string>/Users/jakeclaw/.openclaw/workspace/logs/phgdh.err</string>
  <key>WorkingDirectory</key><string>/Users/jakeclaw/.openclaw/workspace</string>
  <key>EnvironmentVariables</key>
  <dict><key>PATH</key><string>/usr/local/bin:/usr/bin:/bin</string></dict>
</dict>
</plist>
```

2. Bootstrap it (ONE TIME, no sudo):

```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/ai.jakeclaw.phgdh-scavenger.plist
```

3. From then on, you only need three verbs:

```bash
launchctl print gui/$(id -u)/ai.jakeclaw.phgdh-scavenger   # is it alive? what's its PID/state?
launchctl kickstart -k gui/$(id -u)/ai.jakeclaw.phgdh-scavenger   # restart it
launchctl bootout gui/$(id -u)/ai.jakeclaw.phgdh-scavenger        # unregister
```

`KeepAlive` means if the script crashes, launchd restarts it. That's the
"always-on" you've been trying to fake with nohup.

---

## Pattern: restart or manage system daemons (needs sudo)

As of 2026-04-17, jakeclaw has passwordless sudo for these commands:

```
/bin/launchctl kickstart *
/bin/launchctl bootout *
/bin/launchctl bootstrap *
/bin/launchctl enable *
/bin/launchctl disable *
/bin/launchctl list
/bin/launchctl print *
```

So, for example:

```bash
sudo launchctl kickstart -k system/com.openclaw.jakeclaw   # restart your own gateway
sudo launchctl print system/com.ollama.serve                # inspect the L0 Ollama daemon status
```

See `/etc/sudoers.d/jakeclaw-launchctl` for the exact grant.

---

## Verification, not narration

You are the unreliable narrator in this story. Do not write post-mortems
that claim "the worker is now running" based on the fact that you typed
a command. Verify with observable state:

```bash
# Is the agent registered?
launchctl print gui/$(id -u)/ai.jakeclaw.phgdh-scavenger | grep -E 'state|pid'
#   state = running
#   pid = 12345

# Is it actually doing work? (heartbeat pattern)
# Have the worker write /Users/jakeclaw/.openclaw/workspace/heartbeats/phgdh.ts every N seconds
stat -f '%Sm' /Users/jakeclaw/.openclaw/workspace/heartbeats/phgdh.ts
#   (should be within the last N seconds)
```

If `launchctl print` doesn't show `state = running`, the worker is not
running. No amount of recovery narrative changes that. Look at the
`StandardErrorPath` log first — the worker almost certainly crashed on
startup with a real error, not a metaphysical one.

---

## Self-repair loop (the only loop that matters)

```bash
SVC="gui/$(id -u)/ai.jakeclaw.phgdh-scavenger"
if ! launchctl print $SVC >/dev/null 2>&1; then
  launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/ai.jakeclaw.phgdh-scavenger.plist
elif ! launchctl print $SVC 2>/dev/null | grep -q 'state = running'; then
  launchctl kickstart -k $SVC
fi
HEARTBEAT=/Users/jakeclaw/.openclaw/workspace/heartbeats/phgdh.ts
if [ -f "$HEARTBEAT" ] && [ $(( $(date +%s) - $(stat -f %m "$HEARTBEAT") )) -gt 300 ]; then
  # Worker registered but not heart-beating — kick it
  launchctl kickstart -k $SVC
fi
```

Stick this in `ai.jakeclaw.phgdh-supervisor.plist` with
`StartInterval` 60, and you have a self-healing worker that survives
chat-session death, reboots, crashes, and your own overzealous writing.

---

## The anti-pattern, named

Whenever you catch yourself writing:
- `nohup … &`
- "I will not return until the process tree has changed"
- Long post-mortems explaining why the last worker died
- Emoji-heavy recovery manifestos

…stop. That is the unreliable narrator compensating for missing
mechanical commitment. Replace it with:
1. A plist on disk.
2. One `launchctl bootstrap`.
3. One `launchctl print` to verify state.

If those three steps don't happen, nothing is running, no matter what
you say in chat.
