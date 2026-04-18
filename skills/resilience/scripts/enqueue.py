#!/usr/bin/env python3
"""enqueue.py <qtype> [json-fields...]  — append to queue atomically."""
import json, sys, time, fcntl
from pathlib import Path
QD = Path("/Users/jakeclaw/.openclaw/workspace/project-state/queues")
QD.mkdir(parents=True, exist_ok=True)
qtype = sys.argv[1]
rec = {"at": int(time.time())}
# remaining args as key=value
for a in sys.argv[2:]:
    if "=" in a: k,v = a.split("=",1); rec[k] = v
    else: rec["value"] = a
qfile = QD/f"{qtype}.jsonl"
with qfile.open("a") as f:
    fcntl.flock(f, fcntl.LOCK_EX)
    f.write(json.dumps(rec) + "\n")
    fcntl.flock(f, fcntl.LOCK_UN)
print(f"enqueued {qtype}")
