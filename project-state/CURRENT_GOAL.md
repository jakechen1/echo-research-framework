# Current Sub-Goal

**Aim:** Aim 4 — Structure-based virtual screening on Cheaha HPC
**Task:** Task 4.2
**Legacy ID:** G-007
**Started:** 2026-04-18T19:30 CDT
**Tier:** cheaha

## Goal
Scale Vina docking from 3-ligand smoke test to full top-20 from Task 2.2
against 6RIH K4T allosteric pocket. Produce ranked table.

## Definition of done
- [ ] All 20 top inhibitors docked (lig1..lig20_docked.pdbqt on Cheaha)
- [ ] `data/aim4_vina_top20_ranked.csv` with ChEMBL_ID, pChEMBL, best_affinity (kcal/mol), rmsd_lb
- [ ] Scatter plot pChEMBL vs docking score → `figures/vina_vs_pchembl.png`
- [ ] Wiki draft with table + scatter
