---
title: PHGDH allosteric binder discovery — scaling, DrugCLIP, structural neighbors, and the Fan Li 2026 framework
slug: scaling-drugclip-repositioning-strategy
created: 2026-04-27
status: draft
project: PHGDH-Allosteric-RBD-Binder
tags: [strategy, generative-chemistry, drugclip, repositioning, fan-li-2026]
---

# Strategy: scaling the LSTM, DrugCLIP, structural neighbors, repositioning

This doc answers four research-design questions raised in iter 2 closeout, in the
context of the Fan Li et al. 2026 chemical-language-model framework already
implemented (`workers/bin/pretrain_lstm.py`, `task_4_4_lstm_cheaha.sh`).

> **Honesty notice:** numbers below are reasoning + standard-knowledge facts.
> The Fan Li 2026 description follows this project's harness docs (paper:
> Nat Commun s41467-026-71591-w); I have not re-read the paper since the iter
> 2 run. Where I'm uncertain (e.g., whether "RBD" in the project name is
> RNA-binding or Regulatory-Binding domain), I flag it and offer both reads.

---

## 1. Bigger data + deeper net + multi-A100 — would it be better?

**Short answer:** probably not by *just* scaling. The signal-rich axis is
**bioactives**, not raw chemistry; the architectural axis with the highest
ROI right now is *quality* (transformer/SELFIES/graph), not depth.

### What ChEMBL gives you (and what PubChem 100M doesn't)

| Source | Size | Bioactivity-annotated? | Drug-likeness | Signal density |
|---|---|---|---|---|
| ChEMBL (we used) | 1.09 M filtered | yes (curated, pchembl ≥ 5) | high | **highest** |
| PubChem-BioAssay | ~3 M | yes (assay-linked) | mixed | high |
| ZINC bioactive subset | ~30 M | partly (annotated subset) | high (pre-filtered) | high |
| **Full PubChem** | ~119 M | **mostly NO** | mixed (incl. dyes, agro-chem, polymer fragments) | low |
| ZINC drug-like (full) | ~1 B | NO | high | low |

The Fan Li design choice — train on *bioactives*, not raw chemistry — is
deliberate. The pretrain prior should be "drug-like *and* observed to do
something biological," not "every organic structure ever made." Training on
unfiltered PubChem 100M dilutes that signal: the model learns dye chemistry,
agrochemical scaffolds, and synthesis intermediates the same as actives.

### What scaling would actually help

The right scaling axis isn't "10x bigger raw chemistry," it's **"10x bigger
bioactive-annotated subset":**

- **Add PubChem-BioAssay** (~3 M with assay-linked activity) on top of ChEMBL — about 3× the data, all bioactive-relevant.
- **Add BindingDB** (~2 M binding measurements, complements ChEMBL's lit-curated set with vendor data).
- **Add USPTO-extracted reactions / chembl-pchembl≥4** (slightly weaker activity threshold; adds breadth).
- **Re-filter** to deduplicate at the InChIKey level across sources.

A realistic target: **~5–8 M bioactives**, roughly 5–8× this run, all signal.

### When deeper net + multi-GPU starts paying off

Current run: 5.5 M params, 1.09 M SMILES, single A100, 41 min, val PPL 1.59.
Multi-GPU (NCCL-backed DDP) adds gradient-sync overhead and only amortizes
when the per-step compute is large enough that comm fades into the noise.

Order-of-magnitude rule for our setup:
- < 50 M params on < 5 M SMILES → single A100 is fastest.
- 50–500 M params or 5–50 M SMILES → 2× A100 likely worth it.
- > 500 M params or > 50 M SMILES → multi-node A100 / H100.

**Architecture changes that beat depth alone**:

1. **SELFIES tokenizer** instead of char-level SMILES. SELFIES guarantees every
   sampled string is a valid molecule (no need to discard invalid SMILES at
   sampling time — typical char-LSTM gives 10–30% invalid). Cheap win.
2. **Transformer (causal LM) instead of LSTM.** Better long-range deps, more
   parallelizable. ChemGPT, MolGPT have shown 50–100 M-param transformers
   outperform LSTM on validity + diversity for the same compute.
3. **Graph neural net on the molecular graph** (e.g., GraphAF, JT-VAE, GFlowNet).
   Treats molecule as graph (nodes=atoms, edges=bonds); can't generate
   invalid by construction. Best for de novo. Cost: more complex training
   loop, harder to fine-tune incrementally.
4. **Reward-augmented sampling** (REINFORCE / PPO) over a learned reward like
   DrugCLIP score (see §2). Skips much of the perplexity-based ranking step.

**Practical recommendation for the next iter** (3 or 4):
- Hold model size at 5–20 M params, switch to **SELFIES + transformer**.
- Pretrain on **ChEMBL ∪ PubChem-BioAssay** (~4 M).
- Single A100, ~3–6 h.
- The biggest gain will be from validity (no wasted sampling) and the
  transformer's better fine-tune transfer, not from a deeper LSTM.

---

## 2. Where DrugCLIP fits

**DrugCLIP** = contrastive learning on (drug, target) pairs (Gao et al., 2024,
analogous to OpenAI's CLIP for image-text). The trained model gives every
molecule × protein pair a binding-plausibility score from embedding similarity,
without needing docking or a wet assay.

This project already has 1,011 known PHGDH actives in the bucket files
(`bucket_pv5..9.smi`) — a strong anchor set for DrugCLIP-style work.

### Four ways DrugCLIP integrates with the Fan Li pipeline

| # | Use | Where in pipeline | Why |
|---|---|---|---|
| 1 | **Pre-screen generations** | After Fan Li samples 10K → DrugCLIP scores against PHGDH binding site → keep top 1K → only those go to Vina docking | Vina at ~30 s/molecule on 10K = ~80 h; DrugCLIP at ~10 ms/molecule = 100 s |
| 2 | **Counter-screen for selectivity** | Score each candidate against the homologs PSAT1 + PSPH (same pathway) and a panel of off-targets (kinases, GPCRs) → drop promiscuous binders | PHGDH inhibitors that also hit PSAT1 / PSPH would shut down all serine biosynthesis; selectivity is the actual win |
| 3 | **Anchored retrieval** | Embed the 1,011 known PHGDH actives → search PubChem-BioAssay (~3 M) by nearest-neighbor in embedding space → retrieve the top 50K closest molecules → score / dock those | Pure retrieval (no generation); high-prior seeds; complementary to Fan Li |
| 4 | **Reward signal in RL fine-tuning** | Replace the 5-stage potency-bucketed fine-tune with REINFORCE/PPO over DrugCLIP score → model directly optimizes for predicted PHGDH binding | Stronger learning signal than sequential FT; risk of mode collapse if reward is too greedy |

**Most useful for tonight's continuation: (1) and (3).**

(1) plugs into the existing Vina path (Task 4.5) as a fast pre-filter.
(3) is a *parallel discovery track* using the same anchor set — gives a
second list of candidates from a different methodological prior, useful for
ensembling and reducing single-method blind spots.

### Practical DrugCLIP setup

- **Open implementations**: the original DrugCLIP code (Gao et al.) on GitHub;
  alternatives: PLAPT, MolCLR, TransformerCPI 2.0.
- **Training data**: BindingDB + ChEMBL + PDBbind for positive pairs;
  random pairs for negatives. ~1 M positive pairs is enough to start.
- **Compute**: pretraining a small DrugCLIP (~30 M params) is ~6–12 h on
  one A100. Once trained, *inference* is millisecond per molecule.
- **PHGDH input**: protein sequence (UniProt O43175) + 3D structure of the
  allosteric pocket from PDB 6RIH (or 6PLG, 6PLF for variant pockets).

---

## 3. Proteins similar to PHGDH around the (R)BD — and embedding-neighborhood
   repositioning

### What "RBD" means here (note the ambiguity)

The project name says **PHGDH-Allosteric-RBD-Binder**. PHGDH literature uses
multiple acronyms; two plausible reads of "RBD" in this context:

- **Regulatory Binding Domain** — the allosteric ASB / regulatory cleft that
  binds CBR-5884, NCT-503, BI-4924, K4T (the PDB 6RIH pocket). **Most likely
  given "Allosteric" in the project name.**
- **RNA Binding Domain** — recent moonlighting-function papers (~2023–2025)
  characterize PHGDH as an RNA-binding protein in addition to its enzymatic
  role; this RBD lives in the regulatory portion. Less standard in older
  literature but increasingly cited.

Both reads land in roughly the same 3D region. The strategies below apply
to either; I note where they diverge.

### Sources for structural neighbors

**Sequence-level**
- BLAST against UniProt → catches close homologs (PSAT1, PSPH in the same
  serine-biosynthesis pathway).
- HMMER / PSI-BLAST for distant homology in the 2-hydroxyacid-dehydrogenase
  superfamily.
- InterPro (Pfam PF00389 / PF02826) for domain-architecture matches.

**Fold / 3D-structure level (more relevant for repositioning, since drugs
bind 3D pockets)**
- **FoldSeek** — fastest; searches the 200 M AlphaFold-DB structures by
  structural alignment in seconds. Use the PHGDH allosteric-region structure
  (6RIH, chain A, residues bordering the pocket) as the query.
- **DALI** — classical pairwise structural alignment; slower, more
  conservative.
- **TM-align** — local alignment; useful when only the pocket-region fold
  matters.

**Pocket-level (best signal for "drugs that fit our pocket")**
- **ProBiS** (Protein Binding Sites server, Konc & Janežič) — pocket-level
  similarity over the PDB.
- **G-LoSA**, **APoc**, **PocketMatch** — different alignment heuristics,
  worth ensembling.
- **fpocket** + structural similarity downstream.

**RNA-binding-specific** (if "RBD" = RNA-binding)
- **BindUP** (binding-site predictor for RBPs).
- **RBPbase** / **POSTAR3** for known RBPs.
- **ESM-2 + ESM-IF embeddings** clustered by RBP-likeness.

### Embedding-neighborhood as a repositioning strategy

Yes — and it's a real, validated approach (variants used at Recursion,
BenevolentAI, NIBR, multiple academic groups). The basic loop:

1. **Embed all proteins** in a learned space (ESM-2, ProtT5, or
   ProteinBERT) → 1280-D vectors per protein.
2. **Embed all FDA-approved + clinical-trial drugs** in a learned space
   (ChemBERTa, Mol2Vec, MolFormer) → 768–1024-D vectors per molecule.
3. **Find PHGDH's protein neighborhood**: top-N proteins by cosine distance
   in the protein embedding. Filter to those with annotated drug binders.
4. **For each neighbor, pull its known small-molecule binders** (DrugBank,
   BindingDB, ChEMBL).
5. **Those binders become seeds**: they're enriched for binding chemistry
   that works on PHGDH-similar pockets.
6. **Cluster the seed set** (Tanimoto over Morgan fingerprints) →
   representative scaffolds → expand around each scaffold (e.g., GFlowNet
   conditional sampling, or matched-molecular-pair extension, or
   Fan-Li-style fine-tuning anchored to that cluster).

**Genes-as-targets repositioning** flavor: same loop, but step 2 swaps
"drugs" for "genes" via a protein–gene-perturbation co-embedding (e.g.,
Cell Painting + L1000 → drug-gene similarity). Tells you if a CRISPR-Cas9
knockout phenocopies your drug — a genetic-validation lookup.

### Practical seed-set construction for PHGDH

A concrete week-of-work plan:
1. **FoldSeek** AlphaFold-DB with the 6RIH allosteric pocket → top 50
   structural neighbors.
2. **Filter** to human / mammalian targets with annotated binders in
   ChEMBL or DrugBank.
3. **Pull binders** for each → expect 200–2000 unique seed molecules.
4. **Cluster** (Tanimoto > 0.6) → ~50–100 scaffold clusters.
5. Each cluster's centroid → input to (a) Fan Li-style scaffold-conditional
   fine-tune, OR (b) DrugCLIP-anchored neighbor expansion in PubChem-BioAssay.
6. Top expansions → Vina rerank against the PHGDH 6RIH pocket.

This sits *parallel* to the Fan Li generative track: same final docking
funnel, different upstream priors.

---

## 4. Fan Li 2026 in this combined context

Fan Li et al. 2026 (Nat Commun, s41467-026-71591-w) — based on the harness
docs and our iter 2 implementation:

**Core idea: transfer learning + potency-staged fine-tuning.**

1. **Pretrain** an autoregressive char-level LSTM on ~450 K (we used
   1.09 M) ChEMBL bioactives. Output: a model that has learned the
   "grammar" of drug-like SMILES — common functional groups, plausible
   atom positions, valid bracket / bond patterns.
2. **Incrementally fine-tune** in 5 rounds with progressively higher
   pchembl-value cutoffs (≥ 5, ≥ 6, ≥ 7, ≥ 8, ≥ 9). Each round narrows the
   model's distribution toward more potent compounds *for the target of
   interest*. The gradient is the "potency cliff" of the bucket order.
3. **Sample** ~10 K candidates from the final fine-tuned model.
4. **Rank by perplexity** (the model's surprise = inverse confidence;
   low perplexity = predicted potent). Keep top 500.
5. **Validate** by docking (Task 4.5: AutoDock Vina against the
   PHGDH 6RIH allosteric pocket).

### How Fan Li relates to the three other axes

**vs. scaling (§1):** Fan Li's incremental FT is an *inductive bias*
that beats raw scaling for small target-active corpora (PHGDH has only
~1011 actives). The 5-stage potency staircase smooths what would
otherwise be a too-sharp distribution shift. If you scale the *pretrain*
corpus to 5 M bioactives the FT step still works the same way; the prior
just gets richer.

**vs. DrugCLIP (§2):** Fan Li is *generative* (proposes new molecules).
DrugCLIP is *discriminative* (scores existing molecules). They compose:
Fan Li proposes 10 K → DrugCLIP scores → top 1 K → Vina. DrugCLIP can
also replace the perplexity ranking step (which is a weak proxy for
actual binding) with a real binding-affinity proxy. **Adding DrugCLIP
ranking is probably the single highest-ROI improvement to the current
pipeline.**

**vs. structural-neighbor repositioning (§3):** Fan Li is *de novo*
generation; repositioning is *retrieval from existing chemistry.* They
attack different parts of the chemistry space:

- Fan Li explores *novel* scaffolds the model interpolates from its prior.
  Strong for novelty / IP, weaker on reliability.
- Repositioning surfaces *known-binding* scaffolds adjusted for a new
  target. Strong on reliability + safety (drugs already passed Phase 1),
  weaker on novelty.

**A combined three-track strategy:**

1. **Track A — Fan Li generative (now done for pretrain):** char-LSTM →
   SELFIES-transformer in iter 4. Output: 500 novel candidate SMILES per
   round.
2. **Track B — DrugCLIP retrieval-and-scoring:** trained DrugCLIP scores
   PubChem-BioAssay against the PHGDH pocket. Output: 5 K closest existing
   molecules.
3. **Track C — Structural-neighbor seeding:** FoldSeek + InterPro for
   PHGDH neighbors → pull their binders → cluster → use as conditional
   seeds in Track A's fine-tune. Output: 200 scaffold-anchored expansions.

All three feed into the same Vina docking funnel against 6RIH.
Track A gives novelty, B gives selectivity-aware breadth, C gives
chemistry-reliable starting points.

---

## 5. Concrete next-iteration TODO

| Priority | Item | Effort | Track |
|---|---|---|---|
| P0 | Iter 3: 5-stage incremental FT on `bucket_pv{5..9}.smi` from `best.pt` | 0.5 d | A |
| P0 | Sample 10 K candidates from final FT model + RDKit-validity filter + perplexity rank → top 500 | 0.5 d | A |
| P0 | Vina docking of top 500 against PHGDH 6RIH (Task 4.5) | 1 d Cheaha | A |
| P1 | Stand up DrugCLIP (clone reference impl + retrain on BindingDB + ChEMBL) | 2 d | B |
| P1 | DrugCLIP score iter-3 candidates → keep top 1 K for Vina (replaces perplexity-only rank) | 0.5 d | A+B |
| P1 | DrugCLIP counter-score against PSAT1 + PSPH for selectivity | 0.5 d | B |
| P2 | FoldSeek query: 6RIH allosteric pocket vs AlphaFold-DB → top-50 structural neighbors | 0.25 d | C |
| P2 | Pull binders for top neighbors via DrugBank + ChEMBL → cluster (Tanimoto 0.6) → 50-100 scaffolds | 1 d | C |
| P2 | Scaffold-conditional FT pass through Fan Li model | 1 d | A+C |
| P3 | Iter 4: switch char-LSTM → SELFIES + small transformer (~20 M params); add PubChem-BioAssay to pretrain | 3–5 d | A |
| P3 | DrugCLIP-as-reward RL fine-tuning (REINFORCE) | 3–5 d | A+B |

Tracks can run in parallel. P0 alone produces the iter 3 deliverable
(novel candidates + docking scores). P1+P2 produce a much stronger second
batch with selectivity awareness and seeded chemistry.

---

## 6. Open questions and uncertainties

- **RBD ambiguity** — Regulatory Binding Domain or RNA-Binding Domain?
  The decision affects whether step (3) FoldSeek targets the allosteric
  pocket or an RNA-binding fold. Confirm before starting Track C.
- **Selectivity targets** — should counter-screen include PSAT1, PSPH,
  and which off-target panel? Default suggestion: PSAT1, PSPH, the
  10 most-prescribed kinases, the 10 most-prescribed GPCRs. Refine
  with a med-chem consult.
- **DrugCLIP retraining vs. off-the-shelf** — using the reference
  pretrained model is fast but may not be PHGDH-pathway aware; retraining
  on BindingDB + a PHGDH-relevant subset would be slower but more
  PHGDH-tuned. Probably start with off-the-shelf.
- **PubChem-BioAssay vs ZINC-bioactive** for the expanded pretrain
  corpus — both viable; PubChem-BioAssay has stricter activity
  annotation, ZINC has better drug-likeness pre-filtering. Default:
  ChEMBL ∪ PubChem-BioAssay; revisit after iter 4.

---

## 7. Glossary

- **ChEMBL** — EBI's curated bioactivity database; small molecules + targets + measured potencies.
- **PubChem** — NCBI's broad chemical database; ~119 M compounds, mostly without bioactivity annotation. PubChem-BioAssay subset has assay-linked activities.
- **pchembl_value** — log-scaled potency; pchembl ≥ 5 ≈ IC50 ≤ 10 µM ≈ "bioactive."
- **DrugCLIP** — contrastive learning over (drug, target) pairs → joint embedding → fast binding-plausibility scoring.
- **SMILES / SELFIES** — molecule string representations; SMILES allows invalid strings, SELFIES is constructed to be always-valid.
- **FoldSeek** — fast structural similarity search across AlphaFold-DB (~200 M structures).
- **6RIH** — PDB structure of PHGDH with the K4T allosteric inhibitor; defines the allosteric pocket geometry used in Vina docking.
- **Fan Li 2026** — Nat Commun s41467-026-71591-w; transfer-learning chemical-LM with potency-staged incremental fine-tuning. The framework implemented in this project as Task 4.4.
- **Repositioning** — discovering that an existing drug or chemotype binds a new target; here, drugs that bind PHGDH-similar proteins become PHGDH scaffold candidates.
