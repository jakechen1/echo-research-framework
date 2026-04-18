#!/bin/bash
# parallel_local.sh — run N-way parallel locally on W0 (default) or L0.
# Uses xargs for a reliable cross-platform parallel primitive.
#
# Usage:
#   parallel_local.sh --jobs 10 --cmd "bash /path/process_one.sh {}" < items.txt
#   parallel_local.sh --host L0 --jobs 10 --cmd "python3 score.py {}" < items.txt
set -euo pipefail
JOBS=10
HOST=W0
CMD=""
while [ $# -gt 0 ]; do
  case "$1" in
    --jobs) JOBS="$2"; shift 2;;
    --host) HOST="$2"; shift 2;;
    --cmd) CMD="$2"; shift 2;;
    *) shift;;
  esac
done
[ -z "$CMD" ] && { echo "usage: parallel_local.sh [--jobs N] [--host W0|L0] --cmd 'cmd {}' < items.txt"; exit 1; }

case "$HOST" in
  W0) xargs -n 1 -P "$JOBS" -I{} bash -c "$CMD" ;;
  L0) ssh -o ConnectTimeout=5 -o BatchMode=yes jakechen@10.0.0.1 \
         "xargs -n 1 -P $JOBS -I{} bash -c '$CMD'" ;;
  *)  echo "unknown host: $HOST"; exit 1;;
esac
