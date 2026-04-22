#!/usr/bin/env python3
"""Liveness / stuck detector. JSON to stdout + project-state/liveness.json."""
import json, os, subprocess, time, urllib.request, urllib.error, socket, re
from datetime import datetime, timezone
from pathlib import Path

WS   = Path("/Users/jakeclaw/.openclaw/workspace")
REPO = Path("/Users/jakeclaw/phgdh-scavenger")  # local mirror
NOW  = time.time()

def age(p):
    try: return NOW - Path(p).stat().st_mtime
    except: return None

def newest(glob):
    ps = list(Path(".").glob(glob)) if str(glob).startswith("/") is False else list(Path("/").glob(str(glob).lstrip("/")))
    if not ps: return None
    p = max(ps, key=lambda x: x.stat().st_mtime)
    return {"path": str(p), "age_s": NOW - p.stat().st_mtime}

def file_count(d, pat="*"):
    try: return len(list(Path(d).rglob(pat)))
    except: return 0

def curl_status(url, t=3):
    try:
        r = urllib.request.urlopen(url, timeout=t)
        return {"code": r.status, "ok": 200 <= r.status < 400}
    except Exception as e:
        return {"code": None, "ok": False, "err": str(e)[:80]}

def run(cmd, t=5):
    try: return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=t).stdout.strip()
    except: return ""

# ---- L0 GPU (via Ollama /api/ps) ----
l0_busy = None; l0_running_models = []
try:
    r = urllib.request.urlopen("http://192.168.68.200:11434/api/ps", timeout=3)
    d = json.loads(r.read())
    l0_running_models = [m.get("name") for m in d.get("models",[])]
    l0_busy = len(l0_running_models) > 0
except Exception as e:
    l0_busy = False

# ---- W0 CPU load ----
uptime = run("uptime")
load_1m = None
m = re.search(r"load averages?:\s*([\d.]+)", uptime)
if m: load_1m = float(m.group(1))
hot_procs = run("ps aux | awk '$3>5 && $11 !~ /^COMMAND/ {print $3,$11}' | head -5")

# ---- Scavenger ----
scav = list(Path("/Users/jakeclaw/workers/data/phgdh").glob("*.jsonl")) if Path("/Users/jakeclaw/workers/data/phgdh").exists() else []
scav_newest = max(scav, key=lambda x: x.stat().st_mtime) if scav else None

# ---- Figures / aim data ----
figs = list((WS/"figures").glob("*.png")) if (WS/"figures").exists() else []
fig_newest = max(figs, key=lambda x: x.stat().st_mtime) if figs else None

aim3 = file_count(WS/"data/aim3_structures", "*.pdb")
aim4 = file_count(WS/"data/aim4_smiles", "*")

# ---- Iteration state ----
its = WS/"project-state/iteration_state.json"
iter_stage = None; stage_age = None; task = None
if its.exists():
    s = json.loads(its.read_text())
    task = s.get("task"); iter_stage = s.get("stage")
    h = s.get("history",[])
    if h:
        try:
            t = datetime.fromisoformat(h[-1]["at"])
            stage_age = NOW - t.timestamp()
        except: pass

# ---- Git push freshness ----
git_last_push = None
if REPO.exists():
    s = run(f"cd {REPO} && git log -1 --format=%ct 2>/dev/null")
    try:
        if s: git_last_push = NOW - int(s)
    except: pass

# ---- Dashboard ----
dash = curl_status("http://127.0.0.1:3002/api/status", t=3)

# ---- Wiki interlink ----
wih = list((Path("/Users/jakeclaw/wiki/_generated_hubs")).glob("*.md")) if Path("/Users/jakeclaw/wiki/_generated_hubs").exists() else []
wih_newest = max(wih, key=lambda x: x.stat().st_mtime) if wih else None
wiki_audit = WS/"project-state/wiki_audit.json"

# ---- Box sync log ----
box_log = Path("/Users/jakeclaw/workers/logs/box_sync.log")

# ---- Rollup ----
def status_of(healthy_bool, unknown=False):
    if unknown: return "unknown"
    return "green" if healthy_bool else "red"


# ---- Cheaha queue + RWI from /tmp snapshot ----
cheaha_snap = Path("/tmp/phgdh_cheaha_status.json")
cheaha = {}
try:
    if cheaha_snap.exists():
        cheaha = json.loads(cheaha_snap.read_text())
except Exception: pass
cheaha_failed = cheaha.get("failed_recent", 0)
cheaha_running = cheaha.get("running", 0)
cheaha_pending = cheaha.get("pending", 0)
cheaha_has_data = bool(cheaha) and "rwi_pct" in cheaha


# ---- Progress (BS detector) ----
import subprocess as _sp_pa
progress_verdict = "unknown"
try:
    r = _sp_pa.run(["/Users/jakeclaw/.hermes-venv/bin/python",
                 "/Users/jakeclaw/.openclaw/workspace/skills/progress-audit/scripts/delta.py","--json"],
                capture_output=True, text=True, timeout=8)
    if r.returncode == 0:
        progress_verdict = (json.loads(r.stdout) or {}).get("verdict","unknown")
except Exception: pass

channels = {
    "l0_gpu": {
        "status": status_of(l0_busy or bool(l0_running_models), unknown=False),
        "running_models": l0_running_models,
    },
    "w0_cpu": {
        "status": status_of((load_1m or 0) > 0.3 or bool(hot_procs)),
        "load_1m": load_1m, "hot_procs": hot_procs.splitlines()[:3],
    },
    "scavenger": {
        "status": status_of(scav_newest and (NOW - scav_newest.stat().st_mtime) < 26*3600),
        "newest": str(scav_newest) if scav_newest else None,
        "age_h": round((NOW - scav_newest.stat().st_mtime)/3600, 1) if scav_newest else None,
        "file_count": len(scav),
    },
    "figures": {
        "status": status_of(fig_newest and (NOW - fig_newest.stat().st_mtime) < 24*3600),
        "newest": str(fig_newest) if fig_newest else None,
        "age_h": round((NOW - fig_newest.stat().st_mtime)/3600, 1) if fig_newest else None,
        "file_count": len(figs),
    },
    "aim3_structures": {"status": status_of(aim3 >= 3), "count": aim3},
    "aim4_smiles":     {"status": status_of(aim4 >= 1), "count": aim4},
    "iteration": {
        "status": status_of(stage_age is not None and stage_age < 6*3600),
        "task": task, "stage": iter_stage,
        "stage_age_h": round(stage_age/3600, 2) if stage_age else None,
    },
    "git_push": {
        "status": status_of(git_last_push is not None and git_last_push < 6*3600),
        "age_h": round(git_last_push/3600, 1) if git_last_push else None,
    },
    "dashboard_api": dash | {"status": status_of(dash["ok"] or (dash.get("err","").startswith("HTTP Error 401")))},
    "wiki_interlink": {
        "status": status_of(wih_newest and (NOW - wih_newest.stat().st_mtime) < 48*3600),
        "count": len(wih),
        "age_h": round((NOW - wih_newest.stat().st_mtime)/3600, 1) if wih_newest else None,
        "audit_age_h": round((NOW - wiki_audit.stat().st_mtime)/3600, 1) if wiki_audit.exists() else None,
    },
    "cheaha_queue": {
        "status": (status_of(True) if cheaha_running > 0 or (cheaha_has_data and cheaha_failed == 0)
                   else status_of(False) if cheaha_failed > 0 or cheaha_pending > 0
                   else status_of(False, unknown=not cheaha_has_data)),
        "running": cheaha_running, "pending": cheaha_pending,
        "failed_recent": cheaha_failed, "rwi_pct": cheaha.get("rwi_pct", None),
    },
    "progress_work": {
        "status": ("green" if progress_verdict == "PROGRESS"
                   else "red" if progress_verdict == "NO_WORK"
                   else "unknown"),
        "verdict": progress_verdict,
    },
    "box_sync": {
        "status": status_of(box_log.exists() and (NOW - box_log.stat().st_mtime) < 26*3600, unknown=not box_log.exists() or box_log.stat().st_size==0),
        "age_h": round((NOW - box_log.stat().st_mtime)/3600, 1) if box_log.exists() and box_log.stat().st_size>0 else None,
    },
}

red = [k for k,v in channels.items() if v.get("status") == "red"]
out = {
    "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    "overall": "red" if red else "green",
    "red_channels": red,
    "channels": channels,
}
(WS/"project-state/liveness.json").write_text(json.dumps(out, indent=2))
with (WS/"project-state/liveness_history.jsonl").open("a") as f:
    f.write(json.dumps({"at": out["generated_at"], "overall": out["overall"], "red": red}) + "\n")
print(json.dumps(out, indent=2))
