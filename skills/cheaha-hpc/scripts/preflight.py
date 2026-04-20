#!/usr/bin/env python3
"""preflight — validate an sbatch before submission.

Enforces UAB HPC Rules 2, 6, 7:
  Rule 2: partition + time + mem + cpus-per-task declared
  Rule 6: array jobs use %A_%a in output paths
  Rule 7: any `awk -F, ... '{print $N}'` against a CSV matches that
          CSV's schema file (columns[N-1].name matches the bash variable)

Also runs a 1-ligand DRY RUN (single-task array) locally when --dry-run is set.

Exit codes:
  0 = all checks pass
  2 = rule violation (don't submit)
  3 = schema mismatch (definitely don't submit — this is our Apr 18 bug class)
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

REQUIRED_PRAGMAS = ["--partition", "--time", "--mem", "--cpus-per-task"]

def find_schemas(sbatch_text):
    """Return list of (csv_path, schema_path) referenced via awk -F,"""
    hits = []
    # Find any CSV referenced in the sbatch
    for csv_ref in re.findall(r"data/[a-zA-Z0-9_/-]+\.csv", sbatch_text):
        csv_path = Path(f"/Users/jakeclaw/.openclaw/workspace/{csv_ref}")
        sch_path = csv_path.with_suffix(".schema.json")
        if not sch_path.exists():
            # try in data dir
            for p in Path("/Users/jakeclaw/.openclaw/workspace/data").rglob("*.schema.json"):
                try:
                    if json.loads(p.read_text()).get("filename_glob") == csv_path.name:
                        sch_path = p; break
                except: pass
        hits.append((csv_path, sch_path if sch_path.exists() else None))
    return hits

def check_awk_columns(sbatch_text, csv_path, schema_path):
    """Ensure any awk -F, '{print $N}' lines match schema column names."""
    if not schema_path: return ["WARN no schema for " + str(csv_path)]
    schema = json.loads(schema_path.read_text())
    col_by_idx = {c["index"]: c["name"] for c in schema["columns"]}
    errors = []
    # Find bash assignments like VAR=$(echo "$LINE" | awk -F, '{print $N}')
    pattern = r"(\w+)=\$\(\s*echo\s+\"\$LINE\"\s*\|\s*awk\s+-F,\s+'\{print\s+\$(\d+)\}'\s*\)"
    for var, idx in re.findall(pattern, sbatch_text):
        idx = int(idx)
        expected_col = col_by_idx.get(idx, "?")
        var_lower = var.lower()
        # Rough match: SMI→smiles, CID→chembl_id, PV→pchembl
        aliases = {"smi":"smiles","cid":"chembl_id","pv":"pchembl",
                   "rank":"rank","assay":"assay_type","units":"standard_units",
                   "value":"standard_value","type":"standard_type"}
        expected_alias = aliases.get(var_lower, var_lower)
        if expected_alias not in expected_col.lower() and expected_col.lower() not in expected_alias:
            errors.append(
                f"SCHEMA MISMATCH: bash var {var!r} assigned column {idx} "
                f"({expected_col!r} per {schema_path.name}) — expected column named {expected_alias!r}. "
                f"This is the Apr 18 bug class. See cheaha-hpc/SKILL.md Rule 7.")
    return errors

def check_rules(sbatch_text):
    errors = []
    for p in REQUIRED_PRAGMAS:
        if p not in sbatch_text:
            errors.append(f"RULE 2 VIOLATION: missing {p}")
    # Rule 6
    if "#SBATCH --array" in sbatch_text and "%a" not in sbatch_text:
        errors.append("RULE 6 VIOLATION: array job but --output missing %a (collisions)")
    # Rule 1 guard
    if re.search(r"^\s*(python|vina|obabel)\s", sbatch_text, re.M):
        # Only inside a script that has #SBATCH headers — but if run as raw
        # shell this would be head-node abuse. Fine inside sbatch.
        pass
    return errors

def dry_run(sbatch_path, csv_path):
    """Execute just the ligand-prep block on the FIRST row, locally."""
    text = Path(sbatch_path).read_text()
    # Extract the python ligand-prep block
    m = re.search(r"python\s+-\s+\"[^\"]+\"\s+\"[^\"]+\"\s+\"\$SLURM_ARRAY_TASK_ID\"\s+<<PY\n(.+?)\nPY", text, re.DOTALL)
    if not m:
        return ["WARN dry-run could not extract python block"]
    py_block = m.group(1)
    # Set the smi/cid vars from row 1 of CSV
    lines = Path(csv_path).read_text().splitlines()
    if len(lines) < 2: return ["dry-run: CSV has no data rows"]
    row1 = lines[1].split(",")
    if len(row1) < 4: return ["dry-run: row 1 has <4 columns"]
    # From schema we know SMI=col3, CID=col4
    smi, cid, aid = row1[2], row1[3], "0"
    proc = subprocess.run(
        ["/Users/jakeclaw/.hermes-venv/bin/python", "-c", py_block],
        input=None, capture_output=True, text=True, timeout=30,
        env={"__dummy":"1"}, cwd="/Users/jakeclaw/.openclaw/workspace")
    # Re-run with argv
    proc = subprocess.run(
        ["/Users/jakeclaw/.hermes-venv/bin/python", "-", smi, cid, aid],
        input=py_block, capture_output=True, text=True, timeout=30,
        cwd="/tmp")
    if proc.returncode != 0:
        return [f"DRY-RUN FAILED rc={proc.returncode}: {proc.stderr[:300]}"]
    return [f"dry-run OK: {proc.stdout.strip()[:200]}"]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("sbatch")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    text = Path(args.sbatch).read_text()
    errors, warnings = [], []
    errors += check_rules(text)
    for csv_path, schema_path in find_schemas(text):
        errors += check_awk_columns(text, csv_path, schema_path)
    if args.dry_run:
        # Pick the first CSV
        schemas = find_schemas(text)
        if schemas:
            result = dry_run(args.sbatch, schemas[0][0])
            for r in result:
                if r.startswith("DRY-RUN FAILED"): errors.append(r)
                else: warnings.append(r)

    out = {"sbatch": args.sbatch, "errors": errors, "warnings": warnings,
           "verdict": "REJECT" if errors else "OK"}
    print(json.dumps(out, indent=2))
    sys.exit(3 if any("SCHEMA" in e for e in errors)
             else 2 if errors else 0)

if __name__ == "__main__":
    main()
