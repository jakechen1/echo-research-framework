#!/usr/bin/env python3
"""Learner — durable capture of user corrections."""
import argparse, json, re, subprocess
from pathlib import Path
from datetime import datetime, timezone
WS = Path("/Users/jakeclaw/.openclaw/workspace")
NOTES = WS/"project-state/learning_notes"
IDX = WS/"project-state/learning_index.jsonl"
NOW = datetime.now(timezone.utc).isoformat(timespec="seconds")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", required=True)
    ap.add_argument("--rule", required=True)
    ap.add_argument("--context", default="")
    args = ap.parse_args()
    NOTES.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+","-", args.rule.lower())[:60].strip("-")
    path = NOTES / f"{NOW[:10]}-{slug}.md"
    path.write_text(f"""---
category: {args.category}
recorded: {NOW}
---

# Learning: {args.rule}

## Context
{args.context}

## Enforcement
This rule should be checked during Assessor (A-stage) reviews and
enforced by relevant skill upgrades. Future iterations must not repeat
the pattern that triggered this correction.
""")
    with IDX.open("a") as f:
        f.write(json.dumps({"at": NOW, "category": args.category,
                            "rule": args.rule, "note_path": str(path)}) + "\n")
    subprocess.run([
        "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh",
        "📚", "Learner recorded rule", f"{args.rule} — see {path.name}"
    ], check=False, timeout=10)
    print(json.dumps({"path": str(path), "category": args.category, "rule": args.rule}))

if __name__ == "__main__":
    main()
