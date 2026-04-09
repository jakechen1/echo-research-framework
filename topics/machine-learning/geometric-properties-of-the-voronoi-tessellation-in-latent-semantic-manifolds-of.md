---
title: Geometric Properties of the Voronoi Tessellation in Latent Semantic Manifolds of Large Language Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.06767
tags: [ai, machine-learning, geometry, optimization, neural-networks]
---

# Geometric Properties of the Voronoi Tessellation in Latent Semantic Manifolds of LLMs

This article explores the geometric structure of [[Large Language Models]] (LLMs) through the lens of [[Voronoi tessellation]]. While LLMs fundamentally process discrete tokens, their computations occur within continuous [[Latent Space]] manifolds. This study, conducted on the Qwen3.5-4B-Base architecture, examines how token boundaries are formed and how these boundaries can be mathematically manipulated post-training.

## Scaling Laws and Geometric Ambiguity

The research provides significant empirical validation for Mabrok’s (2026) theory regarding the linear scaling law of the expressibility gap, achieving a highly precise $R^2$ of 0.9997. A key discovery is the identification of a "mid-layer geometric ambiguity regime." Within layers 24-28, the researchers observed that the geometry of the token margins is actually anti-correlated with [[Cross-Entropy]] loss ($\rho = -0.29$). This geometric ambiguity eventually resolves as the signal moves toward the output, where margins and loss functions align closely ($\rho = 0.836$) at the final layer.

## Margin Refinement Procedures (MRP)

A major contribution of this paper is the introduction of [[Margin Refinement Procedures]] (MRP). These are short, post-hoc optimization techniques designed to reshape the Voronoi tessellation to widen token-decision margins without the need for full model retraining.

The study compares two primary strategies for refinement:

*   **Direct Margin Maximization:** Focuses on increasing the distance between token boundaries but suffers from escalating "collateral damage" (unintended shifts in other token boundaries) as intervention strength increases.
*   **Fisher Information Distance Maximization:** Utilizes [[Fisher Information]] to guide refinement. This method maintains a constant level of collateral damage