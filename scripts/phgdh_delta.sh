#!/bin/bash
# phgdh_delta.sh - compare the two most recent PHGDH scavenger JSONL outputs.
# Prints a human-readable delta report. If only one file exists, reports baseline.
set -euo pipefail

DATA=/Users/jakeclaw/workers/data/phgdh
FILES=($(ls -1t "$DATA"/*.jsonl 2>/dev/null))
N=${#FILES[@]}

if [ "$N" -eq 0 ]; then
  echo "no scavenge files yet — run phgdh_scavenger.py first"
  exit 1
fi

TODAY="${FILES[0]}"
TODAY_NAME=$(basename "$TODAY" .jsonl)
TODAY_ROWS=$(wc -l < "$TODAY" | tr -d " ")
TODAY_SIZE=$(du -h "$TODAY" | cut -f1)
TODAY_MTIME=$(stat -f "%Sm" "$TODAY")

if [ "$N" -lt 2 ]; then
  cat <<REPORT
## PHGDH scavenge baseline - $TODAY_NAME

- File: $TODAY
- Rows: $TODAY_ROWS
- Size: $TODAY_SIZE
- Written: $TODAY_MTIME
- Prior file: none (this is the first scavenge)

No delta to report yet. Tomorrows scavenger will produce the first diff.
REPORT
  exit 0
fi

PRIOR="${FILES[1]}"
PRIOR_NAME=$(basename "$PRIOR" .jsonl)
PRIOR_ROWS=$(wc -l < "$PRIOR" | tr -d " ")
PRIOR_MTIME=$(stat -f "%Sm" "$PRIOR")

# Extract molecule sets
jq -r ".molecule_chembl_id // empty" "$TODAY" | sort -u > /tmp/phgdh_mols_today
jq -r ".molecule_chembl_id // empty" "$PRIOR" | sort -u > /tmp/phgdh_mols_prior

ADDED_MOLS=$(comm -23 /tmp/phgdh_mols_today /tmp/phgdh_mols_prior | wc -l | tr -d " ")
REMOVED_MOLS=$(comm -13 /tmp/phgdh_mols_today /tmp/phgdh_mols_prior | wc -l | tr -d " ")
TOTAL_MOLS_TODAY=$(wc -l < /tmp/phgdh_mols_today | tr -d " ")
TOTAL_MOLS_PRIOR=$(wc -l < /tmp/phgdh_mols_prior | tr -d " ")

# Sample of added mols (first 5)
ADDED_SAMPLE=$(comm -23 /tmp/phgdh_mols_today /tmp/phgdh_mols_prior | head -5 | paste -sd "," -)
REMOVED_SAMPLE=$(comm -13 /tmp/phgdh_mols_today /tmp/phgdh_mols_prior | head -5 | paste -sd "," -)

# pChEMBL stats
MAX_TODAY=$(jq -r ".pchembl_value // empty" "$TODAY" | grep -v "^$" | sort -g | tail -1)
MAX_PRIOR=$(jq -r ".pchembl_value // empty" "$PRIOR" | grep -v "^$" | sort -g | tail -1)
WITH_PCHEMBL_TODAY=$(jq -r ".pchembl_value // empty" "$TODAY" | grep -vc "^$" || echo 0)
WITH_PCHEMBL_PRIOR=$(jq -r ".pchembl_value // empty" "$PRIOR" | grep -vc "^$" || echo 0)

ROW_DELTA=$((TODAY_ROWS - PRIOR_ROWS))
[ $ROW_DELTA -ge 0 ] && ROW_SIGN="+" || ROW_SIGN=""

cat <<REPORT
## PHGDH scavenge delta - $TODAY_NAME vs $PRIOR_NAME

| Metric | Prior ($PRIOR_NAME) | Current ($TODAY_NAME) | Delta |
|---|---|---|---|
| Rows | $PRIOR_ROWS | $TODAY_ROWS | ${ROW_SIGN}${ROW_DELTA} |
| Unique molecules | $TOTAL_MOLS_PRIOR | $TOTAL_MOLS_TODAY | $(( TOTAL_MOLS_TODAY - TOTAL_MOLS_PRIOR )) |
| Rows with pChEMBL | $WITH_PCHEMBL_PRIOR | $WITH_PCHEMBL_TODAY | $(( WITH_PCHEMBL_TODAY - WITH_PCHEMBL_PRIOR )) |
| Max pChEMBL | $MAX_PRIOR | $MAX_TODAY | - |

**Added molecules:** $ADDED_MOLS
${ADDED_SAMPLE:+Sample: $ADDED_SAMPLE}

**Removed molecules:** $REMOVED_MOLS
${REMOVED_SAMPLE:+Sample: $REMOVED_SAMPLE}

**Files:**
- current: $TODAY ($TODAY_SIZE, written $TODAY_MTIME)
- prior:   $PRIOR (written $PRIOR_MTIME)
REPORT

# Clean up
rm -f /tmp/phgdh_mols_today /tmp/phgdh_mols_prior
