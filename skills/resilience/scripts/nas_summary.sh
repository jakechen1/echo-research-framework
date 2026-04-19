#!/bin/bash
MOUNT=/Volumes/dataset-jakeclaw
OUT=/tmp/phgdh_nas_summary.json

if mount | grep -q "on $MOUNT "; then
  MOUNTED=true
  # Test if SSH session can actually read (TCC allows/blocks this)
  if ls "$MOUNT" >/dev/null 2>&1; then
    SSH_READABLE=true
    DF=$(df -k "$MOUNT" 2>/dev/null | tail -1)
    USED_KB=$(echo "$DF" | awk '{print $3}')
    AVAIL_KB=$(echo "$DF" | awk '{print $4}')
    # Look at known backup locations; try each
    BACKUP=""; for C in $MOUNT/phgdh-project $MOUNT/workspace/phgdh $MOUNT/backups/phgdh; do
      [ -d "$C" ] && { BACKUP="$C"; break; }
    done
    if [ -n "$BACKUP" ]; then
      FILES=$(find "$BACKUP" -type f 2>/dev/null | head -100000 | wc -l | tr -d ' ')
      LAST=$(find "$BACKUP" -type f -print0 2>/dev/null | xargs -0 -I{} stat -f "%m" {} 2>/dev/null | sort -nr | head -1)
      [ -n "$LAST" ] && LAST_ISO=$(date -r "$LAST" -u +%FT%TZ) || LAST_ISO=""
      BACKUP_KB=$(du -sk "$BACKUP" 2>/dev/null | awk '{print $1}')
    else
      FILES=0; LAST_ISO=""; BACKUP_KB=0
    fi
    STATUS="ok"
  else
    SSH_READABLE=false
    USED_KB=0; AVAIL_KB=0; FILES=0; LAST_ISO=""; BACKUP_KB=0; BACKUP=""
    STATUS="ssh_tcc_blocked"
  fi
else
  MOUNTED=false; SSH_READABLE=false
  USED_KB=0; AVAIL_KB=0; FILES=0; LAST_ISO=""; BACKUP_KB=0; BACKUP=""
  STATUS="not_mounted"
fi

LAST_JSON=$([ -n "$LAST_ISO" ] && echo "\"$LAST_ISO\"" || echo null)
BACKUP_JSON=$([ -n "$BACKUP" ] && echo "\"$BACKUP\"" || echo null)

cat > $OUT <<EOF
{
  "mounted": $MOUNTED,
  "ssh_readable": $SSH_READABLE,
  "status": "$STATUS",
  "mount_point": "$MOUNT",
  "backup_path": $BACKUP_JSON,
  "volume_used_gb": $(echo "scale=1; ${USED_KB:-0}/1048576" | bc),
  "volume_avail_gb": $(echo "scale=1; ${AVAIL_KB:-0}/1048576" | bc),
  "backup_size_mb": $(echo "scale=1; ${BACKUP_KB:-0}/1024" | bc),
  "backup_file_count": $FILES,
  "last_backup": $LAST_JSON,
  "note": "$(case "$STATUS" in
    ssh_tcc_blocked) echo 'SSH session cannot write to NAS mount (macOS TCC). Run nas_backup.sh from a Terminal.app window with Full Disk Access.' ;;
    not_mounted) echo 'NAS not mounted — check com.jakeclaw.nas-mount LaunchDaemon' ;;
    ok) echo 'NAS backup pipeline operational' ;;
  esac)",
  "generated_at": "$(date -u +%FT%TZ)"
}
EOF
chmod 644 $OUT
