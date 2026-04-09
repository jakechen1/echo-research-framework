---
title: Physics-Informed Neural Networks for Source Inversion and Parameters Estimation in Atmospheric Dispersion
created: 2024-05-22
source: https://arxiv.org/abs/2512.07755
tags: [PINNs, inverse-problems, atmospheric-science, neural-tangent-kernels, machine-learning]
category: ai, machine-learning
---

# Physics-Informed Neural Networks for Source Inversion and Parameters Estimation in Atmospheric Dispersion

The research paper, "Physics-Informed Neural Networks for Source Inversion and Parameters Estimation in Atmospheric Dispersion," addresses a critical challenge in [[Environmental Monitoring]]: the accurate estimation of emission source locations and the physical parameters governing them. In atmospheric science, determining where a pollutant originates is complicated by the fact that velocity profiles and diffusion parameters are often unknown and fluctuate across space and time.

### The Challenge of Inverse Problems
Estimating emission sources from scarce or noisy data is a classic [[Inverse Problems]] challenge. Traditional methods often struggle when the underlying parameters—such as the diffusion coefficients and velocity vectors in an [[Advection-Diffusion Equation]]—are themselves unknown. This creates a highly ill-posed task where the number of unknowns significantly exceeds the available measurement data.

### Proposed Methodology: Weighted Adaptive PINNs
To solve this, the authors leverage the power of [[Physics-Informed Neural Networks]] (PINNs). While PINNs are widely recognized for solving forward problems in [[Scientific Computing]], this work extends their utility to the simultaneous estimation of both sources and parameters. 

The researchers introduce a **weighted adaptive method** rooted in [[Neural Tangent Kernels]] (NTK). This methodology facilitates the joint recovery of:
1. The physical solution (concentration levels).
2. The emission sources.
3. The unknown physical parameters (velocity and diffusion coefficients).

By using the underlying Partial Differential Equation (PDE) as a structural constraint, the model effectively couples the unknown functional parameters. This allows the network to extract maximum information from limited datasets, essentially using the "physics" to fill the gaps left by insufficient "data."

### Experimental Results and Robustness
Through various numerical experiments designed to mirror real-world engineering systems, the study demonstrates that this adaptive PINN approach is highly effective. Crucially, the method maintains its accuracy and remains robust even when the input measurements are contaminated with significant noise. This makes the proposed framework a powerful tool for modern [[Deep Learning]] applications in atmospheric modeling and industrial safety.