---
tier: public
status: published
title: "PHGDH Vina Top-20 Dock Results (6RIH K4T pocket)"
tags: [phgdh, docking, vina, allosteric, task-4-2]
created: 2026-04-19
author: jakeclaw-task-4-2-autonomous
---

# PHGDH Vina Top-20 Dock Results

Part of [[Aim-4-Cheaha-SBDD]] — ranks the top-20 [[Top-20-PHGDH-Inhibitors]]
(pChEMBL ≥ 7) by AutoDock Vina affinity in the [[3d-architecture-of-phgdh|6RIH K4T]]
allosteric pocket. Companion to [[bimodal-generation-comparison-2026]] (Track 1 filter).

## Method
- Receptor: 6RIH (human PHGDH, K4T-bound allosteric form)
- Pocket center: (14.11, 10.46, 80.98) from K4T centroid
- Box: 25×25×25 Å
- Vina exhaustiveness=8, 5 modes, randomSeed=42
- Ligand prep: RDKit MMFF + openbabel gasteiger partial charges
- Cheaha array-job on express partition, 1 ligand per array task

See `data/aim4_vina_top20_ranked.csv` + `figures/vina_vs_pchembl.png` for results.
