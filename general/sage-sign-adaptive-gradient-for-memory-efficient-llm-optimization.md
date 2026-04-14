---
title: SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization
created: 2024-05-22
source: https://arxiv.org/abs/2604.07663
tags: [optimization, LLM, memory-efficiency, machine-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/sage-sign-adaptive-gradient-for-memory-efficient-llm-optimization.md
dc.language: en
dc.rights: CC-BY-4.0
---

# SAGE: Sign-Adaptive Gradient for Memory-Efficient LLM Optimization

SAGE (Sign Adaptive GradiEnt) is a novel optimization algorithm designed to address the critical memory bottleneck inherent in training [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). Standard training procedures typically rely on the [[AdamW]] optimizer; however, AdamW requires optimizer states equivalent to twice the model's size, making it a major constraint during large-scale [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] pretraining.

### The Embedding Layer Dilemma
While existing lightweight optimizers, such as [[SinkGD]], have been developed to reduce the memory footprint, they encounter a significant "embedding layer dilemma." In modern transformer architectures, the embedding layer contains sparse and high-variance gradients. Current light-