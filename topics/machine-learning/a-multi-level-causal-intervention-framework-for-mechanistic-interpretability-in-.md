---
title: A Multi-Level Causal Intervention Framework for Mechanistic Interpretability in Variational Autoencoders
created: 2024-05-23
source: https://arxiv.org/abs/2505.03530
tags: [machine-learning, interpretability, generative-models, causal-inference]
category: ai
---

This research presents the first general-purpose multi-level [[Causal Intervention]] framework designed specifically for the [[Mechanistic Interpretability]] of [[Variational Autoencoders]] (VAEs). While interpretability research has historically focused on discriminative architectures, this work addresses the unique challenges of understanding how generative models represent and transform data within latent spaces.

### The Framework
The framework provides a structured methodology for exploring the internal logic of VAEs through four distinct manipulation types:
1. **Input manipulation**: Altering raw input to observe downstream changes.
2. **Latent-space perturbation**: Modifying the latent bottleneck to track feature transformations.
3. **Activation patching**: Replacing internal activations to isolate functional components.
4. **Causal mediation analysis**: Quantifying the pathways through which variables influence the output.

### New Quantitative Metrics
To overcome the limitations of traditional [[Disentanglement]] metrics, the authors introduce three new measures to capture properties that existing metrics often overlook:
* **Causal Effect Strength (CES)**: Quantifies the magnitude of a causal impact.
* **Intervention Specificity**: Measures how localized a manipulation's effect remains.
* **Circuit Modularity**: