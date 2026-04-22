#!/usr/bin/env python3
"""Compare the most recent two snapshots. Print the delta no-prose.
Also supports --since=<ISO> to compare against earliest snapshot after that time."""
import argparse, json, os, sys
from datetime import datetime, timezone
from pathlib import Path

SNAP_DIR = Path("/Users/jakeclaw/.openclaw/workspace/project-state/progress_snapshots")
snaps = sorted(SNAP_DIR.glob("*.json"))
if len(snaps) < 2:
    print("need at least 2 snapshots"); sys.exit(1)

ap = argparse.ArgumentParser()
ap.add_argument("--since", help="ISO timestamp; compare latest to earliest snap after this")
ap.add_argument("--json", action="store_true")
args = ap.parse_args()

if args.since:
    target = datetime.fromisoformat(args.since.replace("Z","+00:00"))
    older = None
    for s in snaps:
        d = json.loads(s.read_text())
        if datetime.fromisoformat(d["at"].replace("Z","+00:00")) >= target:
            older = d; break
    older = older or json.loads(snaps[0].read_text())
else:
    older = json.loads(snaps[-2].read_text())
newer = json.loads(snaps[-1].read_text())

minutes = (newer["at_epoch"] - older["at_epoch"]) / 60
delta = {
    "from": older["at"], "to": newer["at"],
    "window_min": round(minutes, 1),
    "dirs": {},
    "net_bytes_in_delta":  newer["network"]["bytes_in"]  - older["network"]["bytes_in"],
    "net_bytes_out_delta": newer["network"]["bytes_out"] - older["network"]["bytes_out"],
    "commits_delta":       newer["git"]["commits_24h"]  - older["git"]["commits_24h"],
}
total_files_added = 0
total_bytes_added = 0
for name in newer["dirs"]:
    o, n = older["dirs"].get(name,{}), newer["dirs"][name]
    files_d = n.get("file_count",0) - o.get("file_count",0)
    bytes_d = n.get("total_bytes",0) - o.get("total_bytes",0)
    sha_changed = o.get("files_sha1") != n.get("files_sha1")
    delta["dirs"][name] = {"files_added": files_d, "bytes_added": bytes_d,
                           "sha_changed": sha_changed,
                           "newest": n.get("newest_mtime"),
                           "sample_new": n.get("top5_newest",[])[:3]}
    total_files_added += max(0, files_d)
    total_bytes_added += max(0, bytes_d)

delta["total_files_added"] = total_files_added
delta["total_bytes_added"] = total_bytes_added

# Verdict (the BS detector)
verdict = "PROGRESS" if (total_files_added > 0 or total_bytes_added > 1024) else "IDLE"
if total_bytes_added == 0 and delta["net_bytes_out_delta"] < 10000:
    verdict = "NO_WORK"
delta["verdict"] = verdict

if args.json:
    print(json.dumps(delta, indent=2))
else:
    print(f"Window: {delta['from']} → {delta['to']} ({delta['window_min']:.1f} min)")
    print(f"VERDICT: {verdict}")
    print(f"Total files added: {total_files_added}")
    print(f"Total bytes added: {total_bytes_added:,}")
    print(f"Network out: {delta['net_bytes_out_delta']:,} bytes")
    print(f"Git commits: {delta['commits_delta']}")
    print(f"Per-dir:")
    for name, d in delta["dirs"].items():
        marker = "*" if d["sha_changed"] else " "
        print(f"  {marker} {name:20s}  +{d['files_added']:>4} files  +{d['bytes_added']:>10,} bytes")
        for s in d["sample_new"]:
            print(f"       └─ {s.get('path','?')}  ({s.get('size',0):,}B)")
