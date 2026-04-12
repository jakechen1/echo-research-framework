---
title: We Still Don't Understand High-Dimensional Bayesian Optimization
created: 2024-05-23
source: https://arxiv.org/abs/2512.00170
tags: [Machine Learning, Bayesian Optimization, Molecular Optimization, Scalable AI]
category: ai, machine-learning, drug-discovery
---

# We Still Don't Understand High-Dimensional Bayesian Optimization

The research paper "We Still Don't Understand High-Dimensional Bayesian Optimization" (arXiv:2510.00170) presents a surprising challenge to established paradigms in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]. For years, the community has approached the "curse of dimensionality" in [[we-still-dont-understand-high-dimensional-bayesian-optimization|Bayesian Optimization]] (BO) by engineering complex structural assumptions—such as [[sparsity|Sparsity]], [[smoothness|Smoothness]], and [[locality|Locality]]—directly into the optimization procedure to navigate high-dimensional search spaces.

## The Complexity Paradox

The authors demonstrate that these highly engineered, complex methods are frequently outperformed by the simplest possible alternative: [[bayesian-linear-regression|Bayesian linear regression]]. The study reveals that the complexity intended to solve high-dimensional problems may actually be counterproductive. By applying a specific geometric transformation to prevent boundary-seeking behavior, the researchers showed that [[gaussian-processes|Gaussian processes]] equipped with linear kernels can match the performance of current state-of-the-art methods. This performance holds true across a massive range of dimensions, specifically from 60 to 6,000-dimensional search spaces.

## Scalability and Application

Beyond accuracy, the shift toward linear models provides a critical advantage in computational efficiency. Unlike their non-parametric counterparts, these linear models allow for closed-form sampling and feature a computational cost that scales linearly with the size of the dataset. This scalability was crucial in the paper's application to [[molecular-optimization|Molecular Optimization]], where the researchers successfully processed datasets containing more than 20,