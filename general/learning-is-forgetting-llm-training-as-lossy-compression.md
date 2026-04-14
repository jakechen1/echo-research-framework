---
title: Learning is Forgetting: LLM Training As Lossy Compression
created: 2024-05-22
source: https://arxiv.org/abs/2604.07569
tags: [LLM, Information Theory, Compression, Machine Learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Learning is Forgetting: LLM Training As Lossy Compression"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/learning-is-forgetting-llm-training-as-lossy-compression.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Learning is Forging: LLM Training As Lossy Compression

The paper "Learning is Forgetting: LLM Training As Lossy Compression" proposes a transformative perspective on how [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) process information during the [[adaptive-input-training-for-many-to-one-pre-training-on-time-series-classificati|Pre-training]] phase. Rather than viewing training as a simple process of accumulating data, the authors argue that LLM training is fundamentally an act of [[learning-is-forgetting-llm-training-as-lossy-compression|Lossy Compression]].

### The Compression Hypothesis

The central thesis is that models learn by actively discarding information from their training datasets that is not essential to their primary objective: [[Next-Sequence Prediction]]. By retaining only the patterns and features necessary to minimize prediction error, these models approach the [[Information Bottleneck]] bound. This implies that "learning" is inextricably linked to "forgetting" irrelevant noise, allowing [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]] to develop highly efficient [[Neural Representations]].

### Predictability and Performance

The researchers examined a variety of [[Open Weights Models]] and observed that compression efficiency varies significantly across different architectures and training recipes. However, a key finding is that the degree of compression optimality and the specific information retained can predict a model's performance on a wide array of downstream benchmarks. This creates a direct link between the mathematical structure of the model's weights and its practical utility.

### Implications for AI Research

This work offers a unified [[Information Theory]] framework that is deployable at scale. By framing the development of [[analyzing-multimodal-interaction-strategies-for-llm-assisted-manipulation-of-3d-|LLM]] capabilities as an optimization problem centered on compression, the paper provides actionable insights into how data selection and training parameters influence the "intelligence" of the resulting model. This paradigm shift suggests that understanding the limits of what a model *forgets* is just as critical as understanding what it