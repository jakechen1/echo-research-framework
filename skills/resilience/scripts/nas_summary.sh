#!/bin/bash
# Produce JSON for the dashboard NAS card, using the actual SMB mount
# (/Volumes/dataset-jakeclaw at //jakeclaw@192.168.68.128/jakeclaw).
MOUNT=/Volumes/dataset-jakeclaw
OUT=/tmp/phgdh_nas_summary.json
if mount | grep -q "on $MOUNT "; then
  MOUNTED=true
  # df-based size (fast)
  DF=$(df -k "$MOUNT" 2>/dev/null | tail -1)
  USED_KB=$(echo "$DF" | awk '{print $3}')
  AVAIL_KB=$(echo "$DF" | awk '{print $4}')
  # fast file count via find with timeout — limit to top-level subdirs we care about
  FILES=0; BYTES=$USED_KB
  LAST_BACKUP=$(find "$MOUNT/workspace" "$MOUNT/backups" -maxdepth 3 -type f -print0 2>/dev/null \
    | xargs -0 -I{} stat -f "%m" {} 2>/dev/null | sort -nr | head -1)
  FILES=$(find "$MOUNT/workspace" "$MOUNT/backups" -type f 2>/dev/null | head -50000 | wc -l | tr -d ' ')
  if [ -n "$LAST_BACKUP" ]; then
    LAST_ISO=$(date -r "$LAST_BACKUP" -u +%FT%TZ 2>/dev/null)
  else
    LAST_ISO=null
  fi
else
  MOUNTED=false; USED_KB=0; AVAIL_KB=0; FILES=0; LAST_ISO=null
fi
cat > $OUT <<EOF
{
  "mounted": $MOUNTED,
  "mount_point": "$MOUNT",
  "used_gb": $(echo "scale=1; ${USED_KB:-0}/1048576" | bc),
  "avail_gb": $(echo "scale=1; ${AVAIL_KB:-0}/1048576" | bc),
  "file_count": $FILES,
  "last_backup": $(if [ "$LAST_ISO" != "null" ]; then echo "\"$LAST_ISO\""; else echo null; fi),
  "generated_at": "$(date -u +%FT%TZ)"
}
EOF
chmod 644 $OUT
cat $OUT
