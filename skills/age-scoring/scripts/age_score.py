#!/usr/bin/env python3
"""Compute A, G, E (1-9 reverse NIH) for a task-iteration window.

Usage:
  age_score.py --task "Task 2.1" --iteration 1 --window-start ISO --window-end ISO
"""
import argparse, json, re, subprocess
from pathlib import Path
from datetime import datetime, timezone, timedelta

WS = Path("/Users/jakeclaw/.openclaw/workspace")
BDIR = WS/"project-state/age_baselines"
OUT_DIR = WS/"project-state/age_scores"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def bucket_utilization(pct: float) -> int:
    """E axis: 1-9 based on absolute utilization %."""
    # fixed anchors per spec
    if pct < 10:  return 1
    if pct < 20:  return 2
    if pct < 33:  return 3
    if pct < 45:  return 4
    if pct <= 55: return 5
    if pct < 67:  return 6
    if pct < 85:  return 7
    if pct < 95:  return 8
    return 9

def bucket_pct_vs_baseline(cur: float, base: float) -> int:
    """A & G axes: score 1-9 based on %-delta vs 7-day baseline.
    Returns 5 in ±5 % margin; buckets at ±10 %, ±20 %, ±33 %, ±50 %."""
    if base <= 0:  # no baseline (fresh repo) — give benefit of doubt
        return 7 if cur > 0 else 5
    delta = (cur - base) / base * 100.0
    if  delta >  50: return 9
    if  delta >  33: return 8
    if  delta >  20: return 7
    if  delta >  10: return 6
    if -5 <= delta <= 5: return 5
    # between -5 and +10 but outside ±5 — closer to 5/6
    if delta > 5:   return 6
    if delta > -10: return 4
    if delta > -20: return 3
    if delta > -33: return 2
    return 1

def load(p, default):
    try: return json.loads(Path(p).read_text())
    except: return default

def score_effort(win_start, win_end):
    util = WS/"project-state/utilization.jsonl"
    cpu_vals, gpu_vals = [], []
    if util.exists():
        for line in util.read_text().splitlines():
            try:
                r = json.loads(line)
                t = datetime.fromisoformat(r["at"].replace("Z","+00:00"))
                if win_start <= t <= win_end:
                    cpu_vals.append(r["w0_cpu_pct"]); gpu_vals.append(r["l0_gpu_pct"])
            except: pass
    cpu_avg = sum(cpu_vals)/len(cpu_vals) if cpu_vals else 0.0
    gpu_avg = sum(gpu_vals)/len(gpu_vals) if gpu_vals else 0.0
    combined = (cpu_avg + gpu_avg) / 2.0
    base = load(BDIR/"effort.json", {})
    return {
        "score": bucket_utilization(combined),
        "cpu_pct_window": round(cpu_avg, 2),
        "gpu_pct_window": round(gpu_avg, 2),
        "combined_pct":   round(combined, 2),
        "baseline":       base,
        "sample_count":   len(cpu_vals),
    }

def score_growth():
    REPO = Path("/Users/jakeclaw/phgdh-scavenger")
    now_bytes = 0; now_skills = 0
    for p in (REPO/"skills").rglob("*"):
        if p.is_file() and p.suffix in (".md",".py",".sh"):
            now_bytes += p.stat().st_size
            if p.name == "SKILL.md": now_skills += 1
    base = load(BDIR/"growth.json", {"byte_count":0, "skill_count":0})
    score = bucket_pct_vs_baseline(now_bytes, base.get("byte_count") or 0)
    return {
        "score": score,
        "current_bytes": now_bytes,
        "current_skills": now_skills,
        "baseline": base,
        "delta_pct": round((now_bytes - (base.get("byte_count") or 1)) / max(base.get("byte_count") or 1, 1) * 100, 2),
    }

def score_achievement(win_start, win_end):
    REPO = Path("/Users/jakeclaw/phgdh-scavenger")
    s0 = win_start.timestamp(); s1 = win_end.timestamp()
    # wiki files touched in window
    wiki_n, wiki_c = 0, 0
    for p in Path("/Users/jakeclaw/wiki").rglob("*.md"):
        try:
            m = p.stat().st_mtime
            if s0 <= m <= s1: wiki_n += 1; wiki_c += p.stat().st_size
        except: pass
    # commits in window
    commits = 0
    try:
        r = subprocess.run(
            ["git","-C",str(REPO),"log",
             f"--since={win_start.strftime('%Y-%m-%dT%H:%M')}",
             f"--until={win_end.strftime('%Y-%m-%dT%H:%M')}","--oneline"],
            capture_output=True, text=True, timeout=10)
        commits = len([l for l in r.stdout.splitlines() if l.strip()])
    except: pass
    # window-length scaled to days for baseline compare
    win_days = max((win_end - win_start).total_seconds() / 86400, 0.01)
    base = load(BDIR/"achievement.json", {})
    scores = []
    scores.append(bucket_pct_vs_baseline(wiki_n/win_days,    base.get("wiki_files_per_day") or 0))
    scores.append(bucket_pct_vs_baseline(wiki_c/win_days,    base.get("wiki_chars_per_day") or 0))
    scores.append(bucket_pct_vs_baseline(commits/win_days,   base.get("commits_per_day") or 0))
    score = round(sum(scores)/len(scores))
    return {
        "score": score,
        "wiki_files": wiki_n,
        "wiki_chars": wiki_c,
        "commits": commits,
        "window_days": round(win_days, 3),
        "component_scores": scores,
        "baseline": base,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--iteration", type=int, default=1)
    ap.add_argument("--window-start", required=True)
    ap.add_argument("--window-end", default=None)
    args = ap.parse_args()
    ws = datetime.fromisoformat(args.window_start).replace(tzinfo=timezone.utc) \
            if "+" not in args.window_start and "Z" not in args.window_start \
            else datetime.fromisoformat(args.window_start.replace("Z","+00:00"))
    we = datetime.now(timezone.utc) if not args.window_end \
         else datetime.fromisoformat(args.window_end.replace("Z","+00:00")) \
              if "Z" in args.window_end or "+" in args.window_end \
              else datetime.fromisoformat(args.window_end).replace(tzinfo=timezone.utc)

    out = {
        "task": args.task, "iteration": args.iteration,
        "window": {"start": ws.isoformat(timespec="seconds"),
                   "end":   we.isoformat(timespec="seconds")},
        "A": score_achievement(ws, we),
        "G": score_growth(),
        "E": score_effort(ws, we),
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out["summary"] = f"A={out['A']['score']} G={out['G']['score']} E={out['E']['score']}"
    slug = args.task.replace(" ","-").replace(".","_")
    fname = OUT_DIR/f"{slug}-iter{args.iteration}.json"
    fname.write_text(json.dumps(out, indent=2))
    # /tmp copy for dashboard
    try: subprocess.run(["cp","-f",str(fname),f"/tmp/phgdh_age_{slug}_iter{args.iteration}.json"], check=False)
    except: pass
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
