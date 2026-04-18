#!/bin/bash
set -euo pipefail
WS=/Users/jakeclaw/.openclaw/workspace
WORKERS=/Users/jakeclaw/workers
PROJ=/Users/jakeclaw/phgdh-scavenger
LOG=/Users/jakeclaw/workers/logs/phgdh_repo_sync.log
HB=/Users/jakeclaw/workers/heartbeats/phgdh_repo_sync.ts
mkdir -p "$(dirname "$LOG")" "$(dirname "$HB")"
log() { echo "[$(date +%Y-%m-%dT%H:%M:%S%z)] $*" | tee -a "$LOG" >&2; }
date +%s > "$HB"
cd "$PROJ" || { log "FATAL: $PROJ missing"; exit 1; }
rsync -a --delete "$WS/project-state/" project-state/
# Sync all shell/python scripts and markdown docs from workers/bin
rsync -a --include="*.sh" --include="*.py" --include="*.md" --exclude="*" "$WORKERS/bin/" scripts/
for d in PROJECT_PLAN.md RESOLUTION_LOG.md TASKS.md PERSISTENCE.md CLAUDE.md PHGDH_BRIEF.md DESIGN_NOTES.md COMMUNICATION_LEVELS.md PROJECT_TAXONOMY.md; do
  [ -f "$WS/$d" ] && cp "$WS/$d" "$d" 2>/dev/null || true
done
[ -d "$WS/skills/cheaha-hpc" ] && rsync -a --delete "$WS/skills/cheaha-hpc/" cheaha-hpc-skill/
[ -d "$WS/skills/task-router" ] && rsync -a --delete "$WS/skills/task-router/" task-router-skill/
if [ -z "$(git status --porcelain)" ]; then
  log "no changes"; exit 0
fi
git add .
CHANGED=$(git diff --cached --name-only | head -5 | paste -sd "," -)
git commit -q -m "auto-sync $(date +%Y-%m-%dT%H:%M) — $CHANGED"
log "committed: $CHANGED"
if git push origin main 2>>"$LOG"; then
  log "pushed"
else
  log "ERROR push"; exit 2
fi
