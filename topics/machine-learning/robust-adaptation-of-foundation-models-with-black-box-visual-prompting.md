---
title: Robust Adaptation of Foundation Models with Black-Box Visual Prompting
created: 2024-05-22
source: https://arxiv.org/abs/2407.17491
tags: [ai, machine-learning, computer-vision, prompt-engineering, black-box-optimization]
category: ai, machine-learning
---

# Robust Adaptation of Foundation Models with Black-Box Visual Prompting

This article explores the challenges and solutions presented in the research paper regarding the adaptation of large-scale [[Pre-trained Models]] (PTMs) when the underlying architecture and parameters are inaccessible.

## The Problem: The Black-Box Limitation
Current advancements in [[Parameter-Efficient Transfer Learning]] (PETL) typically rely on two optimistic assumptions:
1. **Full Parameter Access:** The ability to see and modify the weights of the PTM.
2. **High Memory Capacity:** The availability of sufficient memory to cache intermediate activations for gradient computation.

In practical-world applications, however, many state-of-the-art models are deployed as proprietary software or accessed via [[APIs]]. In these "black-box" scenarios, developers cannot access the internal parameters of the model, nor can they meet the massive memory requirements necessitated by modern [[Deep Learning]] architectures.

## The Solution: BlackVIP
The authors propose **BlackVIP** (Black-box Visual Prompting), a method designed to enable efficient adaptation without any knowledge of the model's internal structure. The framework operates via two core components:

*   **The Coordinator:** A module that designs input-dependent visual prompts. This allows the target PTM to adapt to new domains "in the wild" by modifying the input space rather than the model weights.
*   **SPSA-GC:** This utilizes *Simultaneous Perturbation Stochastic Approximation with Gradient Correction*. This technique allows the system to efficiently estimate the gradients of the black-box PTM, enabling the Coordinator to be updated without direct access to the model's parameters.

For high-efficiency needs, the researchers also introduced **BlackVIP-SE**, a variant that significantly reduces runtime and computational costs.

## Experimental Results and Theory
The effectiveness of BlackVIP was demonstrated across 19 different datasets, proving its ability to achieve robust adaptation across diverse tasks with minimal memory consumption. 

Furthermore, the paper provides a deep theoretical connection between visual prompting and [[Randomized Smoothing]]. The authors demonstrate that the generalization capabilities of visual prompting methods are inherently linked to the *certified robustness* found in randomized smoothing, providing empirical support for the method's enhanced stability and robustness against distribution shifts.