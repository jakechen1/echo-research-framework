#!/usr/bin/env python3
"""Planner — draft executor stub for a task/stage when missing."""
import argparse, json, os, subprocess
from pathlib import Path
from datetime import datetime, timezone
WS = Path("/Users/jakeclaw/.openclaw/workspace")
REG = WS/"project-state/task_executors/registry.json"

STAGE_HINTS = {
    "P": "# Plan: read BACKLOG entry, verify dependencies, write learning_notes/<task>-plan.md\n",
    "L": "# Learning: review prior wiki pages and past iteration notes; append to learning_notes/<task>-iterN.md\n",
    "E": "# Execution: produce the actual artifact (figure, dataset, CSV, page, job submission)\n",
    "A": "# Assessment: run age_score.py for this task; write assessment_notes/\n",
    "S": "# Share: publish or enqueue wiki_drafts / box upload / NAS backup\n",
    "X": "# Expense: log wall-time + tokens + CPU-hrs to project-state/expense_log.jsonl\n",
    "R": "# Resolver: close iteration; promote to next task via post_r_watchdog\n",
}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--task", required=True)
    ap.add_argument("--stage", required=True)
    args = ap.parse_args()
    slug = args.task.replace(" ","_").replace(".","_")
    stub_path = Path(f"/Users/jakeclaw/workers/bin/task_{slug}_{args.stage}.sh.pending")
    stub_path.parent.mkdir(parents=True, exist_ok=True)
    hint = STAGE_HINTS.get(args.stage, "# TODO: fill in\n")
    stub_path.write_text(f"""#!/bin/bash
# Planner draft {datetime.now(timezone.utc).isoformat(timespec='seconds')}
# Task {args.task} — stage {args.stage}
# REVIEW, EDIT, then rename to .sh (drop .pending) to activate.
#
# Return codes:
#   0 = stage complete (advancer will move to next stage)
#   2 = pending (retry next tick — for HPC polls etc.)
#   other = failure
set -euo pipefail

WS=/Users/jakeclaw/.openclaw/workspace
PY=/Users/jakeclaw/.hermes-venv/bin/python

{hint}
# TODO(planner): implement real work here for {args.task}/{args.stage}
# Until you do, this stub will exit 2 (pending) so advancer doesn't lie about progress.
echo "task_{slug}_{args.stage}: stub pending, implement me"
exit 2
""")
    stub_path.chmod(0o755)
    try: reg = json.loads(REG.read_text())
    except: reg = {"_schema": "task_id -> {stage: command}"}
    reg.setdefault(args.task, {})[args.stage] = str(stub_path)
    REG.write_text(json.dumps(reg, indent=2))
    subprocess.run([
        "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh",
        "📝", f"Planner drafted {args.task}/{args.stage} stub",
        f"Stub: {stub_path}. Review, edit, rename .pending → .sh to activate."
    ], check=False, timeout=10)
    print(json.dumps({"stub": str(stub_path), "task": args.task, "stage": args.stage}, indent=2))

if __name__ == "__main__":
    main()
