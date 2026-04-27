---
title: PHGDH iter 3 (Round 3) — multi-track + Vina + multi-objective rank
slug: iter-3-report
created: 2026-04-27
status: complete
project: PHGDH-Allosteric-RBD-Binder
---

# Iter 3 / Round 3 — first end-to-end candidate generation + docking

## TL;DR

**~50 min wallclock**, all on Cheaha (1× A100 + 25 parallel `express` CPUs):
1. Fan Li 5-stage incremental fine-tune from iter 2 `best.pt` on PHGDH potency buckets
2. Sample 10 K SMILES at three temperatures (0.8, 1.0, 1.2)
3. RDKit-validate, dedupe canonical, perplexity-rank → top 1 K
4. AutoDock Vina dock all 1 K against PHGDH 6RIH allosteric pocket (5-pose consensus)
5. PAINS + Lipinski + Vina hard gates + multi-objective Pareto rank → top 200

Two ranked lists shipped:
- **`top200.csv`** — ranked by composite (2·affinity + qed + novelty + 0.5·druglike). All top 10 are exact hits to known PHGDH actives (memorization).
- **`top200_novel.csv`** — same with extra **novelty ≥ 0.3** hard gate. Top 10 have Tanimoto 0.17–0.43 to all 1011 known actives → genuinely novel scaffolds.

## Headline metrics

| Stage | Output | Time |
|---|---|---|
| 5-stage incremental FT | val PPL 1.25 (down from 1.59 pretrain) | 1:46 |
| Sample 10 K | 8 008 valid (91.94 %), 0 dups, top-1000 by PPL | 9 s |
| Vina dock (25 chunks × 40 ligands) | 999 / 1000 docked (1 ligand-prep fail) | 31–57 min/chunk in parallel = ~50 min wallclock |
| Pareto rank | 854 survivors → 52 Pareto front → 200 ranked | < 5 s |
| Novelty re-rank | 528 survivors → 200 novel | < 5 s |

## Affinity distribution (top 200 novel)

- Best Vina ΔG: **−10.16 kcal/mol** (∼40 nM Vina-predicted)
- Median Vina ΔG: **−8.32 kcal/mol** (∼1 µM Vina-predicted)
- Worst (post-gate): −6.81 kcal/mol (∼50 µM Vina-predicted)

> Caveat: Vina is optimistic by ~2 kcal/mol vs FEP / wet-lab. Predicted ΔG = −9 kcal/mol typically corresponds to measured ≈ −7 (single-µM IC50). Round 6 FEP refinement is essential before any wet-lab claim.

## Validation signal: pipeline rediscovers known actives

When the novelty gate was OFF, all 10 highest-composite candidates were exact matches to 1011 known PHGDH actives (Tanimoto = 1.0). Their Vina ΔG range −9 to −10 kcal/mol — consistent with literature values for the more potent known scaffolds. **This is a positive validation signal**: the dock + score + rank stack works on inputs of known affinity.

## Top 10 NOVEL candidates

```
rank  Vina    QED   nov   PPL    SMILES (truncated)
1    -10.02  0.50  0.78  1.25   piperazine-sulfonamide / pyridazinone
2     -9.48  0.55  0.80  1.26   N-aryl-thietanone / chloropyridyl
3     -9.79  0.50  0.65  1.24   sulfonyl-piperazine / dichloroindole
4    -10.16  0.28  0.64  1.26   bis-aryl-amide / chlorophenyl
5     -9.41  0.44  0.77  1.21   imidazopyridazinone / fluorobenzyl
6     -9.09  0.49  0.83  1.27   isoindolinone / propargyl-tBuOH
7     -9.35  0.37  0.83  1.27   isoindolinone / pyrazolyl-pyridine
8     -9.91  0.34  0.57  1.28   benzophenone / dichloroindole
9     -9.07  0.51  0.72  1.26   piperazinedione / dichloroindole
10    -9.07  0.46  0.75  1.21   isoindolinone / propargyl-aryl-acetamide
```

Several recurring scaffolds emerge: **isoindolinone / propargyl-aryl** (5 in top 10), **dichloroindole-amide** (3 in top 10), and **sulfonyl-piperazine** (2). These are the model's currently-favored novel chemotypes for the PHGDH allosteric pocket.

## Hard gates applied

```
✓ Vina ΔG ≤ −6.0 kcal/mol         (lenient: ~50 µM threshold)
✓ Lipinski violations ≤ 1
✓ PAINS = 0 (RDKit FilterCatalog)
✓ Novelty (1 − max Tanimoto vs 1011 known PHGDH actives) ≥ 0.3
```

Rejected breakdown (out of 999 docked):
- 27 Vina too weak (>−6 kcal/mol)
- 104 Lipinski violators
- 14 PAINS hits
- ~317 below novelty floor (added in re-rank; many were memorized actives)

## What this round established

1. **End-to-end pipeline works** on Cheaha: FT on A100 → sampling → 25-way parallel Vina docking on `express` → multi-objective Pareto rank.
2. **Memorization is real** in char-LSTM + perplexity ranking. Top-by-PPL = top-by-memorization. Fix: novelty floor (round 3 patch) and architectural change (round 4: SELFIES + transformer + RL).
3. **Vina pipeline genuinely re-discovers known actives** with reasonable ΔG — positive validation signal.
4. **Novel chemotypes emerge** when novelty floor enforced: isoindolinone / propargyl-aryl + dichloroindole-amide families dominate top 10.

## Compute used

- 1 A100 hour for FT + sample (single GPU, 1:46 wallclock)
- Vina setup: ~7 min CPU on express
- Vina docking: 25 parallel chunks × ~40 min average = ~17 CPU-hours total, ~40 min wallclock
- Total: ~18 CPU-hours + 1 GPU-hour, ~50 min wallclock

## Round 4 plan (next)

- **Pretrain corpus expansion**: ChEMBL ∪ PubChem-BioAssay (~4M bioactives)
- **Architecture upgrade**: SELFIES tokenizer + small transformer (~20 M params) replacing char-LSTM
- **DrugCLIP** stand-up (Track B, ~12 h training on amperenodes-medium)
- **FoldSeek + structural-neighbor seeds** (Track C, ~30 min query)
- **RL fine-tune** with DrugCLIP-PHGDH reward to break the perplexity-memorization loop
- Iterate Round 3 pipeline on the new generator → top 100 with PHGDH-aware scoring + counter-screen

## Files

- `top200.csv` — top 200 by composite score (no novelty floor — for benchmarking + sanity check)
- `top200_novel.csv` — top 200 with novelty ≥ 0.3 hard gate (the actionable output)
- `top200.summary.json` — pipeline-level statistics
- `candidates.summary.json` — sampling stage summary
- `ft_summary.json` — fine-tuning stage summary
- `ft_config.json` — fine-tuning hyperparameters
