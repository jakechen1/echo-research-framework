title: Multirate Stein Variational Gradient Descent for Efficient Bayesian Sampling
created: 2024-05-22
source: https://arxiv.org/abs/2604.03981
tags: [Bayesian Inference, SVGD, Optimization, Machine Learning]
category: machine-learning

# Multirate Stein Variational Gradient Descent for Efficient Bayesian Sampling

The paper "Multirate Stein Variational Gradient Descent for Efficient Bayesian Sampling" addresses a fundamental limitation in [[Stein Variational Gradient Descent]] (SVGD). In standard SVGD, a single global step size is applied to all parts of the particle update. This approach is often inefficient when dealing with complex [[posterior distributions]]—specifically those that are high-dimensional, anisotropic, or hierarchical.

### The Core Problem

An SVGD update consists of two qualitatively different effects:
1. **Attraction**: Driving particles toward high-posterior density regions.
2. **Repulsion**: Maintaining [[particle diversity]] to prevent particle collapse.

Because these two forces can evolve at significantly different rates, a single-rate step size can lead to instability in certain regions of the parameter space or computational inefficiency in others.

### The Multirate Framework

The researchers