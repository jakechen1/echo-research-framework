#!/bin/bash
# Submit a local sbatch file to Cheaha.
# Usage: submit.sh path/to/job.sbatch
set -euo pipefail
SBATCH_FILE="${1:?path to .sbatch required}"
[ -r "$SBATCH_FILE" ] || { echo "not readable: $SBATCH_FILE" >&2; exit 1; }
REMOTE_DIR="~/jobs"
ssh cheaha "mkdir -p $REMOTE_DIR"
scp "$SBATCH_FILE" cheaha:$REMOTE_DIR/
BASENAME=$(basename "$SBATCH_FILE")
OUT=$(ssh cheaha "cd $REMOTE_DIR && sbatch $BASENAME")
echo "$OUT"
JOBID=$(echo "$OUT" | awk '{print $NF}')
echo "Track: ssh cheaha 'sacct -j $JOBID -o jobid,state,elapsed,maxrss'"
