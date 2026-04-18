# Backlog — organized by Aim and Task

Canonical taxonomy per PROJECT_TAXONOMY.md. One active task at a time.

## Aim 1 — Automated data pipeline
*Continuous, self-enriching PHGDH bioactivity data flowing into a living knowledge graph.*

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 1.1 | Daily ChEMBL scavenge + delta reporting | G-001 | local | — | **DONE** |
| Task 1.2 | Scavenger→Hermes enrichment loop (rank new molecules, seed wiki pages) | G-012 | Hermes + local | 2 d | pending |
| Task 1.3 | Entity-page templates (molecule / target / pathway / gene-set) | G-013 | Hermes | 1 d | pending |

## Aim 2 — Computational analysis of PHGDH inhibitors
*Profile existing chemical space; triage candidates for prioritization.*

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| **Task 2.1** | pChEMBL distribution figure | G-002 | local (matplotlib) | 1 d | **ACTIVE** |
| Task 2.2 | Top-20 PHGDH inhibitors by pChEMBL ≥ 7, cross-ref assays | G-003 | local | 1 d | pending |
| Task 2.3 | PDB structure download (4NJN, 6RIH, 7S3R) + binding-site annotation | G-005 | local | 1 d | pending |

## Aim 3 — Literature synthesis & knowledge graph
*Grow a grounded, source-validated wiki of PHGDH biology, drug discovery, and methods.*

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 3.1 | PubMed sweep for "PHGDH allosteric" / "PHGDH RBD" 2024-2026 | G-004 | Hermes | 1 d | pending |
| Task 3.2 | Wiki page `phgdh-scavenger` — pipeline, schema, daily output | G-008 | Hermes | 1 d | pending |
| Task 3.3 | Monthly 2025 AI-drug-discovery digest (Jan 2025) | G-011 | Hermes | 2 d | pending |

## Aim 4 — Structure-based virtual screening on Cheaha HPC
*In silico discovery and triage of novel PHGDH modulators.*

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 4.1 | Cheaha workspace setup + seed SMILES rsync (top-500 by pChEMBL) | G-006 | cheaha | 1 d | pending |
| Task 4.2 | First SBDD virtual-screen sbatch on amperenodes (≤ 100-ligand test) | G-007 | cheaha | 1 d | pending |
| Task 4.2.a | Filter hits by docking score | — | cheaha | — | subtask pending |
| Task 4.2.b | Cluster hits by scaffold | — | local (rdkit) | — | subtask pending |
| Task 4.2.c | Re-score top-50 with short MD | — | cheaha | — | subtask pending |

## Aim 5 — Scientific deliverables
*Paper, slides, public wiki — make the work citable.*

| Task | Title | Legacy ID | Tier | ETA | Status |
|------|-------|-----------|------|-----|--------|
| Task 5.1 | Paper introduction draft | G-009 | Chrome-Claude | 2 d | pending |
| Task 5.2 | Repo README + pipeline diagram | G-010 | local | 1 d | pending |

## Rules
- One task active at a time (PLEASER-ONE principle).
- Task promotion respects Aim dependencies (e.g., Task 4.2 needs 4.1; Task 5.1 needs early Aim 2 + Aim 3 output).
- Subtask activation only when parent Task is the active task.
- When stuck >3 attempts, escalate to Resolver (see PROJECT_TAXONOMY.md §5).
