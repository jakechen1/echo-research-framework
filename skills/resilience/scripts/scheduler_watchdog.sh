#!/bin/bash
# Ensures scheduler_loop is running. Run from cron OR from any shell; idempotent.
PIDFILE=/tmp/phgdh_scheduler.pid
SCHED=/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts/scheduler_loop.sh
if [ -f $PIDFILE ] && kill -0 $(cat $PIDFILE) 2>/dev/null; then
  exit 0
fi
nohup $SCHED > /dev/null 2>&1 &
disown 2>/dev/null || true
echo "[$(date -u +%FT%TZ)] scheduler_watchdog spawned scheduler" >> /Users/jakeclaw/Library/Logs/scheduler_watchdog.log
