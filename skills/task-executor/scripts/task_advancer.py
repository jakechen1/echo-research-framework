#!/usr/bin/env python3
"""Continuously drive the current task through PLEASER stages.

Reads iteration_state + per-task executor registry. For the current stage:
  1. If an executor is defined, run it (respects a per-stage cooldown)
  2. On success (rc=0), advance to the next stage
  3. On rc=2 (pending — e.g. Cheaha job still running), stay in stage
  4. On rc!=0,2: log error, don't advance; retry next tick
"""
import json, os, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts")
from atomic_write import atomic_json_update

WS = Path("/Users/jakeclaw/.openclaw/workspace")
ITER = WS/"project-state/iteration_state.json"
REG  = WS/"project-state/task_executors/registry.json"
COOLDOWN = WS/"project-state/task_executors/cooldowns.json"
LOG = WS/"project-state/task_executors/advancer.log"
ADV_SH = "/Users/jakeclaw/workers/bin/advance_stage.sh"

STAGE_NEXT = {"P":"L","L":"E","E":"A","A":"S","S":"X","X":"R"}  # R handled by post_r_watchdog
COOLDOWN_MIN = 4  # don't rerun same executor more than every 4 min
NOW = time.time()

def load_json(p, default):
    try: return json.loads(p.read_text())
    except: return default

def log(msg):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("a") as f:
        f.write(f"[{datetime.now(timezone.utc).isoformat(timespec='seconds')}] {msg}\n")

def main():
    state = load_json(ITER, {})
    task = state.get("task"); stage = state.get("stage")
    if not task or not stage: log("no task/stage"); return
    if stage == "R": log("in R — handled by post_r_watchdog"); return

    reg = load_json(REG, {})
    task_reg = reg.get(task, {})
    cmd = task_reg.get(stage)

    cd = load_json(COOLDOWN, {})
    key = f"{task}/{stage}"
    last = cd.get(key, 0)
    if NOW - last < COOLDOWN_MIN * 60:
        log(f"{key} cooldown ({NOW-last:.0f}s < {COOLDOWN_MIN*60}s)")
        return

    if not cmd:
        # No executor — auto-advance with a note
        nxt = STAGE_NEXT.get(stage)
        if nxt:
            subprocess.run([ADV_SH, nxt, f"auto-advance (no executor for {task}/{stage})"],
                           check=False, timeout=15)
            log(f"{key} auto-advanced to {nxt} (no executor)")
        return

    # Execute
    log(f"{key} running: {cmd}")
    cd[key] = NOW
    atomic_json_update(COOLDOWN, lambda _: cd, backup=False)
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=1800)
    log(f"{key} rc={r.returncode}  stdout_tail={r.stdout[-300:]!r}  stderr_tail={r.stderr[-200:]!r}")

    if r.returncode == 0:
        # advance
        nxt = STAGE_NEXT.get(stage)
        if nxt:
            subprocess.run([ADV_SH, nxt, f"executor {stage} succeeded"],
                           check=False, timeout=15)
            log(f"{key} advanced to {nxt}")
    elif r.returncode == 2:
        log(f"{key} pending — stay in stage (will retry)")
    else:
        log(f"{key} FAILED rc={r.returncode} — will retry next tick")

if __name__ == "__main__":
    main()
