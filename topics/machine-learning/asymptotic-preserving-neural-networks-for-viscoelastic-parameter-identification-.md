---
title: Asymptotic-Preserving Neural Networks for Viscoelastic Parameter Identification in Multiscale Blood Flow Modeling
created: 2024-05-22
source: https://arxiv.org/abs/2604.06287
tags: [machine-learning, biomedical-engineering, fluid-dynamics, neural-networks]
category: machine-learning
---

# Asymptotic-Preserving Neural Networks for Viscoelastic Parameter Identification in Multiscale Blood Flow Modeling

The research presented in this paper introduces an innovative application of [[Machine Learning]] to the field of [[Fluid Dynamics]], specifically focusing on the challenges of [[Multiscale Blood Flow Modeling]]. The primary objective is to overcome the limitations of traditional numerical methods in identifying the [[Viscoelastic]] parameters that govern how arterial walls deform under pulsatile pressure.

The researchers utilize [[Asymptotic-Preserving Neural Networks]] (APNNs), a specialized architecture that embeds the underlying physical governing principles of a one-dimensional blood flow model directly into the learning process. By integrating these physical constraints, the framework ensures that the neural network remains consistent with the laws of physics, even when addressing complex multiscale phenomena.

A significant practical advantage of this framework is its ability to reconstruct crucial, yet difficult-to-measure, physiological variables—such as pressure waveforms—using easily accessible clinical data. The methodology relies on measurements of blood velocity and vessel cross-sectional area obtained via [[Doppler Ultrasound]]. Through the APNN approach, the system can infer the internal state variables of the vascular system in segments where direct, invasive pressure measurements are not feasible.

The effectiveness of this methodology has been validated through both synthetic simulations and patient-specific datasets. The study highlights the potential for these specialized [[Neural Networks]] to bridge the gap between non-invasive [[Biomedical Imaging]] and accurate [[Numerical Simulations]], offering a highly reliable,