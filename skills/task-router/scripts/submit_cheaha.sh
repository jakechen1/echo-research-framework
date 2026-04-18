#!/bin/bash
# submit_cheaha.sh — thin wrapper over cheaha-hpc-skill/scripts/submit.sh.
# Requires an SBATCH template chosen and filled. This is mostly a pointer.
CHEAHA_SKILL=/Users/jakeclaw/.openclaw/workspace/skills/cheaha-hpc
echo "For Cheaha submission see templates in:"
ls "$CHEAHA_SKILL/templates/"
echo
echo "Then:"
echo "  $CHEAHA_SKILL/scripts/submit.sh <your.sbatch>"
