---
title: Demystifying When Pruning Works via Representation Hierarchies
created: 2024-05-22
source: https://arxiv.org/abs/2603.24652
tags: [network-pruning, large-language-models, representation-learning, model-compression]
category: ai, machine-learning
---

# Demystifying When Pruning Works via Representation Hierarchies

The research paper "Demystifying When Pruning Works via Representation Hierarchies" addresses a central paradox in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]: why does [[neural-network-pruning-via-qubo-optimization|Network Pruning]]—the process of removing less important parameters—often maintain performance in discriminative tasks while causing significant degradation in [[synthetic-trust-attacks-modeling-how-generative-ai-manipulates-human-decisions-i|Generative AI]]?

### Methodology: Representation Hierarchies
To solve this discrepancy, the authors analyze the internal computations of [[$s^3$-stratified-scaling-search-for-test-time-in-diffusion-language-models|Language Models]] by decomposing them into three sequential computational spaces:
1.  **[[geometric-organization-of-cognitive-states-in-transformer-embedding-spaces|Embedding Space]]**: The hidden representations of the model.
2.  **[[logit-space|Logit Space]]**: The pre-softmax outputs.
3.  **[[probability-space|Probability Space]]**: The post-softmax probability distributions.

### Key Findings
The study reveals that the stability of a model is highly dependent on which of these spaces a specific task relies upon.

*   **Robustness in Non-Generative Tasks**: The researchers found that the transformations within the [[geometric-organization-of-cognitive-states-in-transformer-embedding-spaces|Embedding Space]] and [[logit-space|Logit Space]] are remarkably resilient to the perturbations introduced by pruning. Because tasks such as [[information-retrieval|Information Retrieval]] and [[multiple-choice-selection|Multiple-choice Selection]] primarily rely on these stable subspaces, pruning is an effective and efficient strategy for these applications.
*   **Vulnerability in Generative Tasks**: The primary driver of performance decay in [[a-severity-based-curriculum-learning-strategy-for-arabic-medical-text-generation|Text Generation]] is the nonlinear transformation from logits to probabilities. The [[softmax-function|Softmax Function]] acts as an amplifier, magnifying small deviations in the logit space. During [[autoregressive-generation|Autoregressive Generation]], these errors accumulate across successive time steps, leading to substantial degradation in the model's ability to produce coherent sequences.

### Practical Implications
This analysis provides a roadmap for the intelligent application of [[enec-a-lossless-ai-model-compression-method-enabling-fast-inference-on-ascend-np|Model Compression]]. Developers can confidently apply aggressive pruning to models intended for [[natural-language-understanding|Natural Language Understanding]] (NLU) tasks like classification or retrieval. However, for tasks involving complex generation, more specialized pruning techniques are required to mitigate the amplification of errors within the probability subspace.

**Related Resources:**
*   [CASE-Lab-UMD Pruning Repository](https://github.com/CASE-Lab-UMD/Pruning-on-Representations)