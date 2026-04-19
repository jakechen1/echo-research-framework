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
    """E axis (v2, per user spec): exact anchors 5/10/20/33/50/67/80/90/95.
    Score = largest anchor not exceeding measured utilization."""
    ANCHORS = [(95,9),(90,8),(80,7),(67,6),(50,5),(33,4),(20,3),(10,2),(5,1)]
    for thresh, sc in ANCHORS:
        if pct >= thresh: return sc
    return 1

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

def score_achievement(win_start, win_end, task_id=None):
    """A axis (v2): completion % (0-100) × SOTA coverage across declared
    benchmark categories. See AGE_SCORING.md."""
    import re, subprocess
    # --- 1. Completion: parse CURRENT_GOAL.md for checkbox completion ---
    cg = Path("/Users/jakeclaw/.openclaw/workspace/project-state/CURRENT_GOAL.md")
    done = total = 0
    criteria_detail = []
    # Only parse CURRENT_GOAL checklist when it matches this task (fresh iteration);
    # for historical tasks fall straight through to artifact probe.
    cg_matches_task = False
    if cg.exists() and task_id:
        txt0 = cg.read_text()
        import re as _re; cg_matches_task = bool(_re.search(r"^\*\*Task:\*\*\s+" + _re.escape(task_id) + r"\s*$", txt0, _re.MULTILINE))
    if cg_matches_task and cg.exists():
        for line in cg.read_text().splitlines():
            m = re.match(r"-\s*\[([ xX])\]\s*(.+)", line)
            if m:
                total += 1
                is_done = m.group(1).lower() == "x"
                if is_done: done += 1
                criteria_detail.append({"done": is_done, "text": m.group(2).strip()})
    # Fallback: if no criteria found, use artifact probe via plan-sync registry
    if total == 0:
        try:
            import sys as _sys
            _sys.path.insert(0, "/Users/jakeclaw/.openclaw/workspace/skills/plan-sync/scripts")
            from plan_sync import probe
            hits = probe(task_id) if task_id else []
            total = 1
            done = 1 if hits else 0
            criteria_detail = [{"done": done==1, "text": f"artifact probe: {hits}"}]
        except Exception: pass
    completion_pct = (done / total * 100) if total else 0.0

    # --- 2. SOTA coverage: read benchmarks.json + task's sota_wins list ---
    bench_p = Path("/Users/jakeclaw/.openclaw/workspace/project-state/benchmarks.json")
    benchmarks = {}
    if bench_p.exists():
        try: benchmarks = json.loads(bench_p.read_text())
        except: pass
    task_bench = benchmarks.get(task_id or "", {}) if task_id else {}
    categories = task_bench.get("categories", [])
    wins_p = Path(f"/Users/jakeclaw/.openclaw/workspace/project-state/age_scores/_wins_{(task_id or 'x').replace(' ','-').replace('.','_')}.json")
    sota_wins = []
    if wins_p.exists():
        try: sota_wins = json.loads(wins_p.read_text()).get("sota_wins", [])
        except: pass
    n_cat = len(categories); n_wins = len([w for w in sota_wins if w in categories])
    sota_ratio = (n_wins / n_cat) if n_cat else 0.0

    # --- 3. Combined score ---
    if completion_pct < 25:  score = 1
    elif completion_pct < 50: score = 2
    elif completion_pct < 75: score = 3
    elif completion_pct < 100: score = 4
    else:
        # 100% complete — quality tier
        if sota_ratio >= 1.0:     score = 9
        elif sota_ratio >= 0.75:  score = 8
        elif sota_ratio >= 0.50:  score = 7
        elif sota_ratio >= 0.25:  score = 6
        else:                     score = 5

    return {
        "score": score,
        "completion_pct": round(completion_pct, 1),
        "criteria_total": total, "criteria_done": done,
        "sota_categories": categories,
        "sota_wins": sota_wins,
        "sota_ratio": round(sota_ratio, 2),
        "criteria_detail": criteria_detail[:10],
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
        "A": score_achievement(ws, we, args.task),
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
    # --- proactive notification (added 2026-04-18) ---
    try:
        import subprocess
        max_score = max(out['A']['score'], out['G']['score'], out['E']['score'])
        if max_score >= 8:
            subprocess.run([
                "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh",
                "🏆", f"Achievement: {args.task} iter{args.iteration}",
                f"A={out['A']['score']}  G={out['G']['score']}  E={out['E']['score']}  (score ≥ 8)"
            ], check=False, timeout=10)
        elif max_score >= 7:
            subprocess.run([
                "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh",
                "✅", f"{args.task} iter{args.iteration} scored",
                f"A={out['A']['score']}  G={out['G']['score']}  E={out['E']['score']}"
            ], check=False, timeout=10)
    except Exception:
        pass
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
