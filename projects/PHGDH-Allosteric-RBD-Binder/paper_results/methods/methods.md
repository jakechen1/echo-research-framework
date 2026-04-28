---
title: Methods (PHGDH allosteric binder discovery)
status: living document — extended each iteration
---

# Methods

## 1. Bioactive corpus assembly

**Primary corpus (iter 2 / iter 3 / iter 4)** — ChEMBL 35 SQLite bulk download
(`https://ftp.ebi.ac.uk/pub/databases/chembl/ChEMBLdb/releases/chembl_35/chembl_35_sqlite.tar.gz`)
parsed via SQL with PRAGMA-tuned (mmap_size=30GB, cache_size=1GiB) connection.
Query reorders to drive from the small `target_dictionary` table:

```sql
CREATE TEMP TABLE mol_active AS
SELECT DISTINCT a.molregno
FROM target_dictionary td
JOIN assays asy ON asy.tid = td.tid
JOIN activities a ON a.assay_id = asy.assay_id
WHERE td.chembl_id != 'CHEMBL2311243'        -- exclude PHGDH itself
  AND a.pchembl_value >= 5.0;                -- ~10 µM bioactivity threshold

SELECT cs.canonical_smiles
FROM mol_active m JOIN compound_structures cs ON cs.molregno = m.molregno
WHERE cs.canonical_smiles IS NOT NULL
  AND length(cs.canonical_smiles) BETWEEN 5 AND 200;
```

After Python-side dedup (canonical SMILES) and salt rejection (`.` in SMILES):
**1,091,136 unique bioactive SMILES**.

**Augmented corpus (iter 5+)** — adds BindingDB All (release 202604, 3.18 M
binding measurements) parsed with chunked CSV reader:
- Keep rows with any of `Ki`, `IC50`, `Kd`, `EC50` < 10 000 nM
- RDKit-canonicalize, drop salts and molecules with heavy-atom count outside [5, 80]
- Deduplicate vs ChEMBL canonical SMILES set

**Result**: 1,177,443 BindingDB-unique + 495,064 ChEMBL-only = **1,672,507 merged**.

## 2. Generative models

### iter 2 — character-level LSTM (Fan Li 2026 baseline)

- Tokenizer: char-level over SMILES (PAD, START "^", END "$", + observed chars)
- Vocab: 45 tokens
- Architecture: 3-layer LSTM, embedding 128, hidden 512, dropout 0.2
- Training: AdamW (lr 1e-3, weight_decay 1e-5), batch 256, max_len 110, 30 epochs,
  CrossEntropyLoss with PAD ignore_index, gradient-clip 1.0
- Compute: 1× A100 80 GB, **41:13** wallclock
- Result: **val perplexity 1.59**, best.pt = 66 MB

### iter 3 — incremental fine-tune (5-stage potency staircase)

Per Fan Li 2026: load `best.pt` and FT sequentially on bucketed PHGDH actives:
`bucket_pv5.smi` → `pv6` → `pv7` → `pv8` → `pv9` (each is a stricter subset of
1 011 PHGDH actives at progressively higher pchembl thresholds).
- 8 epochs per stage, lr 1e-4 with cosine warmup, batch 64
- Compute: 1× A100, **1:46** total (5 stages combined)
- Result: val PPL 1.25 after stage 5

### iter 4 — SELFIES + small transformer (architecture upgrade)

- Tokenizer: SELFIES (Krenn et al.) — every output guaranteed valid molecule
- Vocab: 169 SELFIES tokens
- Architecture: decoder-only transformer (causal), 8 layers × 8 heads × d_model 512
  × ffn 1024, GELU activation, pre-norm, tied embedding
- **16,975,360 parameters**
- Training: AdamW (lr 3e-4, β=(0.9, 0.95), weight_decay 0.01), batch 128, max_len 128,
  10 epochs, cosine LR with 5 % warmup
- Race: P100 (~46.5 min/epoch) vs A100 (18.6 min/epoch); A100 wins by ~3 h.

### iter 5 — RL fine-tune (planned)

REINFORCE policy gradient with batch-mean baseline:
```
loss = -E[ (reward - baseline) * log_prob ] + β·KL(policy ∥ prior) - λ·H(policy)
```
- KL-to-frozen-prior penalty (β = 0.1) → prevents distribution collapse
- Entropy regularization (λ = 0.01) → prevents mode collapse
- Composite reward: `w_aff·affinity + w_dl·(qed - 0.5) + w_nov·novelty - w_inv·invalid - w_sa·sa_penalty`
- Affinity from DrugCLIP-PHGDH (Track B) once available, else cached-Vina proxy

## 3. Sampling and ranking

### Sampling (iter 3)

- Three temperatures: 0.8, 1.0, 1.2 (≈ 3,333 samples each → 9 999 total)
- Per-sample: RDKit MolFromSmiles validation + canonicalization; perplexity via
  next-token log-probability; QED, Lipinski Ro5, Veber, MW, logP, HBD, HBA, TPSA;
  novelty = 1 − max Tanimoto (Morgan FP r=2, 2048 bit) vs 1 011 known actives
- Output: top 1 000 by perplexity → CSV with all metrics

### Multi-objective Pareto rank

```
score = 2·z(affinity) + 1·z(qed) + 1·z(novelty) + 0.5·z(druglike_penalty)
```
where `z` is z-normalization within the iteration's docked pool.

Hard gates (iter 3, lenient):
- Vina ΔG ≤ −6.0 kcal/mol
- Lipinski violations ≤ 1
- PAINS = 0 (RDKit FilterCatalog)
- (added at re-rank): novelty ≥ 0.3 (Tanimoto ≤ 0.7 to all 1 011 known actives)

Pareto front computed over (z_affinity, z_qed, z_novelty); top 200 by composite.

## 4. Docking pipeline (Vina)

### Receptor preparation

- 6RIH PDB downloaded from RCSB
- Chain A protein extracted, K4T allosteric ligand isolated for pocket centering
- PDBQT generated via OpenBabel (`obabel -i pdb ... -o pdbqt -xr`) with rigid-receptor flag
- Pocket center: K4T HET-atom centroid → `(13.60, −11.84, 73.28) Å`
- Box size: ext + 10 Å pad, floor 20 Å → `(20, 20, 20) Å`
- Counter-receptors (selectivity): PSAT1 (PDB 3E77, PLP-anchored) + PSPH (PDB 1L7M, MG/PO4-anchored)

### Ligand preparation

- RDKit `MolFromSmiles` → `AddHs` → `AllChem.EmbedMolecule(ETKDGv3)` → MMFF optimize
- meeko `MoleculePreparation` + `PDBQTWriterLegacy` → PDBQT string
- Vina (Python lib via `vina` package, version 1.2.x) with exhaustiveness=8, n_poses=5

### Parallelization

Slurm array job: 25 chunks × 40 ligands per chunk = 1 000 ligands docked in parallel
on `express` partition; ~31–57 min per chunk wallclock, ~50 min total.

## 5. Hardware and cluster usage (UAB Cheaha)

- **GPU partition** `amperenodes-medium` (1× A100 80 GB) — pretrain + fine-tune
- **GPU partition** `pascalnodes` (1× P100 16 GB) — fallback / parallel race
- **CPU partition** `express` (4–8 cores per task) — Vina docking arrays, FoldSeek,
  receptor prep, BindingDB processing
- All jobs use `/local/$USER/$SLURM_JOB_ID/` SSD for hot data (A100 I/O discipline)
- Conda envs:
  - `clm-lstm` (iter 2 / iter 3): torch 2.4.1+cu121, rdkit 2026.03.1
  - `clm-trans` (iter 4): adds selfies 2.1.1
  - `vina-py`: vina 1.2.x, meeko 0.7.1, rdkit
  - `foldseek`: foldseek (latest from bioconda)
  - `drugclip` (in progress): DeepPurpose 0.1.5 + lifelines + statsmodels (Track B)

## 6. Data and code provenance

- All sbatch scripts: `~/jobs/aim4_clm/aim4_*.sbatch` on Cheaha → mirrored in GitHub
- Python training/inference: `~/jobs/aim4_clm/{pretrain_lstm,finetune_lstm,sample_lstm,
  pretrain_transformer,vina_dock_chunk,pareto_rank_round3,extract_bioactives,rl_finetune}.py`
- Per-iteration runs: `/data/user/jakechen/aim4_clm/runs/<iter>_<jobid>/`
- Each run dir contains: `config.json`, `loss.csv`, `vocab.json`, `best.pt`, `last.pt`
  (+ iter 3 also has `candidates.csv`, `dock_results/chunk_*.csv`, `top200*.csv`)

## 7. Ongoing limitations

- Vina ΔG is optimistic by ~2 kcal/mol vs FEP / wet-lab — **always treat predicted
  affinities as upper bounds**. iter 6 FEP refinement is the gold standard.
- DrugCLIP-PHGDH not yet trained (Track B blocker — pymoo + dependency chain
  challenges); current affinity proxy is direct Vina docking only.
- iter 3 perplexity-rank top 10 = exact memorized known actives (model
  re-discovers training set). Fix: novelty hard gate at rank stage (active);
  architectural upgrade in iter 4 (transformer + SELFIES); RL with non-perplexity
  reward in iter 5.
- Counter-screen panel currently 2 targets (PSAT1, PSPH); iter 6 expands to
  10–20 off-targets including hERG, CYP3A4, top kinases.
