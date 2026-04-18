#!/bin/bash
PY=/Users/jakeclaw/.hermes-venv/bin/python
WS=/Users/jakeclaw/.openclaw/workspace
OUT=$($PY $WS/skills/liveness-audit/scripts/liveness.py)
echo "$OUT"
# Publish a world-readable copy for the dashboard (jakechen can't traverse /Users/jakeclaw)
cp -f $WS/project-state/liveness.json /tmp/phgdh_liveness.json 2>/dev/null
cp -f $WS/project-state/liveness_history.jsonl /tmp/phgdh_liveness_history.jsonl 2>/dev/null
chmod 644 /tmp/phgdh_liveness.json /tmp/phgdh_liveness_history.jsonl 2>/dev/null
if [[ "$1" == "--resolver" ]]; then
  RED=$(echo "$OUT" | $PY -c "import sys,json; d=json.load(sys.stdin); print(','.join(d.get('red_channels',[])))" 2>/dev/null)
  if [ -n "$RED" ]; then
    TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    echo "- [$TS] Liveness RED: $RED" >> $WS/project-state/ISSUES/OPEN.md
  fi
fi
