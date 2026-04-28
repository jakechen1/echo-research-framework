#!/usr/bin/env python
"""Round 3 multi-objective Pareto rank.

Combines:
  - candidates.csv (perplexity, QED, Lipinski, novelty, etc. from sample_lstm.py)
  - dock_results/chunk_*.csv (Vina ΔG appended by vina_dock_chunk.py)

Applies:
  - Soft gates (Round 3 lenient; Round 4+ tighten):
      vina_score ≤ -6.0 kcal/mol  (weaker than ~50 µM affinity rejected)
      lipinski_violations ≤ 1
      PAINS = 0 (RDKit FilterCatalog)
      perplexity ≤ p95 of pool (drops the outliers)
  - Composite z-scored ranking on:
      affinity = -vina_score  (more negative ΔG = better)
      qed
      novelty (1 - max_tanimoto_known)
      drug-likeness penalty (lipinski_violations, sa-proxy from logp range)
  - Pareto-front filter on (affinity, qed, novelty)

Usage:
  pareto_rank_round3.py \
    --candidates runs/round3_<jobid>/candidates.csv \
    --dock-glob 'runs/round3_<jobid>/dock_results/chunk_*.csv' \
    --out runs/round3_<jobid>/top200.csv \
    --top-k 200
"""
from __future__ import annotations
import argparse, csv, glob, json, math, statistics
from pathlib import Path

import numpy as np
from rdkit import Chem
from rdkit.Chem import FilterCatalog
from rdkit import RDLogger
RDLogger.DisableLog("rdApp.*")


def safe_float(v, default=None):
    try:
        return float(v) if v not in ("", None) else default
    except (ValueError, TypeError):
        return default


def pains_check(smi: str) -> int:
    """Return number of PAINS hits (0 = clean)."""
    mol = Chem.MolFromSmiles(smi)
    if mol is None:
        return -1  # invalid
    params = FilterCatalog.FilterCatalogParams()
    params.AddCatalog(FilterCatalog.FilterCatalogParams.FilterCatalogs.PAINS)
    catalog = FilterCatalog.FilterCatalog(params)
    matches = catalog.GetMatches(mol)
    return len(matches)


def zscore(vals):
    arr = np.array(vals, dtype=float)
    arr = arr[~np.isnan(arr)]
    if arr.size == 0:
        return [0.0] * len(vals)
    mu = float(arr.mean()); sd = float(arr.std() if arr.std() > 1e-9 else 1.0)
    return [((v - mu) / sd) if v is not None and not (isinstance(v, float) and math.isnan(v)) else 0.0
            for v in vals]


def is_pareto(points: np.ndarray) -> np.ndarray:
    """Return boolean mask: True = on Pareto front (higher = better on all dims)."""
    n = len(points)
    on_front = np.ones(n, dtype=bool)
    for i in range(n):
        if not on_front[i]:
            continue
        # Dominated if exists j with all dims >= and at least one >
        dominators = (points >= points[i]).all(axis=1) & (points > points[i]).any(axis=1)
        if dominators.any():
            on_front[i] = False
    return on_front


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", required=True, type=Path)
    ap.add_argument("--dock-glob", required=True, help="glob for dock_results/chunk_*.csv")
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--top-k", type=int, default=200)
    ap.add_argument("--vina-gate", type=float, default=-6.0,
                    help="reject candidates with vina_score > this (default -6.0 = ~50 µM)")
    ap.add_argument("--lipinski-gate", type=int, default=1,
                    help="reject if lipinski_violations > this (default 1)")
    ap.add_argument("--require-pains-clean", action="store_true", default=True,
                    help="reject candidates with any PAINS hit")
    ap.add_argument("--w-affinity", type=float, default=2.0)
    ap.add_argument("--w-qed", type=float, default=1.0)
    ap.add_argument("--w-novelty", type=float, default=1.0)
    ap.add_argument("--w-druglike", type=float, default=0.5)
    args = ap.parse_args()

    args.out.parent.mkdir(parents=True, exist_ok=True)

    # 1) Load candidates.csv (the sampled pool)
    cand_rows = []
    with args.candidates.open() as f:
        for row in csv.DictReader(f):
            cand_rows.append(row)
    print(f"[pareto] loaded {len(cand_rows)} candidates from {args.candidates}")

    # 2) Load all dock chunks
    dock_paths = sorted(glob.glob(args.dock_glob))
    print(f"[pareto] loading {len(dock_paths)} dock chunks")
    dock_by_smi = {}
    for p in dock_paths:
        with open(p) as f:
            for row in csv.DictReader(f):
                smi = row.get("smiles_canonical")
                if not smi:
                    continue
                vs = safe_float(row.get("vina_score"))
                if vs is None:
                    continue
                # keep best (most negative) score if duplicate
                prev = dock_by_smi.get(smi)
                if prev is None or vs < prev:
                    dock_by_smi[smi] = vs
    print(f"[pareto] dock results for {len(dock_by_smi)} unique SMILES")

    # 3) Merge: candidates left-joined with vina_score
    merged = []
    for r in cand_rows:
        smi = r.get("smiles_canonical")
        vs = dock_by_smi.get(smi)
        merged.append({**r, "vina_score": vs})
    docked = [r for r in merged if r["vina_score"] is not None]
    print(f"[pareto] merged: {len(merged)} total, {len(docked)} with vina_score")

    # 4) PAINS filter on docked subset
    pains_count = 0
    for r in docked:
        n_pains = pains_check(r["smiles_canonical"])
        r["pains_hits"] = n_pains
        if n_pains > 0:
            pains_count += 1
    print(f"[pareto] PAINS-flagged: {pains_count}/{len(docked)}")

    # 5) Apply soft hard-gates (Round 3 lenient)
    survivors = []
    rejection_reasons = {"vina_too_weak": 0, "lipinski_violation": 0, "pains": 0,
                         "missing_score": 0}
    for r in docked:
        vs = r["vina_score"]
        liv = int(safe_float(r.get("lipinski_violations"), 0) or 0)
        pains = r.get("pains_hits", 0)
        if vs is None:
            rejection_reasons["missing_score"] += 1; continue
        if vs > args.vina_gate:
            rejection_reasons["vina_too_weak"] += 1; continue
        if liv > args.lipinski_gate:
            rejection_reasons["lipinski_violation"] += 1; continue
        if args.require_pains_clean and pains > 0:
            rejection_reasons["pains"] += 1; continue
        survivors.append(r)
    print(f"[pareto] gated -> {len(survivors)} survivors")
    print(f"[pareto] rejections: {rejection_reasons}")

    if not survivors:
        print("[pareto] WARN: no survivors; emitting empty output")
        args.out.write_text("smiles_canonical,vina_score,qed,novelty,perplexity,composite_score\n")
        return

    # 6) Composite score (z-normalized, weighted)
    affinity = [-r["vina_score"] for r in survivors]   # higher = better (more negative ΔG)
    qed = [safe_float(r.get("qed"), 0.0) for r in survivors]
    novelty = [safe_float(r.get("novelty"), 0.5) for r in survivors]
    # drug-likeness penalty: more violations = worse
    druglike = [-int(safe_float(r.get("lipinski_violations"), 0) or 0) for r in survivors]

    z_aff = zscore(affinity)
    z_qed = zscore(qed)
    z_nov = zscore(novelty)
    z_dl = zscore(druglike)
    for i, r in enumerate(survivors):
        r["z_affinity"] = z_aff[i]
        r["z_qed"] = z_qed[i]
        r["z_novelty"] = z_nov[i]
        r["z_druglike"] = z_dl[i]
        r["composite_score"] = (args.w_affinity * z_aff[i]
                                + args.w_qed * z_qed[i]
                                + args.w_novelty * z_nov[i]
                                + args.w_druglike * z_dl[i])

    # 7) Pareto front on (affinity, qed, novelty)
    pts = np.array([[r["z_affinity"], r["z_qed"], r["z_novelty"]] for r in survivors])
    front_mask = is_pareto(pts)
    for i, r in enumerate(survivors):
        r["on_pareto_front"] = bool(front_mask[i])
    n_front = int(front_mask.sum())
    print(f"[pareto] Pareto front size: {n_front}/{len(survivors)}")

    # 8) Sort by composite score, output top K
    survivors.sort(key=lambda r: r["composite_score"], reverse=True)
    top = survivors[: args.top_k]

    fieldnames = ["smiles_canonical", "smiles_raw", "temperature", "perplexity",
                  "vina_score", "qed", "mw", "logp", "hbd", "hba", "rotbonds", "tpsa",
                  "lipinski_violations", "pains_hits",
                  "max_tanimoto_known", "novelty",
                  "z_affinity", "z_qed", "z_novelty", "z_druglike",
                  "composite_score", "on_pareto_front"]
    with args.out.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(top)
    print(f"[pareto] wrote top {len(top)} -> {args.out}")

    # Summary
    summary = {
        "n_candidates": len(cand_rows),
        "n_docked": len(docked),
        "n_pains_flagged": pains_count,
        "n_survivors_after_gates": len(survivors),
        "n_pareto_front": n_front,
        "top_k_returned": len(top),
        "best_vina": min(r["vina_score"] for r in top),
        "median_vina": statistics.median(r["vina_score"] for r in top),
        "best_qed": max(safe_float(r.get("qed"), 0.0) for r in top),
        "best_novelty": max(safe_float(r.get("novelty"), 0.0) for r in top),
        "rejection_reasons": rejection_reasons,
        "weights": {"affinity": args.w_affinity, "qed": args.w_qed,
                    "novelty": args.w_novelty, "druglike": args.w_druglike},
        "gates": {"vina_gate": args.vina_gate, "lipinski_gate": args.lipinski_gate,
                  "pains_clean": args.require_pains_clean},
    }
    summary_path = args.out.with_suffix(".summary.json")
    summary_path.write_text(json.dumps(summary, indent=2, default=str))
    print(json.dumps(summary, indent=2, default=str))


if __name__ == "__main__":
    main()
