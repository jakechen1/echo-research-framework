#!/bin/bash
# route.sh — pick tier based on estimated cost.
# Reads cost_table.json + input args; prints the recommended tier and host.
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)"
TABLE="$DIR/cost_table.json"
OP=""
N=1
GPU_MB_HINT=0
RAM_MB_HINT=0
while [ $# -gt 0 ]; do
  case "$1" in
    --task) TASK="$2"; shift 2;;
    --op-type) OP="$2"; shift 2;;
    --n-items) N="$2"; shift 2;;
    --gpu-mb) GPU_MB_HINT="$2"; shift 2;;
    --ram-mb) RAM_MB_HINT="$2"; shift 2;;
    *) shift;;
  esac
done
[ -z "$OP" ] && { echo "usage: route.sh --op-type <key> --n-items N [--gpu-mb M] [--ram-mb R]"; exit 1; }

CPU_MS=$(jq -r --arg k "$OP" ".[\$k].cpu_ms // 0" "$TABLE")
RSS_KB=$(jq -r --arg k "$OP" ".[\$k].rss_kb // 0" "$TABLE")
GPU_MB=$(jq -r --arg k "$OP" ".[\$k].gpu_mb // 0" "$TABLE")

TOTAL_S=$(python3 -c "print($CPU_MS * $N / 1000)")
TOTAL_RSS_MB=$(python3 -c "print($RSS_KB * $N / 1024)")
# pick the maximum gpu requirement between hint and per-item * reasonable concurrency
PEAK_GPU=$(python3 -c "print(max($GPU_MB, $GPU_MB_HINT))")

# Tier decision
if (( $(python3 -c "print(1 if $PEAK_GPU > 6000 else 0)") )); then
  TIER=5; HOST=cheaha; PART=amperenodes
elif (( $(python3 -c "print(1 if $TOTAL_RSS_MB > 8000 else 0)") )); then
  TIER=4; HOST=cheaha; PART=medium
elif (( $(python3 -c "print(1 if $TOTAL_S > 1800 else 0)") )); then
  TIER=4; HOST=cheaha; PART=short
elif (( $(python3 -c "print(1 if $PEAK_GPU > 0 else 0)") )); then
  TIER=3; HOST=L0; PART=local-gpu
elif (( $(python3 -c "print(1 if $TOTAL_S > 60 and $N >= 5 else 0)") )); then
  TIER=2; HOST=W0; PART=local-parallel-10
elif (( $(python3 -c "print(1 if $TOTAL_S > 1 else 0)") )); then
  TIER=1; HOST=W0; PART=local-serial
else
  TIER=0; HOST=inline; PART=none
fi

cat <<OUT
{
  "task": "${TASK:-unnamed}",
  "op_type": "$OP",
  "n_items": $N,
  "est_wall_s": $TOTAL_S,
  "est_peak_rss_mb": $TOTAL_RSS_MB,
  "est_peak_gpu_mb": $PEAK_GPU,
  "decision": {
    "tier": $TIER,
    "host": "$HOST",
    "partition": "$PART"
  }
}
OUT
