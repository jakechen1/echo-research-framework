#!/usr/bin/env python
"""Extract ChEMBL bioactives (pchembl >= 5, target != CHEMBL2311243 = PHGDH).

Optimized: PRAGMA mmap_size + 1 GiB cache + reorder-from-small (target_dictionary
~15K rows) -> assays -> activities -> compound_structures. Materialize molregno
subset to a TEMP table first; second pass streams compound SMILES filtered by
the temp table. Python-side dedup with progress every 50K rows.
"""
import sqlite3
import sys
import time

PHGDH_TARGET_CHEMBL_ID = "CHEMBL2311243"


def main(db_path: str, out_path: str) -> None:
    con = sqlite3.connect(db_path)
    con.execute("PRAGMA cache_size = -1048576")     # 1 GiB
    con.execute("PRAGMA mmap_size = 30000000000")    # 30 GB
    con.execute("PRAGMA temp_store = MEMORY")
    con.execute("PRAGMA synchronous = OFF")
    con.execute("PRAGMA journal_mode = OFF")
    cur = con.cursor()

    t0 = time.time()
    print("[sql] step 1: build mol_active temp table (drive from target_dictionary)", flush=True)
    cur.execute(
        f"""
        CREATE TEMP TABLE mol_active AS
        SELECT DISTINCT a.molregno
        FROM target_dictionary td
        JOIN assays asy ON asy.tid = td.tid
        JOIN activities a ON a.assay_id = asy.assay_id
        WHERE td.chembl_id != '{PHGDH_TARGET_CHEMBL_ID}'
          AND a.pchembl_value IS NOT NULL
          AND a.pchembl_value >= 5.0
        """
    )
    con.commit()
    n_mol = cur.execute("SELECT COUNT(*) FROM mol_active").fetchone()[0]
    print(f"[sql] step 1 done: {n_mol} unique bioactive molregnos in {time.time()-t0:.1f}s", flush=True)

    t0 = time.time()
    sql2 = """
        SELECT cs.canonical_smiles
        FROM mol_active m
        JOIN compound_structures cs ON cs.molregno = m.molregno
        WHERE cs.canonical_smiles IS NOT NULL
          AND length(cs.canonical_smiles) BETWEEN 5 AND 200
    """
    seen: set[str] = set()
    n = 0
    with open(out_path, "w") as f:
        for (val,) in cur.execute(sql2):
            if val and "." not in val and val not in seen:
                seen.add(val)
                f.write(val + "\n")
                n += 1
                if n % 50000 == 0:
                    print(f"[sql] step 2: {n} unique rows written...", flush=True)
                    f.flush()
    print(f"[sql] wrote {n} unique bioactive SMILES to {out_path} in {time.time()-t0:.1f}s", flush=True)
    con.close()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
