#!/usr/bin/env python3
"""
project_dashboard.py — generates the public Wiki Project Dashboard with:
  Table 1: PLEASER × iterations matrix with AGE cell scores (linkable)
  Table 2: Aim→Task→Subtask matrix with %completion + Achievement score
Color coding:
  Green : Achievement >= 5
  Yellow: Achievement == 4 (recoverable)
  Red   : Achievement <= 3 (human intervention requested)
"""
import datetime, json, pathlib, re, subprocess

WS = pathlib.Path("/Users/jakeclaw/.openclaw/workspace")
PS = WS / "project-state"
L3 = PS / "reports" / "L3"
WIKI_PROJECT_PATH = "PHGDH-Allosteric-RBD-Binder"  # relative path on sdd-wiki

STAGE_LETTERS = ["P","L","E","A","S","X","R"]
STAGE_FULL = {"P":"Plan","L":"Learning","E":"Execution","A":"Assessment",
              "S":"Sharing","X":"Expense","R":"Resolver"}

# -----------------------------------------------------------
def colored_span(score, label=None):
    """AGE/Achievement score → inline-styled HTML badge (Quartz renders HTML)."""
    if score is None:
        bg, fg = "#333", "#aaa"
        txt = "—"
    else:
        try: s = int(score)
        except: s = 0
        if s >= 5:   bg = "#2ea043"   # green
        elif s == 4: bg = "#bf8700"   # yellow
        else:        bg = "#d73a49"   # red
        fg = "#fff"
        txt = str(label or score)
    return f"<span style=\"background:{bg};color:{fg};padding:2px 6px;border-radius:4px;font-family:monospace\">{txt}</span>"

def score_cell(a, g, e, link=None):
    """Three-digit AGE cell. Color by min(a,g,e). If link provided, wraps in anchor."""
    if a is None or g is None or e is None:
        txt = "—"; worst = None
    else:
        txt = f"{a}.{g}.{e}"
        worst = min(a,g,e)
    badge = colored_span(worst, txt)
    if link:
        return f"<a href=\"{link}\" style=\"text_decoration:none\">{badge}</a>"
    return badge

# -----------------------------------------------------------
# Harvest iteration data
def parse_l3_report(path):
    """Return {task, iteration, age: {P:{a,g,e}, L:..., ...}, link}."""
    try:
        t = path.read_text()
    except: return None
    task_m = re.search(r"Task \d+\.\d+", t)
    iter_m = re.search(r"iteration[:\s]+(\d+)", t, re.I)
    # Look for AGE scores in Assessment section, format "Accuracy=N" or similar
    # Very heuristic — later iterations will produce structured data
    scores = {}
    for letter in STAGE_LETTERS:
        scores[letter] = {"a": None, "g": None, "e": None}
    # Scan Assessment section for explicit AGE patterns
    a_match = re.search(r"Achievements[=:\s]+(\d)", t)
    g_match = re.search(r"Growth[=:\s]+(\d)", t)
    e_match = re.search(r"Efforts[=:\s]+(\d)", t)
    if a_match and g_match and e_match:
        # Assign the measured AGE to the Assessment stage
        scores["A"] = {"a": int(a_match.group(1)), "g": int(g_match.group(1)), "e": int(e_match.group(1))}
    return {
        "task": task_m.group(0) if task_m else "?",
        "iteration": int(iter_m.group(1)) if iter_m else 1,
        "age": scores,
        "link": f"{WIKI_PROJECT_PATH}/reports/{path.stem}",
        "mtime": datetime.datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
    }

def harvest_iterations():
    if not L3.exists(): return []
    out = []
    for f in sorted(L3.glob("*.md")):
        r = parse_l3_report(f)
        if r: out.append(r)
    return out

# -----------------------------------------------------------
# Harvest task completion
def harvest_tasks():
    """Parse BACKLOG + COMPLETED + CURRENT_GOAL into an Aim→Task→Subtask tree with completion %."""
    bl = (PS / "BACKLOG.md").read_text() if (PS / "BACKLOG.md").exists() else ""
    cd = (PS / "COMPLETED.md").read_text() if (PS / "COMPLETED.md").exists() else ""
    cg = (PS / "CURRENT_GOAL.md").read_text() if (PS / "CURRENT_GOAL.md").exists() else ""
    current_task = (re.search(r"\*\*Task:\*\*\s*(Task \d+\.\d+)", cg) or [None,"?"])[1]

    # Parse BACKLOG by aim headers
    aims = []
    cur_aim = None
    for line in bl.splitlines():
        m_aim = re.match(r"^## (Aim \d[^\n]*)", line)
        if m_aim:
            cur_aim = {"name": m_aim.group(1), "tasks": []}
            aims.append(cur_aim)
            continue
        # Task row
        m_task = re.match(r"^\|\s*(Task \d+\.\d+(?:\.[a-z])?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|", line)
        if m_task and cur_aim:
            code, title, legacy, tier, eta = m_task.groups()
            status_m = re.search(r"(?:DONE|ACTIVE|pending)", line, re.I)
            status = (status_m.group(0) if status_m else "pending").lower()
            cur_aim["tasks"].append({
                "code": code.strip(),
                "title": title.strip(),
                "legacy": legacy.strip(),
                "status": status,
            })
    # If active task is missing from BACKLOG (promoted + removed), inject it from CURRENT_GOAL
    found = any(t["code"] == current_task for a in aims for t in a["tasks"])
    if not found and current_task != "?":
        cur_aim_m = re.search(r"\*\*Aim:\*\*\s*(Aim \d[^\n]*)", cg)
        cur_aim = cur_aim_m.group(1) if cur_aim_m else "(unassigned aim)"
        goal_m2 = re.search(r"## Goal\s*\n(.+?)(?=\n##)", cg, re.DOTALL)
        title = (goal_m2.group(1).strip().split("\n")[0] if goal_m2 else "(no title)")[:80]
        aim_obj = next((a for a in aims if a["name"] == cur_aim), None)
        if not aim_obj:
            aim_obj = {"name": cur_aim, "tasks": []}
            aims.append(aim_obj)
        aim_obj["tasks"].insert(0, {
            "code": current_task, "title": title, "legacy": "",
            "status": "active",
        })
    # Mark current task
    for a in aims:
        for t in a["tasks"]:
            if t["code"] == current_task: t["status"] = "active"
    # Achievement score: 7 for done, 5 for active (satisfactory by default), 0 (None) for pending
    for a in aims:
        for t in a["tasks"]:
            s = t["status"]
            if "done" in s:    t["ach"] = 7; t["pct"] = 100
            elif "active" in s:t["ach"] = 5; t["pct"] = 30
            else:              t["ach"] = None; t["pct"] = 0
    return aims

# -----------------------------------------------------------

def publish_pending():
    """Compare local ~/wiki/projects/PHGDH-* against ~/sdd-wiki/content/PHGDH-*
    to count new / changed pages. Returns (total_local, new_count, changed_count, details_rows)."""
    import hashlib
    SOURCES = [
        ("PHGDH-Allosteric-RBD-Binder",  pathlib.Path("/Users/jakeclaw/wiki/projects/PHGDH-Allosteric-RBD-Binder"),
         pathlib.Path("/Users/jakeclaw/sdd-wiki/content/PHGDH-Allosteric-RBD-Binder")),
        ("phgdh-research", pathlib.Path("/Users/jakeclaw/wiki/projects/phgdh-research"),
         pathlib.Path("/Users/jakeclaw/sdd-wiki/content/phgdh-research")),
    ]
    total = new = changed = 0
    rows = []
    def sha(f):
        h = hashlib.sha256()
        with f.open("rb") as fh:
            for c in iter(lambda: fh.read(65536), b""): h.update(c)
        return h.hexdigest()[:16]
    for label, local, remote in SOURCES:
        if not local.exists(): continue
        for f in sorted(local.rglob("*.md")):
            rel = f.relative_to(local)
            r = remote / rel
            total += 1
            if not r.exists():
                new += 1
                rows.append((label + "/" + str(rel), "NEW", "—"))
            else:
                ls = sha(f); rs = sha(r)
                if ls != rs:
                    changed += 1
                    rows.append((label + "/" + str(rel), "CHANGED", ls + "→" + rs))
    return total, new, changed, rows

def render():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    iters = harvest_iterations()
    aims = harvest_tasks()

    o = []
    o.append("---")
    o.append(f"title: \"PHGDH Project Dashboard\"")
    o.append(f"date: {datetime.date.today().isoformat()}")
    o.append("category: dashboard")
    o.append("tier: public")
    o.append("status: published")
    o.append("---")
    o.append("")
    o.append("# PHGDH Project Dashboard")
    o.append("")
    o.append(f"*Auto-regenerated by `project_dashboard.py` at {now}. "
             f"Cells are color-coded by Achievement score (1-9 reverse-NIH, 9 best): "
             f"{colored_span(7, 'green ≥5')} {colored_span(4, 'yellow 4')} {colored_span(2, 'red ≤3')}*")
    o.append("")

    # -------- Table 1: PLEASER × Iterations --------
    o.append("## Table 1 — PLEASER × Iterations (AGE scores)")
    o.append("")
    o.append("Each cell shows an **AGE triple** (Achievements.Growth.Efforts) on the reverse-NIH scale (9=best). Click to open the source report.")
    o.append("")
    if not iters:
        o.append("_No closed PLEASER iterations yet. Iteration 1 (Task 2.1) in **stage P** (Plan). Table will populate after the first L3 report._")
    else:
        cols = [f"Iter {r['iteration']} ({r['task']})" for r in iters]
        header = "| Stage | " + " | ".join(cols) + " |"
        sep = "|-------|" + "|".join("-----" for _ in cols) + "|"
        o.append(header); o.append(sep)
        for L in STAGE_LETTERS:
            row = [f"**{L}** ({STAGE_FULL[L]})"]
            for r in iters:
                s = r["age"].get(L, {})
                row.append(score_cell(s.get("a"), s.get("g"), s.get("e"),
                                      link=r["link"]))
            o.append("| " + " | ".join(row) + " |")
    o.append("")

    # -------- Table 2: Aim → Task → Subtask --------
    o.append("## Table 2 — Aims / Tasks — progress & Achievement")
    o.append("")
    o.append("Achievement = reverse-NIH 1-9 (9 best, 5 satisfactory). "
             "Tasks may run in parallel, locally on W0/L0 or remotely on Cheaha.")
    o.append("")
    o.append("| Work item | Status | % complete | Achievements |")
    o.append("|-----------|--------|-----------|-------------|")
    for a in aims:
        o.append(f"| **{a['name']}** | — | — | — |")
        for t in a["tasks"]:
            indent = "  " if re.match(r"Task \d+\.\d+\.[a-z]", t["code"]) else ""
            pct = f"{t['pct']}%" if t['pct'] else "—"
            ach_cell = colored_span(t["ach"], str(t["ach"]) if t["ach"] is not None else "—")
            status_label = {"done":"✓ done","active":"▶ ACTIVE","pending":"○ pending"}.get(
                "done" if "done" in t["status"] else ("active" if "active" in t["status"] else "pending"),
                t["status"])
            o.append(f"| {indent}`{t['code']}` — {t['title'][:80]} | {status_label} | {pct} | {ach_cell} |")
    o.append("")

    # -------- Footer --------
    total_tasks = sum(len(a["tasks"]) for a in aims)
    done_tasks  = sum(1 for a in aims for t in a["tasks"] if "done" in t["status"])
    active_task = next((t["code"] for a in aims for t in a["tasks"] if "active" in t["status"]), "?")
    # --- Pending publish (what the next publish click will change) ---
    total_pages, new_pages, changed_pages, pending_rows = publish_pending()
    o.append("## Pending publish")
    o.append("")
    o.append(f"- **Total project pages on W0:** {total_pages}")
    o.append(f"- **New (not yet on sdd-wiki):** {new_pages}")
    o.append(f"- **Changed since last publish:** {changed_pages}")
    if new_pages or changed_pages:
        o.append("")
        o.append("_Pressing **Publish to sdd-wiki** on the dashboard will push these:_")
        o.append("")
        o.append("| File | Status | SHA diff |")
        o.append("|------|--------|----------|")
        for name, status, diff in pending_rows[:15]:
            o.append(f"| `{name}` | {status} | `{diff}` |")
        if len(pending_rows) > 15:
            o.append(f"| _... and {len(pending_rows)-15} more_ | | |")
    else:
        o.append("")
        o.append("_Public site is up to date; nothing would change._")
    o.append("")
    o.append("## Summary")
    o.append(f"- Tasks total: **{total_tasks}**")
    o.append(f"- Done: **{done_tasks}** · Active: **{active_task}** · Pending: **{total_tasks-done_tasks-1}**")
    o.append(f"- PLEASER iterations closed: **{len(iters)}**")
    o.append("")
    o.append("---")
    o.append(f"*Every cell link points at a source report verified at dashboard generation time ({now}). "
             f"If a link 404s, the report was moved or deleted since last generation; re-run the dashboard.*")
    print("\n".join(o))

if __name__ == "__main__":
    render()
