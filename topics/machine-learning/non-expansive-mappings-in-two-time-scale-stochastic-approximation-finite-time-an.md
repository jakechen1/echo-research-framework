---
title: Non-Expansive Mappings in Two-Time-Scale Stochastic Approximation: Finite-Time Analysis
created: 2024-05-23
source: https://arxiv.org/abs/2501.10806
tags: [stochastic-approximation, optimization, convergence-analysis, machine-learning]
category: machine-learning
---

# Non-Expansive Mappings in Two-Time-Scale Stochastic Approximation

The paper **"Non-Expansive Mappings in Two-Time-Scale Stochastic Approximation: Finite-Time Analysis"** introduces a significant theoretical advancement in the study of iterative methods used in [[Optimization]], [[Reinforcement Learning]], and [[Control Theory]]. 

## Overview

Traditionally, the finite-time analysis of [[Two-Time-Scale Stochastic Approximation]] algorithms has been constrained to settings where both the fast and slow time-scales utilize contractive mappings. This research expands the mathematical scope by investigating environments where the slower time-scale operates under a **non-expansive mapping**. 

From a theoretical perspective, the authors demonstrate that the slower time-scale in these settings can be modeled as a stochastic, inexact version of the [[Krasnoselskii-Mann iteration]].

## Key Contributions

The authors explore a specific variant of these algorithms where the faster time-scale includes a projection step. This mechanism is shown to induce non-expansiveness within the slower time-scale, creating a more flexible framework for algorithm design. 

The paper provides two primary mathematical guarantees:
1.  **Error Rate:** The last-iterate mean square residual error for these algorithms is proven to decay at a rate of $O(1/k^{1/4-\epsilon})$, where $\epsilon$ is an arbitrarily small positive value.
2.  **Convergence:** The research establishes the [[Almost Sure Convergence]] of the iterates to the set of fixed points.

## Practical Applications

The broader applicability of this framework is validated through its implementation in several critical areas of computational mathematics and [[Artificial Intelligence]]:

*   **[[Minimax Optimization]]**: Essential for training adversarial networks and robust systems.
*   **[[Linear Stochastic Approximation]]**: A foundation for many adaptive signal processing techniques.
*   **[[Lagrangian Optimization]]**: Crucial for solving constrained optimization problems in complex architectures.

By relaxing the necessity for strict contraction mappings, this work provides the theoretical groundwork necessary for analyzing more complex, real-world [[Machine Learning]] algorithms that do not adhere to traditional contraction properties.