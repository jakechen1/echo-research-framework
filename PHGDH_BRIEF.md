---
title: "PHGDH Project Brief"
updated: 2026-04-18
source_of_truth: /Users/jakeclaw/.openclaw/workspace/project_info.md (Master-Blueprint)
---

# PHGDH Project — what we know (distilled)

## The target

**PHGDH** = D-3-phosphoglycerate dehydrogenase
- UniProt: **O43175** (human)
- ChEMBL target: **CHEMBL2311243** (from scavenger)
- Function: rate-limiting enzyme in the serine biosynthesis pathway
  (3-PG → 3-phosphohydroxypyruvate)
- Cofactor: NAD+ / NADH
- Quaternary structure: tetramer
- Key domains: substrate-binding (SBD), nucleotide-binding (NBD),
  allosteric-serine (ACT) regulatory domain, **regulatory-binding domain (RBD)**

## Why this target (project thesis)

1. **Neurodegeneration angle (primary).** PHGDH is dysregulated in
   Alzheimer's — evidence from proteomic and transcriptomic studies already
   indexed in our wiki (`phgdh-dysregulation-in-alzheimers-disease-pathogenesis`,
   `phgdh-and-amyloid-beta-interactions`).
2. **Allosteric / RBD sites, not the active site.** Active-site orthosteric
   inhibitors (NCT-503, CBR-5884) exist but have selectivity problems.
   Our thesis is that allosteric and RBD modulators can offer finer
   regulatory control — up OR down — for CNS application.
3. **Serine → D-serine → NMDA modulation.** Serine biosynthesis is linked
   to D-serine (NMDA co-agonist). Tuning PHGDH tunes synaptic signaling,
   relevant for Alzheimer's and other neurodegenerative diseases.

## Structures we care about

| PDB | Form | Notes |
|-----|------|-------|
| 4NJN | apo human PHGDH tetramer | reference apo |
| 6RIH | with orthosteric ligand | active-site benchmark |
| 7S3R | with allosteric pocket bound | allosteric reference (if matches our thesis) |

Others to download as G-005 progresses.

## Tools already in place

- **Data scavenger** — daily ChEMBL pull to
  `~/workers/data/phgdh/YYYY-MM-DD.jsonl`
  (2613 rows of bioactivity in today's file — SMILES, pChEMBL,
  standard_type, assay IDs)
- **Wiki (Hermes-built)** — 17 PHGDH pages already in `~/wiki/general/`
  and `~/.openclaw/workspace/topics/` covering: structure, SBDD,
  virtual screening, drug-discovery literature, deep-learning for
  binding affinity, serine pathway linkages, AD therapeutic strategies
- **Cheaha-HPC skill** — templates for CPU, single-GPU, multi-GPU,
  and array sbatch; wrappers for submit / status / cancel
- **UAB VPN** — openconnect + credentials in place; W0 can VPN on demand
  to reach internal UAB resources

## Near-term milestones (from BACKLOG.md)

- G-002: pChEMBL distribution figure (local — matplotlib)
- G-003: top-20 inhibitors table (local — pandas)
- G-004: PubMed sweep for allosteric/RBD literature (Hermes wiki-builder)
- G-005: PDB structure download + binding-site annotation (local — BioPython)
- G-006/G-007: Cheaha workspace setup + virtual-screening sbatch
- G-008: wiki page `phgdh-scavenger` summarizing the pipeline
- G-009: paper intro draft (Chrome-Claude)
- G-010: repo README + pipeline diagram
- G-011: January 2025 AI-drug-discovery digest

## Success criteria (project level)

(Copied from PROJECT_PLAN.md for easy reference.)

- [ ] ≥ 30 days of PHGDH bioactivity data accumulated
- [ ] ≥ 100 source-validated PHGDH wiki pages
- [ ] ≥ 1 SBDD virtual-screening run completed on Cheaha
- [ ] Paper draft: intro + methods + preliminary results sections
- [ ] Slide deck: 20+ slides
- [ ] ≥ 30 consecutive autonomous days (only Duo pushes from Jake)
- [ ] 0 unresolved incidents in RESOLUTION_LOG for 7+ days

## Note on project name drift

The `project_info.md` master-blueprint frontmatter says
**"PHGDH-Allosteric-RBD-Binder"** but the body says **"PHAGE"**. That was
a Gemma 4 tokenizer glitch when the model drafted the body. PHGDH is
correct; PHAGE is noise. This brief is canonical.
