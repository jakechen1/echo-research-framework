---
title: "PlaneCycle: Training-Free 2D-to-3D Lifting of Foundation Models Without Adapters"
created: 2024-05-23
source: https://arxiv.org/abs/2603.04165
tags: [ai, machine-learning, computer-vision, 3d-vision, foundation-models]
category: ai, machine-learning
---

# PlaneCycle

**PlaneCycle** is a novel research advancement in [[Computer Vision]] that introduces a training-free, adapter-free operator designed for the 2D-to-3D lifting of [[Foundation Models]]. Traditionally, extending the powerful representations found in 2D models to 3D volumetric data has required expensive retraining, the introduction of specialized [[Adapters]], or complex architectural redesigns. PlaneCycle eliminates these requirements, offering an architecture-agnostic solution.

## Methodology

The core mechanism of PlaneCycle involves a technique that reuses the original pretrained 2D backbone by cyclically distributing spatial aggregation across three orthogonal planes: **HW** (Height-Width), **DW** (Depth-Width), and **DH** (Depth-Height). By distributing these operations throughout the network depth, the operator enables progressive 3D fusion. 

Crucially, this method is:
* **Training-Free**: No new parameters are introduced, and no retraining is required for the initial lifting.
* **Adapter-Free**: It does not rely on additional modules that increase model complexity.
* **Architecture-Agnostic**: It can be applied to any arbitrary 2D network, preserving the original pretrained inductive biases of the backbone.

## Performance and Results

The effectiveness of PlaneCycle was evaluated using pretrained [[DINOv3]] models across six 3D classification benchmarks and three 3D segmentation benchmarks. The results demonstrated significant capabilities:

1. **Linear Probing**: Without any additional training, the lifted models exhibited intrinsic 3D fusion capabilities, significantly outperforming traditional slice-wise 2D baselines and approaching the performance of models specifically trained for 3D tasks.
2. **Full Fine-Tuning**: When subjected to full fine-tuning, PlaneCycle's performance matched that of standard 3D architectures, proving its potential as a seamless [[2D-to-3D Lifting]] operator.

These findings suggest that substantial 3D intelligence is already latent within large-scale 2D models and can be unlocked through efficient structural manipulation rather than massive computational retraining.

## See Also
* [[Computer Vision]]
* [[Machine Learning]]
* [[Neural Networks]]
* [[3D Reconstruction]]