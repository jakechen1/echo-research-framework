---
title: Accelerated Sinkhorn Algorithms for Partial Optimal Transport
created: 2024-05-22
source: https://arxiv.org/abs/2601.17196
tags: [optimal-transport, sinkhorn-algorithm, acceleration, computational-complexity, machine-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Accelerated Sinkhorn Algorithms for Partial Optimal Transport"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/accelerated-sinkhorn-algorithms-for-partial-optimal-transport.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Accelerated Sinkhorn Algorithms for Partial Optimal Transport

The paper **"Accelerated Sinkhorn Algorithms for Partial Optimal Transport"** introduces a novel algorithmic framework known as **ASPOT** (Accelerated Sinkhorn for POT), designed to optimize the efficiency of transport problems involving unequal mass.

## Overview

[[accelerated-sinkhorn-algorithms-for-partial-optimal-transport|Partial Optimal Transport]] (POT) is a specialized variant of the classical [[fast-and-interpretable-protein-substructure-alignment-via-optimal-transport|Optimal Transport]] problem. While standard optimal transport requires the total mass of two distributions to be identical, POT allows for the transport of only a fraction of the total mass between two distributions. This capability is essential when working with [[marginal distributions]] of unequal sizes or datasets characterized by significant [[outliers]].

Despite the utility of POT, existing [[Sinkhorn-based methods]]—which use entropic regularization to make the problem computationally tractable—suffer from suboptimal complexity bounds in the POT setting. These limitations often hinder the scalability of these algorithms when applied to large-scale [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] tasks or complex [[computer-vision|computer vision]] datasets.

## The ASPOT Algorithm

The authors propose **ASPOT**, an algorithm that integrates [[alternating minimization]] with [[Nesterov-style acceleration]] specifically optimized for the POT framework. The primary contribution is a significant reduction in computational complexity, achieving a bound of $\mathcal{O}(n^{7/3}\varepsilon^{-5/3})$.

Key technical contributions include:
* **Accelerated Convergence:** By leveraging Nesterov-style acceleration, ASPOT bypasses the scalability bottlenecks found in traditional POT solvers.
* **Parameter Optimization:** The research demonstrates that the computational rate of classical Sinkhorn methods can be significantly improved through an informed, strategic choice of the entropic regularization parameter $\gamma$.
* **Empirical Validation:** The study provides experimental evidence showing that ASPOT performs favorably on real-world applications, outperforming previous iterations of Sinkhorn-based solvers.

## Applications

The efficiency gains provided by ASPOT have significant implications for [[computational geometry]], [[computer-vision-for-historical-pattern-recognition|pattern recognition]], and any domain utilizing [[distribution matching]] where data noise or unbalanced samples are prevalent.