#!/usr/bin/env python3
"""
Generate L1..L6 project reports with delta-from-previous logic.
Usage:  report_builder.py --level N [--trigger STR] [--telegram] [--wiki] [--box]
"""
import argparse, datetime, json, os, pathlib, re, subprocess, sys, urllib.request

PS = pathlib.Path("/Users/jakeclaw/.openclaw/workspace/project-state")
DATA = pathlib.Path("/Users/jakeclaw/workers/data/phgdh")
WIKI = pathlib.Path("/Users/jakeclaw/wiki")
REPORTS = PS / "reports"
OLLAMA = "http://10.0.0.1:11434/api/chat"

LEVELS = {
    1: {"dir": "L1", "name_fmt": "%Y-%m-%d-%H-%M",   "tokens": 800,   "channel": "telegram"},
    2: {"dir": "L2", "name_fmt": "%Y-%m-%d",         "tokens": 3000,   "channel": "telegram"},
    3: {"dir": "L3", "name_fmt": "G{gid}-%Y-%m-%d",  "tokens": 7000,  "channel": "wiki"},
    4: {"dir": "L4", "name_fmt": "poster-%Y-%m-%d",  "tokens": 7000,  "channel": "wiki"},
    5: {"dir": "L5", "name_fmt": "paper-%Y-%m-%d",   "tokens": 12000,  "channel": "box"},
    6: {"dir": "L6", "name_fmt": "debug-%Y-%m-%d-%H%M","tokens": 4000,"channel": "github"},
}

TEMPLATES = {
    1: """Write a ONE-SENTENCE project status update in plain text. MUST include:
the single-phrase thesis, the current G-NNN goal, and one concrete delta
vs the prior L1 report. No bullets, no emoji, under 200 characters.""",
    2: """Write a ONE-PAGE daily digest. Plain text, no emoji. Include:
- Up to 4 active aims (one line each) with progress today
- Current Task code (e.g., Task 2.1) + one-line goal text + iteration number
- AGE daily scores — three integers 1-9 (REVERSE NIH scale, 9 is best):
    Accuracy=N / Generalizability=N / Efficiency=N
  with one-line justification each. 5 is satisfactory (50th percentile).
  6,7,8,9 are top 33%, 20%, 10%, 5%. 4,3,2,1 are bottom 33%, 20%, 10%, 5%.
- 2-3 line delta vs yesterdays L2 (what moved)
- Blockers (or "none")
- Next 24 hours: one sentence""",
    3: """Write a PLEASER iteration report for the just-closed Task X.Y.
Use EXACTLY these seven section headers:
## 1. Plan
## 2. Learning
## 3. Execution
## 4. Assessment
## 5. Sharing
## 6. Expense
## 7. Resolver

Assessment section: NIH 1-9 scores (Significance, Innovation, Approach)
+ AGE 1-9 scores (Accuracy, Generalizability, Efficiency), each with a
one-line reason.

Expense section: a small markdown table with rows for wall-clock hours,
L0 GPU-hours, Cheaha SU, Claude API $, Telegram msgs — Planned vs Actual
vs Note. Flag overruns AND under-runs. Artifact references (commit SHAs,
files, hashes) live in Execution, not Expense.

Cite the Aim + Task code (e.g., "Aim 2 / Task 2.1"), the current
iteration number, and the PLEASER stage at the top of the report. For
any artifact referenced (file, wiki page, commit, Box doc), include
its actual audited timestamp, size, and hash/SHA from audit_artifact —
never fabricate. If an artifact is missing, write "NOT FOUND at audit
time (task T.X pending)" rather than inventing content.
Delta-vs-prior-L3 goes at the end of the Plan section.""",
    4: """Write a POSTER report combining 3-6 related Tasks into one results
narrative. Title, authors, 1-para background tied to one or more Aims,
1-para methods (tasks referenced by code), numbered results (each with
a figure/table reference + the Task X.Y that produced it), brief
interpretation, future directions, Delta-from-prior-L4.""",
    5: """Write a PAPER draft section update. Include: Abstract, Introduction,
Methods (reproducible enough for a stranger), Results (with quantitative
claims), Discussion (linking results), References (as `[[WikiPage]]` or
DOI stubs), Delta-from-prior-L5.""",
    6: """Compile a DEBUG report: system state (uptimes, daemons, daemon exits),
recent errors from worker logs, resource high-water marks, last 10
commits on phgdh-scavenger, open incidents. No LLM storytelling — just
structured facts.""",
}

def sh(cmd, to=10):
    try:
        return subprocess.check_output(cmd, shell=True, timeout=to, text=True).strip()
    except Exception:
        return ""


def audit_artifact(path_or_url):
    """Return {exists, mtime, size, sha256 or commit, note}. Never fabricate."""
    import hashlib, os, pathlib as _p
    info = {"ref": str(path_or_url), "exists": False}
    if path_or_url.startswith("http"):
        info["note"] = "URL — audit via HEAD skipped (would require network round-trip per call)"
        return info
    pth = _p.Path(path_or_url)
    if not pth.exists():
        info["note"] = "NOT FOUND at audit time"
        return info
    st = pth.stat()
    info["exists"] = True
    info["size"] = st.st_size
    info["mtime"] = datetime.datetime.fromtimestamp(st.st_mtime).isoformat(timespec="seconds")
    if pth.is_file() and st.st_size < 50_000_000:
        h = hashlib.sha256()
        with pth.open("rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        info["sha256"] = h.hexdigest()[:16]
    return info

def gather_state():
    # iteration state (may not exist on very early runs)
    try:
        iter_state = json.loads((PS / "iteration_state.json").read_text())
    except Exception:
        iter_state = {"task": "unknown", "iteration": 0, "stage": "?"}
    today = datetime.date.today().isoformat()
    cg = (PS / "CURRENT_GOAL.md").read_text() if (PS / "CURRENT_GOAL.md").exists() else ""
    bl = (PS / "BACKLOG.md").read_text() if (PS / "BACKLOG.md").exists() else ""
    cd = (PS / "COMPLETED.md").read_text() if (PS / "COMPLETED.md").exists() else ""
    dl_path = PS / "DAILY_LOG" / f"{today}.md"
    dl = dl_path.read_text() if dl_path.exists() else "(no daily log yet)"
    gid_m = re.search(r"G-\d+", cg)
    scav_files = sorted(DATA.glob("*.jsonl"))
    latest_scav = scav_files[-1] if scav_files else None
    scav_rows = int(sh(f"/usr/bin/wc -l < {latest_scav}")) if latest_scav else 0
    wiki_count = int(sh("/usr/bin/find /Users/jakeclaw/wiki -name '*.md' -type f 2>/dev/null | /usr/bin/wc -l") or 0)
    phgdh_wiki = int(sh("/usr/bin/find /Users/jakeclaw/wiki -name '*phgdh*.md' -type f 2>/dev/null | /usr/bin/wc -l") or 0)
    daemons = sh("/usr/bin/sudo -n /bin/launchctl list 2>/dev/null | /usr/bin/grep -cE 'ai.jakeclaw|com.jakeclaw'")
    return {
        "date": today,
        "iter_task": iter_state.get("task", "unknown"),
        "iter_num": iter_state.get("iteration", 0),
        "iter_stage": iter_state.get("stage", "?"),
        "thesis": "Identify allosteric / RBD-site PHGDH modulators for neurodegenerative disease.",
        "current_goal_id": gid_m.group(0) if gid_m else "?",
        "current_goal_md": cg[:1500],
        "backlog_top5": "\n".join(re.findall(r"^\| G-\d+ \|.+$", bl, re.M)[:5]),
        "completed_count": len(re.findall(r"^## G-\d+", cd, re.M)),
        "daily_log_today": dl[:2500],
        "scavenger_rows": scav_rows,
        "scavenger_file": latest_scav.name if latest_scav else "none",
        "scavenger_days": len(scav_files),
        "wiki_phgdh": phgdh_wiki,
        "wiki_total": wiki_count,
        "daemons_up": daemons,
    }

def prior_report(level):
    d = REPORTS / LEVELS[level]["dir"]
    if not d.exists(): return ""
    files = sorted(d.glob("*.md"))
    if not files: return ""
    return files[-1].read_text()[:2500]

def call_llm(prompt, max_tokens):
    # Native Ollama /api/chat; think:false disables reasoning-mode.
    req = json.dumps({
        "model": "gemma4-agent",
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "think": False,
        "options": {"num_predict": max_tokens, "temperature": 0.4},
    }).encode()
    try:
        r = urllib.request.Request(OLLAMA, data=req, headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(r, timeout=600) as resp:
            raw = resp.read().decode(errors="replace")
        # Parse: either a single JSON or newline-delimited JSONs; take the last with a message.
        try:
            d = json.loads(raw)
        except json.JSONDecodeError:
            d = None
            for line in raw.splitlines():
                line = line.strip()
                if not line: continue
                try:
                    obj = json.loads(line)
                    if obj.get("message") or obj.get("done"):
                        d = obj
                except json.JSONDecodeError:
                    pass
            if d is None:
                return f"(LLM parse failed: {raw[:200]})"
        msg = d.get("message", {}) if isinstance(d, dict) else {}
        return (msg.get("content") or "").strip()
    except Exception as e:
        return f"(LLM failed: {e})"

def send_telegram(text):
    try:
        cfg = json.load(open("/Users/jakeclaw/.openclaw/openclaw.json"))
        tok = cfg["channels"]["telegram"]["botToken"]
        body = json.dumps({"chat_id": 8156711151, "text": text[:3900]}).encode()
        urllib.request.urlopen(urllib.request.Request(
            f"https://api.telegram.org/bot{tok}/sendMessage",
            data=body,
            headers={"Content-Type": "application/json"}
        ), timeout=10).read()
        return True
    except Exception as e:
        print(f"telegram failed: {e}", file=sys.stderr)
        return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--level", type=int, required=True, choices=[1,2,3,4,5,6])
    ap.add_argument("--trigger", default="scheduled")
    ap.add_argument("--telegram", action="store_true")
    args = ap.parse_args()

    level = args.level
    cfg = LEVELS[level]
    state = gather_state()
    prior = prior_report(level) or "(no prior L{} report — this is the baseline)".format(level)

    prompt = f"""You are jakeclaw (Gemma 4), reporting for the PHGDH project.
Write an L{level} report per this template:

{TEMPLATES[level]}

## Project state (as of {state['date']}):
- Thesis: {state['thesis']}
- Current goal: {state['current_goal_id']}
- Scavenger: {state['scavenger_rows']} rows in {state['scavenger_file']} ({state['scavenger_days']} daily file(s))
- Wiki: {state['wiki_phgdh']} PHGDH pages / {state['wiki_total']} total
- Iteration: {state['iter_task']} #{state['iter_num']} — current PLEASER stage: {state['iter_stage']}
- Goals completed so far: {state['completed_count']}
- LaunchDaemons up: {state['daemons_up']}

## Today's daily log:
{state['daily_log_today']}

## Current goal detail:
{state['current_goal_md']}

## Prior L{level} report (for DELTA comparison):
{prior}

Trigger: {args.trigger}
Write only the report body, no preamble, no meta-commentary about writing it.
"""

    body = call_llm(prompt, cfg["tokens"])
    now = datetime.datetime.now()
    fname_base = cfg["name_fmt"].replace("{gid}", state["current_goal_id"])
    fname = now.strftime(fname_base) + ".md"
    outdir = REPORTS / cfg["dir"]
    outdir.mkdir(parents=True, exist_ok=True)
    out_path = outdir / fname

    out_path.write_text(f"""---
level: L{level}
date: {now.isoformat(timespec='seconds')}
trigger: {args.trigger}
goal_id: {state['current_goal_id']}
channel: {cfg['channel']}
---

{body}
""")

    # Telegram for L1, L2, and on demand
    if args.telegram or cfg["channel"] == "telegram":
        tag = f"[L{level} {state['current_goal_id']} · {state['date']}]"
        send_telegram(f"{tag}\n\n{body[:3500]}")

    print(str(out_path))

if __name__ == "__main__":
    main()
