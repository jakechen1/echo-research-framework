---
title: Demystifying When Pruning Works via Representation Hierarchies
created: 2024-05-22
source: https://arxiv.org/abs/2603.24652
tags: [network-pruning, large-language-models, representation-learning, model-compression]
category: ai, machine-learning
---

# Demystifying When Pruning Works via Representation Hierarchies

The research paper "Demystifying When Pruning Works via Representation Hierarchies" addresses a central paradox in [[Machine Learning]]: why does [[Network Pruning]]—the process of removing less important parameters—often maintain performance in discriminative tasks while causing significant degradation in [[Generative AI]]?

### Methodology: Representation Hierarchies
To solve this discrepancy, the authors analyze the internal computations of [[Language Models]] by decomposing them into three sequential computational spaces:
1.  **[[Embedding Space]]**: The hidden representations of the model.
2.  **[[Logit Space]]**: The pre-softmax outputs.
3.  **[[Probability Space]]**: The post-softmax probability distributions.

### Key Findings
The study reveals that the stability of a model is highly dependent on which of these spaces a specific task relies upon.

*   **Robustness in Non-Generative Tasks**: The researchers found that the transformations within the [[Embedding Space]] and [[Logit Space]] are remarkably resilient to the perturbations introduced by pruning. Because tasks such as [[Information Retrieval]] and [[Multiple-choice Selection]] primarily rely on these stable subspaces, pruning is an effective and efficient strategy for these applications.
*   **Vulnerability in Generative Tasks**: The primary driver of performance decay in [[Text Generation]] is the nonlinear transformation from logits to probabilities. The [[Softmax Function]] acts as an amplifier, magnifying small deviations in the logit space. During [[Autoregressive Generation]], these errors accumulate across successive time steps, leading to substantial degradation in the model's ability to produce coherent sequences.

### Practical Implications
This analysis provides a roadmap for the intelligent application of [[Model Compression]]. Developers can confidently apply aggressive pruning to models intended for [[Natural Language Understanding]] (NLU) tasks like classification or retrieval. However, for tasks involving complex generation, more specialized pruning techniques are required to mitigate the amplification of errors within the probability subspace.

**Related Resources:**
*   [CASE-Lab-UMD Pruning Repository](https://github.com/CASE-Lab-UMD/Pruning-on-Representations)