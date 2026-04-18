#!/bin/bash
set -u
WS=/Users/jakeclaw/.openclaw/workspace
BK=/Users/jakeclaw/backups/project-state
REPO=/Users/jakeclaw/phgdh-scavenger
TS=$(date +%Y%m%d-%H%M%S)
mkdir -p $BK

# Hourly tarball with mtimes preserved
TARFILE="$BK/project-state-${TS}.tar.gz"
tar -czf "$TARFILE" -C $WS project-state 2>/dev/null
[ -f "$TARFILE" ] && echo "checkpoint $TARFILE $(stat -f%z "$TARFILE") bytes"

# Retain last 168 (7 days hourly)
ls -1t $BK/project-state-*.tar.gz 2>/dev/null | tail -n +169 | xargs rm -f 2>/dev/null

# Also copy a latest-pointer for easy restore
cp -f "$TARFILE" $BK/latest.tar.gz 2>/dev/null

# And push a rolling snapshot of project-state to the repo (commit+push).
# If push fails (no network), it's queued by retry_queue via git log presence.
cd $REPO
# phgdh_repo_sync already handles this every 30 min; we call it to force a new
# commit so the checkpoint is versioned:
/Users/jakeclaw/workers/bin/phgdh_repo_sync.sh >/dev/null 2>&1 || \
  /Users/jakeclaw/.hermes-venv/bin/python $WS/skills/resilience/scripts/enqueue.py git_push "$REPO"
