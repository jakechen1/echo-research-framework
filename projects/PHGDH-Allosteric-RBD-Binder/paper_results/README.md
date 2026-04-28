---
title: PHGDH allosteric binder discovery — paper-results manifest
project: PHGDH-Allosteric-RBD-Binder
created: 2026-04-27
status: in-progress (iter 4 pretrain underway)
---

# PHGDH allosteric binder discovery — paper-results manifest

This folder collects the artifacts that would feed a publication: trained
models, ranked candidate lists, structural-neighbor data, counter-receptor
configs, and corpus statistics. Heavyweight files (model checkpoints
≥ 50 MB, full TSV dumps) live on Cheaha; this folder holds the small
deliverables and pointers.

## Layout

```
paper_results/
├── README.md                          ← this file
├── methods/                           ← reproducible methodology
│   ├── data-prep.md
│   ├── models.md
│   ├── docking.md
│   └── scoring.md
├── iter-2-pretrain/                   ← iter 2 char-LSTM pretrain
│   ├── config.json
│   ├── loss.csv
│   ├── vocab.json
│   └── checkpoint_location.txt
├── iter-3-round3/                     ← iter 3 first generation+dock cycle
│   ├── top200.csv                     ← ranked by composite (memorized hits at top — sanity)
│   ├── top200_novel.csv               ← novelty-floored, the actionable list
│   ├── top200.summary.json
│   ├── candidates.summary.json
│   ├── ft_summary.json
│   └── ft_config.json
├── iter-4-pretrain/                   ← iter 4 SELFIES + transformer (in progress)
│   └── (loss.csv, config.json, vocab.json populated when training completes)
├── structural-neighbors/              ← Track C: FoldSeek 6RIH query
│   ├── 6rih_top50.tsv                 ← top 50 PDB structural matches
│   └── all_hits.m8                    ← raw FoldSeek output
├── counter-receptors/                 ← Track B precursor: selectivity counter-receptors
│   ├── phgdh_6rih.json
│   ├── psat1_3e77.json
│   └── psph_1l7m.json
├── corpus-stats/
│   └── README.md                      ← source counts + filter rules
├── figures/                           ← reserved for future renderings
│   └── (empty — to populate after iter 4/5)
└── next-steps.md                      ← what comes after current iteration
```

## Status snapshot

| Iteration | Status | Highlight |
|---|---|---|
| **iter 2** — char-LSTM pretrain | ✅ done (2026-04-27, 41 min A100) | val PPL 1.59 on 1.09 M ChEMBL bioactives |
| **iter 3** — round 3 multi-track + Vina | ✅ done (50 min wall) | 200 novel candidates, best Vina ΔG = −10.16 kcal/mol |
| **iter 4** — SELFIES + transformer pretrain | 🟢 running (race: P100 vs A100) | A100 ep 1/10 val PPL 2.03 |
| **iter 5** — RL fine-tune | 📝 code ready (`rl_finetune.py`) | composite reward: DrugCLIP-PHGDH + QED + novelty |
| **iter 6** — FEP gold-standard validation | ⏳ planned | Top 25 from iter 5 → OpenFE / FEP+ |
| **iter 7** — wet-lab handoff | ⏳ planned | Synthesize / commercial-source 5–15 final compounds |

## Key headline numbers (current)

- Pretrain corpus: 1,091,136 ChEMBL bioactives (pchembl ≥ 5, target ≠ PHGDH/CHEMBL2311243)
- Augmented corpus: 1,672,507 (ChEMBL ∪ BindingDB-202604, deduped) — ready for iter 5+
- iter 2 model: 5.5 M-param 3-layer char-LSTM; final val PPL 1.59
- iter 3 sampling: 9 999 attempts → 8 008 RDKit-valid (91.94 %) → top 1 000 by perplexity
- iter 3 docking: 999 / 1 000 docked vs PHGDH 6RIH allosteric pocket; best ΔG **−10.16 kcal/mol**, median **−8.32**
- iter 3 final novel: 200 candidates with Tanimoto ≤ 0.7 to 1 011 known PHGDH actives
- iter 4 model: 16.97 M-param SELFIES transformer (8 layers × 8 heads × 512 dim × 1024 ffn)

## Reproducibility

Every iter has a `config.json` capturing all hyperparameters and a `loss.csv` of
the training curve. The Cheaha sbatch scripts (`~/jobs/aim4_clm/aim4_*.sbatch`)
are version-controlled in the GitHub repo at
[`projects/PHGDH-Allosteric-RBD-Binder/`](https://github.com/jakechen1/echo-research-framework/tree/main/projects/PHGDH-Allosteric-RBD-Binder).

Major heavyweight checkpoints (~50–70 MB each) stay on Cheaha rather than
GitHub — see each iter's `checkpoint_location.txt` for the path.

## See also

- Strategy: `scaling-drugclip-repositioning-strategy.md` (in `strategy/` on GitHub) — the *why* of each track
- Closed-loop plan: `closed-loop-discovery-plan.md` — round-by-round execution roadmap with hard gates, FEP step, ADMET stack, IP screen
- iter-3 narrative: `iter-3-report.md` — the proof-of-concept run-through
