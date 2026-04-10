---
title: Orthogonal Representation Learning for Estimating Causal Quantities
created: 2024-05-22
source: https://arxiv.org/abs/2502.04274
tags: [causal-inference, machine-learning, representation-learning, statistics]
category: machine-learning
---

# Orthogonal Representation Learning for Estimating Causal Quantities

The paper "Orthogonal Representation Learning for Estimating Causal Quantities" addresses a fundamental discrepancy in [[causal inference]] methodologies: the gap between the practical performance of [[end-to-end representation learning]] and the theoretical rigor of [[Neyman-orthogonal learners]].

## The Central Tension

In the era of high-dimensional observational data, researchers face a difficult trade-off between two primary-stage approaches for estimating causal quantities:

1.  **End-to-End Representation Learning:** These methods are highly effective in practice for feature extraction but suffer from a lack of **quasi-oracle efficiency**, meaning they lack certain asymptotic optimality properties.
2.  **Two-Stage Neyman-Orthogonal Learners:** These learners provide essential theoretical guarantees and efficiency; however, they do not explicitly benefit from the powerful dimensionality reduction capabilities provided by modern [[representation learning]].

## The OR-Learner Framework

To resolve this tension, the authors introduce a unifying framework known as **OR-learners**. The research focuses on two primary research questions:
*   Under what conditions do learned representations actually strengthen existing Neyman-orthogonal learners?
*   Can the **balancing constraint**—a popular technique in representation learning—serve as a substitute for Neyman-orthogonality?

## Key Findings

The study provides several critical insights into the intersection of [[deep learning]] and [[statistics]]:

*   **Manifold Hypothesis Advantage:** The authors prove that under the **low-dimensional manifold hypothesis**, OR-learners can strictly improve the estimation error compared to standard Neyman-orthogonal learners. This suggests that proper feature extraction can enhance theoretical efficiency.
*   **Limitations of Balancing Constraints:** The research finds that balancing constraints require an additional inductive bias and are insufficient to compensate for the lack of Neyman-orthogonality found in end-to-end approaches.
*   **Practical Guidelines:** The paper concludes by offering specific guidelines for researchers on how to effectively combine the strengths of representation learning with the theoretical guarantees of classical [[statistical inference]].

This work serves as a foundational bridge for developing algorithms that are both practically performant in high-dimensional settings and theoretically sound for reliable causal estimation.