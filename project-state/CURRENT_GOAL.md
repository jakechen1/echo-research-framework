# Current Sub-Goal

**Aim:** Aim 4 — Structure-based virtual screening (bimodal)
**Task:** Task 4.4
**Legacy ID:** G-018
**Started:** 2026-04-20
**Tier:** local L0 GPU (LSTM pretrain) + Cheaha (gen → dock)

## Goal
Port Fan Li 2026 CLM pipeline: LSTM pretrain on ~450K ChEMBL bioactives
(PHGDH-excluded), incremental fine-tune across 5 potency buckets
(pv≥5/6/7/8/9), generate 10K candidates, rank by perplexity.

## Definition of done
- [ ] Potency buckets prepared (`data/aim4_clm/bucket_pv{5,6,7,8,9}.smi`)
- [ ] PyTorch env on L0 with rdkit + smiles_pair_encoder
- [ ] ChEMBL bioactive download (~450K SMILES, PHGDH-excluded)
- [ ] LSTM pretrain 10-20 epochs on ChEMBL
- [ ] 5-step incremental fine-tune on PHGDH buckets
- [ ] Generate 10K candidates, rank by perplexity, top 500 → data/aim4_clm_top500.smi

## Dependencies
- L0 GPU free (killswitch doesn't block L0)
- Task 2.2 top-20 molecules as training anchor (DONE)

## Parallel work running now
- Task 2.4 scaffold clustering (W0 CPU, minutes)
- infrastructure-watchdog every 5 min (diagnostic-only)
