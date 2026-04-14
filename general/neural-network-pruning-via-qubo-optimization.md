---
title: Neural Network Pruning via QUBO Optimization
created: 2024-05-23
source: https://arxiv.org/abs/2604.05856
tags: [neural networks, pruning, optimization, compression, QUBO]
categories: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "Neural Network Pruning via QUBO Optimization"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/neural-network-pruning-via-qubo-optimization.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Neural Network Pruning via QUBO Optimization

[[neural-network-pruning-via-qubo-optimization|Neural network pruning]] is a vital technique in [[Neural network compression]], aimed at reducing model complexity and memory footprint without sacrificing predictive accuracy. Historically, most pruning strategies have relied on greedy heuristics, such as the L1-norm, which evaluate filters in isolation. However, these approaches often fail to account for the complex, non-linear interactions and functional redundancies between different filters within a network.

This article presents a novel **Hybrid QUBO framework** designed to treat pruning as a formal combinatorial optimization problem using [[Quadratic Unconstrained Binary Optimization (QUBO)]]. To overcome the limitations of previous optimization-based methods, this framework introduces a more sophisticated objective function:

*   **Linear Term:** Incorporates gradient-aware sensitivity metrics, specifically utilizing first-order [[Taylor expansion]] and second-order [[Fisher information]] to determine individual filter importance.
*   **Quadratic Term:** Utilizes data-driven activation similarity to capture and mitigate inter-filter functional redundancy.

To maintain structural integrity during the pruning process, the authors introduce a **dynamic capacity-driven search**. This mechanism strictly enforces target sparsity levels, ensuring the pruned model meets specific resource constraints without distorting the optimization landscape.

The proposed methodology follows a two-stage pipeline. Following the initial QUBO optimization, a **Tensor-Train (TT) Refinement** stage is applied. This stage functions as a gradient-free optimizer that fine-tunes the solution directly against the true evaluation metric, compensating for any inaccuracies in the initial combinatorial approximation.

Experimental evaluations conducted on the SIDD image denoising dataset demonstrate that the Hybrid QUBO approach significantly outperforms both traditional L1-based QUBO and greedy Taylor pruning. The integration of TT Refinement provides consistent performance gains, particularly at larger combinatorial scales. This research highlights the potential of using hybrid combinatorial formulations to create more robust, scalable, and interpretable models in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]].