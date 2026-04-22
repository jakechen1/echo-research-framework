#!/usr/bin/env python3
"""Snapshot file counts + sizes + newest-file mtimes across key project dirs.

Writes: project-state/progress_snapshots/YYYY-MM-DDTHH-MM.json
Also updates: /tmp/phgdh_progress_latest.json (for dashboard)

No prose. Just numbers.
"""
import hashlib, json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

WS = Path("/Users/jakeclaw/.openclaw/workspace")
SNAP_DIR = WS/"project-state/progress_snapshots"
SNAP_DIR.mkdir(parents=True, exist_ok=True)

TRACK = [
    ("workspace_data",     WS/"data"),
    ("workspace_figures",  WS/"figures"),
    ("workspace_wiki",     WS/"wiki_drafts"),
    ("workspace_reports",  WS/"project-state/reports"),
    ("workspace_logs",     WS/"logs"),
    ("scavenger",          Path("/Users/jakeclaw/workers/data/phgdh")),
    ("logs_system",        Path("/Users/jakeclaw/Library/Logs")),
]

def scan(root: Path):
    files = []
    total_bytes = 0
    newest_mtime = 0
    if not root.exists():
        return {"exists": False, "file_count": 0, "total_bytes": 0,
                "newest_mtime": None, "newest_file": None, "files_sha1": None,
                "top5_largest": [], "top5_newest": []}
    for p in root.rglob("*"):
        if not p.is_file(): continue
        if any(part.startswith(".") for part in p.relative_to(root).parts): continue
        try:
            st = p.stat()
            files.append((str(p.relative_to(root)), st.st_size, st.st_mtime))
            total_bytes += st.st_size
            if st.st_mtime > newest_mtime:
                newest_mtime = st.st_mtime
        except: pass
    h = hashlib.sha1()
    for rel, sz, mt in sorted(files):
        h.update(f"{rel}:{sz}".encode())
    top5_large = sorted(files, key=lambda f: -f[1])[:5]
    top5_new = sorted(files, key=lambda f: -f[2])[:5]
    return {
        "exists": True,
        "file_count": len(files),
        "total_bytes": total_bytes,
        "newest_mtime": datetime.fromtimestamp(newest_mtime, timezone.utc).isoformat(timespec="seconds") if newest_mtime else None,
        "newest_file": top5_new[0][0] if top5_new else None,
        "files_sha1": h.hexdigest()[:16],
        "top5_largest": [{"path": f[0], "size": f[1]} for f in top5_large],
        "top5_newest": [{"path": f[0], "size": f[1],
                         "mtime": datetime.fromtimestamp(f[2], timezone.utc).isoformat(timespec="seconds")}
                        for f in top5_new],
    }

# Network bytes via netstat
def net_bytes():
    try:
        r = subprocess.run(["netstat","-ibn"], capture_output=True, text=True, timeout=5)
        total_in = total_out = 0
        for line in r.stdout.splitlines():
            parts = line.split()
            if len(parts) < 10 or parts[0] == "Name" or parts[0] == "lo0": continue
            try:
                total_in += int(parts[6]); total_out += int(parts[9])
            except: pass
        return {"bytes_in": total_in, "bytes_out": total_out}
    except: return {"bytes_in": 0, "bytes_out": 0}

# Git commits (counts) 24h
def git_activity():
    try:
        r = subprocess.run(
          ["git","-C","/Users/jakeclaw/phgdh-scavenger","log","--since=24 hours ago","--oneline"],
          capture_output=True, text=True, timeout=10)
        return {"commits_24h": len([l for l in r.stdout.splitlines() if l.strip()]),
                "latest_sha": r.stdout.splitlines()[0].split()[0] if r.stdout.strip() else None}
    except: return {"commits_24h": 0, "latest_sha": None}

# Process activity (jakeclaw-relevant)
def proc_activity():
    try:
        r = subprocess.run(["ps","-Ao","pid,%cpu,%mem,etime,comm"], capture_output=True, text=True, timeout=5)
        relevant = []
        for line in r.stdout.splitlines():
            if any(k in line for k in ["python","ollama","vina","openvpn","node","ssh"]):
                if "grep" in line: continue
                parts = line.split(None, 4)
                if len(parts) == 5 and float(parts[1]) > 0.5:
                    relevant.append({"pid":parts[0],"cpu":parts[1],"mem":parts[2],
                                     "elapsed":parts[3],"cmd":parts[4][:80]})
        return relevant[:10]
    except: return []

now = datetime.now(timezone.utc)
ts = now.isoformat(timespec="seconds")
snap = {
    "at": ts,
    "at_epoch": now.timestamp(),
    "dirs": {name: scan(p) for name, p in TRACK},
    "network": net_bytes(),
    "git": git_activity(),
    "active_procs": proc_activity(),
}
out = SNAP_DIR / f"{now.strftime('%Y-%m-%dT%H-%M-%S')}.json"
out.write_text(json.dumps(snap, indent=2))
Path("/tmp/phgdh_progress_latest.json").write_text(json.dumps(snap, indent=2))
os.chmod("/tmp/phgdh_progress_latest.json", 0o644)
print(f"snapshot {out.name}: "
      f"{sum(d['file_count'] for d in snap['dirs'].values())} files, "
      f"{sum(d['total_bytes'] for d in snap['dirs'].values()):,} bytes, "
      f"{snap['network']['bytes_out']:,} bytes out")
