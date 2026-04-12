# Research Decision Log: Strategic Session Re-Architecture
**Date:** 2026-04-11
**Project:** PHGDH Allosteric Modulator Discovery
**Status:** Active Execution (Aim 1)

## 🧠 Executive Summary
This session marks a fundamental pivot from task-oriented execution to a high-level **Scientific Research Program** architecture. We have moved from tracking simple "to-do" items to managing a hierarchy of **Research Aims**, each with its own hypothesis, methodology, and validation criteria. Additionally, we have implemented rigorous data provenance and operational tracking systems to ensure long-term research integrity.

---

## 🧬 Strategic Re-Architecture: The "Research Aim" Framework

The project has been restructured into a modular, hierarchical framework designed for scientific reproducibility and scalable complexity.

### **Established Research Aims**
*   **Aim 1: Functional Identification of PHGDH Allosteric Modulators**
    *   *Objective:* High-throughput screening and lead extraction from docking datasets.
    *   *Current Status:* **Active Execution (Task 1.3.4)**.
*   **Aim 2: Proteome-Wide Specificity & Risk Assessment**
    *   *Objective:* Utilizing DrugCLIP/BioNeMo embeddings to predict and mitigate off-target reactivity.
*   **Aim 3: Conformational Dynamics & Allosteric Mechanism Validation**
    *   *Objective:* MD simulations to prove functional change in the RGG/RBD interface.
*   **Aim 4: Lead Optimization & Chemical Expansion**
    *   *Objective:* Iterative SAR expansion and library growth.

**Key Rule Change:** Each Aim is now a self-contained investigation. Success is defined by mission-specific validation criteria (e.g., $\Delta G$ thresholds), not just task completion.

---

## 📊 Operational Infrastructure Deployment

To manage the increased complexity, three new persistent tracking systems were deployed:

1.  **The Token Ledger (`~/reports/token_usage_ledger.md`)**
    *   Tracks the computational "weight" and token-cost of session windows.
    *   Provides visibility into the financial/computational footprint of the research.
2.  **The Project Clock (`~/reports/project_timeline.md`)**
    *   Tracks the temporal progress of each Aim.
    *   Enables **Drift Analysis** (comparing estimated vs. actual completion time).
3.  **The Dual-Stream Data Pipeline**
    *   **Narrative Stream (Box):** High-level reasoning, decision logs (in `.md`), and processed reports.
    *   **Data Stream (GitHub/Local):** Raw docking logs, molecular structures (PDB/SDF), and processed CSVs/JSONs.
    *   **The Notion Journal:** High-level "Lab Notebook" for conceptual breakthroughs and scientific "wins."

---

## 🛠️ Decision Log
| Decision | Rationale | Impact |
| :--- | :--- | :--- |
| **Adopt "Research Aim" Hierarchy** | Elevate project from task-list to scientific program. | Enables modularity and backup plans for failed experiments. |
| **Implement Token/Time Tracking** | Ensure visibility into computational costs and timeline drift. | Enables proactive resource management. |
| **Automated Data Routing** | Ensure scientific provenance and automated archiving. | Eliminates manual error in data preservation. |

***
*End of Session Export.*
