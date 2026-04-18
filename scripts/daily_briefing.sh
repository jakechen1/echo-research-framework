#!/bin/bash
# Fires once per day. Asks Gemma 4 (via Ollama direct) for a short self-report.
# Output saved to briefings/YYYY-MM-DD.md. GPU spike: one per day.
set -e
DATE=$(date +%Y-%m-%d)
DIR=/Users/jakeclaw/workers/briefings
mkdir -p "$DIR"
OUT="$DIR/$DATE.md"

PROMPT="You are jakeclaw on W0. Write a brief morning self-report (4-6 bullet points): what workers are currently running on W0, any heartbeat files older than 10 minutes, any gateway log errors in the last 24h, and one proactive suggestion for the user. Keep it under 200 words. Today is $DATE."

# Gather observable state first (no LLM needed for this part)
WORKERS=$(launchctl list 2>/dev/null | awk '/ai\.jakeclaw\./ {printf "%s (pid=%s)\n", $3, $1}' | head -20 || echo "none")
STALE=$(find /Users/jakeclaw/workers/heartbeats -type f -mmin +10 2>/dev/null | head -10 || echo "none")
ERRLOG=$(tail -200 /Users/jakeclaw/.openclaw/logs/gateway.err.log 2>/dev/null | grep -iE "error|fail" | tail -5 || echo "none")

CTX="Observable state collected at $(date):
Running LaunchAgents:
$WORKERS

Stale heartbeats (>10min):
$STALE

Recent gateway errors:
$ERRLOG
"

# Call Ollama direct on L0
RESPONSE=$(curl -s --max-time 300 -X POST http://10.0.0.1:11434/api/generate \
  -H 'Content-Type: application/json' \
  -d "$(jq -n --arg p "$PROMPT" --arg c "$CTX" '{model:"gemma4-agent", prompt:($p + "\n\n" + $c), stream:false, options:{num_predict:400}}')" \
  | jq -r '.response // "ERROR: no response"')

cat > "$OUT" << EOF
# Daily briefing — $DATE

## Observable state
\`\`\`
$CTX
\`\`\`

## jakeclaw's summary
$RESPONSE
EOF

echo "$(date): briefing written to $OUT"
date +%s > /Users/jakeclaw/workers/heartbeats/daily_briefing.ts
