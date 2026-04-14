---
title: QNAS: A Neural Architecture Search Framework for Accurate and Efficient Quantum Neural Networks
created: 2024-05-22
source: https://arxiv.org/abs/2604.07013
tags: [quantum computing, neural architecture search, NISQ, optimization, hybrid-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "QNAS: A Neural Architecture Search Framework for Accurate and Efficient Quantum Neural Networks"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/qnas-a-neural-architecture-search-framework-for-accurate-and-efficient-quantum-n.md
dc.language: en
dc.rights: CC-BY-4.0
---

# QNAS: A Neural Architecture Search Framework

The paper introduces **QNAS**, an advanced [[qnas-a-neural-architecture-search-framework-for-accurate-and-efficient-quantum-n|Neural Architecture Search]] (NAS) framework specifically engineered to address the complexities of designing [[shot-based-quantum-encoding-a-data-loading-paradigm-for-quantum-neural-networks|Quantum Neural Networks]] (QNNs) for use on [[NISQ hardware]]. A primary challenge in the current era of quantum computing is the difficulty of designing ansatze that balance high expressivity and trainability with the severe resource constraints of near-term devices.

### The QNAS Framework

Designing efficient models often requires [[Circuit Cutting]] to manage limited qubit availability; however, existing methods often ignore the exponential computational overhead this process introduces. QNAS addresses this by providing a unified, hardware-aware evaluation system for [[Hybrid Quantum-Classical Neural Networks]] (HQNNs). 

The framework utilizes a shared parameter "SuperCircuit" and employs the [[NSGA-II]] algorithm to perform multi-objective optimization. The search evaluates candidate architectures based on three critical dimensions:
1. **Validation Error:** Minimizing prediction error to ensure accuracy.
2. **Runtime Cost Proxy:** Measuring the estimated wall-clock evaluation time.
3. **Cutting Overhead:** Optimizing the number of subcircuits required under a specific qubit budget.

### Experimental Benchmarks

QNAS demonstrates significant performance gains across various datasets, uncovering clear Pareto fronts that illustrate the trade-offs between accuracy and efficiency:

* **MNIST:** Achieved a 97.16% test accuracy using a highly compact 8-qubit, 2-layer circuit.
* **Fashion-MNIST:** Achieved 87.38% accuracy with a 5-qubit, 2-layer configuration.
* **Iris (Tabular Data):** Reached 100% validation accuracy using a minimal 4-qubit, 2-layer architecture.

### Design Insights

