#!/bin/bash
# phgdh_publish.sh — rsync PHGDH wiki from W0 to aimed-lab/sdd-wiki v4.
# Cloudflare Pages deploys on push; site lives at sdd-wiki-public.pages.dev.
#
# Emits a JSON one-liner to stdout on success / failure.

set -euo pipefail
REPO_DIR=/Users/jakeclaw/sdd-wiki
TOKEN_FILE=/Users/jakeclaw/.config/gh/hosts.yml
LOG=/Users/jakeclaw/workers/logs/phgdh_publish.log
HB=/Users/jakeclaw/workers/heartbeats/phgdh_publish.ts
WIKI=/Users/jakeclaw/wiki
mkdir -p "$(dirname "$LOG")" "$(dirname "$HB")"
date +%s > "$HB"

TOKEN=$(grep -oE "gho_[A-Za-z0-9]+" "$TOKEN_FILE" | head -1)
[ -z "$TOKEN" ] && { echo "{\"ok\":false,\"error\":\"no github token\"}"; exit 1; }

log() { echo "[$(date '+%Y-%m-%dT%H:%M:%S%z')] $*" >> "$LOG"; }
log "=== publish start ==="

# 1. Clone or refresh
if [ ! -d "$REPO_DIR/.git" ]; then
  log "first clone"
  /usr/bin/git clone -b v4 --depth 5 "https://jakechen1:${TOKEN}@github.com/aimed-lab/sdd-wiki.git" "$REPO_DIR" >>"$LOG" 2>&1
else
  log "pulling latest v4"
  cd "$REPO_DIR"
  /usr/bin/git fetch origin v4 >>"$LOG" 2>&1
  /usr/bin/git reset --hard origin/v4 >>"$LOG" 2>&1
fi
cd "$REPO_DIR"
/usr/bin/git config user.email "14241094+jakechen1@users.noreply.github.com"
/usr/bin/git config user.name "Jake Y. Chen (via W0)"

# 2. Sync PHGDH content
mkdir -p content/PHGDH-topics content/PHGDH-Allosteric-RBD-Binder content/phgdh-research

# Project: PHGDH-Allosteric-RBD-Binder — full mirror
if [ -d "$WIKI/projects/PHGDH-Allosteric-RBD-Binder" ]; then
  # PHGDH-Allosteric-RBD-Binder: NO --delete (human-curated files on sdd-wiki we never want to lose)
  /usr/bin/rsync -a --exclude=".git" \
    "$WIKI/projects/PHGDH-Allosteric-RBD-Binder/" content/PHGDH-Allosteric-RBD-Binder/ >>"$LOG" 2>&1
  log "synced PHGDH-Allosteric-RBD-Binder"

  # LIVE documents from workspace → mirrored into the project folder with LIVE- prefix
  # so they render on Quartz without clobbering human-curated Master-Blueprint etc.
  _copy_live() {
    local src_path="$1" dest_name="$2" title="$3" category="$4"
    [ -f "$src_path" ] || return 0
    # Prepend Quartz-compatible frontmatter, then the source content
    {
      echo "---"
      echo "title: \"$title\""
      echo "date: $(/bin/date +%Y-%m-%d)"
      echo "category: $category"
      echo "tier: live"
      echo "source: jakeclaw@W0:$src_path"
      echo "note: \"auto-synced from the autonomous system; do not edit here\""
      echo "---"
      echo ""
      /bin/cat "$src_path"
    } > "content/PHGDH-Allosteric-RBD-Binder/$dest_name"
  }
  _copy_live "/Users/jakeclaw/.openclaw/workspace/PROJECT_PLAN.md"      LIVE-PROJECT_PLAN.md      "LIVE: Project Plan"        plan
  _copy_live "/Users/jakeclaw/.openclaw/workspace/DESIGN_NOTES.md"      LIVE-DESIGN_NOTES.md      "LIVE: Design Notes"        plan
  _copy_live "/Users/jakeclaw/.openclaw/workspace/PHGDH_BRIEF.md"       LIVE-PHGDH_BRIEF.md       "LIVE: PHGDH Project Brief" reference
  _copy_live "/Users/jakeclaw/.openclaw/workspace/CLAUDE.md"            LIVE-CLAUDE.md            "LIVE: Agent Rules"         methodology
  _copy_live "/Users/jakeclaw/.openclaw/workspace/RESOLUTION_LOG.md"    LIVE-RESOLUTION_LOG.md    "LIVE: Resolution Log"      operations
  _copy_live "/Users/jakeclaw/.openclaw/workspace/project-state/CURRENT_GOAL.md"  LIVE-CURRENT_GOAL.md  "LIVE: Current Goal"  operations
  _copy_live "/Users/jakeclaw/.openclaw/workspace/project-state/BACKLOG.md"       LIVE-BACKLOG.md       "LIVE: Backlog"       operations
  log "live docs mirrored into PHGDH-Allosteric-RBD-Binder/"

fi

# Project: phgdh-research — full mirror
if [ -d "$WIKI/projects/phgdh-research" ]; then
  # phgdh-research: --delete OK (mostly Hermes-generated)
  /usr/bin/rsync -a --delete --exclude=".git" \
    "$WIKI/projects/phgdh-research/" content/phgdh-research/ >>"$LOG" 2>&1
  log "synced phgdh-research"
fi

# Individual PHGDH pages from general/ → content/PHGDH-topics/
for f in "$WIKI/general"/*phgdh*.md; do
  [ -f "$f" ] && /bin/cp "$f" content/PHGDH-topics/ 2>/dev/null
done
# Also surface the scavenger-built projects/phgdh-* folders
for sub in "$WIKI"/projects/phgdh-*/; do
  [ -d "$sub" ] || continue
  NAME=$(basename "$sub")
  [ "$NAME" = "phgdh-research" ] && continue  # already handled above
  mkdir -p "content/$NAME"
  /usr/bin/rsync -a --delete --exclude=".git" "$sub" "content/$NAME/" >>"$LOG" 2>&1
  log "synced $NAME"
done

# Count what we staged
COPIED=$(find content/PHGDH-topics content/PHGDH-Allosteric-RBD-Binder content/phgdh-research content/phgdh-* -type f -name "*.md" 2>/dev/null | wc -l | tr -d " ")
log "staged $COPIED markdown files in content/"

# 3. Commit + push
/usr/bin/git add content/
if /usr/bin/git diff --cached --quiet; then
  log "no content changes — nothing to publish"
  echo "{\"ok\":true,\"published\":false,\"reason\":\"no changes\",\"files_staged\":$COPIED}"
  exit 0
fi

NCHANGED=$(/usr/bin/git diff --cached --name-only | wc -l | tr -d " ")
/usr/bin/git commit -q -m "publish: PHGDH wiki update from W0 ($(date '+%Y-%m-%dT%H:%M'))" >>"$LOG" 2>&1
COMMIT=$(/usr/bin/git rev-parse --short HEAD)
log "commit $COMMIT with $NCHANGED files changed"

if /usr/bin/git push origin v4 >>"$LOG" 2>&1; then
  log "pushed successfully — cloudflare pages will build in ~1-2 min"
  echo "{\"ok\":true,\"published\":true,\"commit\":\"$COMMIT\",\"files_changed\":$NCHANGED,\"site\":\"sdd-wiki-public.pages.dev\"}"
else
  log "ERROR push failed"
  echo "{\"ok\":false,\"error\":\"push failed — see $LOG\"}"
  exit 2
fi
