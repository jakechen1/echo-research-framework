---
title: Importance Sparsified for Sinkhorn Algorithm
created: 2024-05-22
source: https://arxiv.org/abs/2306.06581
tags: [optimal transport, sinkhorn algorithm, sparsification, machine learning, medical imaging]
category: machine-learning
author: wiki-pipeline
dc.title: "Importance Sparsified for Sinkhorn Algorithm"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/importance-sparsification-for-sinkhorn-algorithm.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Importance Sparsification for Sinkhorn Algorithm

The **Sinkhorn algorithm** is a fundamental computational tool used to approximate solutions for [[fast-and-interpretable-protein-substructure-alignment-via-optimal-transport|Optimal Transport]] (OT) and [[Unbalanced Optimal Transport]] (UOT) problems. While highly effective for various applications, its practical deployment in large-scale datasets is often hindered by prohibitive [[Computational Complexity]].

## The Spar-Sink Method

To mitigate these computational burdens, this paper introduces **Spar-Sink**, a novel importance sparsification method designed to efficiently approximate entropy-regularized OT and UOT solutions. The core innovation involves a strategic reduction in the density of the computation through the following mechanisms:

