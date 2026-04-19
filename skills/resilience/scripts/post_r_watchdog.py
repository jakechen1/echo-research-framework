#!/usr/bin/env python3
"""Post-R watchdog — if iteration is in stage R for >10 min, auto-promote to
next task from BACKLOG.md (if COMPLETED.md has that task) or start iter+1.
Runs every 5 min from scheduler_loop.
"""
import json, re, sys, datetime, subprocess
from pathlib import Path
sys.path.insert(0, "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts")
from atomic_write import atomic_json_update

WS = Path("/Users/jakeclaw/.openclaw/workspace")
ITER = WS/"project-state/iteration_state.json"
BACKLOG = WS/"project-state/BACKLOG.md"
COMPLETED = WS/"project-state/COMPLETED.md"
STALL_MIN = 10  # minutes

def next_task_from_backlog(current_task: str, completed_text: str):
    """Find next 'pending' task in BACKLOG order."""
    rows = []
    for line in BACKLOG.read_text().splitlines():
        m = re.match(r"\|\s*\*?\*?(Task\s+\d+\.\d+)\*?\*?\s*\|.+?\|\s*(G-\d+)\s*\|", line)
        if m:
            rows.append((m.group(1), m.group(2), "DONE" in line or "ACTIVE" in line))
    # find first task whose legacy id is NOT in COMPLETED.md AND is not current
    for task, lid, done_in_row in rows:
        if task == current_task: continue
        if f"## {lid} —" in completed_text: continue
        return task, lid
    return None, None

def main():
    s = json.loads(ITER.read_text())
    if s.get("stage") != "R":
        print("not in R — nothing to do"); return
    hist = s.get("history", [])
    if not hist: print("no history"); return
    last = hist[-1]
    try:
        last_t = datetime.datetime.fromisoformat(last["at"])
    except Exception:
        print(f"bad history timestamp"); return
    age_min = (datetime.datetime.now() - last_t).total_seconds() / 60
    if age_min < STALL_MIN:
        print(f"R age {age_min:.1f} min < {STALL_MIN} — no action")
        return
    cur_task = s.get("task","?")
    comp = COMPLETED.read_text() if COMPLETED.exists() else ""
    nxt, nxt_lid = next_task_from_backlog(cur_task, comp)
    if not nxt:
        print("no next task in BACKLOG — nothing to promote"); return
    def upd(x):
        x["task"] = nxt; x["legacy_id"] = nxt_lid or "?"
        x["iteration"] = 1; x["stage"] = "P"
        x["started"] = datetime.datetime.now().isoformat(timespec="seconds")
        x["history"].append({"stage":"P","at": x["started"],
            "note": f"Auto-promoted by post_r_watchdog (prev {cur_task} R stalled {age_min:.0f} min)"})
        return x
    atomic_json_update(ITER, upd, backup=True)
    # Notify
    subprocess.run([
        "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh",
        "🔄", f"Auto-promoted {cur_task} → {nxt}",
        f"Resolver R stalled {age_min:.0f} min → post_r_watchdog advanced state."
    ], check=False, timeout=10)
    print(f"promoted {cur_task} -> {nxt} (was stalled {age_min:.0f} min)")

if __name__ == "__main__":
    main()
