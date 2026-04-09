---
title: Beyond Loss Values: Robust Dynamic Pruning via Loss Trajectory Alignment
created: 2024-05-22
source: https://arxiv.org/abs/2604.07306
tags: [dynamic pruning, label noise, loss trajectory, AlignPrune, data selection]
category: machine-learning
---

# Beyond Loss Values: Robust Dynamic Pruning via Loss Trajectory Alignment

## Overview
In the field of [[Machine Learning]], [[Dynamic Data Pruning]] has emerged as a vital technique for optimizing training efficiency. By selecting a high-quality subset of data, researchers can reduce the computational burden of training large-scale [[Neural Networks]]. However, a significant challenge arises when training datasets contain [[Label Noise]]. 

Standard pruning methods typically use per-sample loss as the primary ranking criterion. In a noisy-label environment, this strategy often fails; because noisy samples inherently produce higher loss values, the pruning algorithm mistakenly identifies them as "important" samples to be preserved. This leads to the retention of errors, which fundamentally degrades the model's final accuracy.

## The AlignPrune Solution
To address the instability of loss-based ranking, the paper introduces **AlignPrune**, a noise-robust module designed to stabilize dynamic pruning. The core innovation is the **Dynamic Alignment Score (DAS)**. 

Unlike traditional methods that look at a single snapshot of loss, the DAS utilizes a **Loss Trajectory-based** criterion. By analyzing the evolution of loss over the course of the training process, AlignPrune can more accurately distinguish between truly informative, difficult samples and those that are simply mislabeled. This trajectory-based approach allows the system to identify patterns characteristic of noise, effectively filtering them out during the pruning phase.

## Key Features and Performance
AlignPrune is designed to be a "plug-and-play" solution, making it highly versatile for the [[Artificial Intelligence]] community. Its primary advantages include:

* **Seamless Integration:** It can be integrated into existing [[State-of-the-Art (SOTA)]] dynamic pruning frameworks without requiring changes to the model architecture.
* **Pipeline Compatibility:** The module does not necessitate modifications to the standard [[Training Pipeline]].
* **Superior Accuracy:** Experimental results across five widely-used benchmarks show that AlignPrune can increase accuracy by up to 6.3% compared to existing baselines.

## Resources
The project's implementation is available for research use via the official [GitHub repository](https://github.com/leonqin430/AlignPrune).