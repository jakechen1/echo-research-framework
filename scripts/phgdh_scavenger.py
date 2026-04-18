#!/usr/bin/env python3
"""PHGDH scavenger — pulls bioactivities for PHGDH (UniProt O43175) from ChEMBL.

Writes JSONL to /Users/jakeclaw/workers/data/phgdh/YYYY-MM-DD.jsonl
Touches heartbeat /Users/jakeclaw/workers/heartbeats/phgdh_scavenger.ts
Uses the ChEMBL REST API (no scraping). Polite: 1s between paginated calls.
"""
import json, os, sys, time, urllib.request, urllib.error
from datetime import datetime

OUT_DIR = "/Users/jakeclaw/workers/data/phgdh"
HB      = "/Users/jakeclaw/workers/heartbeats/phgdh_scavenger.ts"
CHEMBL  = "https://www.ebi.ac.uk/chembl/api/data"
UNIPROT = "O43175"  # PHGDH, human

def fetch(url, retries=3):
    last = None
    for i in range(retries):
        try:
            req = urllib.request.Request(url, headers={
                "Accept": "application/json",
                "User-Agent": "jakeclaw-phgdh-scavenger/1.0 (research)",
            })
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except (urllib.error.URLError, TimeoutError) as e:
            last = e
            time.sleep(2 ** i)
    raise last

def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    today = datetime.utcnow().strftime("%Y-%m-%d")
    outfile = os.path.join(OUT_DIR, f"{today}.jsonl")

    # 1. Resolve UniProt -> ChEMBL target(s)
    tdata = fetch(f"{CHEMBL}/target.json?target_components__accession={UNIPROT}")
    tids = [t["target_chembl_id"] for t in tdata.get("targets", [])]
    if not tids:
        print(f"ERROR: no ChEMBL targets for {UNIPROT}", file=sys.stderr)
        sys.exit(1)
    print(f"[{datetime.utcnow().isoformat()}] resolved {UNIPROT} -> {tids}")

    # 2. Fetch bioactivities (paginated) for each target
    count = 0
    with open(outfile, "w") as f:
        for tid in tids:
            offset, page = 0, 0
            while True:
                url = (f"{CHEMBL}/activity.json?target_chembl_id={tid}"
                       f"&limit=1000&offset={offset}")
                data = fetch(url)
                acts = data.get("activities", [])
                if not acts:
                    break
                for a in acts:
                    row = {
                        "molecule_chembl_id": a.get("molecule_chembl_id"),
                        "target_chembl_id":   a.get("target_chembl_id"),
                        "target_pref_name":   a.get("target_pref_name"),
                        "standard_type":      a.get("standard_type"),
                        "standard_value":     a.get("standard_value"),
                        "standard_units":     a.get("standard_units"),
                        "standard_relation":  a.get("standard_relation"),
                        "pchembl_value":      a.get("pchembl_value"),
                        "canonical_smiles":   a.get("canonical_smiles"),
                        "assay_chembl_id":    a.get("assay_chembl_id"),
                        "assay_description":  a.get("assay_description"),
                        "document_chembl_id": a.get("document_chembl_id"),
                        "uniprot":            UNIPROT,
                        "fetched_at":         datetime.utcnow().isoformat(),
                    }
                    f.write(json.dumps(row) + "\n")
                    count += 1
                page += 1
                if len(acts) < 1000:
                    break
                offset += 1000
                time.sleep(1)  # polite
            print(f"  {tid}: {count} rows after page {page}")

    print(f"wrote {count} bioactivities to {outfile}")
    with open(HB, "w") as f:
        f.write(str(int(time.time())))

if __name__ == "__main__":
    main()
