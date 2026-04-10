---
title: Approximation of the Basset force in the Maxey-Riley-Gatignol equations via universal differential equations
created: 2024-05-24
source: https://arxiv.org/abs/2604.08194
tags: [Machine Learning, Fluid Dynamics, Neural Networks, ODEs, Physics-Informed ML]
category: machine-learning
---

# Approximation of the Basting Force in MaRGE via UDEs

The research paper "Approximation of the Basset force in the Maxey-Riley-Gatignol equations via universal differential equations" introduces a computational breakthrough in modeling particle dynamics within fluid environments. The study focuses on the [[Maxey-Riley-Gatignol equations]] (MaRGE), which are the standard mathematical framework used to model the motion of spherical inertial particles moving through a fluid.

## The Challenge of the Basset Force

A primary difficulty in accurately simulating these particles is the presence of the **Basset force**. This specific component accounts for the "history effects" of a particle's movement, specifically the physical impact of wake formation and boundary layer effects. 

Unlike simpler forces that depend only on the current state of the particle, the Basset force is represented as an integral term. This means the force acting on a particle at any given moment is intrinsically linked to its entire past trajectory. From a computational perspective, this transforms the MaRGE equations from standard differential equations into complex integro-differential equations. Because of the heavy computational cost associated with calculating these historical integrals, researchers frequently neglect the Basset force entirely. However, as noted in the paper, omitting this term can lead to significant errors in both the quantitative and qualitative prediction of particle movement patterns.

## The Proposed Solution: Universal Differential Equations

To overcome this computational bottleneck, the authors propose using [[Universal Differential Equations]] (UDEs). By integrating [[Neural Networks]] into the mathematical framework, the researchers developed a method to approximate the complex history-dependent integral term.

The innovation lies in the transformation of the mathematical structure:
* **Input:** The complex, history-dependent integral of the Basset force.
* **Mechanism:** A trained neural network architecture that learns to represent the effect of the force.
* **Output:** A simplified system of [[Ordinary Differential Equations]] (ODEs).

By approximating the Basset force this way, the complex MaRGE equations can be solved using standard, highly efficient [[Numerical Analysis]] tools, such as [[Runge-Kutta methods]]. This advancement allows for high-fidelity simulations of [[Fluid Dynamics]] that capture essential physical phenomena without the prohibitive computational overhead previously required.