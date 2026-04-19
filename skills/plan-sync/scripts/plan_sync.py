#!/usr/bin/env python3
"""plan-sync: reconcile BACKLOG.md statuses with COMPLETED.md + artifacts.

Writes PLAN_STATUS.md. Sends 📋 Telegram when a task status flips."""
import json, re, subprocess, sys, time
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts")
from atomic_write import atomic_write

WS = Path("/Users/jakeclaw/.openclaw/workspace")
BACKLOG = WS/"project-state/BACKLOG.md"
COMPLETED = WS/"project-state/COMPLETED.md"
ITER = WS/"project-state/iteration_state.json"
STATUS = WS/"project-state/PLAN_STATUS.md"
CACHE = WS/"project-state/plan_sync_cache.json"

NOW = datetime.now(timezone.utc)

# Artifact probes: (task_id, required_paths, min_bytes)
PROBES = {
    "Task 1.1": [("/Users/jakeclaw/workers/data/phgdh", "*.jsonl", 10_000, 30*3600)],
    "Task 2.1": [(str(WS/"figures"), "pchembl_dist.png", 10_000, None)],
    "Task 2.2": [(str(WS/"data"), "aim2_top20_inhibitors.csv", 1_000, None)],
    "Task 2.3": [(str(WS/"data"), "aim2_pdb_binding_sites.json", 1_000, None)],
    "Task 3.1": [(str(WS/"data"), "aim3_pubmed_phgdh_allosteric.json", 1_000, None)],
    "Task 4.1": [(str(WS/"data/aim4_docking_results"), "lig1_docked.pdbqt", 5_000, None)],
    "Task 4.2": [(str(WS/"data"), "aim4_vina_top20_ranked.csv", 500, None)],
}

def probe(task_id):
    specs = PROBES.get(task_id, [])
    if not specs: return None
    hits = []
    for root, pat, min_bytes, max_age_s in specs:
        for p in Path(root).glob(pat) if Path(root).exists() else []:
            try:
                st = p.stat()
                if st.st_size < min_bytes: continue
                if max_age_s is not None and (time.time() - st.st_mtime) > max_age_s: continue
                hits.append({"path": str(p), "size": st.st_size,
                             "mtime": datetime.fromtimestamp(st.st_mtime, timezone.utc).isoformat(timespec="seconds")})
                break
            except: pass
    return hits

def parse_backlog():
    """Return list of {aim, task, title, legacy_id, status_line}."""
    tasks = []
    cur_aim = None
    for line in BACKLOG.read_text().splitlines():
        m = re.match(r"^##\s+Aim\s+(\d+)\s*—\s*(.+)$", line)
        if m: cur_aim = f"Aim {m.group(1)}"; continue
        m = re.match(r"\|\s*\*?\*?(Task\s+\d+\.\d+(?:\.\w+)?)\*?\*?\s*\|\s*([^|]+)\s*\|\s*(G-\d+|—|-)\s*\|", line)
        if m:
            tasks.append({
                "aim": cur_aim, "task": m.group(1), "title": m.group(2).strip(),
                "legacy_id": m.group(3).strip(),
                "raw_line": line,
            })
    return tasks

def derive_status(task, completed_text, current_task):
    # 1. COMPLETED.md wins
    if task["legacy_id"] and task["legacy_id"] != "—" and f"## {task['legacy_id']} —" in completed_text:
        return "DONE", "via COMPLETED.md"
    # 2. artifact probe
    hits = probe(task["task"])
    if hits:
        return "DONE", f"artifact: {Path(hits[0]['path']).name} ({hits[0]['size']}B)"
    # 3. active
    if current_task == task["task"]:
        return "ACTIVE", "current iteration"
    return "pending", ""

def main():
    if not BACKLOG.exists():
        print("no BACKLOG.md"); sys.exit(2)
    completed = COMPLETED.read_text() if COMPLETED.exists() else ""
    try: iter_state = json.loads(ITER.read_text())
    except: iter_state = {}
    current_task = iter_state.get("task","")

    tasks = parse_backlog()
    prev_cache = {}
    if CACHE.exists():
        try: prev_cache = json.loads(CACHE.read_text())
        except: pass

    flips = []
    new_cache = {}
    for t in tasks:
        status, reason = derive_status(t, completed, current_task)
        t["status"] = status; t["reason"] = reason
        key = t["task"]
        prev_status = prev_cache.get(key, {}).get("status")
        new_cache[key] = {"status": status, "reason": reason,
                          "at": NOW.isoformat(timespec="seconds")}
        if prev_status and prev_status != status:
            flips.append((key, prev_status, status))

    # Aim-level rollup
    per_aim = {}
    for t in tasks:
        aim = t["aim"]
        per_aim.setdefault(aim, {"done":0,"active":0,"pending":0,"tasks":[]})
        s = {"DONE":"done","ACTIVE":"active","pending":"pending"}.get(t["status"],"pending")
        per_aim[aim][s] += 1
        per_aim[aim]["tasks"].append(t)

    # Write PLAN_STATUS.md
    lines = [
        f"# Plan Status — auto-generated {NOW.isoformat(timespec='seconds')}",
        "",
        f"Current task: **{current_task or '—'}**  stage: **{iter_state.get('stage','?')}**  iter: {iter_state.get('iteration','?')}",
        "",
        "## Aim rollup",
        "",
        "| Aim | Done | Active | Pending |",
        "|-----|-----:|-------:|--------:|",
    ]
    for aim, d in sorted(per_aim.items()):
        lines.append(f"| {aim} | {d['done']} | {d['active']} | {d['pending']} |")
    lines.append("")
    lines.append("## Per-task detail")
    lines.append("")
    for aim, d in sorted(per_aim.items()):
        lines.append(f"### {aim}")
        lines.append("")
        lines.append("| Task | Title | Status | Evidence |")
        lines.append("|------|-------|--------|----------|")
        for t in d["tasks"]:
            icon = {"DONE":"✅","ACTIVE":"🟡","pending":"⚪"}[t["status"]]
            lines.append(f"| {t['task']} | {t['title']} | {icon} {t['status']} | {t['reason']} |")
        lines.append("")
    if flips:
        lines.append("## Flips this sync")
        for k,a,b in flips:
            lines.append(f"- **{k}**: {a} → {b}")
    STATUS.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(STATUS, ("\n".join(lines) + "\n").encode())

    # Cache for flip detection
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    atomic_write(CACHE, json.dumps(new_cache, indent=2).encode())

    # Also emit a /tmp copy for dashboard
    try: subprocess.run(["cp","-f", str(STATUS), "/tmp/phgdh_plan_status.md"], check=False)
    except: pass

    # Notify on any flip
    if flips:
        msg = "; ".join(f"{k} {a}→{b}" for k,a,b in flips)
        subprocess.run([
            "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh",
            "📋", "Plan status updated", msg[:500]
        ], check=False, timeout=8)

    print(json.dumps({
        "aim_totals": {a: {k:v for k,v in d.items() if k!="tasks"} for a,d in per_aim.items()},
        "flips": flips,
        "status_file": str(STATUS),
    }, indent=2))

if __name__ == "__main__":
    main()
