---
title: SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization
created: 2024-05-22
source: https://arxiv.org/abs/2604.07663
tags: [optimization, LLM, memory-efficiency, machine-learning]
category: machine-learning
---

# SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization

SAGE (Sign Adaptive GradiEnt) is a novel optimization algorithm designed to address the critical memory bottleneck inherent in training [[Large Language Models]] (LLMs). Standard training procedures typically rely on the [[AdamW]] optimizer; however, AdamW requires optimizer states equivalent to twice the model's size, making it a major constraint during large-scale [[machine-learning]] pretraining.

### The Embedding Layer Dilemma
While existing lightweight optimizers, such as [[SinkGD]], have been developed to reduce the memory footprint, they encounter a significant "embedding layer dilemma." In modern transformer architectures, the embedding layer contains sparse and high-variance gradients. Current light-