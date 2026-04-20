#!/bin/bash
# Polls sacct for all jobs in the last 48 h. Writes cheaha_utilization.jsonl
# append + /tmp/phgdh_cheaha_status.json snapshot. Cadence: 3 min.
set -u
WS=/Users/jakeclaw/.openclaw/workspace
OUT_JSONL=$WS/project-state/cheaha_utilization.jsonl
SNAP=/tmp/phgdh_cheaha_status.json
TS=$(date -u +%FT%TZ)

# Ask sacct for jobs in last 48h. -X excludes steps. -p pipe-delimited. -n no header.
SACCT=$(ssh -o ConnectTimeout=6 cheaha \
  "sacct -u jakechen -S 2026-04-18T00:03:20 -X -n -p \
   --format=JobID,JobName,State,ReqCPUS,Timelimit,CPUTimeRAW,Elapsed,ReqTRES,AllocTRES,TRESUsageInMax" \
   2>/dev/null)

if [ -z "$SACCT" ]; then
  echo "{\"at\":\"$TS\",\"error\":\"sacct empty or SSH failed\",\"rwi\":0.0,\"jobs\":[]}" > $SNAP
  chmod 644 $SNAP
  exit 0
fi

# Parse + compute Remote Workload Intensity
/Users/jakeclaw/.hermes-venv/bin/python - "$SACCT" "$TS" "$OUT_JSONL" "$SNAP" <<'PYEOF'
import sys, json, re, os
from datetime import datetime, timezone
raw, ts, out_jsonl, snap = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

def parse_hms(s):
    # Slurm time: [D-]HH:MM:SS or HH:MM:SS or MM:SS
    if not s or s in ("UNLIMITED","Partition_Limit"): return 0
    days = 0
    if "-" in s: d,rest = s.split("-",1); days = int(d); s = rest
    parts = s.split(":")
    parts = [int(p) for p in parts]
    while len(parts) < 3: parts.insert(0, 0)
    h,m,sec = parts
    return days*86400 + h*3600 + m*60 + sec

def gpu_hours_from_tres(tres_str):
    # TRESUsageInMax like "cpu=2,mem=3G,gres/gpu=1" (but TRESUsageInMax is seconds)
    if not tres_str: return 0.0
    m = re.search(r"gres/gpu=(\d+)", tres_str)
    return float(m.group(1)) if m else 0.0

jobs = []
total_actual_cpuseconds = 0
total_requested_cpuseconds = 0
pending_ages = []
failed_states = 0
running_count = 0

for line in raw.strip().split("\n"):
    if not line or "|" not in line: continue
    fields = line.split("|")
    if len(fields) < 10: continue
    jobid, name, state, reqcpus, timelimit, cputime_raw, elapsed, req_tres, alloc_tres, tres_usage_max = fields[:10]
    try: req_cpus = int(reqcpus) if reqcpus.isdigit() else 0
    except: req_cpus = 0
    try: cpu_raw = int(cputime_raw) if cputime_raw.isdigit() else 0
    except: cpu_raw = 0
    wt_sec = parse_hms(timelimit)

    total_actual_cpuseconds += cpu_raw
    total_requested_cpuseconds += req_cpus * wt_sec

    if state.startswith("PENDING"):
        # Age of pending = unknown from sacct alone — rough proxy
        pending_ages.append(jobid)
    if state.startswith(("FAILED","CANCELLED","TIMEOUT","NODE_FAIL","BOOT_FAIL")):
        failed_states += 1
    if state.startswith("RUNNING"):
        running_count += 1

    jobs.append({
        "jobid": jobid, "name": name, "state": state,
        "req_cpus": req_cpus, "timelimit_s": wt_sec,
        "cpu_time_raw_s": cpu_raw, "elapsed": elapsed,
        "gpu_hours_est": gpu_hours_from_tres(tres_usage_max) * max(1, parse_hms(elapsed)) / 3600
    })

# Remote Workload Intensity: how well we used what we requested.
rwi = (total_actual_cpuseconds / total_requested_cpuseconds) if total_requested_cpuseconds > 0 else 0.0
rwi_pct = min(100.0, rwi * 100.0)

snapshot = {
    "at": ts,
    "job_count_48h": len(jobs),
    "running": running_count,
    "pending": len(pending_ages),
    "failed_recent": failed_states,
    "rwi_pct": round(rwi_pct, 2),
    "total_actual_cpu_hours": round(total_actual_cpuseconds/3600, 2),
    "total_requested_cpu_hours": round(total_requested_cpuseconds/3600, 2),
    "total_gpu_hours_est": round(sum(j["gpu_hours_est"] for j in jobs), 3),
    "jobs": jobs[-10:],  # tail only in snapshot
}
os.makedirs(os.path.dirname(out_jsonl), exist_ok=True)
with open(out_jsonl, "a") as f:
    compact = {k: v for k, v in snapshot.items() if k != "jobs"}
    f.write(json.dumps(compact) + "\n")
with open(snap, "w") as f:
    json.dump(snapshot, f, indent=2)
os.chmod(snap, 0o644)
print(f"wrote snapshot: rwi={rwi_pct:.1f}% jobs={len(jobs)} running={running_count} pending={len(pending_ages)}")
PYEOF
