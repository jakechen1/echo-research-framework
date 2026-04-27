---
task: Task 4.4
iteration: 2
stage: P
planned_at: 2026-04-27T06:00:00Z
compute_target: cheaha
---

# Task 4.4 Plan iter 2 — LSTM CLM pretrain on Cheaha (Fan Li 2026)

## What changed since iter 1
Iter 1 was data-prep only on W0 (PHGDH potency buckets `bucket_pv5..9.smi`).
Iter 2 ports the **real LSTM pretrain** to Cheaha A100 instead of L0 M4 Pro
because (a) 24 GB shared M4 RAM is tight for 450K SMILES pretrain;
(b) Cheaha A100 80 GB cuts wall-time ~5x; (c) frees L0 for inference.

## Goal
Train a char-level autoregressive LSTM on ~450K ChEMBL bioactives
(excluding PHGDH target `CHEMBL2311243`) so iter 3 can incrementally
fine-tune on PHGDH potency buckets and sample ranked candidates.

## Compute target
Cheaha HPC (UAB), via SSH alias `cheaha` on W0. NOT L0.
- setup + smoke: `express` partition (CPU, 2 h max) — env build + ChEMBL extract
- full pretrain: `amperenodes` (1x A100 80 GB, 12 h max) — 8 h walltime requested

## Data
- **Pretrain corpus**: ChEMBL bulk SQLite, filter `pchembl_value >= 5 AND target.chembl_id != CHEMBL2311243`, dedup canonical SMILES, length 5..200. Expect ~400-500K mols.
- **Source**: EBI FTP `https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_35/chembl_35_sqlite.tar.gz` (~5 GB). Bumpable via env var `CHEMBL_VERSION`.
- **Storage** (A100 I/O discipline): persistent on `/data/user/jakechen/aim4_clm/`; per-job scratch on `/local/$USER/$SLURM_JOB_ID/`.

## Model (Fan Li 2026 reproduction)
- Tokenizer: char-level (PAD=" ", START="^", END="$", + all observed chars)
- Architecture: 3-layer LSTM, embed=128, hidden=512, dropout=0.2
- Optim: AdamW lr=1e-3, weight_decay=1e-5
- Loss: cross-entropy over next-char prediction (ignore PAD)
- Batch=256, max_len=110, 30 epochs, val-frac=0.05
- Checkpoint: best-val every epoch + last; resumable

## Sub-stages (PLEASXR)
- **P (this doc)** — plan, decisions, success criteria
- **L** — confirm Fan Li 2026 hyperparams; survey any post-2026 SMILES-LM improvements worth trialing in iter 3 (note: do not block iter 2 on L)
- **E** — `task_4_4_lstm_cheaha.sh` (state machine):
  - E.1 setup.sbatch (express): mamba env `clm-lstm` + ChEMBL bulk download + SQL extract → `bioactives.smi`
  - E.2 smoke.sbatch (express, CPU): 1k subset, 2 epochs, validate end-to-end
  - E.3 pretrain.sbatch (amperenodes, A100): full 450K, 30 epochs, save best-val
  - E.4 retrieve: rsync `runs/<jobid>/` from `/data/user/jakechen/aim4_clm/runs/` back to `~/.openclaw/workspace/data/aim4_clm/runs/<jobid>/`
- **A** — validate: train/val perplexity curve; SMILES validity rate (RDKit parse on 1k samples); novelty vs ChEMBL; loss converged
- **S** — publish best checkpoint + perplexity plot to wiki + Box; CHANGELOG entry
- **X** — log GPU-hours (from sacct), Cheaha SU est, wall-clock
- **R** — close iter 2; promote iter 3 (incremental FT on PHGDH buckets)

## Success criteria
- Achievement >=6: pretrain converges (val perplexity flat for >=3 epochs); >=95% RDKit-valid samples
- Growth >=5: checkpoint reproducible (vocab + config + weights all saved)
- Efforts <=6: <12 GPU-hours total (single A100, ~6 h target)

## Heartbeat
Stage E writes `/Users/jakeclaw/workers/heartbeats/pleaser_E.ts` on every executor invocation.

## Decisions log
- 2026-04-27 — char-level over SELFIES (matches Fan Li, simpler debugging); revisit in iter 3 if validity <90%
- 2026-04-27 — single A100 over multi-GPU (model fits trivially; multi-GPU overhead not worth it)
- 2026-04-27 — pchembl>=5 cutoff (canonical "bioactive"); refine in L if corpus too noisy
- 2026-04-27 — exclude only target `CHEMBL2311243` (PHGDH); not other serine biosynthesis enzymes (could leak; ablation deferred)

## Open questions for iter 3
- Sampling strategy: greedy / temperature / nucleus
- FT order: ascending pv (5->9) vs descending; Fan Li shows ascending wins
- Stop FT when sample novelty plateaus

## State file
`project-state/aim4_clm_state.json` — owned by `task_4_4_lstm_cheaha.sh`
