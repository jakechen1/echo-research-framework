---
title: "pDANSE: Particle-based Data-driven Nonlinear State Estimation from Nonlinear Measurements"
created: 2024-05-22
source: https://arxiv.org/abs/2510.27503
tags: [state-estimation, RNN, particle-filtering, nonlinear-dynamics, machine-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "pDANSE: Particle-based Data-driven Nonlinear State Estimation from Nonlinear Measurements"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/pdanse-particle-based-data-driven-nonlinear-state-estimation-from-nonlinear-meas.md
dc.language: en
dc.rights: CC-BY-4.0
---

# pDANSE

**pDANSE** (Particle-based Data-driven Nonlinear State Estimation) is an advanced computational framework designed to estimate the hidden state of a "model-free" process—a system where the underlying [[State Transition Model]] (STM) is unknown. 

## Overview

In many complex physical or biological systems, the governing equations are too intricate to be modeled analytically. Traditional [[pdanse-particle-based-data-driven-nonlinear-state-estimation-from-nonlinear-meas|State Estimation]] often requires a known model to function; however, pDANSE operates by learning from noisy, nonlinear measurements directly. 

While previous iterations of Data-driven Nonlinear State Estimation (DANSE) were limited to linear measurement systems (allowing for closed-form mathematical solutions), pDANSE addresses the more computationally challenging reality of **nonlinear measurement systems**. In these scenarios, closed-form solutions are mathematically infeasible.

## Methodology

The pDANSE architecture leverages [[Recurrent Neural Networks]] (RNNs) to analyze sequential measurement data. The RNN provides the parameters for a Gaussian prior that characterizes the state of the model-free process. To handle the complexities introduced by nonlinear measurements, the method implements:

*   **Particle Sampling:** A sampling approach based on the [[reparameterization trick]] to estimate the second-order statistics of the state posterior.
*   **Efficiency:** Unlike traditional [[Sequential Monte-Carlo]] (SMC) or ancestral sampling methods, which are often computationally intensive, pDANSE is designed to use sequential measurements efficiently without the heavy overhead of standard particle filters.
*   **Learning Paradigms:** The framework is highly adaptable, supporting [[loft-parameter-efficient-fine-tuning-for-long-tailed-semi-supervised-learning-in|semi-supervised learning]] when partial labels are available and transitioning seamlessly to [[unsupervised learning]] in the absence of labeled data.

## Experimental Validation

The performance of pDANSE was benchmarked using highly chaotic [[nonlinear dynamics]] models, specifically the [[Lorenz system]] (Lorenz-63 and Lorenz-96). The researchers tested the algorithm against various nonlinear measurement types, including:

1.  **Cubic nonlinearity** and **camera model nonlinearity** (using unsupervised learning).
2.  **Half-wave rectification** and **Cartesian-to-spherical transformations** (using semi-supervised learning).

The experimental results demonstrate that pDANSE provides state estimation performance that is competitive with established model-driven approaches, even in complex, stochastic environments.