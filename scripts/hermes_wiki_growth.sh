#!/bin/bash
# hermes_wiki_growth.sh — invoke Hermes wiki_builder.py for a seed topic.
# Exits quickly (wiki_builder backgrounds itself via its own PID file).
# Prints a one-line JSON summary of state after kickoff.
#
# Usage: hermes_wiki_growth.sh "seed topic string" [output-subdir] [depth] [pages-per-level]

set -euo pipefail
SEED="${1:-}"
OUT_SUB="${2:-phgdh-auto}"
DEPTH="${3:-2}"
PAGES="${4:-10}"

[ -z "$SEED" ] && { echo "usage: hermes_wiki_growth.sh \"seed topic\" [output-subdir] [depth] [pages]"; exit 1; }

HERMES_BIN=/Users/jakeclaw/.hermes-venv/bin/python
WIKI_BUILDER=/Users/jakeclaw/.hermes/scripts/wiki_builder.py
LOG=/Users/jakeclaw/workers/logs/hermes_wiki_growth.log
HB=/Users/jakeclaw/workers/heartbeats/hermes_wiki_growth.ts
mkdir -p "$(dirname "$LOG")" "$(dirname "$HB")"

date +%s > "$HB"
echo "[$(date '+%Y-%m-%dT%H:%M:%S%z')] start seed=\"$SEED\" depth=$DEPTH pages=$PAGES out=projects/$OUT_SUB" | tee -a "$LOG"

# First, stop any running wiki-builder to avoid conflicting runs
$HERMES_BIN $WIKI_BUILDER stop >/dev/null 2>&1 || true
sleep 1

# Fire the builder (it daemonizes itself)
cd /Users/jakeclaw
HOME=/Users/jakeclaw nohup $HERMES_BIN $WIKI_BUILDER start "$SEED" \
    --depth "$DEPTH" --pages-per-level "$PAGES" \
    --rebuild --strategy full \
    --output-dir "projects/$OUT_SUB" \
    >> /Users/jakeclaw/.hermes/logs/wiki-builder.log 2>&1 </dev/null &
disown

sleep 2

# Report state
if [ -f /Users/jakeclaw/.hermes/wiki-builder-state.json ]; then
    STATUS=$(/opt/homebrew/bin/jq -r ".status // \"unknown\"" /Users/jakeclaw/.hermes/wiki-builder-state.json 2>/dev/null || echo "unknown")
    GENERATED=$(/opt/homebrew/bin/jq -r ".total_generated // 0" /Users/jakeclaw/.hermes/wiki-builder-state.json 2>/dev/null || echo "0")
    CURRENT=$(/opt/homebrew/bin/jq -r ".current_page // \"-\"" /Users/jakeclaw/.hermes/wiki-builder-state.json 2>/dev/null || echo "-")
    echo "{\"status\":\"$STATUS\",\"total_generated\":$GENERATED,\"current_page\":\"$CURRENT\",\"seed\":\"$SEED\",\"out\":\"projects/$OUT_SUB\"}"
else
    echo "{\"status\":\"no_state\",\"seed\":\"$SEED\",\"out\":\"projects/$OUT_SUB\"}"
fi
