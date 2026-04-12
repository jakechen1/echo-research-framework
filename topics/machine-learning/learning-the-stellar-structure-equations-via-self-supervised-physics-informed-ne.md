---
title: Learning the Stellar Structure Equations via Self-supervised Physics-Informed Neural Networks
created: 2024-05-22
source: https://arxiv.org/abs/2604.06255
tags: [PINNs, Astrophysics, Stellar Evolution, Machine Learning, Self-Supervised Learning]
category: machine-learning
---

# Learning the Stellar Structure Equations via Self-supervised Physics-Informed Neural Networks

The research paper "Learning the Stellar Structure Equations via Self-supervised Physics-Informed Neural Networks" introduces a revolutionary computational framework for modeling the internal physical conditions of stars. In the field of [[stellar-astrophysics|Stellar Astrophysics]], accurate descriptions of stellar interiors are vital. Traditionally, researchers have relied on complex solvers such as [[mesa|MESA]] (Modules for Experiments in Stellar Astrophysics). While highly accurate, these adaptive finite-difference methods are computationally intensive, creating significant bottlenecks when attempting to scale simulations to large stellar population syntheses involving over a billion stars.

### Methodology
To overcome these scaling challenges, the authors present a [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Physics-Informed Neural Network]] (PINN) framework. This approach is fundamentally different from standard [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] because it is self-supervised and data-free. Rather than requiring large datasets of pre-calculated stellar models, the PINN learns by enforcing the governing [[ae-vit-stable-long-horizon-parametric-partial-differential-equations-modeling|Differential Equations]] of stellar structure—specifically those governing hydrostatic and thermal equilibrium—directly within its loss function.

The model processes stellar boundary conditions (at the center and surface) and chemical composition as inputs to predict continuous radial profiles for:
* Mass $M_r(r)$
* Pressure $P(r)$
* Density $\rho(r)$
* Temperature $T(r)$
* Luminosity $L_r(r)$

A key innovation in this architecture is the integration of auxiliary [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]] to serve as differentiable surrogates for microphysics. These networks approximate the equation of state and opacity tables as smooth, differentiable functions, allowing for an end-to-end differentiable training process that avoids the errors associated with traditional interpolated lookup tables.

### Results and Impact
The framework's performance was validated against benchmark [[mesa|MESA]] models, demonstrating exceptional accuracy with a Mean Relative Absolute Error of $3.06\%$ and an average $R^2$ score of $99.98\%$. 

Because the PINN approach is mesh-free and provides continuous solutions without the need for discretization, it offers a highly scalable alternative for massive astrophysical simulations. This work establishes a foundation for the widespread use of physics-informed AI in [[astrophysics|Astrophysics]], potentially extending to the complex modeling of time-dependent stellar evolution.