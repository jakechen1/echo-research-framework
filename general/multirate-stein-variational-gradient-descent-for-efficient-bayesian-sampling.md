---
title: "Multirate Stein Variational Gradient Descent For Efficient Bayesian Sampling"
category: machine-learning
created: 2026-04-12
author: wiki-pipeline
dc.title: "Multirate Stein Variational Gradient Descent For Efficient Bayesian Sampling"
dc.creator: wiki-pipeline
dc.date: 2026-04-12
dc.type: Text
dc.format: text/markdown
dc.identifier: general/multirate-stein-variational-gradient-descent-for-efficient-bayesian-sampling.md
dc.language: en
dc.rights: CC-BY-4.0
---

title: Multirate Stein Variational Gradient Descent for Efficient Bayesian Sampling
created: 2024-05-22
source: https://arxiv.org/abs/2604.03981
tags: [Bayesian Inference, SVGD, Optimization, Machine Learning]
category: machine-learning

# Multirate Stein Variational Gradient Descent for Efficient Bayesian Sampling

The paper "Multirate Stein Variational Gradient Descent for Efficient Bayesian Sampling" addresses a fundamental limitation in [[multirate-stein-variational-gradient-descent-for-efficient-bayesian-sampling|Stein Variational Gradient Descent]] (SVGD). In standard SVGD, a single global step size is applied to all parts of the particle update. This approach is often inefficient when dealing with complex [[posterior distributions]]—specifically those that are high-dimensional, anisotropic, or hierarchical.

### The Core Problem

An SVGD update consists of two qualitatively different effects:
1. **Attraction**: Driving particles toward high-posterior density regions.
2. **Repulsion**: Maintaining [[particle diversity]] to prevent particle collapse.

Because these two forces can evolve at significantly different rates, a single-rate step size can lead to instability in certain regions of the parameter space or computational inefficiency in others.

### The Multirate Framework

The researchers