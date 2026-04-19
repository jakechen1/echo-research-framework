# Task 4.2 Learning — prior art review

- Task 2.2 top-20: data/aim2_top20_inhibitors.csv, rank1 CHEMBL4541133 pv=9.52
- Task 4.1 smoke dock: CHEMBL4541133 → 6RIH K4T pocket = -6.2 kcal/mol
- Pocket center (K4T centroid from 6RIH): (14.11, 10.46, 80.98)
- Pocket box: 25×25×25 Å
- Receptor: data/pdbs/6RIH.pdb (allosteric, has real ligand reference)
- Scaffolding: Murcko via RDKit (Task 2.4 prep)
- Novelty metric: 1 - max Tanimoto to training pv≥7 set

**Strategy:** submit sbatch ARRAY job for 20 ligands (one task per ligand,
parallel on express partition), collect best ΔG per ligand, rerank by
combined score (dG_z + Tanimoto_novelty), emit CSV + scatter PNG.
