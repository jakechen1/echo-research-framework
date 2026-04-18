#!/bin/bash
# session_compactor.sh
# Auto-compact any openclaw session that crosses the overflow threshold.
# Runs as a scheduled LaunchDaemon every 30 min.
#
# Thresholds:  >80 messages OR >500 KB  (well under the ~300-msg overflow point)
#
# On violation:
#   1. stop gateway cleanly
#   2. for each violating .jsonl:
#        a. extract last 10 messages into a summary log
#        b. archive the file to _archived_<ts>/
#   3. restart gateway
#   4. log outcome

set -euo pipefail

MAX_LINES=80
MAX_BYTES=512000
SESSIONS_GLOB="/Users/jakeclaw/.openclaw/agents/*/sessions"
LOG=/Users/jakeclaw/workers/logs/session_compactor.log
SUMMARY_LOG=/Users/jakeclaw/.openclaw/workspace/memory/session-compactor-log.md
HEARTBEAT=/Users/jakeclaw/workers/heartbeats/session_compactor.ts
TS=$(date +%Y%m%d-%H%M%S)

mkdir -p "$(dirname "$LOG")" "$(dirname "$HEARTBEAT")" "$(dirname "$SUMMARY_LOG")"

log() { echo "[$(date +%Y-%m-%dT%H:%M:%S%z)] $*" | tee -a "$LOG"; }

date +%s > "$HEARTBEAT"

# Collect violators
VIOLATORS=()
for DIR in $SESSIONS_GLOB; do
  [ -d "$DIR" ] || continue
  for F in "$DIR"/*.jsonl; do
    [ -f "$F" ] || continue
    LINES=$(wc -l < "$F" 2>/dev/null | tr -d ' ')
    BYTES=$(stat -f %z "$F" 2>/dev/null || echo 0)
    if [ "$LINES" -gt "$MAX_LINES" ] || [ "$BYTES" -gt "$MAX_BYTES" ]; then
      VIOLATORS+=("$F:$LINES:$BYTES")
    fi
  done
done

if [ "${#VIOLATORS[@]}" -eq 0 ]; then
  log "ok — no sessions over threshold (max_lines=$MAX_LINES max_bytes=$MAX_BYTES)"
  exit 0
fi

log "WARN — ${#VIOLATORS[@]} session(s) over threshold; compacting"

# Stop gateway so we can safely move files
log "stopping openclaw gateway..."
sudo -n launchctl bootout system/com.openclaw.jakeclaw 2>/dev/null || true
# give it a moment to release file handles
sleep 2

# Process each violator
for entry in "${VIOLATORS[@]}"; do
  F="${entry%%:*}"
  rest="${entry#*:}"
  LINES="${rest%%:*}"
  BYTES="${rest#*:}"
  DIR=$(dirname "$F")
  ARCH="$DIR/_archived_$TS"
  mkdir -p "$ARCH"

  # Extract last 10 messages into summary log before archiving
  {
    echo ""
    echo "## Compacted $TS — $(basename "$F")"
    echo "- lines: $LINES"
    echo "- bytes: $BYTES"
    echo "- archive: $ARCH"
    echo ""
    echo "### Last 10 messages (trimmed)"
    tail -10 "$F" 2>/dev/null | python3 -c '
import sys, json
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    try:
        d = json.loads(line)
        role = d.get("role") or d.get("type") or "?"
        content = d.get("content") or d.get("text") or ""
        if isinstance(content, list):
            content = " ".join([str(c.get("text","")) for c in content if isinstance(c, dict)])
        content = str(content)[:400].replace("\n"," ")
        print(f"- **{role}**: {content}")
    except Exception:
        print(f"- (unparseable): {line[:200]}")
' 2>/dev/null || echo "- (summary extraction failed)"
    echo ""
    echo "---"
  } >> "$SUMMARY_LOG"

  # Archive the full file
  mv "$F" "$ARCH/"
  # Archive companion checkpoint files matching the session id prefix
  BASENAME=$(basename "$F" .jsonl)
  for COMP in "$DIR/${BASENAME}"*.jsonl; do
    [ -f "$COMP" ] && mv "$COMP" "$ARCH/"
  done

  log "archived $F ($LINES lines, $BYTES bytes) -> $ARCH"
done

# Restart gateway
log "restarting openclaw gateway..."
sudo -n launchctl bootstrap system /Library/LaunchDaemons/com.openclaw.jakeclaw.plist 2>&1 | tee -a "$LOG" || true
sleep 3

# Verify gateway is up
if pgrep -u jakeclaw -f "openclaw-gateway" >/dev/null; then
  log "gateway back up — compaction complete"
else
  log "ERROR — gateway did not come back; alert jakechen"
fi

exit 0
