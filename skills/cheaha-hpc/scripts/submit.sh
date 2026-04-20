#!/bin/bash
# Submit an sbatch, but REFUSE if preflight fails.
# Rules enforced: 2, 6, 7 (column-schema mismatch).
SB="${1:?sbatch file required}"
DRY="${DRY_RUN:-1}"  # default: run dry-run check
if [ ! -f "$SB" ]; then echo "no such sbatch: $SB"; exit 1; fi

echo "=== preflight ==="
/Users/jakeclaw/.hermes-venv/bin/python \
  /Users/jakeclaw/.openclaw/workspace/skills/cheaha-hpc/scripts/preflight.py \
  "$SB" ${DRY:+--dry-run}
RC=$?
if [ $RC -ne 0 ]; then
  echo "PREFLIGHT FAILED rc=$RC — NOT submitting. Fix errors above."
  exit $RC
fi
echo "=== submitting ==="
for i in 1 2 3 4 5; do
  R=$(ssh cheaha "sbatch $SB" 2>&1)
  if echo "$R" | grep -q "Submitted"; then
    echo "$R"
    JOBID=$(echo "$R" | grep -oE "[0-9]+" | head -1)
    echo "$JOBID" > /tmp/phgdh_last_jobid.txt
    exit 0
  fi
  echo "attempt $i: $R"; sleep 10
done
echo "FAILED after 5 retries"; exit 1
