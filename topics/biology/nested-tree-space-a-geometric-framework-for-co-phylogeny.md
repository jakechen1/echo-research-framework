---
title: Nested tree space: a geometric framework for co-phylogeny
created: 2024-05-22
source: https://arxiv.org/abs/2604.05056
tags: [phylogenetics, geometry, mathematical-biology, evolution]
category: biology
---

# Nested tree space: a geometric framework for co-phylogeny

The paper **"Nested tree space: a geometric framework for co-phylogeny"** introduces a novel mathematical structure, known as $\sigma$-space, designed to model [[co-evolutionary systems]]. These systems are characterized by a hierarchical evolutionary relationship where one evolutionary history is embedded within another, a phenomenon most commonly observed in [[host-parasite]] interactions.

### The $\sigma$-space Construction

The authors define $\sigma$-space as a moduli space consisting of fully nested [[ultrametric phylogenetic trees]] with a fixed leaf map. This framework represents a significant generalization of the $\tau$-space originally proposed by Gavryushkin and Drummond. Mathematically, $\sigma$-space is constructed as a cubical complex. This complex is parameterized by two primary components:
1. Nested ranked tree topologies.
2. The inter-event time coordinates of the combined host and parasite speciation events.

To manage the complexity of these evolutionary histories, the researchers characterize admissible orderings through the implementation of binary *nesting sequences*, which are organized into a natural partially ordered set (poset).

### Geometric Properties and Implications

A central achievement of this research is the demonstration that $\sigma$-space is contractible and satisfies Gromov's cube condition. As a result, the space is classified as a [[CAT(0)]] space. This geometric classification carries profound implications for [[mathematical biology]] and computational phylogenetics:
* **Unique Geodesics:** The $\text{CAT}(0)$ property ensures that there is a single, well-defined shortest path between any two points in the space.
* **Fréchet Means:** The space allows for well-defined Fréchet means, providing a robust method for calculating the "average" tree within a dataset of co-evolutionary histories.

Furthermore, the paper describes the boundary strata of the space, which correspond to specific [[cospeciation]] events. By utilizing natural forgetful maps, the authors relate $\sigma$-space to products of [[ultrametric tree spaces]], establishing a comprehensive geometric foundation for the study of complex, interdependent biological lineages.