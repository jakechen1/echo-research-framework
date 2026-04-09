---
title: Resistance Distance and Linearized Optimal Transport on Graphs
created: 2024-05-23
source: https://arxiv.org/abs/2404.15261
tags: [graph-theory, optimal-transport, mathematics, probability, network-science]
category: machine-learning
---

# Resistance Distance and Linearized Optimal Learning on Graphs

The paper *Resistance Distance and Linearized Optimal Transport on Graphs* explores the mathematical properties of discrete transportation distances on finite weighted graphs. Building on the foundational work of Maas regarding the gradient flows of entropy for [[Markov Chains]], the authors investigate the linearization of transportation distances between probability distributions.

## Core Findings

The central achievement of this research is a nonasymptotic local linearization theorem. This theorem states that if a probability distribution $\nu$ behaves as a small additive perturbation of a reference density $\mu$, their squared discrete transportation distance is controlled by the quadratic form of the pseudoinverse of a re-weighted [[Graph Laplacian]] matrix. 

A significant consequence occurs when the reference measure is stationary for a simple random walk on the graph. In this specific state, the weights of the matrix align with the original graph structure, effectively representing the distance as a form of [[Resistance Distance]] between probability measures.

## Combinatorial and Variational Characterizations

The authors demonstrate that this linearized distance is deeply embedded in the structural properties of the graph. They provide several distinct characterizations, including:

*   **Variational Formulas:** The Beckmann and Benamou–Brenier formulas.
*   **Structure-based Formulas:** A spanning 2-forest formula and a dual homogeneous Sobolev norm formula.
*   **Stochastic Representations:** Representations utilizing random walk hitting times.

## Geometric Implications for Random Walks

The research further investigates the "resistance manifold" resulting from this distance metric. The authors prove that the gradient flow of the $\chi^2$ functional on this manifold is equivalent to the continuous-time [[Random Walk]]. 

Crucially, the study connects geometry to convergence rates by showing that the geodesic strong convexity modulus is equal to the [[Spectral Gap]] of the normalized Laplacian. This provides a rigorous geometric vantage point to recover the classical mathematical fact that the spectral gap governs the exponential rate at which a random walk converges to its stationary distribution.

This work provides significant theoretical foundations for [[Machine Learning]] applications involving diffusion processes, information geometry, and analysis on complex networks.