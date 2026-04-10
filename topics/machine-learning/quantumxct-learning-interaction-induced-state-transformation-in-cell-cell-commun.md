---
title: "QuantumXCT: Learning Interaction-Induced State Transformation in Cell-Cell Communication via Quantum Entanglement and Generative Modeling"
created: 2024-05-22
source: "https://arxiv.org/abs/260\_2203"
tags: [quantum-computing, bioinformatics, generative-modeling, single-cell-analysis]
category: ai
---

# QuantumXCT

[[QuantumXCT]] is a novel hybrid [[quantum machine learning]] framework designed to advance the study of [[cell-cell communication]] (CCC). Traditional methods for inferring communication from [[single-cell RNA-seq]] data are typically limited by their reliance on pre-curated [[ligand-receptor]] databases. These databases primarily identify co-expression patterns but often fail to capture the system-level, dynamic changes in [[cellular states]] triggered by signaling events.

## Methodology

QuantumXCT addresses these limitations by reframing CCC as a generative problem of learning interaction-induced state transformations. The framework employs the following mechanism:

1.  **Encoding**: Transcriptomic profiles are encoded into a high-dimensional [[Hilbert space]].
2.  **Transformation**: The model utilizes [[parameterized quantum circuits]] to learn a unitary transformation.
3.  **Mapping**: This transformation maps the distribution of a baseline, non-interacting cellular state to a new, interacting cellular state.

Unlike traditional approaches, this method does not require prior biological assumptions, enabling the *de novo* discovery of communication-driven changes in cellular distributions.

## Results and Interpretability

In validation experiments using both synthetic data and ovarian cancer-fibroblast co-culture models, QuantumXCT demonstrated high accuracy in recovering complex regulatory dependencies, including regulatory feedback structures. The model successfully identified critical communication hubs, such as the PDGFB-PDGFRB-STAT3 axis.

