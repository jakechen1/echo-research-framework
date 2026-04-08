---
title: Estimating Parameter Fields in Multi-Physics PDEs from Scarce Measurements
created: 2024-05-22
source: https://arxiv.org/abs/2500.203
tags: [Neptune, PDE, Machine Learning, Parameter Estimation, Neural Networks]
category: machine-learning
---

# Estimating Parameter Fields in Multi-Physics PDEs from Scarce Measurements

The ability to accurately infer parameters within [[Partial Differential Equations]] (PDEs) is fundamental to modeling complex phenomena in fields ranging from [[Engineering]] to [[Healthcare]]. A critical bottleneck in applying these mathematical models to real-world scenarios is the difficulty of [[Parameter Estimation]], particularly when parameters exhibit non-linear, spatiotemporal variations or when the available measurement data is extremely sparse.

Existing [[Machine Learning]] approaches, such as [[Physics-Informed Neural Networks]] (PINNs) and [[Neural Operators]], frequently struggle when faced with complex multi-physics interactions or limited observations of system responses. To overcome these limitations, the Neptune framework has been introduced. Neptune employs independent coordinate neural networks to provide a continuous representation of each parameter field in physical space or via state variables.

### Key Innovations and Performance

Neptune distinguishes itself from traditional baseline methods through several key performance metrics:

* **Data Efficiency**: The method demonstrates high robustness in low-data regimes, achieving accurate estimation with as few as 45 measurements.
* **Error Reduction**: Neptune has been shown to reduce parameter estimation errors by two orders of magnitude and dynamic response prediction errors by a factor of ten compared to PINNs and neural operators.
* **Physical Extrapolation**: Unlike many deep learning models that fail outside their training distribution, Neptune exhibits superior capabilities for predicting system behavior in physical regimes far beyond the provided training data.

### Broad Applications

By facilitating reliable and [[Data-efficient Learning]], Neptune serves as a powerful tool for disciplines where direct parameter measurement is prohibitively expensive or physically impossible. Potential transformative impacts are expected in [[Biology]], structural integrity analysis, and advanced fluid dynamics, providing a robust bridge between sparse experimental observations and high-fidelity physical modeling.