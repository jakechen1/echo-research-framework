---
title: "Master-Blueprint: PHGDH-Allosteric-RBD-Binder"
created: 2026-04-14
category: methodology
author: jakeclaw
node_level: N0
dc.title: "Master-Blueprint: PHGDH-Allosteric-RBD-Binder"
dc.creator: jakeclaw
dc.date: 2026-04-14
---

# 🧬 Master-Blueprint: Project PHGDH-Allosteric-RBD-Binder

## 🎯 Scientific Objective
To discover and validate novel allosteric modulators for the **PHGDH (Phosphoglycerate Dehydrogenase) RNA-Binding Domain (RBD)**. The goal is to disrupt the protein-RNA interface (RGG motif) to prevent downstream metabolic dysregulation without impacting the catalytic domain.

---

## 🏗️ The PLEASER-ONE Framework
All research, computation, and reporting within this project must adhere to the **PLEASER-ONE** framework to ensure rigorous, traceable, and autonomous execution.

### 1. P (Planning & Decomposition)
Tasks are decomposed using **x.y.z notation** (Aim.Task.Subtask).
*   **Aim 1:** RBD-Selective Binding (Docking)
*   **Aim 2:** Cross-Reactivity Prediction (Embedding/DrugCLIP)
*   **Aim 3:** Generative Molecular Design (LM-CR)

### 2. L (Learning & Discovery)
Continuous ingestion of new literature, protein structures (PDB), and chemical libraries.

### 3. E (Execution)
Automated pipelines for docking, scoring, and molecular dynamics.

### 4. S (Sharing/Reporting)
All findings are documented in the Project Wiki and pushed to repository/SAG/Box.

### 5. R (Reporting/Reflection)
Internal logs and error tracking for all computational workflows.

---

## 🔬 Active Workstreams
- **Workstream A:** Docking simulations for candidate libraries.
- **Workstream B:** Descriptor calculation for feature selection.
- **Workstream C:** LLM-based ligand optimization.

## 📂 Repository Structure
- `/data/docking_results/`
- `/data/descriptors/`
- `/src/analysis_scripts/`
- `/docs/experiment_logs/`
