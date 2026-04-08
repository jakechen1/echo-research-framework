---
title: Generative modeling of granular flow on inclined planes using conditional flow matching
created: 2023-10-27
source: https://arxiv.org/abs/2604.04453
tags: [Generative AI, Granular Physics, Flow Matching, Inverse Problems, Computational Fluid Dynamics]
category: machine-learning
---

# Generative modeling of granular flow on inclined planes using conditional flow matching

The paper "Generative modeling of granular flow on inclined planes using conditional flow matching" introduces a novel framework for the non-invasive reconstruction of hidden mechanics in [[Granular Flows]]. Traditionally, observing the interior kinematics of granular media is exceptionally difficult because experimental methods are largely limited to surface or boundary measurements. While [[Numerical Simulations]], specifically the [[Discrete Element Method (DEM)]], provide high-fidelity data for such systems, these simulations are often too computationally expensive for real-time [[Inverse Problems]] reconstruction.

To address this limitation, the authors implement a [[Conditional Flow Matching (CFM)]] framework. This generative approach is trained on large-scale, particle-resolved simulations to learn the underlying probability distributions of flow states. During the inference stage, the model utilizes a differentiable forward operator equipped with a sparsity-aware gradient guidance mechanism. This mechanism ensures that the reconstructed velocity fields remain consistent with sparse boundary observations without the need for manual hyperparameter tuning, effectively preventing unphysical predictions in non-material regions.

A significant contribution of this work is the integration of a "physics decoder." This component maps the reconstructed velocity fields to critical physical quantities, such as the [[Stress Tensor]] (including mean and deviatoric stress) and [[Granular Temperature]]. 

The experimental results demonstrate the significant robustness of the CFM framework. The model can accurately recover interior flow fields even when only 16% of the informative window is observed, and it maintains effectiveness with as little as 11% spatial resolution. Significantly, the generative model outperforms deterministic [[Convolutional Neural Networks (CNN)]] in highly ill-posed, sparse-data scenarios. Furthermore, by utilizing [[Ensemble Generation]], the framework provides spatially resolved [[Uncertainty Quantification]], offering a complete picture of both the predicted state and the confidence of the reconstruction. This methodology holds broad potential for solving complex reconstruction tasks in [[Multiphase Systems]] and other particulate-driven industrial processes.