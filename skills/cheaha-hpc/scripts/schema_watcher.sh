#!/bin/bash
# Periodic: every schema file's declared columns match the current CSV header.
# Flags drift early before it bites a Cheaha array job.
WS=/Users/jakeclaw/.openclaw/workspace
ERRORS=()
for sch in $(find $WS/data -name "*.schema.json"); do
  /Users/jakeclaw/.hermes-venv/bin/python - "$sch" <<'PY' || ERRORS+=("$sch")
import sys, json
from pathlib import Path
s = json.loads(Path(sys.argv[1]).read_text())
# Find the CSV beside the schema
csv = None
for p in Path(sys.argv[1]).parent.glob(s["filename_glob"]):
    csv = p; break
if not csv:
    print(f"CSV not found: {s['filename_glob']}"); sys.exit(1)
delim = s.get("delimiter", ",")
actual_header = csv.read_text().splitlines()[0].split(delim)
expected_header = [c["name"] for c in s["columns"]]
if actual_header != expected_header:
    print(f"DRIFT {csv.name}: expected {expected_header} got {actual_header}")
    sys.exit(1)
print(f"OK {csv.name}")
PY
done
if [ ${#ERRORS[@]} -gt 0 ]; then
  $WS/skills/notifier/scripts/notify.sh "🔍" "Schema drift detected" \
    "Files with header mismatch: ${ERRORS[*]}" --urgent
fi
