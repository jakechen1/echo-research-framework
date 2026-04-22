#!/usr/bin/env python3
"""Assessor tick — the single source of truth for 'what's happening'.

Runs every 3 min. Consolidates:
  - progress-audit delta (files/bytes/network)
  - liveness snapshot (10 channels)
  - iteration_state (current task/stage + stage age)
  - utilization (L0 GPU + W0 CPU + Cheaha RWI)
  - AGE scores (latest per task)

Writes: project-state/assessor_log.jsonl (append-only, one line per tick)
Also: /tmp/phgdh_assessor_latest.json (dashboard)

Every other component (Planner, Resolver, Executor, Learner, report_builder,
task_advancer) reads this log instead of making up its own view. This
prevents "background preparation phase" style prose from diverging from
reality — the ledger is authoritative.
"""
import json, os, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path

WS = Path("/Users/jakeclaw/.openclaw/workspace")
LOG = WS/"project-state/assessor_log.jsonl"
LATEST = Path("/tmp/phgdh_assessor_latest.json")

def _read_json(path, default=None):
    try: return json.loads(Path(path).read_text())
    except: return default or {}

def _delta():
    try:
        r = subprocess.run(["/Users/jakeclaw/.hermes-venv/bin/python",
                            "/Users/jakeclaw/.openclaw/workspace/skills/progress-audit/scripts/delta.py","--json"],
                            capture_output=True, text=True, timeout=10)
        return json.loads(r.stdout) if r.returncode == 0 else None
    except: return None

def _latest_age():
    d = WS/"project-state/age_scores"
    if not d.exists(): return None
    files = sorted(d.glob("*.json"), key=lambda p: p.stat().st_mtime)
    return _read_json(files[-1]) if files else None

def _iteration_age_min(state):
    h = state.get("history", [])
    if not h: return None
    try:
        t = datetime.fromisoformat(h[-1]["at"].replace("Z","+00:00"))
        return round((datetime.now(timezone.utc) - t).total_seconds()/60, 1)
    except: return None

def _stall_alerts():
    p = WS/"project-state/task_executors/stall_alerts.json"
    return _read_json(p, {})

now = datetime.now(timezone.utc)
state = _read_json(WS/"project-state/iteration_state.json")
liveness = _read_json("/tmp/phgdh_liveness.json")
delta = _delta()
age = _latest_age()

entry = {
    "at": now.isoformat(timespec="seconds"),
    "task": state.get("task"),
    "stage": state.get("stage"),
    "iteration": state.get("iteration"),
    "stage_age_min": _iteration_age_min(state),
    "progress": {
        "verdict": (delta or {}).get("verdict", "unknown"),
        "files_added": (delta or {}).get("total_files_added", 0),
        "bytes_added": (delta or {}).get("total_bytes_added", 0),
        "net_bytes_out": (delta or {}).get("net_bytes_out_delta", 0),
        "commits": (delta or {}).get("commits_delta", 0),
        "window_min": (delta or {}).get("window_min", 0),
    },
    "liveness": {
        "overall": liveness.get("overall"),
        "red_channels": liveness.get("red_channels", []),
    },
    "age": {
        "task": (age or {}).get("task"),
        "summary": (age or {}).get("summary"),
        "A": (age or {}).get("A", {}).get("score"),
        "G": (age or {}).get("G", {}).get("score"),
        "E": (age or {}).get("E", {}).get("score"),
    } if age else None,
    "stalls": list(_stall_alerts().keys()),
    # Computed decisions the assessor makes visible for others to consume
    "flags": {
        "STAGE_STALLED": (_iteration_age_min(state) or 0) > 60,
        "NO_WORK_THIS_WINDOW": (delta or {}).get("verdict") == "NO_WORK",
        "BLOCKED": bool(_stall_alerts()),
        "AGE_SUBPAR": ((age or {}).get("A", {}).get("score") or 5) < 5,
    },
}

LOG.parent.mkdir(parents=True, exist_ok=True)
with LOG.open("a") as f:
    f.write(json.dumps(entry) + "\n")

# Also write the latest entry to /tmp for dashboard + fast reads
LATEST.write_text(json.dumps(entry, indent=2))
os.chmod(LATEST, 0o644)

print(json.dumps(entry, indent=2))
