# Plan Status — auto-generated 2026-04-22T20:05:57+00:00

Current task: **Task 1.2**  stage: **A**  iter: 1

## Aim rollup

| Aim | Done | Active | Pending |
|-----|-----:|-------:|--------:|
| Aim 1 | 1 | 1 | 5 |
| Aim 2 | 3 | 0 | 1 |
| Aim 3 | 1 | 0 | 9 |
| Aim 4 | 2 | 0 | 9 |
| Aim 5 | 0 | 0 | 3 |

## Per-task detail

### Aim 1

| Task | Title | Status | Evidence |
|------|-------|--------|----------|
| Task 1.1 | Daily ChEMBL scavenge + delta reporting | ✅ DONE | via COMPLETED.md |
| Task 1.2 | Scaveng→Hermes enrichment loop (rank new molecules, seed wiki pages) | 🟡 ACTIVE | current iteration |
| Task 1.2.a | Implement ranker script for ChEMBL delta parsing | ⚪ pending |  |
| Task 1.2.b | Automated wiki stub creation for top hits | ⚪ pending |  |
| Task 1.3 | Entity-page templates (molecule / target / pathway / gene-set) | ⚪ pending |  |
| Task 1.3.a | Molecule template design (SMILES, properties) | ⚪ pending |  |
| Task 1.3.b | Target/Pathway template design (UniProt, KEGG) | ⚪ pending |  |

### Aim 2

| Task | Title | Status | Evidence |
|------|-------|--------|----------|
| Task 2.1 | pChEMBL distribution figure | ✅ DONE | via COMPLETED.md |
| Task 2.2 | Top-20 PHGDH inhibitors by pChEMBL ≥ 7 | ✅ DONE | via COMPLETED.md |
| Task 2.3 | PDB binding-site annotation (4NJN/6RIH/7S3R + more) | ✅ DONE | via COMPLETED.md |
| Task 2.4 | Scaffold clustering of top-20 (RDKit Murcko) | ⚪ pending |  |

### Aim 3

| Task | Title | Status | Evidence |
|------|-------|--------|----------|
| Task 3.1 | PubMed sweep "PHGDH all</strong> allosteric / RBD" 2024-2026 | ✅ DONE | via COMPLETED.md |
| Task 3.2 | Wiki page `phgdh-scavenger` — pipeline, schema, output | ⚪ pending |  |
| Task 3.2.a | Document technical pipeline & data schema | ⚪ pending |  |
| Task 3.2.b | Create "How-to" guide for scaffold scavenger | ⚪ pending |  |
| Task 3.3 | Monthly 2025 AI-drug-discovery digest (Jan 2025) | ⚪ pending |  |
| Task 3.3.a | ArXiv curation (Jan 2025) | ⚪ pending |  |
| Task 3.3.b | Generate summary for Telegram/Wiki | ⚪ pending |  |
| Task 3.4 | Publish 3 wiki drafts + 20 Gemma concept stubs | ⚪ pending |  |
| Task 3.4.a | Metadata & link audit for new pages | ⚪ pending |  |
| Task 3.4.b | Git automation (commit/push) for all drafts | ⚪ pending |  |

### Aim 4

| Task | Title | Status | Evidence |
|------|-------|--------|----------|
| Task 4.1 | Cheaha workspace setup + first dock | ✅ DONE | via COMPLETED.md |
| Task 4.2 | Vina top-20 × 6RIH K4T pocket — ranked CSV + scatter | ✅ DONE | artifact: aim4_vina_top20_ranked.csv (635B) |
| Task 4.2.a | Filter hits by docking score | ⚪ pending |  |
| Task 4.2.b | Cluster hits by scaffold | ⚪ pending |  |
| Task 4.2.c | Re-score top-50 with short MD | ⚪ pending |  |
| Task 4.2.d | Generate Scatter plot (Score vs. Ligand Efficiency) | ⚪ pending |  |
| Task 4.2.e | Export ranked results to CSV | ⚪ pending |  |
| Task 4.3 | Scale-out: top-500 SMILES virtual screen | ⚪ pending |  |
| Task 4.4 | Port Fan Li 2026 CLM: LSTM pretrain + 5-step incremental FT on PHGDH SMILES | ⚪ pending |  |
| Task 4.5 | Vina rerank top-500 CLM generations into 6RIH K4T pocket | ⚪ pending |  |
| Task 4.6 | Bimodal combined-score shortlist + synthesis triage | ⚪ pending |  |

### Aim 5

| Task | Title | Status | Evidence |
|------|-------|--------|----------|
| Task 5.1 | Paper introduction draft | ⚪ pending |  |
| Task 5.2 | Repo README + pipeline diagram | ⚪ pending |  |
| Task 5.3 | Poster (L4 deliverable) | ⚪ pending |  |

