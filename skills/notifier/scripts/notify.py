#!/usr/bin/env python3
"""Proactive Telegram notifier with rate-limit + dedup.

CLI:  notify.py <emoji> <title> [body]
Lib:  from notify import notify; notify("🎯", "Task done", "...")
"""
import json, os, sys, time, urllib.request, urllib.parse, hashlib
from pathlib import Path

CFG = Path("/Users/jakeclaw/.openclaw/openclaw.json")
CHAT_ID = "8156711151"
LOG = Path("/Users/jakeclaw/.openclaw/workspace/project-state/notifications.jsonl")
DEDUP = Path("/tmp/phgdh_notify_dedup.json")
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

def notify(emoji: str, title: str, body: str = "", urgent: bool = False) -> bool:
    """Returns True if sent, False if suppressed (dedup/rate-limit)."""
    now = time.time()
    d = _load_dedup()
    key = hashlib.sha1(f"{emoji}|{title}".encode()).hexdigest()[:12]
    # dedup
    d["recent"] = [r for r in d.get("recent", []) if now - r["t"] < DEDUP_SECS]
    if not urgent and any(r["k"] == key for r in d["recent"]):
        return False
    # hourly cap
    hour_ago = now - 3600
    if len([r for r in d["recent"] if r["t"] > hour_ago]) >= HOURLY_CAP and not urgent:
        return False
    # min-gap
    gap = now - d.get("last_send", 0)
    if gap < MIN_GAP and not urgent:
        time.sleep(MIN_GAP - gap)
    # send
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
            f.write(json.dumps({"at": now, "emoji": emoji, "title": title, "err": str(e)[:200]}) + "\n")
        try:
            import subprocess
            subprocess.run([
                "/Users/jakeclaw/.hermes-venv/bin/python",
                "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts/enqueue.py",
                "notify", f"emoji={emoji}", f"title={title}", f"body={body[:2000]}"
            ], check=False, timeout=5)
        except Exception:
            pass
        return False
    d["recent"].append({"t": now, "k": key})
    d["last_send"] = now
    _save_dedup(d)
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(json.dumps({"at": now, "emoji": emoji, "title": title, "body": body, "ok": ok}) + "\n")
    return ok

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: notify.py <emoji> <title> [body]"); sys.exit(2)
    emoji, title = sys.argv[1], sys.argv[2]
    body = sys.argv[3] if len(sys.argv) > 3 else ""
    urgent = "--urgent" in sys.argv
    ok = notify(emoji, title, body, urgent=urgent)
    print("sent" if ok else "suppressed")
