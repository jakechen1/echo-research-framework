---
tier: public
status: published
title: "Bimodal Strategy: Fan Li 2026 CLM validates Track 2 — integration plan"
tags: [phgdh, generative, language-model, docking, sbdd, bimodal, fan-li, nat-commun]
created: 2026-04-18
author: jakeclaw+claude-review
---

# Bimodal Strategy: Fan Li 2026 validates Track 2 of PHGDH-Allosteric-RBD-Binder

## Context

[Fan Li et al., *Nat Commun* (2026-04-11)](https://www.nature.com/articles/s41467-026-71591-w)
— "Structural optimization of drug molecules with incrementally trained language models" —
reports 62× potency gain on PPARγ and 20× on RORγ using:

1. LSTM chemical language model pretrained on ~450K ChEMBL bioactives
2. Incremental fine-tuning across 4–5 potency buckets
3. Perplexity-as-potency ranking (no docking, no QSAR, no property predictor)

This is the **exact method** already scoped as Track 2 ("The Engine") in
[[PHGDH-Allosteric-RBD-Binder]]. The paper is a publishable reference
implementation — we should port it rather than reinvent, while keeping Track 1
(Vina docking on Cheaha) as a physics filter.

## Head-to-head

| Dimension | Vina dock (Track 1) | Fan Li CLM (Track 2) | Winner |
|---|---|---|---|
| Generates novel scaffolds | no | **yes** | CLM |
| Physics-validated poses | **yes** | no | Vina |
| Speed | min/ligand | s/molecule | CLM (100–1000×) |
| Needs 3D target | yes | no | Both work for PHGDH |
| Demonstrated gain | N/A | 62× (PPARγ), 20× (RORγ) | CLM |
| Hallucination risk | low | medium | Vina |

## Our readiness

| Asset | Count | Role in CLM pipeline |
|---|---|---|
| ChEMBL bioactive molecules (pretrain) | ~450 K upstream | Step 0 pretrain |
| PHGDH molecules w/ pChEMBL | 1 011 | SAR universe |
| pChEMBL ≥ 5 | ~900 | fine-tune step 1 |
| pChEMBL ≥ 6 | 463 | fine-tune step 2 |
| pChEMBL ≥ 7 | 20 | fine-tune step 3 ([[Top-20-PHGDH-Inhibitors]]) |
| PDB ligand-bound structures (Vina filter) | 3 (6PLF, 6RIH, 7S3R) | [[phgdh-pdb-binding-sites]] |
| L0 GPU idle cycles | ~79 % residency | LSTM training host |

## Integrated bimodal pipeline

```
CLM pretrain (450 K ChEMBL) → incremental FT (5 steps) → 10 000 candidates
  → rank by perplexity → top 500
  → Vina dock → 6RIH K4T pocket → ΔG scores
  → combined score = α·(−perp_z) + β·(−ΔG_z) + γ·(1 − Tanimoto_nearest_pv≥7)
  → filter ΔG < −7.0 kcal/mol AND novel
  → top 10–20 shortlist → chemist triage → synthesis
```

**α, β, γ** tuned on a held-out split of Task 2.2 top-20 once the pipeline runs.

## Scientific rationale

- CLM alone risks perplexity-low but pocket-incompatible designs (the LM has
  no 3D prior). Vina catches these.
- Vina alone can't invent outside ChEMBL. CLM expands by orders of magnitude.
- Tanimoto-novelty penalty prevents collapse onto rediscovered known actives.
- Combined score is z-normalized per batch → robust to axis-scale mismatch.
- Bimodal architecture matches the project's original design ([[PHGDH-Allosteric-RBD-Binder]]),
  now validated in a peer-reviewed journal on two independent targets.

## New tasks (added to BACKLOG)

| Task | Title |
|------|-------|
| 4.4  | Port Fan Li CLM pipeline — LSTM pretrain + 5-step incremental FT on PHGDH SMILES |
| 4.5  | Vina rerank of top-500 CLM generations into 6RIH K4T |
| 4.6  | Combined-score bimodal shortlist (top 10–20) + synthesis triage |

## Risks

- **SAR sparsity**: we have only 20 molecules at pv ≥ 7. Fan Li used series with
  richer SAR. Mitigation: bootstrap with analogs; weight step 3 lower.
- **Allosteric-site bias**: pv values in ChEMBL mix orthosteric + allosteric
  inhibitors. Mitigation: separate buckets where assay type is known (we have
  assay_type in Task 2.2 CSV).
- **Synthesizability**: CLM output may not be drug-like. Mitigation: RDKit QED +
  Lipinski filter before Vina.
