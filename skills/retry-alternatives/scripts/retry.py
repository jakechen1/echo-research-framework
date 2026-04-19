#!/usr/bin/env python3
"""Retry-alternatives — execute one alternative strategy, re-score, accept-if-better."""
import argparse, json, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts")
from atomic_write import atomic_write

WS = Path("/Users/jakeclaw/.openclaw/workspace")
LOG = WS/"project-state/retry_attempts.jsonl"
AGE = "/Users/jakeclaw/.openclaw/workspace/skills/age-scoring/scripts/age_score.py"
NOTIFY = "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh"
MAX_ATTEMPTS = 3

# Playbook map — thin stubs. Most real work lives in workload-optimizer + task scripts.
PLAYBOOKS = {
    "rerun_with_logging":   "echo 'rerun_with_logging: hand-edit last task script with set -x'",
    "relax_DoD":            "echo 'relax_DoD: review CURRENT_GOAL.md DoD with user'",
    "expand_data":          "/Users/jakeclaw/workers/bin/phgdh_scavenger.py",
    "more_benchmarks":      "echo 'more_benchmarks: populate benchmarks.json + declare sota_wins'",
    "scale_data":           "echo 'scale_data: submit larger Cheaha sbatch (see cheaha-hpc skill)'",
    "tune_hyperparams":     "echo 'tune_hyperparams: grid-search handled per-task'",
    "ensemble":             "echo 'ensemble: combine top-3 configs; task-specific'",
    "parallelize":          "/Users/jakeclaw/.hermes-venv/bin/python /Users/jakeclaw/.openclaw/workspace/skills/workload-optimizer/scripts/optimizer.py",
    "batch_larger":         "echo 'batch_larger: bump batch size in task script'",
    "enable_GPU":           "echo 'enable_GPU: edit sbatch --partition=amperenodes and --gres=gpu:1'",
    "reduce_concurrency":   "pkill -f 'wiki_interlink|scaffold_cluster|tanimoto' 2>/dev/null; echo 'killed expansion jobs'",
}

def log(rec):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f: f.write(json.dumps(rec) + "\n")

def count_attempts(task, iteration):
    if not LOG.exists(): return 0
    n = 0
    for line in LOG.read_text().splitlines():
        try:
            r = json.loads(line)
            if r.get("task")==task and r.get("iteration")==iteration and not r.get("transient"):
                n += 1
        except: pass
    return n

def rescore(task, iteration):
    try:
        r = subprocess.run([AGE, "--task", task, "--iteration", str(iteration),
                            "--window-start", "2026-04-18T00:00:00"],
                           capture_output=True, text=True, timeout=30)
        # find first JSON object in output
        s = r.stdout
        i = s.find("{")
        d = json.loads(s[i:])
        return d["A"]["score"], d["E"]["score"]
    except Exception as e:
        return None, None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--iteration", type=int, default=1)
    ap.add_argument("--alternative", required=True)
    args = ap.parse_args()

    n_prev = count_attempts(args.task, args.iteration)
    if n_prev >= MAX_ATTEMPTS:
        print(f"MAX_ATTEMPTS hit ({n_prev}) — escalate")
        subprocess.run([NOTIFY, "🆘", f"Retry budget exhausted: {args.task}",
                        f"3 alternatives tried without A≥target. HUMAN_ESCALATION.", "--urgent"],
                       check=False)
        sys.exit(3)

    A_before, E_before = rescore(args.task, args.iteration)
    cmd = PLAYBOOKS.get(args.alternative)
    if not cmd:
        print(f"unknown alternative {args.alternative}"); sys.exit(2)
    start = time.time()
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=1800)
    elapsed = time.time() - start
    A_after, E_after = rescore(args.task, args.iteration)

    improved = (A_after is not None and A_before is not None and A_after > A_before)
    rec = {
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "task": args.task, "iteration": args.iteration,
        "alternative": args.alternative,
        "A_before": A_before, "A_after": A_after,
        "E_before": E_before, "E_after": E_after,
        "elapsed_s": round(elapsed, 1),
        "stdout_tail": (r.stdout or "")[-300:],
        "rc": r.returncode,
        "improved": improved,
    }
    log(rec)
    emoji = "✅" if improved else "❌"
    subprocess.run([NOTIFY, emoji, f"Retry {args.alternative}: {args.task}",
                    f"A {A_before}→{A_after}, E {E_before}→{E_after} in {elapsed:.0f}s"],
                   check=False)
    print(json.dumps(rec, indent=2))

if __name__ == "__main__":
    main()
