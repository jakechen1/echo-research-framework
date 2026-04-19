#!/usr/bin/env python3
"""Auto-resolver: read liveness, run playbook for each RED channel,
escalate per attempt ladder, log everything."""
import argparse, json, subprocess, time, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts")
from atomic_write import atomic_json_update

WS = Path("/Users/jakeclaw/.openclaw/workspace")
LIVENESS = Path("/tmp/phgdh_liveness.json")
if not LIVENESS.exists(): LIVENESS = WS/"project-state/liveness.json"
STATE = WS/"project-state/resolver_state.json"
ACTIONS = WS/"project-state/resolver_actions.jsonl"
NOTIFY = "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh"

NOW = datetime.now(timezone.utc)
NOW_STR = NOW.isoformat(timespec="seconds")

# Playbook registry: channel → function returning (action_desc, success_bool)
def pb_iteration(details):
    """Runs post_r_watchdog which handles both R-stuck and auto-promotion."""
    r = subprocess.run(
        ["/Users/jakeclaw/.hermes-venv/bin/python",
         "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts/post_r_watchdog.py"],
        capture_output=True, text=True, timeout=30)
    return f"post_r_watchdog: {r.stdout.strip()[:200]}", r.returncode == 0

def pb_l0_gpu(details):
    """Warm the L0 Gemma by issuing a tiny completion."""
    import urllib.request, urllib.error
    body = json.dumps({
        "model":"gemma4-agent-fast:latest","prompt":"ok",
        "stream":False,"options":{"num_predict":2}
    }).encode()
    try:
        req = urllib.request.Request("http://192.168.68.200:11434/api/generate",
                                      data=body, headers={"Content-Type":"application/json"})
        urllib.request.urlopen(req, timeout=10).read()
        return "L0 warm-up prompt OK", True
    except Exception as e:
        return f"L0 warm-up failed: {e}", False

def pb_scavenger(details):
    r = subprocess.run(["/Users/jakeclaw/workers/bin/phgdh_scavenger.py"],
                       capture_output=True, text=True, timeout=300)
    return f"phgdh_scavenger rc={r.returncode} out={r.stdout[-120:].strip()}", r.returncode == 0

def pb_git_push(details):
    r = subprocess.run(["/Users/jakeclaw/workers/bin/phgdh_repo_sync.sh"],
                       capture_output=True, text=True, timeout=60)
    if r.returncode != 0:
        # enqueue
        subprocess.run(["/Users/jakeclaw/.hermes-venv/bin/python",
                        "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts/enqueue.py",
                        "git_push", "repo=/Users/jakeclaw/phgdh-scavenger"],
                       check=False, timeout=5)
        return "repo_sync failed — enqueued for retry", False
    return "repo_sync OK", True

def pb_dashboard(details):
    # Dashboard runs under jakechen; we can only signal via SSH to jakechen
    r = subprocess.run(
        ["ssh","-o","ConnectTimeout=4","jakechen@localhost",
         "launchctl kickstart -k system/com.openclaw.dashboard"],
        capture_output=True, text=True, timeout=10)
    return f"dashboard kickstart rc={r.returncode}", r.returncode == 0

def pb_wiki_interlink(details):
    # Trigger the wiki_interlinker (Gemma on L0)
    r = subprocess.run(
        ["/Users/jakeclaw/.hermes-venv/bin/python",
         "/Users/jakeclaw/phgdh-scavenger/scripts/aims/aim5_wiki_interlink_gemma.py"],
        capture_output=True, text=True, timeout=600)
    return f"wiki interlink rc={r.returncode} tail={r.stdout[-120:].strip()}", r.returncode == 0


def pb_cheaha_queue(details):
    """Requeue failed Cheaha jobs once. Escalate if repeated failures."""
    try:
        import json as _j
        snap = _j.loads(Path("/tmp/phgdh_cheaha_status.json").read_text())
    except Exception:
        return "no cheaha snapshot", False
    failed = snap.get("failed_recent", 0)
    if failed == 0 and snap.get("pending", 0) > 0:
        return f"pending={snap.get('pending')} — waiting (no action)", True
    # Try one-shot resubmit of Task 4.2 sbatch
    r = subprocess.run(
        ["ssh","-o","ConnectTimeout=6","cheaha",
         "cd phgdh-sbdd && sbatch scripts/vina_top20_array.sbatch"],
        capture_output=True, text=True, timeout=30)
    ok = r.returncode == 0 and "Submitted" in r.stdout
    return f"resubmit rc={r.returncode}: {r.stdout[:120]}", ok

def pb_noop(details):
    return "no-op (channel doesn't need auto-remediation)", True

PLAYBOOKS = {
    "iteration":      pb_iteration,
    "l0_gpu":         pb_l0_gpu,
    "scavenger":      pb_scavenger,
    "git_push":       pb_git_push,
    "dashboard_api":  pb_dashboard,
    "wiki_interlink": pb_wiki_interlink,
    "box_sync":       pb_noop,
    "cheaha_queue":   pb_cheaha_queue,
    "w0_cpu":         pb_noop,
    "figures":        pb_noop,
    "aim3_structures":pb_noop,
    "aim4_smiles":    pb_noop,
}

ESCALATION = {
    1: ("🔧", "auto-remediation attempt 1 (silent)",       False, False),
    2: ("🔧", "auto-remediation attempt 2",                 True,  False),
    3: ("🚨", "auto-remediation attempt 3 (URGENT)",        True,  True),
}

def notify(emoji, title, body, urgent=False):
    args = [NOTIFY, emoji, title, body]
    if urgent: args.append("--urgent")
    try: subprocess.run(args, check=False, timeout=10)
    except: pass

def load_state():
    try: return json.loads(STATE.read_text())
    except: return {"channels": {}}

def save_state(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    def upd(_): return s
    atomic_json_update(STATE, upd, backup=False)

def log_action(rec):
    ACTIONS.parent.mkdir(parents=True, exist_ok=True)
    with ACTIONS.open("a") as f: f.write(json.dumps(rec) + "\n")

def resolve():
    live = json.loads(LIVENESS.read_text())
    red = live.get("red_channels", [])
    state = load_state()
    channels_state = state.setdefault("channels", {})

    # Reset attempt counters for channels that have been green ≥ 30 min
    for ch, cs in list(channels_state.items()):
        if ch not in red:
            last_green = cs.get("last_green_at")
            if last_green is None or (NOW - datetime.fromisoformat(last_green)).total_seconds() >= 1800:
                cs["last_green_at"] = NOW_STR
                if cs.get("attempts",0) > 0:
                    cs["attempts"] = 0
                    cs["human_required"] = False

    actions_this_run = []
    for ch in red:
        cs = channels_state.setdefault(ch, {"attempts": 0, "last_green_at": None,
                                             "human_required": False})
        cs["last_red_at"] = NOW_STR

        if cs.get("human_required"):
            # Hourly nag only
            last_nag = cs.get("last_nag_at")
            if last_nag is None or (NOW - datetime.fromisoformat(last_nag)).total_seconds() >= 3600:
                notify("🆘", f"HUMAN_REQUIRED: {ch}",
                       f"auto-resolver exhausted {cs['attempts']} attempts. Check ISSUES/OPEN.md.",
                       urgent=True)
                cs["last_nag_at"] = NOW_STR
            actions_this_run.append({"channel":ch, "skipped":"human_required"})
            continue

        cs["attempts"] = cs.get("attempts", 0) + 1
        attempt = cs["attempts"]
        playbook = PLAYBOOKS.get(ch)
        if not playbook:
            action_desc, success = f"no playbook for {ch}", False
        else:
            try: action_desc, success = playbook(live["channels"].get(ch, {}))
            except Exception as e: action_desc, success = f"playbook exception: {e}", False

        rec = {"at": NOW_STR, "channel": ch, "attempt": attempt,
               "action": action_desc, "success": success}
        log_action(rec)
        actions_this_run.append(rec)

        if success:
            # Will reset attempts once liveness reports this channel green
            pass
        else:
            if attempt in ESCALATION:
                emoji, note, do_notify, urgent = ESCALATION[attempt]
                if do_notify:
                    notify(emoji, f"auto-resolver: {ch} attempt {attempt}",
                           action_desc[:300], urgent=urgent)
            elif attempt >= 4:
                cs["human_required"] = True
                notify("🆘", f"HUMAN_REQUIRED: {ch}",
                       f"auto-resolver failed {attempt} attempts. Last action: {action_desc[:200]}",
                       urgent=True)

    save_state(state)
    print(json.dumps({"red": red, "actions": actions_this_run}, indent=2))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel", help="force run a specific channel's playbook")
    args = ap.parse_args()
    if args.channel:
        pb = PLAYBOOKS.get(args.channel)
        if not pb: print(f"no playbook: {args.channel}"); sys.exit(2)
        desc, ok = pb({})
        print(json.dumps({"channel": args.channel, "action": desc, "success": ok}))
    else:
        resolve()
