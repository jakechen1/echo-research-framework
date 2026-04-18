#!/usr/bin/env python3
"""Replay failed Telegram sends, git pushes, wiki publishes.

Called every 120 s + on boot. Scans project-state/queues/*.jsonl, attempts
each queued action, on success removes the line from the queue.
"""
import json, os, subprocess, sys, time, urllib.request, urllib.parse
from pathlib import Path

QD = Path("/Users/jakeclaw/.openclaw/workspace/project-state/queues")
QD.mkdir(parents=True, exist_ok=True)

def _token():
    import json
    return json.loads(Path("/Users/jakeclaw/.openclaw/openclaw.json").read_text())["channels"]["telegram"]["botToken"]

def process_notify(rec):
    try:
        data = urllib.parse.urlencode({
            "chat_id": "8156711151",
            "text": f"{rec['emoji']} *{rec['title']}*\n{rec.get('body','')}",
            "parse_mode": "Markdown",
        }).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{_token()}/sendMessage", data=data)
        with urllib.request.urlopen(req, timeout=8) as r:
            return 200 <= r.status < 300
    except Exception:
        return False

def process_git_push(rec):
    repo = rec.get("repo","/Users/jakeclaw/phgdh-scavenger")
    try:
        r = subprocess.run(["git","-C",repo,"push","origin","main"],
                           capture_output=True, text=True, timeout=60)
        return r.returncode == 0
    except Exception:
        return False

def process_wiki_publish(rec):
    try:
        r = subprocess.run(["/Users/jakeclaw/workers/bin/phgdh_publish.sh"],
                           capture_output=True, text=True, timeout=300)
        return r.returncode == 0
    except Exception:
        return False

HANDLERS = {
    "notify": process_notify,
    "git_push": process_git_push,
    "wiki_publish": process_wiki_publish,
}

def replay(qfile: Path):
    if not qfile.exists() or qfile.stat().st_size == 0: return 0, 0
    remaining, ok_ct, fail_ct = [], 0, 0
    qtype = qfile.stem
    handler = HANDLERS.get(qtype)
    if not handler:
        print(f"no handler for {qtype}"); return 0, 0
    for line in qfile.read_text().splitlines():
        line = line.strip()
        if not line: continue
        try: rec = json.loads(line)
        except: continue
        if handler(rec): ok_ct += 1
        else:
            rec.setdefault("attempts", 0); rec["attempts"] += 1
            if rec["attempts"] < 50:
                remaining.append(json.dumps(rec))
            fail_ct += 1
    qfile.write_text("\n".join(remaining) + ("\n" if remaining else ""))
    return ok_ct, fail_ct

def main():
    totals = {}
    for qfile in QD.glob("*.jsonl"):
        ok, fail = replay(qfile)
        if ok or fail: totals[qfile.stem] = {"sent": ok, "failed": fail}
    if totals: print(json.dumps({"replayed": totals, "at": int(time.time())}))

if __name__ == "__main__":
    main()
