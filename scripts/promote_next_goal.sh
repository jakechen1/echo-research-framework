#!/bin/bash
# promote_next_goal.sh - atomic goal rotation:
#   1. take CURRENT_GOAL content, append to COMPLETED.md with date
#   2. read first G-NNN row from BACKLOG.md that isnt in COMPLETED
#   3. rewrite CURRENT_GOAL.md from that backlog row
#   4. remove that row from BACKLOG.md
#
# Emits the new goal id + one-line goal text on stdout.
set -euo pipefail

PS=/Users/jakeclaw/.openclaw/workspace/project-state
LOG=/Users/jakeclaw/workers/logs/promote_next_goal.log
mkdir -p "$(dirname "$LOG")"

log() { echo "[$(date +%Y-%m-%dT%H:%M:%S%z)] $*" >> "$LOG"; }
log "=== promote_next_goal start ==="

/usr/bin/python3 << "PY"
import re, datetime, sys, pathlib

PS = pathlib.Path("/Users/jakeclaw/.openclaw/workspace/project-state")
today = datetime.date.today().isoformat()

cur_path = PS / "CURRENT_GOAL.md"
bl_path = PS / "BACKLOG.md"
done_path = PS / "COMPLETED.md"

cur = cur_path.read_text()
bl = bl_path.read_text()
done = done_path.read_text()

# 1. Extract current goals id + title line
m = re.search(r"\*\*ID:\*\*\s*(G-\d+)", cur)
cur_id = m.group(1) if m else "G-???"
goal_block = re.search(r"## Goal\s*\n(.+?)(?=\n##|\Z)", cur, re.DOTALL)
cur_summary = (goal_block.group(1).strip().split("\n")[0] if goal_block else "(no summary)")

# 2. Append to COMPLETED (skip if already there)
if f"## {cur_id} —" not in done:
    done_entry = f"\n## {cur_id} — {cur_summary[:120]}\n" \
                 f"- **Done:** {today}\n" \
                 f"- **Promoted-via:** promote_next_goal.sh\n" \
                 f"- **Notes:** auto-promoted after done-criteria satisfied\n"
    # Append before the "*(empty" placeholder if present, else append at end
    if "*(empty" in done:
        done = done.replace("*(empty — first sub-goal G-001 in progress)*", done_entry)
    else:
        done = done.rstrip() + "\n" + done_entry
    done_path.write_text(done)
    print(f"completed: {cur_id}")

# 3. Read first eligible backlog row
# Backlog format: | G-NNN | description | tier | ETA |
backlog_rows = re.findall(r"^\|\s*(G-\d+)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|$", bl, re.MULTILINE)
completed_ids = set(re.findall(r"^## (G-\d+)", done, re.MULTILINE))
completed_ids.add(cur_id)  # just-completed
next_row = None
for row in backlog_rows:
    if row[0] not in completed_ids:
        next_row = row; break

if not next_row:
    print("ERROR: no eligible backlog goal", file=sys.stderr); sys.exit(2)

new_id, new_desc, new_tier, new_eta = next_row
print(f"promoted: {new_id}")
print(f"new-goal: {new_desc[:160]}")

# 4. Write new CURRENT_GOAL.md
owner = "jakeclaw (executor) / qwenclaw (PM) / jakechen (human)"
new_current = f"""# Current Sub-Goal

**ID:** {new_id}
**Started:** {today}
**Owner:** {owner}
**Deadline:** within {new_eta}
**Status:** open
**Tier:** {new_tier}

## Goal
{new_desc}

## Definition of done
- [ ] goal primary output produced
- [ ] output committed to phgdh-scavenger repo (if code/data)
- [ ] DAILY_LOG entry written referencing artifact(s)
- [ ] (refine above criteria with qwenclaw or jakechen if ambiguous)

## Commands jakeclaw may run
(depends on the goal — qwenclaw will plan the first command at next 07:00 cycle)

## Notes
Auto-promoted from BACKLOG row by promote_next_goal.sh on {today}.
Original backlog entry: `| {new_id} | {new_desc} | {new_tier} | {new_eta} |`
"""
cur_path.write_text(new_current)

# 5. Remove that row from BACKLOG
bl_new = re.sub(
    rf"^\|\s*{re.escape(new_id)}\s*\|.+?\|\s*{re.escape(new_eta)}\s*\|\n",
    "",
    bl,
    count=1,
    flags=re.MULTILINE
)
bl_path.write_text(bl_new)
print(f"removed {new_id} from BACKLOG")
PY
log "=== promote_next_goal done ==="
