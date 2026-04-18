#!/bin/bash
# Quick status of your Cheaha jobs. Optional jobid for details.
if [ -n "${1:-}" ]; then
  ssh cheaha "sacct -j $1 -o jobid,jobname%20,state,elapsed,maxrss,reqmem,alloccpu,exitcode"
else
  ssh cheaha "squeue -u \$USER -o '%10i %12j %8T %10M %6D %R'"
fi
