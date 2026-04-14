---
title: Intensity Dot Product Graphs
created: 2024-05-22
source: https://arxiv.org/abs/2604.07810
tags: [machine-learning, network-science, stochastic-processes, graph-theory]
category: machine-learning
---

# Intensity Dot Product Graphs

**Intensity Dot Product Graphs (IDPGs)** represent a novel advancement in [[network-science|Network Science]] and [[stochastic-processes|Stochastic Processes]], providing a bridge between continuous latent structures and discrete graph observations. Introduced as an evolution of the [[random-dot-product-graphs|Random Dot Product Graphs]] (RDPGs) framework, IDPLs address a fundamental limitation in traditional latent-position models: the assumption of a fixed node set once the sample size is chosen.

## Core Methodology
While traditional RDPGs rely on a fixed collection of latent positions, IDPGs replace these with a [[poisson-point-process|Poisson point process]] situated within a [[euclidean-space|Euclidean space]]. This fundamental shift allows for models with random node populations, where edge probabilities are determined via dot-product affinities in the latent space.

The defining feature of IDPGs is the **population-level intensity**. This intensity function serves as the mathematical tether, linking the continuous underlying latent structure to the finite, observed graphs. This allows the model to capture the density and distribution of nodes across a latent landscape dynamically.

## Mathematical Framework
The theory introduces several continuous analogues to replace discrete graph properties:
*   **Heat Map**: A continuous-space representation of the traditional probability matrix.
*   **Desire Operator**: A continuous analogue of the adjacency-based affinity.

A significant theoretical contribution of the IDPG framework is the **spectral consistency result**. This theorem establishes a direct connection between the singular values of a graph's adjacency matrix and the spectrum of the underlying operator. Furthermore, the research provides a comparative analysis between IDPGs, [[graphon|Graphon]] models, and [[digraphon|Digraphon]] representations, demonstrating that classical RDPGs emerge as a concentrated limit of this more flexible model.

## Applications and Temporal Modeling
Because the IDPG model is parameterized by an evolving intensity, it is uniquely positioned for temporal analysis. By utilizing [[ae-vit-stable-long-horizon-parametric-partial-differential-equations-modeling|Partial Differential Equations]] (PDEs), the model can be naturally extended to track how network structures evolve over time, making it a potent tool for studying [[dynamic-networks|Dynamic Networks]].