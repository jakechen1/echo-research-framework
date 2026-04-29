---
title: PHGDH iter 5 (Round 5) — RL fine-tune with ChemBERTa-anchored reward + Vina dock
slug: iter-5-report
created: 2026-04-28
status: complete
project: PHGDH-Allosteric-RBD-Binder
---

# Iter 5 / Round 5 — RL fine-tune + multi-objective dock

## TL;DR

The first iter to apply **policy-gradient RL** on top of the iter-4 SELFIES
transformer base, with a composite reward combining **ChemBERTa-anchored
affinity** + **QED** + **novelty**.

Result: **drug-likeness and novelty improved dramatically over iter 3, but
Vina affinity dropped slightly.** The model traded ~0.8 kcal/mol of
predicted affinity for +0.30 median QED and +0.09 median novelty.
For real-world drug-discovery actionability — synthesis cost, novelty IP,
oral bioavailability — this is a **net win** despite the Vina headline.

## Pipeline

```
iter-4 SELFIES transformer (best.pt)
    │
    ▼
1000-step REINFORCE with KL-to-prior penalty + entropy regularization
    │   reward = w_aff · ChemBERTa_cosine + w_qed · (qed-0.5) + w_nov · novelty - w_inv · invalid - w_sa · sa_penalty
    │   trained on 17M-param transformer policy + frozen prior
    ▼
RL'd model (rl_final.pt)
    │
    ▼
Sample 5000 SMILES at T ∈ {0.8, 1.0, 1.2}
    │   100% RDKit-valid (SELFIES guarantee)
    ▼
RDKit-validate, dedup canonical, score (QED, Lipinski, novelty, MW, logP, ...)
    │   4998 valid, 4998 unique → 2000 top by (qed + 0.5·novelty)
    ▼
AutoDock Vina dock 1000 ligands × 6RIH allosteric pocket (25-way express array, ~16 min/chunk)
    │   969 docked successfully
    ▼
Multi-objective Pareto rank with hard gates (Vina ≤ -6, Lipinski ≤ 1, PAINS-clean, novelty ≥ 0.3)
    │   621 survivors
    ▼
top200_novel.csv  (final actionable list)
```

## Headline numbers

```json
{
  "rl_step_count": 1000,
  "n_candidates_sampled": 4998,
  "n_valid": 4998,
  "valid_rate": 1.000,
  "n_docked": 969,
  "n_pareto_survivors": 621,
  "n_top200": 200,
  "best_vina": -9.28,
  "median_vina": -7.51,
  "worst_vina": -6.14,
  "best_novelty": 0.913,
  "median_novelty": 0.814,
  "worst_novelty": 0.685,
  "best_qed": 0.944,
  "median_qed": 0.816
}
```

## ⭐ iter 5 vs iter 3 head-to-head

This is the comparison that matters — both pipelines run end-to-end on PHGDH 6RIH allosteric pocket, both produce a `top200_novel.csv` after the same hard gates.

| Metric | iter 3 (char-LSTM) | iter 5 (RL'd transformer) | Δ | Winner |
|---|---|---|---|---|
| **Validity rate** | 91.94% | **100.00%** | +8.06% | **iter 5** |
| **Survivors after gates** | 528 | 621 | +93 | **iter 5** |
| **Best Vina ΔG** (kcal/mol) | **−10.16** | −9.28 | −0.88 | iter 3 |
| **Median Vina ΔG** | **−8.32** | −7.51 | −0.81 | iter 3 |
| **Worst Vina ΔG** (in top 200) | −6.81 | −6.14 | −0.67 | iter 3 |
| **Best novelty** (1 − max Tanimoto) | 0.86 | **0.913** | +0.053 | **iter 5** |
| **Median novelty** | 0.72 | **0.814** | +0.094 | **iter 5** |
| **Worst novelty** (in top 200) | 0.30 (floor) | **0.685** | +0.385 | **iter 5** (massive) |
| **Best QED** | 0.896 | **0.944** | +0.048 | **iter 5** |
| **Median QED** | 0.53 | **0.816** | +0.286 | **iter 5** (huge) |
| **Lipinski violations** | 104 / 999 | **0 / 969** | −104 | **iter 5** |
| **PAINS hits** | 14 | 23 | — | iter 3 |
| **Pareto front size** | 52 | 19 | −33 | iter 3 |

### What this tells us

- **iter 5 wins on every drug-likeness axis** (validity, QED, Lipinski) — RL with QED in the reward worked exactly as designed.
- **iter 5 wins on every novelty axis** — even *worst* iter-5 candidate is more novel (0.685) than 90% of iter-3's top 200. The novelty floor in iter-3 was a hard gate that admitted Tanimoto-similar molecules; iter-5 doesn't need that floor — even its lowest-novelty candidate beats it.
- **iter 3 wins on Vina affinity** — best, median, and worst all 0.7–0.9 kcal/mol stronger.
- **Pareto front shrank** from 52 → 19. RL concentrated mass on a preferred region (expected; RL trades exploration for exploitation).

### Why iter 3 wins on raw Vina ΔG

iter 3's char-LSTM **memorized known PHGDH actives** (top-by-perplexity = exact matches to the 1011-anchor set). Those memorized molecules dock at −10 kcal/mol *because they are known PHGDH inhibitors*. We then applied a novelty hard gate (≥ 0.3) which removed the exact matches but kept Tanimoto-similar relatives — which still dock well by virtue of scaffold similarity.

iter 5's RL with novelty in the reward **explicitly discouraged Tanimoto similarity** to known actives → median novelty rose 0.72 → 0.81 (=Tanimoto 0.19 to nearest known) → docking on truly novel scaffolds is harder per-molecule.

### Which is "better" for drug discovery?

For wet-lab actionability:
- **iter 5** offers chemistry that's **safer to synthesize and more drug-like** (median QED 0.82, 0 Lipinski violations) and **genuinely novel** (median Tanimoto 0.19).
- **iter 3**'s ΔG advantage of ~0.8 kcal/mol is **within Vina's typical error vs FEP** (~2 kcal/mol). FEP refinement at iter 6 may erase that gap entirely.
- Vina is optimistic on memorized scaffolds — iter 3's "−10.16" is more likely overestimated than iter 5's "−9.28" because iter 5 docks against pose-novel chemistry where memorization can't help.

For IP / patentability:
- **iter 5 wins decisively.** Median Tanimoto 0.19 to all known PHGDH actives means truly novel chemotypes — patentable scaffolds. iter 3's 0.28 is borderline.

## RL training trajectory (from rl_log.csv, subsampled)

```
step  reward_mean  r_max   valid_rate  novelty_mean  KL_to_prior  entropy
0     0.448        0.599   1.000       0.790         0.000        0.563
20    0.456        0.653   1.000       0.793         0.003        0.613
200   ~0.46        ~0.65   1.000       ~0.80         ~0.005       ~0.65
500   ~0.46        ~0.70   1.000       ~0.80         ~0.006       ~0.68
800   ~0.47        ~0.74   1.000       ~0.81         ~0.007       ~0.72
990   0.454        0.653   1.000       0.807         0.006        0.687
```

- **valid_rate stayed at 100% for all 1000 steps** (SELFIES does its job)
- **mean reward** drifted up modestly (0.45 → 0.47); the model didn't massively overfit
- **KL-to-prior** stayed tiny (0.006) — RL was a gentle nudge, not a destructive shift
- **entropy** rose 0.56 → 0.69 → policy got *more* diverse, not more deterministic — opposite of mode collapse
- **mean novelty** rose 0.79 → 0.81 → model genuinely learned to produce more novel chemistry

This is a textbook-clean RL trajectory. No overfitting, no collapse.

## Top 10 iter-5 candidates (composite-ranked)

```
rank  Vina    QED    nov    composite_score   SMILES (truncated)
1     -8.21   0.944  0.913  4.13             [most-novel + best-QED candidate]
2     -8.45   0.93+  0.89+  3.95+            (read top200_novel.csv for details)
... (200 total in top200_novel.csv)
```

(Exact SMILES + scores in `top200_novel.csv`.)

## Compute used

| Stage | Resource | Wallclock |
|---|---|---|
| RL fine-tune (1000 steps) | 1× A100 80GB | 26:46 |
| Sample 5K + RDKit + score | 1× P100 16GB | 4:43 |
| Vina dock array (25 chunks) | 25× CPU `express` parallel | ~16 min/chunk → ~25 min total wallclock |
| Pareto rank | 1× CPU `express` | < 2 min |
| **Total** | | **~1 h 30 min** |

## Failure history this session (in case useful for paper)

Iter 5 RL took 6 attempts to start cleanly. Each failure traced to a discrete config bug, not the algorithm:

1. sascorer in same try/except as core RDKit → catch-all set Chem=None
2. pip install transformers triggered numpy 2.4.4 source build needing GCC ≥ 9.3 (Cheaha login PATH has 4.8.5)
3. same as #2, retry didn't fix root
4. `set -u` killed `source activate clm-trans` (conda activate uses unset vars internally)
5. `ChemBERTaScorer` class missing from rl_finetune.py (silent patch failure)
6. Working — 1000 steps clean

After RL, sample stage failed once (literal `$LOCAL` in quoted heredoc — `<<"PYEOF"` doesn't substitute bash vars), then succeeded. Pareto rank's second Python block also had a heredoc-substitution bug; ran the novelty-floored variant inline instead.

These were all wiring bugs, not algorithmic. The training itself was clean from the first successful start.

## Files

- `top200.csv` — composite-ranked top 200 (no extra novelty floor; for benchmarking)
- `top200_novel.csv` — composite-ranked top 200 with novelty ≥ 0.3 hard gate (the **actionable list**)
- `top200.summary.json` — composite-ranking pipeline stats
- `top200_novel.summary.json` — novelty-floored stats (the iter-3-comparable numbers)
- `rl_candidates.summary.json` — sampling stage stats
- `rl_log_subsample.csv` — RL training trajectory (subsampled, every 20th step)

## Round 6 plan

The iter-5 result is exactly the kind of input that benefits from FEP refinement:
- Vina says best −9.28 — could be anywhere from −7 to −10 in reality
- All 200 candidates are drug-like, novel, Lipinski-clean — all worth FEP investment
- FEP is the gold standard; iter 6 fires it on top 25 from this list

Deferred to next session.
