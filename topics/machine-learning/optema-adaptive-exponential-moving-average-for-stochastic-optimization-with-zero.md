---
title: "OptEMA: Adaptive Exponential Moving Average for Stochastic Optimization with Zero-Noise Optimality"
created: 2024-05-22
source: "https://arxiv.org/abs/260lar.09923"
tags: [optimization, stochastic-gradient-descent, machine-learning, convergence-analysis]
category: machine-learning
---

# OptEMA

**OptEMA** (Adaptive Exponential Moving Average) is a novel framework designed to advance the efficiency and theoretical robustness of [[Stochastic Optimization]]. While the [[Exponential Moving Average]] (EMA) serves as a fundamental building block for widely utilized optimizers such as [[Adam]], existing analyses of Adam-style methods often face significant theoretical bottlenecks. These include a reliance on known [[Lipschitz constants]], the requirement for bounded gradients, and suboptimal performance in the zero-noise regime.

## Overview of Variants

The OptEMA framework introduces two distinct variants designed to optimize different components of the momentum calculation:

*   **OptEMA-M**: Utilizes an adaptive, decreasing EMA coefficient applied to the first-order moment, while maintaining a fixed second-order decay.
*   **OptEMA-V**: Inverts this logic, applying the adaptive, decreasing EMA coefficient to the second-order decay.

The foundational innovation of both variants is the **Corrected AdaGrad-Norm** stepsize. This mechanism allows the optimizer to operate in a "closed-loop" and "Lipschitz-free" manner. Unlike traditional methods, the effective stepsize is strictly trajectory-dependent, meaning it adapts to the optimization path without requiring prior knowledge of the objective's smoothness or Lipschitz constants.

## Theoretical Convergence

Under standard [[Stochastic Gradient Descent]] (SGD) assumptions—specifically smoothness, a lower-bounded objective, and unbiased gradients with bounded variance—OptEMA achieves a noise-adaptive convergence rate of $\widetilde{\mathcal{O}}(T^{-1/2}+\sigma^{1/2} T^{-1/4})$, where $\sigma$ represents the noise level.

A critical feature of this method is its **zero-noise optimality**. In deterministic scenarios where noise is absent ($\sigma=0$), the convergence bounds automatically reduce to the nearly optimal deterministic rate of $\widetilde{\mathcal{O}}(T^{-1/2})$. This transition occurs seamlessly without the need for manual hyperparameter retuning, making OptEMA a highly robust candidate for complex [[Deep Learning]] tasks where noise levels vary across training stages.