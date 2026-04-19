#!/usr/bin/env python3
"""Workload optimizer — reads AGE + live util, dispatches next chunk."""
import json, subprocess, sys, time, os
from datetime import datetime, timezone, timedelta
from pathlib import Path

sys.path.insert(0, "/Users/jakeclaw/.openclaw/workspace/skills/resilience/scripts")
from atomic_write import atomic_write

WS = Path("/Users/jakeclaw/.openclaw/workspace")
AGE_DIR = WS/"project-state/age_scores"
UTIL    = WS/"project-state/utilization.jsonl"
POLICY  = WS/"project-state/workload_policy.json"
ACTIONS = WS/"project-state/workload_actions.jsonl"
STATUS  = Path("/tmp/phgdh_optimizer_status.json")
PAUSE_F = Path("/tmp/phgdh_optimizer_pause")
NOTIFY  = "/Users/jakeclaw/.openclaw/workspace/skills/notifier/scripts/notify.sh"

NOW = time.time()
NOW_ISO = datetime.now(timezone.utc).isoformat(timespec="seconds")
MAX_LOCAL = 3        # max concurrent expansion jobs
COOLDOWN_S = 1800    # 30 min cooldown per action

# --- Action registry: id -> (host, cmd, estimated_seconds) ---
# Each cmd is a shell command fragment executed via `bash -c` on W0
# (Cheaha ones SSH through the cheaha alias).
ACTIONS_REG = {
    "W0_utilization_booster": (
        "W0", f"{WS}/skills/plan-sync/scripts/plan_sync.py && "
              f"/Users/jakeclaw/.hermes-venv/bin/python "
              f"{WS}/skills/age-scoring/scripts/utilization_sampler.py",
        30),
    "L0_wiki_interlink_batch": (
        "L0", f"{WS}/skills/plan-sync/scripts/plan_sync.py; "
              f"/Users/jakeclaw/.hermes-venv/bin/python "
              f"/Users/jakeclaw/phgdh-scavenger/scripts/aims/aim5_wiki_interlink_gemma.py",
        600),
    "W0_scaffold_cluster": (
        "W0", f"/Users/jakeclaw/.hermes-venv/bin/python - <<'PYEOF'\n"
              "import csv\n"
              "from rdkit import Chem\n"
              "from rdkit.Chem.Scaffolds import MurckoScaffold\n"
              "rows=list(csv.DictReader(open('/Users/jakeclaw/.openclaw/workspace/data/aim2_top20_inhibitors.csv')))\n"
              "scaffolds={}\n"
              "for r in rows:\n"
              "    m=Chem.MolFromSmiles(r['smiles'])\n"
              "    if m is None: continue\n"
              "    s=Chem.MolToSmiles(MurckoScaffold.GetScaffoldForMol(m))\n"
              "    scaffolds.setdefault(s,[]).append(r['chembl_id'])\n"
              "out='/Users/jakeclaw/.openclaw/workspace/data/aim2_scaffolds.json'\n"
              "import json; json.dump(scaffolds, open(out,'w'), indent=2)\n"
              "print(f'{len(scaffolds)} unique Murcko scaffolds across {len(rows)} inhibitors -> {out}')\n"
              "PYEOF",
        120),
    "W0_qed_lipinski_filter": (
        "W0", f"/Users/jakeclaw/.hermes-venv/bin/python - <<'PYEOF'\n"
              "import csv\n"
              "from rdkit import Chem\n"
              "from rdkit.Chem import QED, Lipinski, Descriptors\n"
              "rows=list(csv.DictReader(open('/Users/jakeclaw/.openclaw/workspace/data/aim4_smiles/smiles_potency_sorted.tsv'), delimiter='\\t'))\n"
              "out=[]\n"
              "for r in rows:\n"
              "    m=Chem.MolFromSmiles(r['smiles'])\n"
              "    if m is None: continue\n"
              "    qed=QED.qed(m); mw=Descriptors.MolWt(m); logp=Descriptors.MolLogP(m)\n"
              "    hbd=Lipinski.NumHDonors(m); hba=Lipinski.NumHAcceptors(m)\n"
              "    lipinski=int(mw<=500 and logp<=5 and hbd<=5 and hba<=10)\n"
              "    out.append({'chembl_id':r['chembl_id'],'pchembl':r['pchembl'],'qed':round(qed,3),'mw':round(mw,1),'logp':round(logp,2),'lipinski':lipinski})\n"
              "import json; json.dump(out, open('/Users/jakeclaw/.openclaw/workspace/data/aim4_qed_filter.json','w'), indent=2)\n"
              "print(f'{len(out)} molecules filtered. Lipinski-passing: {sum(1 for x in out if x[chr(34)+\"lipinski\"+chr(34)])}')\n"
              "PYEOF",
        60),
    "W0_tanimoto_matrix": (
        "W0", f"/Users/jakeclaw/.hermes-venv/bin/python - <<'PYEOF'\n"
              "import csv, json\n"
              "from rdkit import Chem, DataStructs\n"
              "from rdkit.Chem import AllChem\n"
              "rows=list(csv.DictReader(open('/Users/jakeclaw/.openclaw/workspace/data/aim2_top20_inhibitors.csv')))\n"
              "fps=[]; ids=[]\n"
              "for r in rows:\n"
              "    m=Chem.MolFromSmiles(r['smiles'])\n"
              "    if m is None: continue\n"
              "    fps.append(AllChem.GetMorganFingerprintAsBitVect(m,2,2048)); ids.append(r['chembl_id'])\n"
              "mat=[[round(DataStructs.TanimotoSimilarity(a,b),3) for b in fps] for a in fps]\n"
              "json.dump({'ids':ids,'tanimoto':mat}, open('/Users/jakeclaw/.openclaw/workspace/data/aim2_tanimoto_top20.json','w'), indent=2)\n"
              "print(f'{len(ids)} x {len(ids)} Tanimoto matrix written')\n"
              "PYEOF",
        180),
    "cheaha_vina_top20": (
        "cheaha",
        "ssh cheaha 'cd ~/phgdh-sbdd && for i in 1 2 3; do JOB=$(sbatch scripts/smoke_vina2.sbatch 2>&1); "
        "echo $JOB | grep -q Submitted && break; sleep 8; done; squeue -u jakechen'",
        1800),
}

# --- helpers ---
def load_policy():
    try: return json.loads(POLICY.read_text())
    except: return {"cooldowns": {}, "weights": {k: 1.0 for k in ACTIONS_REG}}

def save_policy(p):
    atomic_write(POLICY, json.dumps(p, indent=2).encode())

def latest_age():
    if not AGE_DIR.exists(): return None
    files = sorted(AGE_DIR.glob("*.json"), key=lambda p: p.stat().st_mtime)
    if not files: return None
    try: return json.loads(files[-1].read_text())
    except: return None

def recent_util(window_s=300):
    """Mean W0 CPU %, L0 GPU %, Cheaha RWI % over last N seconds."""
    if not UTIL.exists(): return 0, 0, 0, 0
    cpus, gpus, cheahas = [], [], []
    for line in UTIL.read_text().splitlines()[-50:]:
        try:
            r = json.loads(line)
            t = datetime.fromisoformat(r["at"].replace("Z","+00:00")).timestamp()
            if NOW - t > window_s: continue
            cpus.append(r["w0_cpu_pct"]); gpus.append(r["l0_gpu_pct"])
            cheahas.append(r.get("cheaha_rwi_pct", 0.0))
        except: pass
    if not cpus: return 0, 0, 0, 0
    return (sum(cpus)/len(cpus), sum(gpus)/len(gpus),
            sum(cheahas)/len(cheahas) if cheahas else 0, len(cpus))

def count_running_expansion():
    try:
        out = subprocess.check_output(
            "ps -eo pid,command | grep -E 'wiki_interlink|scaffold_cluster|qed_lipinski|tanimoto_matrix|smoke_vina' "
            "| grep -v grep | wc -l", shell=True, text=True).strip()
        return int(out)
    except: return 0

def choose_action(decision, policy):
    """Pick an eligible action for the current decision."""
    cooldowns = policy.get("cooldowns", {})
    candidates = []
    if decision == "LOCAL_EXPAND":
        pool = [k for k,(host,_,_) in ACTIONS_REG.items() if host in ("L0","W0")]
    elif decision == "OFFLOAD_CHEAHA":
        pool = [k for k,(host,_,_) in ACTIONS_REG.items() if host == "cheaha"]
    else:
        return None
    for k in pool:
        last = cooldowns.get(k, 0)
        if NOW - last < COOLDOWN_S: continue
        candidates.append(k)
    if not candidates: return None
    # weighted choice by policy.weights; break ties by oldest cooldown
    candidates.sort(key=lambda k: (-policy["weights"].get(k,1.0), cooldowns.get(k,0)))
    return candidates[0]

def dispatch(action_id):
    host, cmd, est = ACTIONS_REG[action_id]
    logpath = Path(f"/Users/jakeclaw/Library/Logs/optimizer_{action_id}.log")
    logpath.parent.mkdir(parents=True, exist_ok=True)
    # Fire and forget via nohup
    try:
        subprocess.Popen(
            ["bash", "-c", f"({cmd}) > {logpath} 2>&1"],
            preexec_fn=os.setpgrp  # detach
        )
        return True, f"pid-detached (est ~{est}s, log {logpath})"
    except Exception as e:
        return False, str(e)

def log_action(rec):
    ACTIONS.parent.mkdir(parents=True, exist_ok=True)
    with ACTIONS.open("a") as f: f.write(json.dumps(rec) + "\n")

def main():
    if PAUSE_F.exists():
        print("paused via /tmp/phgdh_optimizer_pause"); return

    age = latest_age()
    cpu_pct, gpu_pct, cheaha_pct, n = recent_util()
    combined = max(cpu_pct, gpu_pct, cheaha_pct)  # v3 cheaha-aware
    running = count_running_expansion()

    A = (age or {}).get("A", {}).get("score") if age else None
    E = (age or {}).get("E", {}).get("score") if age else None

    # Decision
    if running >= MAX_LOCAL:
        decision = "BACKOFF_CAP"
    elif combined >= 90 and n >= 2:
        decision = "BACKOFF_SATURATED"
    elif E is not None and E >= 4 and A is not None and A < 4:
        decision = "OFFLOAD_CHEAHA"
    elif (E is None or E < 4) and combined < 50:
        decision = "LOCAL_EXPAND"
    elif E is not None and E >= 7 and A is not None and A >= 7:
        decision = "HEALTHY"
    else:
        decision = "HOLD"

    policy = load_policy()
    action_id = choose_action(decision, policy)
    status = {
        "at": NOW_ISO, "decision": decision,
        "A": A, "E": E, "cpu_pct": round(cpu_pct,2),
        "gpu_pct": round(gpu_pct,2), "combined_pct": round(combined,2),
        "running_expansion_jobs": running,
        "chosen_action": action_id,
    }
    atomic_write(STATUS, json.dumps(status, indent=2).encode())

    if not action_id:
        print(json.dumps(status, indent=2))
        return

    ok, note = dispatch(action_id)
    policy.setdefault("cooldowns", {})[action_id] = NOW
    save_policy(policy)
    log_action({**status, "action_id": action_id, "dispatched": ok, "note": note})
    if ok:
        subprocess.run([NOTIFY, "⚙️", f"Auto-dispatch: {action_id}",
                        f"decision={decision}  A={A} E={E}  util={combined:.0f}%  running={running}"],
                       check=False, timeout=8)
    print(json.dumps({**status, "action": action_id, "ok": ok, "note": note}, indent=2))

if __name__ == "__main__":
    main()
