#!/usr/bin/env python3
"""Sample W0 CPU% and L0 GPU% every 60 s. Write JSONL."""
import json, subprocess, time, os, re, urllib.request
from datetime import datetime, timezone
from pathlib import Path

OUT = Path("/Users/jakeclaw/.openclaw/workspace/project-state/utilization.jsonl")
OUT.parent.mkdir(parents=True, exist_ok=True)

def w0_cpu_pct():
    try:
        cores = int(subprocess.check_output(["sysctl","-n","hw.ncpu"], text=True).strip())
    except: cores = 10
    try:
        out = subprocess.run(
            "ps -eo %cpu,comm | awk '$2 ~ /python|ollama|node|smina|vina|fpocket|pymol/ {s+=$1} END {print s+0}'",
            shell=True, capture_output=True, text=True, timeout=5
        ).stdout.strip()
        pct = float(out) / cores
    except: pct = 0.0
    try:
        up = subprocess.check_output("uptime", shell=True, text=True, timeout=3)
        load = float(re.search(r"load averages?:\s*([\d.]+)", up).group(1))
    except: load = 0.0
    load_pct = min(100.0, load / cores * 100.0)
    return max(pct, load_pct)  # whichever signal is higher

def l0_gpu_pct():
    # 1) Try powermetrics via SSH (best signal, needs jakechen keyauth)
    try:
        r = subprocess.run(
            ["ssh","-o","ConnectTimeout=3","-o","StrictHostKeyChecking=no",
             "jakechen@192.168.68.200",
             "sudo -n powermetrics -n 1 --samplers gpu_power -i 500 2>/dev/null | grep -E 'active residency' | head -1"],
            capture_output=True, text=True, timeout=6
        )
        m = re.search(r"([\d.]+)\s*%", r.stdout)
        if m: return float(m.group(1))
    except: pass
    # 2) Fallback: Ollama /api/ps — any loaded model => treat as 100%
    try:
        with urllib.request.urlopen("http://192.168.68.200:11434/api/ps", timeout=3) as resp:
            d = json.load(resp)
            return 100.0 if d.get("models") else 0.0
    except: return 0.0

def main():
    rec = {
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "w0_cpu_pct": round(w0_cpu_pct(), 2),
        "l0_gpu_pct": round(l0_gpu_pct(), 2),
    }
    with OUT.open("a") as f:
        f.write(json.dumps(rec) + "\n")
    # publish a /tmp copy for dashboard (jakechen can't traverse /Users/jakeclaw)
    try: subprocess.run(["cp","-f",str(OUT),"/tmp/phgdh_utilization.jsonl"], check=False)
    except: pass
    print(json.dumps(rec))

if __name__ == "__main__":
    main()
