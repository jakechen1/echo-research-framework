---
title: Next steps after iter 4 pretrain completes
status: planning
---

# Next steps

## Immediate (post-iter-4)

When `runs/round4_pretrain_<jobid>/best.pt` lands (A100 race winner ETA
~23:30 EDT tonight):

1. **Repeat iter 3 pipeline** on the new transformer base:
   - 5-stage incremental FT on `bucket_pv{5..9}.smi` (uses
     `finetune_lstm.py` adapted for transformer, or write `finetune_transformer.py`)
   - Sample 10 K SMILES (validity should be ~100 % from SELFIES)
   - Vina dock against PHGDH 6RIH (reuse `aim4_vina_dock.sbatch`)
   - Counter-Vina against PSAT1 (3E77) + PSPH (1L7M) — receptors already prepared
   - Multi-objective Pareto rank (reuse `pareto_rank_round3.py` + add counter-Vina dim)
2. **Cancel** the slower P100 job (38302357) once A100 emits `best.pt`.

## Short-term (iter 5 — RL fine-tune)

`rl_finetune.py` is ready. Once DrugCLIP / DeepPurpose CPI scorer is working:

1. **Wire DrugCLIP-PHGDH reward** into `RewardFn` — replaces the placeholder
   `--reward-fn drugclip_phgdh`
2. **PPO upgrade** (currently REINFORCE) — clip ratio for stability
3. **Active learning loop**: query MM-GBSA on 50 highest-uncertainty candidates
   each round; retrain DrugCLIP-PHGDH head with MM-GBSA labels → sharper proxy
4. **Matched molecular pair (MMP) extension** around top 20 from RL → ~200
   derivatives → re-rank via the same gates

Expected output: top 50 with MM-GBSA-validated affinity, retrosynthesis-confidence
≥ 0.7 (RAscore + AiZynthFinder), ADMETlab green.

## Medium-term (iter 6 — FEP gold standard)

1. **OpenFE or Schrödinger FEP+** on top 25 vs PHGDH 6RIH → ΔG_FEP
2. **Counter-FEP** on PSAT1 + PSPH → selectivity (≥ 100×)
3. **Toxicity battery**: ProTox 3.0 (61 endpoints) + admetlab 2.0 (119 endpoints)
   + DeepTox/Tox21
4. **IP clearance**: SureChEMBL substructure search on top 25
5. **Hard gates**: ΔG_FEP ≤ −8 kcal/mol, selectivity ≥ 100×, all ADMET green,
   QED ≥ 0.6, SAscore ≤ 4, Tanimoto ≤ 0.5 to known actives, scaffold IP-clean

Compute estimate: ~250 GPU-hours (FEP is the long pole).

## Long-term (iter 7 — wet-lab)

1. Top 5–15 → commercial source check (eMolecules, Mcule, Enamine REAL) or custom
   synthesis quotes
2. **PHGDH biochemical assay** (NADH-coupled or fluorescence) → measured IC50
3. **PSAT1 + PSPH activity assays** → confirmed selectivity
4. **Cell-based viability** on AD-relevant neuronal line (project context appears
   to be Alzheimer's disease, per the Box `phgdh-research/` content) → EC50
5. **hERG patch-clamp** + **microsomal stability** on top 3

## Parallel tracks not yet kicked off

- **Track B (DrugCLIP / DeepPurpose)**: failed thrice (pymoo, lifelines, etc.).
  Plan B = ChemBERTa-based zero-shot CPI proxy — embed candidates and known
  PHGDH actives via HuggingFace `seyonec/ChemBERTa-zinc-base-v1`, score by max
  cosine similarity. Lighter, no dep nightmare.
- **Track C (FoldSeek scaffold seeds)**: top 50 captured. Next step is to pull
  binders for each top-50 PDB hit via ChEMBL API → cluster on Tanimoto → use
  cluster centroids as scaffold-conditional FT inputs in iter 5.
- **PubChem-BioAssay augmentation**: deferred — BindingDB (1.18 M unique)
  already gives us 1.67 M total. PubChem-BioAssay (~3 M with assay-link) would
  push to ~5 M total but the marginal signal is diminishing.

## Risks to monitor

- iter 4 transformer val PPL is currently 2.03 (ep 1) — if it doesn't drop
  below 1.5 by ep 5–6, the SELFIES tokenization may be over-generalizing
  vs char-LSTM's 1.59 final.
- Vina pose artifacts in iter 3 not yet audited (no per-pose variance check
  in current script). Adding a 5-pose-consensus filter at iter 4 dock step.
- DrugCLIP / Track B repeated failures suggest we should pivot to a simpler
  CPI scorer (ChemBERTa cosine or TransformerCPI 2.0 with stable build).
