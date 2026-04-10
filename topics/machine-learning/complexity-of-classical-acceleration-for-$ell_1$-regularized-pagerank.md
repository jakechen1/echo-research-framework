---
title: Complexity of Classical Acceleration for $\ell_1$-Regularized PageRank
created: 2024-05-23
source: https://arxiv.org/abs/2602.21138
tags: [machine-learning, optimization, algorithms, graph-theory]
category: machine-learning
---

# Complexity of Classical Acceleration for $\ell_1$-Regularized PageRank

This article explores the computational complexity and convergence behavior of applying accelerated proximal-gradient methods, specifically the **Fast Iterative Shrinkage-Thresholding Algorithm (FISTA)**, to the problem of computing $\ell_1$-regularized [[PageRank]].

## Overview

In the context of [[graph-theory]] and [[network-science]], computing the $\ell_1$-regularized [[PageRank]] is a vital task for identifying influential nodes in sparse structures. The efficiency of this computation is heavily dependent on two key parameters: the teleportation parameter $\alpha$ and the $\ell_1$-regularization parameter $\rho$. 

Prior research into the non-accelerated **Iterative Shrinkage-Thresholding Algorithm (ISTA)** established a worst-case work complexity of $\widetilde{O}((\alpha\rho)^{-1})$. A major open question in [[optimization]] was whether classical acceleration techniques could improve the dependency on the teleportation parameter from $1/\alpha$ to $1/\sqrt{\alpha}$ while maintaining the $1/\rho$ locality scaling.

## Key Findings

The paper presents a nuanced view of [[accelerated proximal-gradient]] performance, providing both negative and positive theoretical results:

*   **The Negative Result:** The authors demonstrate that standard **FISTA** is not a universal improvement. Through the construction of specific graph instances, they prove that FISTA can be asymptotically worse than the non-accelerated **ISTA**.
*   **The Positive Result:** The researchers identify a regime where acceleration is beneficial. By analyzing a slightly over-regularized objective function under a specific "confinement condition," they show that spurious activations are restricted to a boundary set $\mathcal{B}$. 
*   **Complexity Bound:** In this confined regime, the complexity bound is composed of an accelerated term, $(\rho\sqrt{\alpha})^{-1}\log(\alpha/\varepsilon)$, and a boundary overhead term, $\sqrt{vol(\mathcal{B})}/(\rho\alpha^{3/2})$.

## Implications

The research contributes to the field of [[machine-learning]] by providing the structural graph conditions necessary to guarantee the efficacy of accelerated methods. This is particularly significant for [[large-scale graph analysis]], where understanding the trade-offs between regularization and convergence speed is critical for efficient [[algorithm]] design.