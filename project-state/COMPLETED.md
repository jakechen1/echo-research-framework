# Completed sub-goals

*Most recent first. Entry format:*
```
## G-NNN — <one-line summary>
- **Done:** YYYY-MM-DD
- **Artifacts:** <links to commits, files, wiki pages>
- **Verification:** <what proved it done>
- **Notes:** <tidbits for future reference>
```

---


## G-001 — Verify the PHGDH scavenger ran successfully (scheduled 02:00 daily) and sanity-check
- **Done:** 2026-04-18
- **Promoted-via:** promote_next_goal.sh
- **Notes:** auto-promoted after done-criteria satisfied

## G-002 — Task 2.1: pChEMBL distribution figure
- **Done:** 2026-04-18T12:00
- **Artifact:** /Users/jakeclaw/.openclaw/workspace/figures/pchembl_dist.png (53 KB)
- **Verification:** n=1011 pChEMBL values from 2613 ChEMBL rows; mean=5.995 median=5.840
- **AGE:** A=7 (accurate, matches known PHGDH bioactivity spread), G=6 (one snapshot), E=8 (<30 s wall time)
- **Parallel bonus:** Aims 3+4 prep done in same dispatch (PDBs, SMILES)

## G-003 — Task 2.2: Top-20 PHGDH inhibitors (pChEMBL ≥ 7)
- **Done:** 2026-04-18T12:47
- **Artifacts:** data/aim2_top20_inhibitors.csv, figures/top20_inhibitors.png, wiki_drafts/top20-phgdh-inhibitors.md
- **Rank 1:** CHEMBL4541133 (pChEMBL 9.52)
- **Notes:** dedupe by chembl_id keeping best pv

## G-005 — Task 2.3: PDB binding-site annotation
- **Done:** 2026-04-18T12:47
- **Artifacts:** data/aim2_pdb_binding_sites.json, wiki_drafts/phgdh-pdb-binding-sites.md
- **Findings:** 4NJN/2G76 apo; 6PLF=ONV, 6RIH=K4T, 7S3R=NH2 (5Å residue environments captured)

## G-004 — Task 3.1: PubMed PHGDH allosteric sweep 2024-2026
- **Done:** 2026-04-18T12:47
- **Artifacts:** data/aim3_pubmed_phgdh_allosteric.json, wiki_drafts/phgdh-allosteric-literature-2024-2026.md
- **Findings:** 29 unique papers via NCBI eutils esearch+esummary
