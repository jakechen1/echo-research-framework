---
title: Minimum-Action Learning (MAL)
created: 2024-05-22
source: https://arxiv.org/abs/2603.16951
tags: [symbolic-regression, scientific-ml, physics-informed-ml, model-selection]
category: machine-learning
---

# Minimum-Action Learning (MAL)

[[minimum-action-learning-energy-constrained-symbolic-model-selection-for-physical|Minimum-Action Learning]] (MAL) is a computational framework within [[scientific-machine-learning|Scientific Machine Learning]] designed to identify symbolic physical laws from highly noisy observational data. The method addresses the fundamental challenge of extracting interpretable force laws from datasets where the Signal-to-Noise Ratio (SNR) is extremely low, making traditional regression techniques unreliable.

## Methodology

The MAL framework operates by selecting symbolic force laws from a pre-specified basis library. It utilizes a unique **Triple-Action functional** that optimizes three simultaneous objectives:
1. **Trajectory Reconstruction:** Minimizing the error between observed and predicted paths.
2. **Architectural Sparsity:** Encouraging simpler, more interpretable mathematical models.
3. **Energy-Conservation Enforcement:** Utilizing physical invariants to validate the selected law.

A pivotal innovation in the MAL pipeline is the **wide-stencil acceleration-matching technique**. This preprocessing step serves as a critical enabler by reducing noise variance by a factor of 10,000x. This transformation shifts the problem from an intractable state (SNR ~0.02) to a manageable, learnable state (SNR ~1.6).

## Experimental Results

The framework was benchmarked using two fundamental physical models: **Kepler gravity** and **Hooke's law**. Key performance metrics include:
* **Precision:** Successfully recovered the Kepler exponent with a precision of $p = 3.01 \pm 0.01$.
* **Computational Efficiency:** Achieved a 40% reduction in energy consumption (approximately 0.07 kWh) compared to standard prediction-error-only baselines.
* **Identification Accuracy:** While raw basis selection rates were 40% for Kepler and 90% for Hooke, the implementation of an energy-conservation-based diagnostic yielded a **100% pipeline-level identification rate**.

## Comparative Analysis

MAL provides a distinct alternative to existing [[symbolic-regression|Symbolic Regression]] and neural network architectures. Unlike [[a-robust-sindy-autoencoder-for-noisy-dynamical-system-identification|SINDy]] (Sparse Identification of Nonlinear Dynamics) variants, which focus primarily on sparse regression, or [[hamiltonian-neural-networks|Hamiltonian Neural Networks]] and [[lagrangian-neural-networks|Lagrangian Neural Networks]], which focus on learning dynamics, MAL focuses on **energy-constrained model selection**. It excels in scenarios where the model must not only fit the data but also satisfy the underlying physical constraints of the system.