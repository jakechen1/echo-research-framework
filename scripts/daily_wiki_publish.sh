#!/bin/bash
# daily_wiki_publish.sh — 17:05 daily.
# Orchestrates: (a) ensure L2 report exists for today, (b) copy it into the
# public wiki project folder, (c) generate/update the daily Project Summary
# index page linking to all relevant artifacts, (d) trigger phgdh_publish.sh
# to push everything to sdd-wiki → Cloudflare Pages.
set -euo pipefail

WS=/Users/jakeclaw/.openclaw/workspace
PS=$WS/project-state
WIKI=/Users/jakeclaw/wiki
PW=$WIKI/projects/PHGDH-Allosteric-RBD-Binder
DAILY_DIR=$PW/daily-summaries
SUMMARY=$PW/Project-Summary.md
LOG=/Users/jakeclaw/workers/logs/daily_wiki_publish.log
HB=/Users/jakeclaw/workers/heartbeats/daily_wiki_publish.ts
mkdir -p "$DAILY_DIR" "$(dirname "$LOG")" "$(dirname "$HB")"
date +%s > "$HB"

log() { echo "[$(date +%Y-%m-%dT%H:%M:%S%z)] $*" >> "$LOG"; }
log "=== start ==="

TODAY=$(date +%Y-%m-%d)

# (a) Ensure an L2 report for today exists
L2_FILE="$PS/reports/L2/${TODAY}.md"
if [ ! -f "$L2_FILE" ]; then
  log "no L2 for today — generating"
  /usr/bin/python3 /Users/jakeclaw/workers/bin/report_builder.py --level 2 --trigger "wiki-publish" >>"$LOG" 2>&1
fi

# (b) Copy L2 into the public wiki with Quartz frontmatter
if [ -f "$L2_FILE" ]; then
  # Prepend frontmatter so Quartz renders it nicely
  {
    echo "---"
    echo "title: \"Daily Digest $TODAY\""
    echo "date: $TODAY"
    echo "category: daily"
    echo "tier: live"
    echo "source: jakeclaw@W0:$L2_FILE"
    echo "---"
    echo ""
    # Strip the source frontmatter (between first and second ---) and keep body
    awk "BEGIN{f=0} /^---$/{f++; next} f>=2" "$L2_FILE"
  } > "$DAILY_DIR/${TODAY}.md"
  log "copied L2 to $DAILY_DIR/${TODAY}.md"
fi

# (c) Generate Project-Summary.md — the daily index
/usr/bin/python3 /Users/jakeclaw/workers/bin/project_summary.py > "$SUMMARY.tmp" && mv "$SUMMARY.tmp" "$SUMMARY"
log "regenerated $SUMMARY"

# Dashboard — regenerated alongside Project-Summary
/usr/bin/python3 /Users/jakeclaw/workers/bin/project_dashboard.py > "/Users/jakeclaw/wiki/projects/PHGDH-Allosteric-RBD-Binder/Project-Dashboard.md.tmp" \
    && mv "/Users/jakeclaw/wiki/projects/PHGDH-Allosteric-RBD-Binder/Project-Dashboard.md.tmp" "/Users/jakeclaw/wiki/projects/PHGDH-Allosteric-RBD-Binder/Project-Dashboard.md"
log "regenerated Project-Dashboard.md"

# (d) Publish to sdd-wiki → Cloudflare Pages
/Users/jakeclaw/workers/bin/phgdh_publish.sh >>"$LOG" 2>&1 && log "published" || log "publish FAILED"

log "=== end ==="
