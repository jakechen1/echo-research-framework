#!/usr/bin/env python
"""Vina-dock a chunk of candidates from candidates.csv against a prepared receptor.

Usage:
  vina_dock_chunk.py \
    --candidates candidates.csv \
    --receptor receptors/6rih_chainA_protein.pdbqt \
    --pocket-config receptors/pocket_config.json \
    --out runs/round3_<jobid>/dock_results/chunk_<task_id>.csv \
    --task-id $SLURM_ARRAY_TASK_ID \
    --chunk-size 40

Reads rows [task_id*chunk_size : (task_id+1)*chunk_size] from candidates.csv.
For each: SMILES -> 3D embed (RDKit) -> meeko PDBQT -> vina dock -> best ΔG.
Writes per-chunk CSV.
"""
from __future__ import annotations
import argparse, csv, json, sys, time, traceback
from pathlib import Path

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import RDLogger
RDLogger.DisableLog("rdApp.*")

from meeko import MoleculePreparation, PDBQTWriterLegacy
from vina import Vina


def smiles_to_pdbqt_string(smi: str, n_confs: int = 1) -> str | None:
    """Embed SMILES → 3D (single conf) → PDBQT string via meeko."""
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return None
    mol = Chem.AddHs(mol)
    params = AllChem.ETKDGv3()
    params.randomSeed = 0xf00d
    cid = AllChem.EmbedMolecule(mol, params=params)
    if cid < 0:
        # try a relaxed embed
        cid = AllChem.EmbedMolecule(mol, useRandomCoords=True)
        if cid < 0:
            return None
    try:
        AllChem.MMFFOptimizeMolecule(mol, maxIters=200)
    except Exception:
        pass
    prep = MoleculePreparation()
    try:
        mol_setups = prep.prepare(mol)
    except Exception:
        return None
    if not mol_setups:
        return None
    # Take first conformer / setup
    setup = mol_setups[0]
    try:
        pdbqt_string, is_ok, error_msg = PDBQTWriterLegacy.write_string(setup)
        if not is_ok:
            return None
        return pdbqt_string
    except Exception:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", required=True, type=Path)
    ap.add_argument("--receptor", required=True, type=Path, help="PDBQT receptor")
    ap.add_argument("--pocket-config", required=True, type=Path, help="JSON with pocket_center + pocket_box_size")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--task-id", type=int, required=True)
    ap.add_argument("--chunk-size", type=int, default=40)
    ap.add_argument("--exhaustiveness", type=int, default=8)
    ap.add_argument("--n-poses", type=int, default=5)
    ap.add_argument("--cpu", type=int, default=2)
    args = ap.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)

    # Load candidates.csv (must have smiles_canonical column)
    rows = []
    with args.candidates.open() as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    print(f"[dock] candidates total={len(rows)}", flush=True)

    start = args.task_id * args.chunk_size
    end = min(start + args.chunk_size, len(rows))
    chunk = rows[start:end]
    print(f"[dock] task_id={args.task_id} chunk=[{start}:{end}] n={len(chunk)}", flush=True)
    if not chunk:
        args.out.write_text("smiles_canonical,vina_score,best_pose,error\n")
        return

    # Pocket config
    cfg = json.loads(args.pocket_config.read_text())
    center = cfg["pocket_center"]
    box = cfg["pocket_box_size"]
    print(f"[dock] receptor={args.receptor} center={center} box={box}", flush=True)

    # Init Vina
    v = Vina(sf_name="vina", cpu=args.cpu, verbosity=0)
    v.set_receptor(str(args.receptor))
    v.compute_vina_maps(center=center, box_size=box)

    out_rows = []
    for idx, row in enumerate(chunk):
        smi = row.get("smiles_canonical") or row.get("smiles_raw") or ""
        if not smi:
            out_rows.append({**row, "vina_score": "", "best_pose": "", "error": "empty smiles"})
            continue
        t0 = time.time()
        try:
            pdbqt = smiles_to_pdbqt_string(smi)
            if not pdbqt:
                out_rows.append({**row, "vina_score": "", "best_pose": "", "error": "ligand prep failed"})
                continue
            v.set_ligand_from_string(pdbqt)
            v.dock(exhaustiveness=args.exhaustiveness, n_poses=args.n_poses)
            energies = v.energies(n_poses=args.n_poses)
            # energies is array shape (n_poses, 9?); first column is total energy in kcal/mol
            best = float(energies[0][0]) if len(energies) else None
            out_rows.append({
                **row,
                "vina_score": f"{best:.3f}" if best is not None else "",
                "best_pose": "1",
                "error": "",
            })
            if idx < 3 or idx % 10 == 0:
                print(f"[dock] {start+idx}/{len(rows)}: ΔG={best:.2f} kcal/mol ({time.time()-t0:.1f}s) {smi[:60]}", flush=True)
        except Exception as e:
            out_rows.append({**row, "vina_score": "", "best_pose": "", "error": str(e)[:120]})
            print(f"[dock] {start+idx}: ERROR {e}", flush=True)

    # Write output CSV (preserve original columns + new ones)
    if out_rows:
        # union of all keys
        keys = list(out_rows[0].keys())
        for r in out_rows[1:]:
            for k in r.keys():
                if k not in keys:
                    keys.append(k)
        with args.out.open("w", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys, extrasaction="ignore")
            w.writeheader()
            w.writerows(out_rows)
    print(f"[dock] wrote {len(out_rows)} rows -> {args.out}", flush=True)


if __name__ == "__main__":
    main()
