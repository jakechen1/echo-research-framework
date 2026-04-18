#!/bin/bash
# Runs on LaunchAgent RunAtLoad. Validates state, sends resumption notice.
set -u
WS=/Users/jakeclaw/.openclaw/workspace
PY=/Users/jakeclaw/.hermes-venv/bin/python
LOG=/Users/jakeclaw/Library/Logs/ai.jakeclaw.resilience_boot.out
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] on_boot start" >> $LOG

# 1. Validate JSON state files; restore from .bak on corruption
$PY - <<'PYEOF' >> $LOG 2>&1
import json, os
from pathlib import Path
WS = Path("/Users/jakeclaw/.openclaw/workspace")
CHECK = [
    WS/"project-state/iteration_state.json",
    WS/"project-state/liveness.json",
]
CHECK += list((WS/"project-state/age_baselines").glob("*.json"))
CHECK += list((WS/"project-state/age_scores").glob("*.json"))
for p in CHECK:
    if not p.exists(): continue
    try: json.loads(p.read_text()); print(f"ok   {p}")
    except Exception as e:
        bak = p.with_suffix(p.suffix + ".bak")
        if bak.exists():
            try:
                json.loads(bak.read_text())
                os.replace(str(bak), str(p))
                print(f"RESTORED {p} from .bak")
            except Exception:
                print(f"CORRUPT {p} and .bak: {e}")
        else:
            print(f"CORRUPT {p} (no .bak): {e}")
PYEOF

# 2. Kick off liveness + baseline + sampler once
bash $WS/skills/liveness-audit/scripts/liveness.sh >> $LOG 2>&1 || true
bash $WS/skills/age-scoring/scripts/baseline_refresh.sh >> $LOG 2>&1 || true
$PY $WS/skills/age-scoring/scripts/utilization_sampler.py >> $LOG 2>&1 || true

# 3. Check iteration stall
$PY - <<'PYEOF' >> $LOG 2>&1
import json, datetime
p = "/Users/jakeclaw/.openclaw/workspace/project-state/iteration_state.json"
s = json.load(open(p))
last = s["history"][-1] if s.get("history") else None
if last:
    age_min = (datetime.datetime.now() - datetime.datetime.fromisoformat(last["at"])).total_seconds() / 60
    print(f"stage={s.get('stage')} last_change={last['at']} age_min={age_min:.1f}")
    if age_min > 60:
        import subprocess
        subprocess.run([
            "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh",
            "🔁", "W0 resumed — iteration stalled",
            f"Task {s.get('task','?')} in stage {s.get('stage')} for {age_min:.0f} min. on_boot recovery firing.",
            "--urgent"
        ], check=False)
PYEOF

# 4. Replay any queued items
$PY $WS/skills/resilience/scripts/retry_queue.py >> $LOG 2>&1 || true

# 5. Send boot notification
BOOT_TIME=$(sysctl -n kern.boottime | sed -E 's/.*sec = ([0-9]+).*/\1/')
NOW=$(date +%s)
UP_MIN=$(( (NOW - BOOT_TIME) / 60 ))
bash $WS/skills/notifier/scripts/notify.sh "🔁" "W0 booted — resilience OK" "Uptime ${UP_MIN} min. State validated. Queues replayed." --urgent >> $LOG 2>&1
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] on_boot done" >> $LOG
