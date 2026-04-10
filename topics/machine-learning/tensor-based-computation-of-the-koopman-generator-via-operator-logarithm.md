---
title: Tensor-based computation of the Koopman generator via operator logarithm
created: 2024-05-24
source: https://arxiv.org/abs/2604.07685
tags: [machine-learning, dynamical-systems, tensor-networks, system-identification]
category: machine-learning
---

# Tensor-based computation of the Koopman generator via operator logarithm

The identification of governing equations for [[nonlinear dynamics]] remains a fundamental challenge in the field of [[system identification]]. While methods such as [[Sparse Identification of Nonlinear Dynamics (SINDy)]] are widely utilized, they often rely on time differentiation, which can be sensitive to noise and restricted by sampling intervals. 

### The Dimensionality Challenge
An alternative approach involves using the operator logarithm to bypass the need for differentiation, allowing for much larger sampling intervals. However, traditional operator-logarithm approaches are historically plagued by the "curse of dimensionality," making them computationally intractable as the number of state variables increases.

### Proposed Methodology
The research introduces a novel data-driven method designed to compute the [[Koopman generator]] within a low-rank [[Tensor Train (TT)]] format. The breakthrough lies in the technical ability to compute the logarithms of [[Koopman eigenvalues]] while preserving the underlying [[Tensor Train (TT)]] structure. By representing the operator in this compressed format, the method effectively mitigates the exponential growth of computational complexity associated with high-dimensional systems.

### Experimental Validation
The efficacy of this tensor-based approach was tested against two benchmark models:
* **4-dimensional [[Lotka-Volterra]] system:** Demonstrating accurate recovery of the underlying vector field coefficients.
* **10-dimensional [[Lorenz-96]] system:** Demonstrating the method's ability to scale to higher-dimensional complexities.

### Conclusion and Implications
The proposed framework provides a scalable pathway for applying [[Koopman operator]] theory to large-scale, complex systems. By combining [[machine learning]] with [[tensor networks]], this method offers a robust tool for researchers in [[computational physics]], fluid mechanics, and autonomous control systems where high-dimensional data is prevalent.