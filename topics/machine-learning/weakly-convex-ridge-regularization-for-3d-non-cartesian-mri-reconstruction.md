---
title: Weakly Convex Ridge Regularization for 3D Non-Cartesian MRI Reconstruction
created: 2024-05-22
source: https://arxiv.org/abs/2603.27158
tags: [MRI, Reconstruction, WCRR, Deep Learning, Medical Imaging]
category: [ai, machine-learning, technology]
---

# Weakly Convex Ridge Regularization for 3D Non-Cartesian MRI Reconstruction

The research presented in this paper addresses a critical bottleneck in modern [[Medical Imaging]]: the computational delay associated with highly accelerated [[Magnetic Resonance Imaging]] (MRI) protocols. 

### The Reconstruction Challenge
While [[non-Cartesian acquisition]] protocols are instrumental in reducing patient scan times, they frequently introduce significant reconstruction delays. To combat this, many researchers have turned to [[Deep Learning]]-based reconstruction methods. While these neural networks offer rapid processing, they often lack [[stability]] and exhibit extreme sensitivity to [[distribution shifts]]. This lack of robustness means that when the clinical acquisition parameters deviate from the training data, the reconstruction accuracy can