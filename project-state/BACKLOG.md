# Backlog — prioritized

Next 10 sub-goals, one day each. Move to CURRENT_GOAL.md when picked, move to
COMPLETED.md when done.

| # | Sub-goal | Tier | ETA |
|---|----------|------|-----|
| G-002 | Plot pChEMBL distribution of latest PHGDH scavenge; commit figure to repo `figures/pchembl_dist.png` | local (matplotlib) | 1 d |
| G-003 | Top 20 PHGDH inhibitors by pChEMBL ≥ 7; cross-ref with ChEMBL assay types; write to `workspace/phgdh/top20.md` | local | 1 d |
| G-004 | Search PubMed for "PHGDH allosteric" + "PHGDH RBD" 2024-2026; grow wiki pages via Hermes wiki-builder | Hermes | 1 d |
| G-005 | Download PHGDH crystal structures (PDB 4NJN, 6RIH, 7S3R) to `workers/data/pdb/`; annotate binding sites | local | 1 d |
| G-006 | Set up ~/phgdh on cheaha; rsync seed SMILES (top-500 by pChEMBL) for docking | cheaha | 1 d |
| G-007 | Write SBDD virtual-screening sbatch: AutoDock Vina on `amperenodes`; submit ≤ 100-ligand test | cheaha | 1 d |
| G-008 | Grow wiki page `phgdh-scavenger` summarizing data sources, schema, and daily output | Hermes | 1 d |
| G-009 | Draft paper Introduction (PHGDH in neurodegeneration) in Box/PHGDH/paper/intro.md | Chrome-Claude | 2 d |
| G-010 | Add repo README + pipeline diagram + CONTRIBUTING | local | 1 d |
| G-011 | Monthly 2025 AI-drug-discovery digest for January (see wiki/research/drug_discovery_2025_progress.md) | Hermes | 2 d |
| G-012 | Build data→knowledge enrichment loop: phgdh_enrichment daemon reads scavenger JSONL, ranks new molecules/targets, seeds Hermes wiki pages for each, cross-links in wiki | Hermes + local | 2 d |
| G-013 | Entity-page templates (molecule / target / pathway / gene-set) with standardized frontmatter and wikilink conventions | Hermes | 1 d |

## Rules
- Only one sub-goal active at a time (PLEASER-ONE principle).
- When picking next, consider dependencies first (e.g. G-007 needs G-006).
- If stuck >3 attempts on a goal, escalate to jakechen.
