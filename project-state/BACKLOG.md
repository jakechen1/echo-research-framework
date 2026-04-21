# Backlog — organized by Aim and Task

*Statuses are auto-maintained by `plan-sync` skill — do not hand-edit status
columns. See `project-state/PLAN_STATUS.md` for live rollup.*

Canonical taxonomy per PROJECT_TAXONOMY.md. Stage codes in STAGE_CODES.md.

## Aim 1 — Automated data pipeline

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 1.1 | Daily ChEMBL scavenge + delta reporting | G-001 | local | — | **DONE** |
| Task 1.2 | Scaveng→Hermes enrichment loop (rank new molecules, seed wiki pages) | G-012 | Hermes + local | 2 d | pending |
| Task 1.2.a | Implement ranker script for ChEMBL delta parsing | — | local | — | subtask pending |
| Task 1.2.b | Automated wiki stub creation for top hits | — | Hermes | — | subtask pending |
| Task 1.3 | Entity-page templates (molecule / target / pathway / gene-set) | G-013 | Hermes | 1 d | pending |
| Task 1.3.a | Molecule template design (SMILES, properties) | — | Hermes | — | subtask pending |
| Task 1.3.b | Target/Pathway template design (UniProt, KEGG) | — | Hermes | — | subtask pending |

## Aim 2 — Computational analysis of PHGDH inhibitors

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 2.1 | pChEMBL distribution figure | G-002 | local | — | **DONE** |
| Task 2.2 | Top-20 PHGDH inhibitors by pChEMBL ≥ 7 | G-003 | local | — | **DONE** |
| Task 2.3 | PDB binding-site annotation (4NJN/6RIH/7S3R + more) | G-005 | local | — | **DONE** |
| Task 2.4 | Scaffold clustering of top-20 (RDKit Murcko) | G-014 | local | 1 d | pending |

## Aim 3 — Literature synthesis & knowledge graph

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 3.1 | PubMed sweep "PHGDH all</strong> allosteric / RBD" 2024-2026 | G-004 | local | — | **DONE** |
| Task 3.2 | Wiki page `phgdh-scavenger` — pipeline, schema, output | G-008 | Hermes | 1 d | pending |
| Task 3.2.a | Document technical pipeline & data schema | — | Hermes | — | subtask pending |
| Task 3.2.b | Create "How-to" guide for scaffold scavenger | — | Hermes | — | subtask pending |
| Task 3.3 | Monthly 2025 AI-drug-discovery digest (Jan 2025) | G-011 | Hermes | 2 d | pending |
| Task 3.3.a | ArXiv curation (Jan 2025) | — | Hermes | — | subtask pending |
| Task 3.3.b | Generate summary for Telegram/Wiki | — | Hermes | — | subtask pending |
| Task 3.4 | Publish 3 wiki drafts + 20 Gemma concept stubs | G-015 | user-gated | 1 d | pending |
| Task 3.4.a | Metadata & link audit for new pages | — | local | — | subtask pending |
| Task 3.4.b | Git automation (commit/push) for all drafts | — | local | — | subtask pending |

## Aim 4 — Structure-based virtual screening on Cheaha HPC

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 4.1 | Cheaha workspace setup + first dock | G-006 | cheaha | — | **DONE** |
| **Task 4.2** | Vina top-20 × 6RIH K4T pocket — ranked CSV + scatter | G-007 | cheaha | 1 d | **IN_PROGRESS** |
| Task 4.2.a | Filter hits by docking score | — | cheaha | — | subtask pending |
| Task 4.2.b | Cluster hits by scaffold | — | local (rdkit) | — | subtask pending |
| Task 4.2.c | Re-score top-50 with short MD | — | cheaha | 2 d | subtask pending |
| Task 4.2.d | Generate Scatter plot (Score vs. Ligand Efficiency) | — | local | — | subtask pending |
| Task 4.2.e | Export ranked results to CSV | — | local | — | subtask pending |
| Task 4.3 | Scale-out: top-500 SMILES virtual screen | G-016 | cheaha | 3 d | pending |
| Task 4.4 | Port Fan Li 2026 CLM: LSTM pretrain + 5-step incremental FT on PHGDH SMILES | G-018 | local (L0 GPU) | 3 d | **ACTIVE** |
| Task 4.5 | Vina rerank top-500 CLM generations into 6RIH K4T pocket | G-019 | cheaha | 2 d | pending |
| Task 4.6 | Bimodal combined-score shortlist + synthesis triage | G-020 | local | 1 d | pending |

## Aim 5 — Scientific deliverables

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 5.1 | Paper introduction draft | G-009 | Chrome-Claude | 2 d | pending |
| Task 5.2 | Repo README + pipeline diagram | G-010 | local | 1 d | pending |
| Task 5.3 | Poster (L4 deliverable) | G-017 | local | 3 d | pending |

## Aim ∞ — Infrastructure (cross-cutting, complete 2026-04-18)

| Task | Title | Status |
|------|-------|--------|
| Inf.1 | liveness-audit skill | **DONE** |
| Inf.2 | age-scoring skill (reverse-NIH + samplers + baselines) | **DONE** |
| Inf.3 | notifier skill (Telegram proactive) | **DONE** |
| Inf.4 | resilience skill (atomic + queues + checkpoint + boot recovery) | **DONE** |
| Inf.5 | auto-forresolver skill (playbook + escalation ladder) | **DONE** |
| Inf.6 | plan-sync skill (auto BACKLOG reconciliation) | **DONE** |
| Inf.7 | STAGE_CODES.md (X = eXpense canonical) | **DONE** |

## Rules
- One task active at atime (PLEASER-ONE).
- `plan-sync` updates this file automatically — do not hand-edit statuses.
- Task promotion respects Aim dependencies (e.g. Task 4.2 needs 4.1; Task 5.1 needs Aim 2 + 3 output).
- When stuck > 3 attempts, escalate to Resolver (see PROJECT_TAXONOMY.md §5).
