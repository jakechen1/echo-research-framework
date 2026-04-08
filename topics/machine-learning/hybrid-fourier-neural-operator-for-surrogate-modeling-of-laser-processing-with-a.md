---
title: Hybrid Fourier Neural Operator for Surrogate Modeling of Laser Processing with a Quantum-Circuit Mixer
created: 2024-05-22
source: https://arxiv.org/abs/2604.04828
tags: [quantum machine learning, neural operators, surrogate modeling, laser processing, hybrid computing]
categories: [ai, machine-learning, technology]
---

# Hybrid Fourier Neural Operator for Surrogate Modeling of Laser Processing with a Quantum-Circuit Mixer

The paper introduces **HQ-LP-FNO**, a novel hybrid architecture designed to optimize the performance of [[Fourier Neural Operator]] (FNO) models for high-dimensional, complex engineering simulations. The primary challenge addressed is the scaling inefficiency of classical FNOs, where the dense spectral channel mixing scales linearly with the number of Fourier modes, significantly increasing parameter counts and hindering [[Real-time Simulation]].

### Methodology: The Quantum-Classical Hybrid Approach
The researchers developed a hybrid quantum-classical framework that replaces a configurable portion of dense spectral blocks with a compact, mode-shared [[Variational Quantum Circuit]] (VQC) mixer. Unlike traditional classical blocks, the parameter count of this VQC mixer remains independent of the Fourier mode budget. To provide a rigorous scientific benchmark, the authors utilized a parameter-matched classical bottleneck control, allowing for an "apples-to-apples" comparison between classical and quantum-enhanced architectures.

### Application in [[Laser Processing]]
The architecture was evaluated on the 3D surrogate modeling of high-energy [[Laser Processing]]. This domain is characterized by extreme [[Multiphysics]] complexity, requiring the simultaneous modeling of:
* [[Heat Transfer]]
* Melt-pool convection
* Free-surface deformation
* Phase change phenomena

### Key Findings and Performance
The integration of quantum circuits into the operator learning framework yielded significant improvements in both efficiency and accuracy:
* **Parameter Reduction:** The HQ-LP-FNO model achieved a 15.6% reduction in trainable parameters relative to the classical baseline.
* **Enhanced Accuracy:** The model reduced phase-fraction mean absolute error (MAE) by 26% and improved the relative temperature MAE from 2.89% to 2.56%.
* **Optimal Partitioning:** A sweep of the quantum-channel budget revealed that a moderate allocation of VQC layers (rather than a fully quantum or fully classical approach) provides the