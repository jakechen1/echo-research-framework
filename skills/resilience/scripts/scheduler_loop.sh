#!/bin/bash
# Persistent scheduler loop — runs every 60s, dispatches tasks based on
# minute/hour of wall clock. Replaces cron since macOS SSH can't install it.
# Re-exec-resistant: writes PID to /tmp/phgdh_scheduler.pid and checks for
# duplicates on startup.
set -u
PIDFILE=/tmp/phgdh_scheduler.pid
if [ -f $PIDFILE ] && kill -0 $(cat $PIDFILE) 2>/dev/null; then
  echo "scheduler already running PID=$(cat $PIDFILE)" >&2
  exit 0
fi
echo $$ > $PIDFILE

WS=/Users/jakeclaw/.openclaw/workspace
LOG=/Users/jakeclaw/Library/Logs/phgdh_scheduler.log
PY=/Users/jakeclaw/.hermes-venv/bin/python
echo "[$(date -u +%FT%TZ)] scheduler started PID=$$" >> $LOG

last_min=-1
while :; do
  now=$(date +%s)
  min=$(( now / 60 % 60 ))
  hour=$(( now / 3600 % 24 ))

  # Every minute: utilization sampler
  $PY $WS/skills/age-scoring/scripts/utilization_sampler.py >> /Users/jakeclaw/Library/Logs/utilization_sampler.log 2>&1

  # Every 2 min: retry queue
  if (( now / 60 % 2 == 0 )); then
    $PY $WS/skills/resilience/scripts/retry_queue.py >> /Users/jakeclaw/Library/Logs/resilience_retry.log 2>&1
  fi

  # Every 5 min: liveness + resolver
  if (( now / 60 % 5 == 0 )); then
    $WS/skills/liveness-audit/scripts/liveness.sh --resolver >> /Users/jakeclaw/Library/Logs/liveness_audit.log 2>&1
    $PY $WS/skills/resilience/scripts/post_r_watchdog.py >> /Users/jakeclaw/Library/Logs/post_r_watchdog.log 2>&1
  fi

  # Every 30 min at :00 and :30: repo sync
  if (( now / 60 % 30 == 0 )); then
    /Users/jakeclaw/workers/bin/phgdh_repo_sync.sh >> /Users/jakeclaw/Library/Logs/phgdh_repo_sync.log 2>&1
  fi

  # Hourly at :15 → checkpoint
  if [ $min -eq 15 ] && [ $min -ne $last_min ]; then
    $WS/skills/resilience/scripts/checkpoint.sh >> /Users/jakeclaw/Library/Logs/resilience_checkpoint.log 2>&1
  fi

  # Daily at 03:00 → age baseline refresh
  if [ $hour -eq 3 ] && [ $min -eq 0 ] && [ $min -ne $last_min ]; then
    $WS/skills/age-scoring/scripts/baseline_refresh.sh >> /Users/jakeclaw/Library/Logs/age_baseline.log 2>&1
  fi


  # Hourly at :45 → plan-sync (BACKLOG reconciliation)
  if [ $min -eq 45 ] && [ $min -ne $last_min ]; then
    $PY $WS/skills/plan-sync/scripts/plan_sync.py >> /Users/jakeclaw/Library/Logs/plan_sync.log 2>&1
  fi


  # Every 15 min: workload optimizer (resourceful E/A balancing)
  if (( now / 60 % 15 == 0 )); then
    $PY $WS/skills/workload-optimizer/scripts/optimizer.py >> /Users/jakeclaw/Library/Logs/optimizer.log 2>&1
  fi


  # NAS backup every 30 min + summary
  if (( now / 60 % 30 == 0 )); then
    /Users/jakeclaw/workers/bin/nas_backup.sh >> /Users/jakeclaw/Library/Logs/nas_backup.log 2>&1
    $WS/skills/resilience/scripts/nas_summary.sh >> /dev/null 2>&1
  fi
  # Box status every 5 min
  if (( now / 60 % 5 == 0 )); then
    $WS/skills/box-sync/scripts/box_status.sh >> /dev/null 2>&1
  fi

  last_min=$min
  sleep 60
done
