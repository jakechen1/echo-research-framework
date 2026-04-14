---
title: Multi-objective Evolutionary Merging Enables Efficient Reasoning Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.06465
tags: [Evo-L2S, Model Merging, Pareto Optimization, LLM Efficiency, Evolutionary Algorithms]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "Multi-objective Evolutionary Merging Enables Efficient Reasoning Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/multi-objective-evolutionary-merging-enables-efficient-reasoning-models.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Multi-objective Evolutionary Merging Enables Efficient Reasoning Models

The advancement of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) capable of complex reasoning has increasingly relied on the use of extended [[tool-mcot-tool-augmented-multimodal-chain-of-thought-for-content-safety-moderati|Chain of Thought]] (CoT) sequences. While these "long" reasoning traces enable the resolution of intricate problems, they introduce the **Long-to-Short (L2S) reasoning problem**: a significant increase in computational overhead, latency, and token costs during [[Inference Efficiency]]-sensitive applications.

## The Limitations of Traditional Merging
Current training-free [[Model Merging]] approaches attempt to mitigate this issue by compressing reasoning traces. However, traditional methods typically rely on scalarized, fixed-hyperparameter arithmetic. These methods are often brittle and struggle to navigate the complex trade-offs between different performance metrics, frequently forcing the model into suboptimal compromises where accuracy is sacrificed for brevity.

## The Evo-L2S Framework
To address these shortcomings, the **Evo-L2S** framework introduces a novel approach by formulating the L2S problem as a [[Multi-objective Optimization]] challenge. Rather than searching for a single static model, Evo-L2S utilizes **evolutionary model merging** to explicitly optimize the trade-off between accuracy and output length. This methodology produces a robust **Pareto front**, providing a diverse set of merged models that allow developers to choose the optimal balance between computational cost and reasoning precision.

### Innovation: Entropy-Based Subset Sampling
A primary obstacle in applying evolutionary strategies to large-scale models is the intense computational cost of evaluating the fitness of each candidate model. The authors propose an **entropy-based subset sampling** technique. This innovation significantly reduces the overhead required for fitness estimation, making the evolutionary search process computationally tractable for larger architectures.

## Experimental Findings
The framework was tested across 1.5B, 7B, and 14B parameter scales using six distinct mathematical reasoning benchmarks. The results demonstrated that Evo-L2S can:
* Reduce the length of generated reasoning traces by **over 50%**.
*