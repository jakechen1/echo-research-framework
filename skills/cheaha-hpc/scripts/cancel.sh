#!/bin/bash
# Cancel a Cheaha job by id, or all my jobs with --all
if [ "${1:-}" = "--all" ]; then
  ssh cheaha "scancel -u \$USER" && echo "cancelled all jobs for $USER on cheaha"
elif [ -n "${1:-}" ]; then
  ssh cheaha "scancel $1" && echo "cancelled job $1"
else
  echo "usage: cancel.sh <jobid>  |  cancel.sh --all"; exit 1
fi
