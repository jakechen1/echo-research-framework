#!/bin/bash
# qwenclaw_morning.sh — ONE PLEASER-ONE cycle per day.
# Scheduled at 07:00 daily via LaunchDaemon ai.jakeclaw.qwenclaw_morning.
#
# Flow:
#   1. qwenclaw reads CURRENT_GOAL.md and outputs ONE command for jakeclaw.
#   2. jakeclaw executes it (embedded, no Telegram round-trip) and returns output.
#   3. qwenclaw evaluates result (DONE / PROGRESS / BLOCKED).
#   4. Append to DAILY_LOG.
#   5. Post one-line summary to Jake's Telegram.
#
# Safety:
# - Both agents invoked with --local (embedded, no Telegram chatter)
# - 180-s timeout each call; script aborts on hang
# - All outputs logged to /Users/jakeclaw/workers/logs/qwenclaw_morning.log

set -euo pipefail

DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M)
STATE=/Users/jakeclaw/.openclaw/workspace/project-state
LOG=/Users/jakeclaw/workers/logs/qwenclaw_morning.log
DAYLOG="$STATE/DAILY_LOG/$DATE.md"
HEARTBEAT=/Users/jakeclaw/workers/heartbeats/qwenclaw_morning.ts

OC=/opt/homebrew/opt/node@22/bin/node
CLI=/Users/jakeclaw/.npm-global/lib/node_modules/openclaw/dist/index.js

mkdir -p "$(dirname "$LOG")" "$(dirname "$HEARTBEAT")" "$(dirname "$DAYLOG")"
[ -f "$DAYLOG" ] || echo "# $DATE" > "$DAYLOG"

log() { echo "[$(date '+%Y-%m-%dT%H:%M:%S')] $*" | tee -a "$LOG" >&2; }
fail() { log "FATAL: $*"; exit 1; }

# Run an openclaw agent and extract the finalAssistantVisibleText.
# --json writes the run summary to STDERR, not stdout. We capture both and jq-parse.
oc_agent() {
  local agent="$1"; shift
  local prompt="$1"; shift
  local timeout_s="${1:-180}"
  # Capture stderr (where JSON goes under --json) into a temp file; stdout is mostly empty.
  local tmpf="/tmp/oc_$$_$(date +%s%N).log"
  "$OC" "$CLI" agent --agent "$agent" --local --timeout "$timeout_s" \
    -m "$prompt" --json >>"$LOG" 2>"$tmpf"
  local rc=$?
  # Extract last JSON object from the file (it's a single JSON per run)
  # Strip non-JSON prefix (node warnings) — start from first '{' on its own line
  local json
  json=$(awk '/^\{/{found=1} found' < "$tmpf" | /opt/homebrew/bin/jq -s 'last' 2>/dev/null)
  if [ -z "$json" ] || [ "$json" = "null" ]; then
    json=$(awk '/^\{/{found=1} found' < "$tmpf")
  fi
  rm -f "$tmpf"
  echo "$json"
  return $rc
}


date +%s > "$HEARTBEAT"
log "=== morning cycle start ==="

# KILL-01 pre-flight — abort if kill switch found in today'\''s log
if grep -q -iE "(STOP-CHROME-CLAUDE|KILL-SWITCH)" "$DAYLOG" 2>/dev/null; then
  log "KILL-01 triggered — abort cycle"
  exit 0
fi

# -------- Phase 1: qwenclaw plans --------
PLAN_JSON=$(oc_agent qwenclaw "Read /Users/jakeclaw/.openclaw/workspace/project-state/CURRENT_GOAL.md. Output ONLY one shell command jakeclaw should run to advance the goal. When writing to a file, use >> (append) never > (overwrite). No preamble. No explanation. Just the command, on one line. If CURRENT_GOAL already shows all done-criteria checked, output the single word: GOAL_DONE." 180) || fail "qwenclaw plan call failed"

PLAN=$(echo "$PLAN_JSON" | /opt/homebrew/bin/jq -r '.payloads[0].text // .finalAssistantVisibleText // .response // empty' 2>/dev/null || echo "")
[ -z "$PLAN" ] && fail "qwenclaw returned empty plan"
log "plan: $PLAN"

if [ "$PLAN" = "GOAL_DONE" ]; then
  # Append to DAILY_LOG; flag for human promotion
  cat >> "$DAYLOG" << EOF

## $TIME — Morning cycle: CURRENT_GOAL complete
- qwenclaw reports all done-criteria satisfied.
- **Action needed**: jakechen to promote next goal from BACKLOG.md
  or invoke qwenclaw with "promote next goal" to do it manually.
EOF
  MSG="Morning cycle $DATE: CURRENT_GOAL reports done. Awaiting promotion from BACKLOG."
else
  # -------- Phase 2: jakeclaw executes --------
  EXEC_JSON=$(oc_agent main "Run this command and paste ONLY its raw stdout/stderr output. No prose. No markdown fences. Just the output: $PLAN" 180) || fail "jakeclaw exec call failed"

  EXEC=$(echo "$EXEC_JSON" | /opt/homebrew/bin/jq -r '.payloads[0].text // .finalAssistantVisibleText // .response // empty' 2>/dev/null || echo "(no output)")
  log "exec output (trimmed): $(echo "$EXEC" | head -c 300)"

  # -------- Phase 3: qwenclaw evaluates --------
  EVAL_JSON=$(oc_agent qwenclaw "The CURRENT_GOAL is at /Users/jakeclaw/.openclaw/workspace/project-state/CURRENT_GOAL.md. Command executed: $PLAN Output received: $EXEC — Assess in EXACTLY this format: STATUS: <DONE|PROGRESS|BLOCKED> | REASON: <one sentence> | NEXT: <next command or '-' if DONE>" 120) || fail "qwenclaw eval call failed"

  EVAL=$(echo "$EVAL_JSON" | /opt/homebrew/bin/jq -r '.payloads[0].text // .finalAssistantVisibleText // .response // empty' 2>/dev/null || echo "(no eval)")
  log "eval: $EVAL"

  # -------- Phase 4: log --------
  cat >> "$DAYLOG" << EOF

## $TIME — Morning cycle
**Plan:** \`$PLAN\`
**Output:**
\`\`\`
$(echo "$EXEC" | head -c 2000)
\`\`\`
**Evaluation:**
\`\`\`
$EVAL
\`\`\`
EOF

  MSG="Morning cycle $DATE: $(echo "$EVAL" | head -c 300)"
fi

# -------- Phase 5: notify Jake on Telegram --------
CHAT_ID=8156711151
BOT_TOKEN=$(/usr/bin/python3 -c 'import json; d=json.load(open("/Users/jakeclaw/.openclaw/openclaw.json")); print(d["channels"]["telegram"]["botToken"])' 2>/dev/null || echo "")
if [ -n "$BOT_TOKEN" ]; then
  /usr/bin/curl -s --max-time 10 -X POST "https://api.telegram.org/bot$BOT_TOKEN/sendMessage" \
    --data-urlencode "chat_id=$CHAT_ID" \
    --data-urlencode "text=$MSG" \
    >/dev/null && log "telegram sent" || log "telegram send FAILED"
else
  log "no bot token found — skipping telegram"
fi

log "=== morning cycle end ==="
exit 0
