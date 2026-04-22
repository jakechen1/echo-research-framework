#!/usr/bin/env python3
import subprocess
import json
import time
import collections
import os
from datetime import datetime

# Configuration
DATA_FILE = "/Users/jakeclaw/.openclaw/workspace/project-state/e_score_trend.json"
HISTORY_LIMIT = 10  # 10 minutes
CHECK_INTERVAL = 60 # 60 seconds

# State
history = collections.deque(maxlen=HISTORY_LIMIT)

def get_cpu_usage():
    try:
        # top -l 1 provides a single sample
        output = subprocess.check_output(["top", "-l", "1", "-n", "0"], text=True)
        for line in output.splitlines():
            if "CPU usage" in line:
                # Format: "CPU usage: 3.84% user, 12.50% sys, 83.65% idle"
                parts = line.replace("CPU usage: ", "").split(", ")
                user = float(parts[0].split("%")[0])
                sys = float(parts[1].split("%")[0])
                idle = float(parts[2].split("%")[0])
                return 100.0 - idle
    except Exception as e:
        print(f"Error getting CPU usage: {e}")
    return 0.0

def calculate_e_score(cpu_usage):
    # E-score as a simple representation of utilization.
    # In a real scenario, this would be more complex (e.g. involving RAM/GPU).
    return round(cpu_usage, 2)

def run_monitor():
    print(f"Starting E-score monitor. Writing to {DATA_FILE}")
    while True:
        try:
            cpu_val = get_cpu_usage()
            e_score = calculate_e_score(cpu_val)
            history.append(e_score)
            
            avg_e = sum(history) / len(template_history) if (template_history := list(history)) else 0
            
            data = {
                "last_updated": datetime.now().isoformat(),
                "current_e_score": e_score,
                "average_e_score_10min": round(avg_e, 2),
                "samples_in_history": len(history),
                "cpu_utilization": cpu_val
            }
            
            # Atomic-like write
            temp_file = DATA_FILE + ".tmp"
            with open(temp_file, 'w') as f:
                json.dump(data, f, indent=2)
            os.rename(temp_file, DATA_FILE)
            
            print(f"[{datetime.now().isoformat()}] E-Score: {e_score}, 10m-Avg: {round(avg_e, 2)}")
            
        except Exception as e:
            print(f"Monitor error: {e}")
        
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    run_monitor()
