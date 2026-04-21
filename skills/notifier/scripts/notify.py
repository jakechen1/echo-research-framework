#!/usr/bin/env python3
"""notify v2 — adds SUPPRESS_ALERTS.json check."""
import json, os, sys, time, urllib.request, urllib.parse, hashlib
from pathlib import Path
from datetime import datetime, timezone

CFG = Path("/Users/jakeclaw/.openclaw/openclaw.json")
CHAT_ID = "8156711151"
LOG = Path("/Users/jakeclaw/.openclaw/workspace/project-state/notifications.jsonl")
DEDUP = Path("/tmp/phgdh_notify_dedup.json")
SUPPRESS_PATHS = [
    Path("/Users/jakeclaw/phgdh-scavenger/SUPPRESS_ALERTS.json"),
    Path("/Users/jakeclaw/.openclaw/workspace/SUPPRESS_ALERTS.json"),
]
DEDUP_SECS = 600
MIN_GAP = 5.0
HOURLY_CAP = 20

def _load_dedup():
    try: return json.loads(DEDUP.read_text())
    except: return {"recent": [], "last_send": 0}

def _save_dedup(d):
    try: DEDUP.write_text(json.dumps(d))
    except: pass

def _token():
    d = json.loads(CFG.read_text())
    return d["channels"]["telegram"]["botToken"]

def _suppress_check(emoji, title, body):
    """Returns True if this alert should be suppressed."""
    for p in SUPPRESS_PATHS:
        if not p.exists(): continue
        try:
            cfg = json.loads(p.read_text())
            until = cfg.get("suppressed_until")
            if until:
                until_dt = datetime.fromisoformat(until.replace("Z","+00:00"))
                if datetime.now(timezone.utc) > until_dt: continue
            for needle in cfg.get("suppress_titles_containing", []):
                if needle.lower() in title.lower() or needle.lower() in body.lower():
                    return True
        except: pass
    return False

def notify(emoji, title, body="", urgent=False):
    now = time.time()
    if _suppress_check(emoji, title, body):
        with LOG.open("a") as f:
            f.write(json.dumps({"at": now, "emoji": emoji, "title": title,
                                "suppressed": True}) + "\n")
        return False
    d = _load_dedup()
    key = hashlib.sha1(f"{emoji}|{title}".encode()).hexdigest()[:12]
    d["recent"] = [r for r in d.get("recent", []) if now - r["t"] < DEDUP_SECS]
    if not urgent and any(r["k"] == key for r in d["recent"]):
        return False
    hour_ago = now - 3600
    if len([r for r in d["recent"] if r["t"] > hour_ago]) >= HOURLY_CAP and not urgent:
        return False
    gap = now - d.get("last_send", 0)
    if gap < MIN_GAP and not urgent:
        time.sleep(MIN_GAP - gap)
    text = f"{emoji} *{title}*"
    if body: text += f"\n{body[:3500]}"
    try:
        data = urllib.parse.urlencode({
            "chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown",
        }).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{_token()}/sendMessage", data=data)
        with urllib.request.urlopen(req, timeout=8) as r:
            ok = 200 <= r.status < 300
    except Exception as e:
        ok = False
        with LOG.open("a") as f:
            f.write(json.dumps({"at": now, "emoji": emoji, "title": title,
                                "err": str(e)[:200]}) + "\n")
        try:
            import subprocess
            subprocess.run([
                "/Users/jakeclaw/.hermes-venv/bin/python",
                "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts/enqueue.py",
                "notify", f"emoji={emoji}", f"title={title}", f"body={body[:2000]}"
            ], check=False, timeout=5)
        except Exception: pass
        return False
    d["recent"].append({"t": now, "k": key}); d["last_send"] = now
    _save_dedup(d)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(json.dumps({"at": now, "emoji": emoji, "title": title,
                            "body": body, "ok": ok}) + "\n")
    return ok

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: notify.py <emoji> <title> [body]"); sys.exit(2)
    emoji, title = sys.argv[1], sys.argv[2]
    body = sys.argv[3] if len(sys.argv) > 3 else ""
    urgent = "--urgent" in sys.argv
    ok = notify(emoji, title, body, urgent=urgent)
    print("sent" if ok else "suppressed")
