---
title: PHGDH allosteric binder — closed-loop multi-objective discovery plan
slug: closed-loop-multiobjective-discovery-plan
created: 2026-04-27
status: draft
project: PHGDH-Allosteric-RBD-Binder
tags: [strategy, closed-loop, multi-objective, drug-discovery, fan-li-2026, drugclip, vina, admet]
companion_to: scaling-drugclip-repositioning-strategy.md
---

# Closed-loop multi-objective PHGDH binder discovery plan

This is the **execution roadmap** that operationalizes the three-track strategy
(Fan Li generative + DrugCLIP scoring + structural-neighbor repositioning) into
an iterative, multi-objective closed loop. Companion to
`scaling-drugclip-repositioning-strategy.md` (which covers the *why* of each
track); this doc covers the *how, when, gates, and success criteria*.

> **Honesty notice:** technical claims here are reasoning + standard practice.
> Compute estimates assume amperenodes A100 80 GB at the rates we observed in
> iter 2 (e.g., 1.09 M SMILES × 30 epochs char-LSTM = 41 min). FEP, MM-GBSA,
> and synthetic-feasibility tooling estimates are typical literature ranges,
> not benchmarked on this account.

---

## 1. Goal

Deliver **5–15 final candidate molecules** at the end of iteration 7 with:

| Property | Target |
|---|---|
| Predicted binding affinity vs PHGDH (6RIH allosteric pocket) | FEP ΔG ≤ −8 kcal/mol |
| Selectivity vs PSAT1 + PSPH (same pathway homologs) | ≥ 100× |
| Selectivity vs broader off-target panel (kinases, GPCRs, hERG) | ≥ 30× |
| Drug-likeness (QED) | ≥ 0.6 |
| Lipinski Ro5 violations | ≤ 1 |
| Synthesizability (SAscore) | ≤ 4.0 |
| ADMET green flags (admetlab2.0 panel) | ≥ 80 % of endpoints |
| Toxicity alerts (Tox21, Ames, hERG, hepatotoxicity, PAINS) | 0 |
| Novelty (Tanimoto vs known PHGDH actives) | ≤ 0.5 |
| IP defensibility (Markush exposure) | clean substructure |

Final 5–15 molecules go to wet-lab synthesis or commercial sourcing →
biochemical IC50 assay → confirmed hits go to lead-optimization round.

---

## 2. The multi-objective scoring stack

Every candidate that survives past Vina is scored on a **composite, weighted,
multi-objective vector**. We never reduce to a single number until the
final ranking — instead we Pareto-filter and apply hard gates.

### 2.1 Binding-affinity ladder (cheap → expensive)

| Tool | Cost / molecule | Use stage | Trust |
|---|---|---|---|
| **DrugCLIP** | ~10 ms (A100) | initial pre-screen | medium (embedding proxy) |
| **AutoDock Vina** | ~30 s (CPU) | docking pass | medium-high (pose-quality dependent) |
| **smina + 5-pose consensus** | ~2 min | refined docking | high |
| **MM-GBSA** | ~30 min (GPU) | top 50–100 only | high (post-docking endpoint) |
| **FEP+ / Schrödinger / OpenFE** | ~4–10 h GPU | top 15–25 only | gold standard |

Funnel widths: DrugCLIP keeps top 10 % → Vina keeps top 20 % → MM-GBSA top 30 % →
FEP top 80 %. Each filter is a **soft Pareto cut**, not a hard threshold,
because top scorers in one metric may compensate for weakness in another.

### 2.2 Selectivity / cross-reactivity stack

| Tool | Targets | Stage |
|---|---|---|
| **DrugCLIP cross-target scoring** | PSAT1, PSPH, top-50 kinase panel, GPCR panel, hERG | every iter, post-DrugCLIP |
| **Counter-Vina** | PSAT1 (PDB 3E77), PSPH (1L7M), hERG homology model | iter 4+, on top 200 |
| **PAINS filter** (Baell & Holloway) | universal pan-assay nuisance flags | every iter |
| **BMS pan-assay filter** | additional liability flags | every iter |
| **Counter-FEP** | PSAT1, PSPH | iter 6, on top 20 |

A candidate must beat its PHGDH score by ≥ 100× over PSAT1/PSPH and ≥ 30× over
broader off-target panel, evaluated post-FEP at iter 6.

### 2.3 Drug-likeness and synthesizability

| Tool | What it tells you |
|---|---|
| **QED** (Bickerton 2012) | composite drug-likeness, 0–1, want ≥ 0.6 |
| **Lipinski Ro5** | MW, logP, HBD, HBA, oral-bioavailability proxy |
| **Veber rules** | rotatable bonds, PSA |
| **Ghose / Egan / Muegge** | secondary drug-likeness |
| **SAscore** (Ertl & Schuffenhauer) | synthetic accessibility, 1 (easy) – 10 (hard) |
| **RAscore** (Thakkar 2021) | retrosynthesis-aware accessibility |
| **AiZynthFinder** | actual retrosynthesis tree (slower; iter 5+ on top 50) |
| **BBB-permeability** (admetlab) | only if AD-relevant CNS penetration needed |

### 2.4 ADMET / toxicity

| Tool | What it covers |
|---|---|
| **admetlab 2.0** | ~30 ADMET endpoints (microsomal stability, plasma protein binding, hERG, etc.) |
| **SwissADME** | classical ADME profile |
| **Tox21 / DeepTox** | nuclear receptor, stress response panel |
| **hERG predictors** (CardPred, hERG-Att) | cardiac liability |
| **AMES mutagenicity** (DeepAMES) | genotoxicity |
| **Hepatotoxicity** (DILI predictors) | liver toxicity |
| **PAINS / BMS filters** | promiscuity / assay artifacts |

Hard gate at iter 5: any **predicted hERG IC50 < 10 µM** or any **AMES alert**
or any **PAINS hit** → drop the molecule. ADMET endpoint failures soft-cost
the composite score.

### 2.5 Novelty and IP

| Tool | What it gives |
|---|---|
| **Tanimoto vs training set** (Morgan FP r=2, 2048 bit) | structural distance from known PHGDH actives |
| **Murcko-scaffold novelty** | novelty at scaffold (not just decoration) level |
| **SureChEMBL substructure search** | patent-prior-art exposure |
| **Markush analyzer** | broader Markush claims that might cover candidates |

Final molecules must have Tanimoto ≤ 0.5 to all 1011 known PHGDH actives AND
their core scaffold absent from the top 20 PHGDH-related patents.

### 2.6 Composite score (for ranking only — never gates)

```
score = w_aff·z(affinity) + w_sel·z(selectivity) − w_tox·z(toxicity)
        + w_dl·z(drug-likeness) − w_sa·z(SAscore) + w_nov·z(novelty)
```

where `z(·)` is z-normalized to the iteration's distribution and `w_·` are
weights chosen per iteration (e.g., later iterations weight selectivity and
toxicity more heavily). Used only for sorting within a Pareto-survivor set.

---

## 3. Three-track generation in detail

### Track A — Fan Li generative (already pretrained)

| Iteration | Action |
|---|---|
| **iter 3** (current next) | 5-stage incremental FT on `bucket_pv5..9.smi` from `best.pt`; sample 10 K; RDKit-validity filter; perplexity rank → top 1 K |
| **iter 4** | Architecture upgrade: SELFIES tokenizer + small transformer (~20 M params); pretrain on ChEMBL ∪ PubChem-BioAssay (~4 M); rerun FT chain |
| **iter 5** | RL fine-tune via REINFORCE / PPO with DrugCLIP-PHGDH score as reward; entropy regularization + KL-to-prior penalty against mode collapse |
| **iter 6** | Conditional generation around top 20 from iter 5 (matched-molecular-pair extension; scaffold-anchored decoder) |
| **iter 7** | Final shortlist generation; small additions only |

### Track B — DrugCLIP scoring and retrieval

| Iteration | Action |
|---|---|
| **iter 3 (parallel)** | Stand up DrugCLIP from open-source impl (Gao 2024); pretrain on BindingDB + ChEMBL + PDBbind |
| **iter 3** | Pre-screen Track A's 10 K → 1 K by PHGDH-pocket score |
| **iter 3** | Anchored retrieval: 1011 actives → nearest neighbors in PubChem-BioAssay → top 5 K candidates (Track B's own output) |
| **iter 4** | Train DrugCLIP-PHGDH head on iter 3's top scorers (positive labels) and bottom scorers (negative); now PHGDH-pathway-aware |
| **iter 4** | Counter-screen Track A + B candidates against PSAT1, PSPH, kinase/GPCR panels |
| **iter 5+** | Use as the active-learning oracle (cheap proxy) before MM-GBSA / FEP on uncertain candidates |

### Track C — Structural-neighbor repositioning

| Iteration | Action |
|---|---|
| **iter 3** | FoldSeek 6RIH allosteric region → top 50 AlphaFold-DB neighbors; ProBiS pocket-similarity ensemble |
| **iter 3** | Pull binders from top neighbors via DrugBank + ChEMBL + BindingDB → 200–2000 raw scaffolds |
| **iter 3** | Tanimoto cluster (0.6 cutoff) → 50–100 scaffold cluster centroids |
| **iter 4** | Each centroid → input to scaffold-conditional FT in Track A; expand with matched-molecular-pair → 20 expansions per scaffold |
| **iter 5** | Top scaffolds (best Vina + lowest cross-reactivity) replicate into Track A's RL prior |
| **iter 6** | Drop Track C — by now its seeds are absorbed into Tracks A+B |

---

## 4. Closed-loop iteration architecture

Five iteration cycles (rounds 3–7) form a closed loop where each round's
top molecules become anchors for the next. Active learning queries
high-uncertainty candidates for expensive validation.

### Round 3 — initial multi-track generation (1 week)

**Goal:** prove the three-track + Vina pipeline on existing pretrain.

| Step | Tool | Output |
|---|---|---|
| 3.1 | Track A: 5-stage FT from `best.pt` on `bucket_pv{5..9}.smi` | FT model checkpoints |
| 3.2 | Track A: sample 10 K SMILES, RDKit-validate, perplexity-rank | 1 K candidates |
| 3.3 | Track B: train DrugCLIP, score Track A's 1 K | Track A composite top 500 |
| 3.4 | Track B: anchored retrieval from PubChem-BioAssay | 5 K Track B retrieval candidates |
| 3.5 | Track B: dedupe Track B against Track A (Tanimoto > 0.85) | Track B unique 4 K |
| 3.6 | Track C: FoldSeek + cluster → 100 scaffolds | 100 scaffold seeds |
| 3.7 | Track C: dock each scaffold center against 6RIH | Top 30 scaffold seeds |
| 3.8 | Combine: 500 (A) + 500 from Track B top + 100 (C) = ~1 100 | unified candidate set |
| 3.9 | Vina dock all 1 100 against 6RIH (5-pose consensus) | docked candidates |
| 3.10 | Apply hard ADMET gates (PAINS, hERG > 10 µM, no AMES) | 700–900 survivors |
| 3.11 | Pareto rank by (affinity, selectivity-DrugCLIP, QED, SAscore, novelty) | top 200 |

**Round 3 deliverable:** 200 multi-track candidates with Vina + DrugCLIP +
ADMET scores, ranked Pareto.

**Compute budget:** ~50 GPU-hours (Cheaha) + ~20 CPU-hours (Vina) + ~12 h
DrugCLIP training (one-time).

### Round 4 — architecture upgrade + DrugCLIP-PHGDH (2 weeks)

**Goal:** stronger generative prior + PHGDH-aware scoring.

| Step | Tool | Output |
|---|---|---|
| 4.1 | Pretrain SELFIES + transformer on ChEMBL ∪ PubChem-BioAssay (~4 M) | new pretrain.pt |
| 4.2 | 5-stage FT on PHGDH buckets from new pretrain | new FT model |
| 4.3 | Track C scaffold-conditional FT pass | scaffold-conditioned outputs |
| 4.4 | Sample 20 K SMILES from FT model | candidates |
| 4.5 | Train DrugCLIP-PHGDH head on Round 3 top/bottom labels | tuned scorer |
| 4.6 | DrugCLIP-PHGDH score the 20 K | top 5 K |
| 4.7 | Counter-DrugCLIP: PSAT1, PSPH, hERG, kinase panel | drop > 30 % counter-score |
| 4.8 | Vina dock survivors (top 1 K) on 6RIH and counter-Vina on PSAT1 + PSPH | scored |
| 4.9 | smina + 5-pose consensus on top 300 | refined docking |
| 4.10 | admetlab 2.0 batch on top 300 | ADMET vector |
| 4.11 | Pareto rank | top 100 |

**Round 4 deliverable:** 100 candidates with PHGDH-aware scoring,
selectivity counter-screen, refined docking, full ADMET vector.

**Compute budget:** ~150 GPU-hours.

### Round 5 — closed-loop active learning (2 weeks)

**Goal:** narrow on a Pareto front using MM-GBSA and active learning.

| Step | Tool | Output |
|---|---|---|
| 5.1 | RL fine-tune Track A model with DrugCLIP-PHGDH reward (PPO) | RL-tuned generator |
| 5.2 | Sample 10 K from RL model, validate, dedupe vs R3+R4 sets | candidates |
| 5.3 | DrugCLIP-PHGDH + counter-screen | top 1 K |
| 5.4 | Active learning: query MM-GBSA on 50 high-uncertainty candidates (high mean DrugCLIP score, high variance across DrugCLIP / Vina / SMINA) | MM-GBSA labels |
| 5.5 | Retrain DrugCLIP-PHGDH head with MM-GBSA labels | sharper scorer |
| 5.6 | smina + MM-GBSA on top 100 | refined affinity |
| 5.7 | RAscore + AiZynthFinder retrosynthesis on top 100 | synthesis trees |
| 5.8 | Lead-optimization: matched-molecular-pair (MMP) around top 20 → 200 derivatives | MMP set |
| 5.9 | Score MMPs same way; merge with parents | top 50 |

**Round 5 deliverable:** 50 candidates with MM-GBSA, retrosynthesis trees,
scaffold-MMP exploration.

**Compute budget:** ~150 GPU-hours.

### Round 6 — FEP gold standard + final selectivity (3 weeks)

**Goal:** physics-based affinity validation on the survivors.

| Step | Tool | Output |
|---|---|---|
| 6.1 | FEP+ (Schrödinger) or OpenFE on top 25 vs 6RIH | ΔG_FEP |
| 6.2 | Counter-FEP on PSAT1 + PSPH for top 20 | selectivity ΔG |
| 6.3 | Reject any candidate with FEP-based selectivity < 100× | survivors |
| 6.4 | Re-run admetlab 2.0 + DeepTox on survivors | toxicity vector |
| 6.5 | hERG patch-clamp model + DILI predictor | tox flags |
| 6.6 | Synthesizability: AiZynthFinder full retrosynthesis on survivors | route confidence |
| 6.7 | Novelty + IP: SureChEMBL + Markush analyzer | freedom-to-operate flags |
| 6.8 | Final composite Pareto rank | top 10–15 |

**Round 6 deliverable:** 10–15 candidates with FEP affinity, FEP selectivity,
full toxicity, retrosynthesis, IP clearance.

**Compute budget:** ~250 GPU-hours (FEP is the long pole).

### Round 7 — wet-lab handoff (1 week)

**Goal:** synthesize / source / assay the final shortlist.

| Step | Tool | Output |
|---|---|---|
| 7.1 | Commercial source check (eMolecules, Mcule, Enamine REAL) | which can be bought |
| 7.2 | Custom synthesis quote for the rest | cost / timeline |
| 7.3 | Order or synthesize | physical compounds |
| 7.4 | PHGDH biochemical assay (NADH-coupled or fluorescence) | IC50 |
| 7.5 | PSAT1, PSPH activity assay | selectivity confirmed |
| 7.6 | Cell-based viability on PHGDH-dependent line (HCC1937 for cancer; AD-relevant neural line if AD context) | EC50 |
| 7.7 | hERG patch-clamp on top 3 | safety check |

**Round 7 deliverable:** 5–15 measured compounds with biochemical IC50,
selectivity, cell-based EC50.

---

## 5. Final selection criteria (gates at end of round 6)

A candidate **must pass all hard gates** AND rank in top 15 by composite
score:

```
HARD GATES (yes/no):
  ✓ FEP ΔG vs 6RIH ≤ −8 kcal/mol
  ✓ FEP selectivity vs PSAT1 ≥ 100×
  ✓ FEP selectivity vs PSPH ≥ 100×
  ✓ DrugCLIP off-target panel z-score < +1 (not flagged promiscuous)
  ✓ QED ≥ 0.6
  ✓ Lipinski violations ≤ 1
  ✓ SAscore ≤ 4.0
  ✓ AiZynthFinder retrosynthesis confidence ≥ 0.7
  ✓ No PAINS, no BMS, no Tox21 alerts
  ✓ admetlab predicted hERG IC50 ≥ 10 µM
  ✓ admetlab AMES predicted negative
  ✓ admetlab DILI risk ≤ "moderate"
  ✓ Tanimoto ≤ 0.5 to all 1011 known PHGDH actives
  ✓ Murcko scaffold absent from top 20 PHGDH patents
```

Survivors of all gates → composite Pareto rank → top 5–15 → wet lab.

---

## 6. Resource budget

| Item | Compute (GPU-hr) | Compute (CPU-hr) | Walltime |
|---|---|---|---|
| Round 3 (initial multi-track) | 50 | 20 | 1 week |
| Round 4 (arch upgrade + DrugCLIP-PHGDH) | 150 | 60 | 2 weeks |
| Round 5 (RL + MM-GBSA + MMP) | 150 | 30 | 2 weeks |
| Round 6 (FEP + final tox) | 250 | 40 | 3 weeks |
| Round 7 (wet lab) | — | — | 4–8 weeks (lab time) |
| **Compute total** | **~600** | **~150** | — |
| Wet lab budget (commercial sourcing 10 × $200 + 5 custom × $2000) | — | — | $12 K |
| Wet lab assays (PHGDH biochem, cell-based, hERG) | — | — | $8 K |

Total compute fits comfortably inside the typical Cheaha researcher allocation
(thousands of GPU-hours per quarter on amperenodes).

Wallclock optimistic: ~10 weeks for rounds 3–6, plus 4–8 weeks wet lab.
With parallelism on Cheaha (multiple rounds queued), 3 months end-to-end is
realistic.

---

## 7. Risks and mitigations

| # | Risk | Mitigation |
|---|---|---|
| 1 | **RL mode collapse** in iter 5 — generator memorizes a few high-scoring molecules | KL-penalty to pretrained prior; entropy regularization; freeze generator embedding after epoch N |
| 2 | **Reward hacking** — generator exploits DrugCLIP loopholes (e.g., produces aromatic-soup that scores high but doesn't bind) | Ensemble scorer (DrugCLIP + Vina + smina), require agreement; periodic spot-check with FEP |
| 3 | **Vina pose artifact** — single-pose Vina score over-confident | 5-pose consensus, smina rescoring, drop any candidate with > 2 kcal/mol pose-score variance |
| 4 | **DrugCLIP false positives** — embedding similarity ≠ true binding | Cross-validate top set with MM-GBSA; require Vina + DrugCLIP agreement |
| 5 | **Cross-reactivity blindspot** — only screening 5–10 off-targets misses the long tail | Use kinome-wide DrugCLIP if available; flag any candidate whose scaffold has known promiscuity |
| 6 | **Synthesizability illusion** — RAscore is optimistic on novel scaffolds | Validate with AiZynthFinder; require ≥ 1 retrosynthesis route with confidence > 0.7 |
| 7 | **Novel scaffold = uncertain SAR** — the model might propose chemistry no one has explored | Require at least 30 % of final list to be scaffold-similar to known actives (Tanimoto 0.4–0.6 band) as safety hedge |
| 8 | **FEP convergence failure** — perturbations fail to converge for novel scaffolds | Use absolute binding free energy (ABFE) as backup; cap FEP attempts at 3 per molecule |
| 9 | **Counter-screen panel insufficient** — PSAT1/PSPH alone might miss a critical homolog | Add aldehyde dehydrogenases, malate dehydrogenases (broader 2-hydroxyacid family) at iter 6 |
| 10 | **Patent landmines** — high-scoring scaffolds may overlap existing claims | SureChEMBL search at iter 5 (not just iter 6); kill problematic scaffolds early |
| 11 | **PHGDH RBD ambiguity** (RNA- vs Regulatory-Binding Domain) | Confirm at iter 3 start; if RNA-binding, swap pocket and rerun Track C with RBP database |

---

## 8. Active-learning oracle hierarchy

Active learning queries different oracles based on uncertainty and stakes:

```
Cheap oracle (every candidate, every iter):
  DrugCLIP score, Vina, RDKit validity, ADMET prediction
Medium oracle (top 1 K per iter):
  smina + 5-pose consensus, admetlab 2.0 full panel
Expensive oracle (top 50–100 per iter, queried by uncertainty):
  MM-GBSA, AiZynthFinder retrosynthesis
Gold oracle (top 15–25 per round, only at iter 6):
  FEP+ / ABFE
Ground truth (top 5–15 only):
  Wet-lab biochemical IC50
```

The active-learning gain comes from re-training the cheap oracle (DrugCLIP-
PHGDH) on labels from the medium and expensive oracles each round. By iter 5,
DrugCLIP-PHGDH should correlate r > 0.6 with MM-GBSA on a held-out set —
strong enough to use as the primary scoring proxy for that iter's 10 K
candidates.

---

## 9. Validation checkpoints

### Computational sanity checks (each iter)

- **Hold out 10 % of known PHGDH actives** from Track A's pretrain + FT data;
  check whether the pipeline's top 200 contains any of the held-out ones
  (rediscovery rate). Target: > 30 % rediscovery in iter 4+.
- **Literature ΔG control**: include 5 known PHGDH inhibitors with published
  IC50 (CBR-5884, NCT-503, BI-4924, K4T) in every Vina/MM-GBSA/FEP batch.
  Check that pipeline ΔG correlates with their published potencies (Spearman
  ρ > 0.7).
- **Decoy injection**: add 50 random decoys per round; flag if they score in
  top 10 % (indicates pipeline artifact).

### Experimental validation (round 7)

- **PHGDH biochemical assay** (NADH-coupled, plate-reader format) →
  measured IC50.
- **PSAT1, PSPH activity assays** → selectivity ratio.
- **Cell-based viability** on a PHGDH-dependent line (HCC1937 for cancer;
  if AD context, an AD-relevant neuronal line) → EC50.
- **hERG patch-clamp** on top 3 → cardiac safety.
- **Microsomal stability** (rat + human) on top 5 → metabolic liability.

---

## 10. Decision points and gates

After each round, a **gate review** decides whether to advance, stay,
or restart:

| Round | Gate question | Advance criterion | Restart criterion |
|---|---|---|---|
| 3 → 4 | Does multi-track + Vina produce a coherent top 200 with > 5 % overlap with literature actives? | yes | no — diagnose pipeline before architecture upgrade |
| 4 → 5 | Does DrugCLIP-PHGDH correlate (r > 0.4) with Vina on top 1 K? | yes | no — DrugCLIP retraining failed; revisit data |
| 5 → 6 | Does MM-GBSA on top 100 separate top from bottom (delta > 5 kcal/mol)? | yes | no — generator output too narrow; widen RL temperature |
| 6 → 7 | Does FEP on top 25 produce ≥ 5 candidates passing all hard gates? | yes | no — round-6 too aggressive on selectivity; relax to 50× and rerun |
| 7 wet lab | Does any synthesized compound show IC50 < 1 µM with selectivity > 100×? | yes → SAR opt | no → diagnose, retrain, restart at round 5 |

---

## 11. Deliverables per iteration

Every round produces, in `wiki/projects/PHGDH-Allosteric-RBD-Binder/iter-N/`:

1. `top_candidates.csv` — ranked candidate list with all scores
2. `loss_curves.csv` — model training curves (if applicable)
3. `validation_decoy_injection.csv` — decoy + literature-control results
4. `iter-N-report.md` — narrative + figures (loss curves, score
   distributions, scaffold diversity, Tanimoto map, ADMET histograms)
5. `iter-N-fep.csv` (round 6 only) — FEP results
6. `iter-N-handoff.md` (round 7 only) — final list + sourcing/synthesis plan

Every deliverable goes to GitHub (echo-research-framework) and Box
(phgdh-research/) on the round's completion. Vina docked structures and
checkpoints to NAS (volumes too large for git) with a manifest.

---

## 12. Operational hookup to the harness

The plan extends the existing harness state machine
(`task_4_4_lstm_cheaha.sh`) with new task IDs:

- **Task 4.5** — Round 3 (already partly designed: Vina docking)
- **Task 4.6** — Round 4 (architecture upgrade + DrugCLIP-PHGDH)
- **Task 4.7** — Round 5 (RL + MM-GBSA + MMP)
- **Task 4.8** — Round 6 (FEP gold standard)
- **Task 4.9** — Round 7 (wet-lab handoff)

Each task's PLEASXR cycle:
- **P** — round-specific plan (e.g., which scoring weights to use)
- **L** — literature scan for any new methodology since last iter
- **E** — the round's compute pipeline (executor inherits from
  `task_4_4_lstm_cheaha.sh` pattern: state machine, idempotent, multi-stage)
- **A** — automated assessment against the round's gate
- **S** — publish round deliverables to wiki + Box + GitHub
- **X** — log compute cost (GPU-hours, CPU-hours, dollar equivalent)
- **R** — close round, promote to next task (gate-conditional)

The Sharer + Expenser executors I wired in iter 2 generalize to all these.

---

## 13. Glossary additions (extending the strategy doc's glossary)

- **Pareto front** — set of candidates not dominated on every objective; we keep the front, not just the top-1 by composite.
- **MM-GBSA** — Molecular Mechanics / Generalized Born / Surface Area; ~30 min per molecule, refines docking score with implicit-solvent free energy.
- **FEP+ / OpenFE / ABFE** — physics-based free-energy calculations; gold standard for affinity, ~hours per molecule.
- **MMP** (Matched-Molecular-Pair) — pair of molecules differing by one transformation; used for fast SAR exploration around hits.
- **Active learning** — iteratively query an expensive oracle (FEP, wet lab) on the most-informative candidates to retrain a cheap oracle (DrugCLIP).
- **PAINS** — Pan-Assay Interference Compounds; substructure flags for nuisance binders.
- **QED** — Quantitative Estimate of Drug-likeness (Bickerton 2012).
- **SAscore** — Synthetic Accessibility score (Ertl & Schuffenhauer 2009).
- **RAscore** — Retrosynthesis-Aware score (Thakkar 2021).
- **AiZynthFinder** — open-source retrosynthesis tool.
- **SureChEMBL** — patent chemistry database for IP / freedom-to-operate searches.

---

## 14. What I would do **right now**, given last night's pretrain

If I were operating tomorrow morning:

1. **Kick off Round 3.1** — copy `bucket_pv{5..9}.smi` into a new
   `aim4_clm_finetune.sbatch`, write a `finetune_lstm.py` that loads
   `best.pt` and FTs sequentially on the 5 buckets with low LR (1e-4) and
   warmup, save 5 checkpoints.
2. **In parallel**, clone the DrugCLIP reference impl on Cheaha; queue the
   ~12 h DrugCLIP-base training on amperenodes-medium.
3. **In parallel**, install FoldSeek on Cheaha; query 6RIH allosteric pocket
   against AlphaFold-DB (~30 min); pull the binders for the top 50 hits via
   ChEMBL API.
4. By end of Round 3 day 3, all three tracks should have produced their
   first batch; Vina docking is the next bottleneck (CPU-bound, 1 100 mols
   × 30 s = 9 h on one node, parallelize across the express partition).
5. By end of Round 3 day 7, top-200 list with full multi-objective scoring
   exists; gate review for Round 4.

This concrete first-step is essentially Task 4.5 in the harness — the same
state-machine pattern as Task 4.4 iter 2, but now scoring instead of just
generating.
