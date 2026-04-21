#!/usr/bin/env python3
"""Auto-resolver v2 — 2026-04-20 hardened.

Changes from v1:
  1. KILLSWITCH file check: if KILLSWITCH exists in repo OR
     /Users/jakeclaw/.openclaw/workspace/KILLSWITCH, all SSH-dependent
     playbooks fail-closed with ("KILLSWITCH active", False).
  2. SSH circuit breaker: any SSH timeout trips a 1-hour cooldown on
     ALL ssh-dependent playbooks via /tmp/phgdh_ssh_breaker_until.txt.
  3. Counter reset bug fix: `last_green_at is None` no longer resets
     attempts. Reset requires sustained-green ≥ 30 min from known-green
     baseline.
  4. Hard MAX_ATTEMPTS in 24 h: separate counter that NEVER resets
     within a day. Prevents flapping loops.
"""
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

KILLSWITCH_PATHS = [
    WS/"KILLSWITCH",
    Path("/Users/jakeclaw/phgdh-scavenger/KILLSWITCH"),
]
SSH_BREAKER_FILE = Path("/tmp/phgdh_ssh_breaker_until.txt")
HARD_MAX_24H = 4  # hard cap per channel per 24 hours, never resets

NOW = datetime.now(timezone.utc)
NOW_STR = NOW.isoformat(timespec="seconds")
NOW_TS = NOW.timestamp()

# ---- KILLSWITCH ----
def killswitch_active():
    for p in KILLSWITCH_PATHS:
        if p.exists(): return str(p)
    return None

# ---- SSH circuit breaker ----
def ssh_breaker_open():
    try:
        until = float(SSH_BREAKER_FILE.read_text().strip())
        return NOW_TS < until
    except Exception: return False

def trip_ssh_breaker(seconds=3600):
    SSH_BREAKER_FILE.write_text(str(NOW_TS + seconds))

# ---- Playbooks ----
def pb_cheaha_queue(details):
    ks = killswitch_active()
    if ks:
        return f"KILLSWITCH active ({ks}) — refusing SSH submit", False
    if ssh_breaker_open():
        return "SSH circuit breaker open — refusing SSH submit", False
    try: snap = json.loads(Path("/tmp/phgdh_cheaha_status.json").read_text())
    except Exception: return "no cheaha snapshot", False
    # GUARD: if we had a successful recent submission, don't resubmit same job
    if snap.get("running",0) > 0:
        return f"running={snap.get('running')} — letting it finish", True
    if snap.get("failed_recent",0) == 0:
        return "no recent failures — nothing to remediate", True
    r = subprocess.run(
        ["ssh","-o","ConnectTimeout=6","-o","BatchMode=yes","cheaha",
         "cd phgdh-sbdd && sbatch scripts/vina_top20_array.sbatch"],
        capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        if "timed out" in (r.stderr or "").lower() or r.returncode == 124:
            trip_ssh_breaker(3600)
            return f"SSH timeout — tripped 1h breaker", False
    return f"rc={r.returncode}: {(r.stdout or r.stderr)[:120]}", "Submitted" in r.stdout

def pb_l0_gpu(details):
    if ssh_breaker_open(): return "breaker open", False
    import urllib.request
    try:
        urllib.request.urlopen(urllib.request.Request(
            "http://192.168.68.200:11434/api/generate",
            data=json.dumps({"model":"gemma4-agent-fast:latest","prompt":"ok",
                             "stream":False,"options":{"num_predict":2}}).encode(),
            headers={"Content-Type":"application/json"}), timeout=10).read()
        return "warmed", True
    except Exception as e: return f"warm failed: {e}", False

def pb_noop(details): return "no-op", True

PLAYBOOKS = {
    "cheaha_queue":   pb_cheaha_queue,
    "l0_gpu":         pb_l0_gpu,
    "w0_cpu":         pb_noop,
    "scavenger":      pb_noop,
    "figures":        pb_noop,
    "aim3_structures":pb_noop,
    "aim4_smiles":    pb_noop,
    "dashboard_api":  pb_noop,
    "wiki_interlink": pb_noop,
    "box_sync":       pb_noop,
    "iteration":      pb_noop,
    "git_push":       pb_noop,
}

def load_state():
    try: return json.loads(STATE.read_text())
    except: return {"channels": {}}

def save_state(s):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    atomic_json_update(STATE, lambda _: s, backup=False)

def log_action(rec):
    ACTIONS.parent.mkdir(parents=True, exist_ok=True)
    with ACTIONS.open("a") as f: f.write(json.dumps(rec) + "\n")

def resolve():
    # KILLSWITCH short-circuits the whole resolver
    ks = killswitch_active()
    if ks:
        print(json.dumps({"killswitch_active": ks, "at": NOW_STR}))
        return

    live = json.loads(LIVENESS.read_text())
    red = live.get("red_channels", [])
    state = load_state()
    channels = state.setdefault("channels", {})

    # Hard 24-hour cap — count attempts in window from actions log
    attempts_24h = {}
    cutoff = NOW_TS - 86400
    if ACTIONS.exists():
        for line in ACTIONS.read_text().splitlines()[-2000:]:
            try:
                r = json.loads(line)
                t = datetime.fromisoformat(r["at"].replace("Z","+00:00")).timestamp()
                if t >= cutoff:
                    attempts_24h[r.get("channel","?")] = attempts_24h.get(r.get("channel","?"),0)+1
            except: pass

    # Reset ephemeral counters only after 30 min sustained green AND had been green before
    for ch, cs in list(channels.items()):
        if ch not in red:
            lg = cs.get("last_green_at")
            if lg is not None:
                age = NOW_TS - datetime.fromisoformat(lg.replace("Z","+00:00")).timestamp()
                if age >= 1800 and cs.get("attempts",0) > 0:
                    cs["attempts"] = 0
            # Note: never reset from "never been green" state.

    actions_this_run = []
    for ch in red:
        cs = channels.setdefault(ch, {"attempts":0, "last_green_at":None})
        cs["last_red_at"] = NOW_STR

        # Hard 24h cap
        if attempts_24h.get(ch, 0) >= HARD_MAX_24H:
            actions_this_run.append({"channel":ch, "skipped":f"24h cap ({HARD_MAX_24H}) reached"})
            continue

        cs["attempts"] += 1
        attempt = cs["attempts"]
        pb = PLAYBOOKS.get(ch)
        if not pb:
            action_desc, success = f"no playbook for {ch}", False
        else:
            try: action_desc, success = pb(live["channels"].get(ch, {}))
            except Exception as e: action_desc, success = f"playbook exception: {e}", False

        rec = {"at":NOW_STR, "channel":ch, "attempt":attempt,
               "attempts_24h":attempts_24h.get(ch,0)+1,
               "action":action_desc, "success":success}
        log_action(rec)
        actions_this_run.append(rec)

        # Escalation
        if not success:
            if attempt == 2:
                subprocess.run([NOTIFY, "🔧", f"auto-resolver: {ch} attempt 2",
                                action_desc[:300]], check=False, timeout=8)
            elif attempt >= 3:
                subprocess.run([NOTIFY, "🚨", f"auto-resolver: {ch} attempt {attempt} (24h={attempts_24h.get(ch,0)+1})",
                                action_desc[:300], "--urgent"], check=False, timeout=8)

    save_state(state)
    print(json.dumps({"red":red, "actions":actions_this_run,
                      "killswitch":ks, "ssh_breaker":ssh_breaker_open()}, indent=2))

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--channel")
    args = ap.parse_args()
    if args.channel:
        pb = PLAYBOOKS.get(args.channel)
        if not pb: print(f"no playbook: {args.channel}"); sys.exit(2)
        desc, ok = pb({})
        print(json.dumps({"channel":args.channel,"action":desc,"success":ok}))
    else:
        resolve()
