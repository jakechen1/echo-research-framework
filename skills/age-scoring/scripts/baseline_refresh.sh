#!/bin/bash
# Rebuild 7-day baselines for A, G, E axes.
set -u
PY=/Users/jakeclaw/.hermes-venv/bin/python
WS=/Users/jakeclaw/.openclaw/workspace
BDIR=$WS/project-state/age_baselines
mkdir -p $BDIR
$PY <<'PYEOF'
import json, re, subprocess
from pathlib import Path
from datetime import datetime, timezone, timedelta

WS = Path("/Users/jakeclaw/.openclaw/workspace")
BDIR = WS/"project-state/age_baselines"
NOW = datetime.now(timezone.utc)
CUT = NOW - timedelta(days=7)

# ---- E baseline ----
util = WS/"project-state/utilization.jsonl"
cpu_vals, gpu_vals = [], []
if util.exists():
    for line in util.read_text().splitlines():
        try:
            r = json.loads(line)
            t = datetime.fromisoformat(r["at"].replace("Z","+00:00"))
            if t >= CUT:
                cpu_vals.append(r["w0_cpu_pct"]); gpu_vals.append(r["l0_gpu_pct"])
        except: pass
e_base = {
    "cpu_mean_7d": round(sum(cpu_vals)/len(cpu_vals),2) if cpu_vals else 0.0,
    "gpu_mean_7d": round(sum(gpu_vals)/len(gpu_vals),2) if gpu_vals else 0.0,
    "sample_count": len(cpu_vals),
    "refreshed_at": NOW.isoformat(timespec="seconds"),
}
(BDIR/"effort.json").write_text(json.dumps(e_base, indent=2))

# ---- G baseline (skill tree size 7 days ago) ----
REPO = Path("/Users/jakeclaw/phgdh-scavenger")
g_base = {"byte_count": 0, "skill_count": 0, "refreshed_at": NOW.isoformat(timespec="seconds")}
try:
    sha = subprocess.check_output(
        ["git","-C",str(REPO),"log","--before",(NOW - timedelta(days=7)).strftime("%Y-%m-%d"),
         "-1","--format=%H"], text=True).strip()
    if sha:
        tree = subprocess.check_output(
            ["git","-C",str(REPO),"ls-tree","-lr",sha,"skills/"],
            text=True, stderr=subprocess.DEVNULL).strip().splitlines()
        g_base["byte_count"] = sum(int(l.split()[3]) for l in tree if len(l.split())>=4 and l.split()[3].isdigit())
        g_base["skill_count"] = sum(1 for l in tree if l.endswith("SKILL.md"))
except subprocess.CalledProcessError: pass
(BDIR/"growth.json").write_text(json.dumps(g_base, indent=2))

# ---- A baseline (avg daily output 7 days) ----
def count_in(dir_, pat, since):
    n, chars = 0, 0
    for p in Path(dir_).rglob(pat):
        try:
            if p.stat().st_mtime >= since.timestamp():
                n += 1; chars += p.stat().st_size
        except: pass
    return n, chars
wiki_n, wiki_c = count_in("/Users/jakeclaw/wiki", "*.md", CUT)
try:
    commits = int(subprocess.check_output(
        ["git","-C",str(REPO),"log","--since",CUT.strftime("%Y-%m-%d"),"--oneline"],
        text=True).strip().count("\n")+1)
except: commits = 0
a_base = {
    "wiki_files_per_day": round(wiki_n/7, 2),
    "wiki_chars_per_day": round(wiki_c/7, 2),
    "commits_per_day": round(commits/7, 2),
    "refreshed_at": NOW.isoformat(timespec="seconds"),
}
(BDIR/"achievement.json").write_text(json.dumps(a_base, indent=2))

print("E:", e_base)
print("G:", g_base)
print("A:", a_base)
PYEOF
