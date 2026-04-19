#!/usr/bin/env python3
"""Assessor — writes improvement plan at PLEASER A-stage."""
import argparse, json, sys, re
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts")
from atomic_write import atomic_write

WS = Path("/Users/jakeclaw/.openclaw/workspace")
NOTES = WS/"project-state/assessment_notes"
HIST  = WS/"project-state/assessment_history.jsonl"
AGE_DIR = WS/"project-state/age_scores"
BENCH   = WS/"project-state/benchmarks.json"
NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")

ALT_REGISTRY_BY_AXIS = {
  "A_completion": [
    ("rerun_with_logging",  "Re-run failing step with set -x + tee logs; fix DoD item",    1),
    ("relax_DoD",           "Lower size-bound or dedup more aggressively; iter 1.x",        1),
    ("expand_data",         "Re-pull source data (ChEMBL/PubMed) with broader query",       2),
  ],
  "A_quality": [
    ("more_benchmarks",     "Compute comparator metrics vs benchmark; declare wins",        1),
    ("scale_data",          "10× more molecules / 10× more epochs",                          3),
    ("tune_hyperparams",    "Grid-search 3 settings on held-out 10%",                        2),
    ("ensemble",            "Combine top-3 seeds / models / docking configs",                2),
  ],
  "E_low": [
    ("parallelize",         "Fan-out N sibling jobs (respect parallelism guidance)",         1),
    ("batch_larger",        "Increase batch size (LLM num_predict, sbatch array)",           1),
    ("enable_GPU",          "Swap CPU partition → GPU partition (amperenodes/pascalnodes)",  2),
  ],
  "E_saturated": [
    ("reduce_concurrency",  "Cut parallelism if A is flat (diminishing return)",             1),
  ],
}

def load_age(task, iteration):
    slug = task.replace(" ","-").replace(".","_")
    f = AGE_DIR/f"{slug}-iter{iteration}.json"
    if not f.exists(): return None
    return json.loads(f.read_text())

def load_bench(task):
    if not BENCH.exists(): return {}
    try: return json.loads(BENCH.read_text()).get(task, {})
    except: return {}

def propose(age, bench):
    alts = []
    if not age: return []
    A = age["A"]["score"]; E = age["E"]["score"]
    A_detail = age["A"]
    # A axis
    if A_detail.get("completion_pct", 0) < 100:
        alts.extend(ALT_REGISTRY_BY_AXIS["A_completion"])
    elif A < 6:
        alts.extend(ALT_REGISTRY_BY_AXIS["A_quality"])
    # E axis
    if E < 4:
        alts.extend(ALT_REGISTRY_BY_AXIS["E_low"])
    elif E >= 8:
        alts.extend(ALT_REGISTRY_BY_AXIS["E_saturated"])
    # Dedup by id keep lowest-cost-first
    seen = set(); uniq = []
    for alt in alts:
        if alt[0] in seen: continue
        seen.add(alt[0]); uniq.append(alt)
    # Sort by cost, keep top-3
    uniq.sort(key=lambda t: t[2])
    return uniq[:3]

def decide(age, alts):
    if not age: return "NO_AGE", "run age_score.py first"
    A = age["A"]["score"]
    if A >= 7 and age["E"]["score"] >= 5:
        return "ACCEPT", "A≥7 and E≥5 — close iteration"
    if not alts:
        return "ESCALATE", f"A={A}, no matching alternatives"
    return "RETRY", f"A={A}, try: {alts[0][0]}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--iteration", type=int, default=1)
    args = ap.parse_args()
    age = load_age(args.task, args.iteration)
    bench = load_bench(args.task)
    alts = propose(age, bench)
    rec, reason = decide(age, alts)
    # Write note
    lines = [
        f"# Assessment — {args.task} iter {args.iteration}",
        f"*{NOW}*", "",
        "## Scores vs target",
        "",
        "| Axis | Actual | Target | Diagnosis |",
        "|------|-------:|-------:|-----------|",
    ]
    if age:
        A = age["A"]; E = age["E"]; G = age["G"]
        lines.append(f"| A | {A['score']} | 7+ | completion={A.get('completion_pct','?')}%, SOTA={A.get('sota_ratio','?')} |")
        lines.append(f"| G | {G['score']} | — | delta_pct={G.get('delta_pct','?')} |")
        lines.append(f"| E | {E['score']} | 6+ | combined={E.get('combined_pct','?')}% |")
    lines += ["", f"## Recommendation: **{rec}** — {reason}", "", "## Alternatives (ranked)", ""]
    for i,(aid,desc,cost) in enumerate(alts,1):
        lines.append(f"{i}. **`{aid}`** (cost {cost}) — {desc}")
    if bench:
        lines += ["", "## Benchmark comparator categories", ""]
        for cat in bench.get("categories", []):
            win = cat in (age["A"].get("sota_wins") or []) if age else False
            lines.append(f"- {'✅' if win else '⚪'} `{cat}` — baseline: {bench.get('baseline',{}).get(cat,'—')}")
    note_path = NOTES/f"{args.task.replace(' ','-').replace('.','_')}-iter{args.iteration}.md"
    note_path.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(note_path, ("\n".join(lines) + "\n").encode())
    # Append to history
    rec_obj = {"at": NOW, "task": args.task, "iteration": args.iteration,
               "recommendation": rec, "reason": reason,
               "alternatives": [a[0] for a in alts],
               "A": age["A"]["score"] if age else None,
               "E": age["E"]["score"] if age else None}
    HIST.parent.mkdir(parents=True, exist_ok=True)
    with HIST.open("a") as f: f.write(json.dumps(rec_obj) + "\n")
    print(json.dumps(rec_obj, indent=2))
    print(f"note: {note_path}")

if __name__ == "__main__":
    main()
