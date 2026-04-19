#!/bin/bash
OUT=/tmp/phgdh_box_status.json
PENDING=/tmp/phgdh_box_pending.json
LOG=/Users/jakeclaw/workers/logs/box_sync.log
mkdir -p /Users/jakeclaw/workers/logs

PCOUNT=0
[ -f $PENDING ] && PCOUNT=$(wc -l < $PENDING 2>/dev/null | tr -d '[:space:]')
[ -z "$PCOUNT" ] && PCOUNT=0

MB_LAST=$(tail -1 $LOG 2>/dev/null | grep -oE "20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]T[0-9:]+Z" | head -1)

HERMES_BOX=$(/Users/jakeclaw/.hermes-venv/bin/hermes mcp list 2>/dev/null | grep -c "box\b" | tr -d '[:space:]')
[ -z "$HERMES_BOX" ] && HERMES_BOX=0
RCLONE_OK=0
if command -v rclone >/dev/null 2>&1; then
  RCLONE_OK=$(rclone listremotes 2>/dev/null | grep -c "box" | tr -d '[:space:]')
  [ -z "$RCLONE_OK" ] && RCLONE_OK=0
fi

if [ "$HERMES_BOX" -gt 0 ] 2>/dev/null; then MODE=hermes
elif [ "$RCLONE_OK" -gt 0 ] 2>/dev/null; then MODE=rclone
else MODE=macbook-only
fi

MB_JSON=$([ -n "$MB_LAST" ] && echo "\"$MB_LAST\"" || echo null)
cat > $OUT <<EOF
{
  "pending_count": $PCOUNT,
  "macbook_last_seen": $MB_JSON,
  "w0_rclone_configured": $([ "$RCLONE_OK" -gt 0 ] 2>/dev/null && echo true || echo false),
  "hermes_mcp_configured": $([ "$HERMES_BOX" -gt 0 ] 2>/dev/null && echo true || echo false),
  "mode": "$MODE",
  "generated_at": "$(date -u +%FT%TZ)"
}
EOF
chmod 644 $OUT
