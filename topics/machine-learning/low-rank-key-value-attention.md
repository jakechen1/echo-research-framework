---
title: Low-Rank Key-Value Attention
created: 2024-05-22
source: https://arxiv.org/abs/2601.11471
tags: [attention-mechanisms, transformer-efficiency, kv-cache, low-rank-approximation, deep-learning]
category: machine-learning
---

# Low-Rank Key-Value Attention

[[Low-Rank Key-Value (LRKV) Attention]] is an architectural innovation designed to address the significant memory bottlenecks associated with the [[KV cache]] in [[Transformers]]. As large language models continue to scale, the memory footprint of the key-value cache has become a primary constraint for efficient inference and long-context processing.

## Overview

The core innovation of LRKV attention is its ability to reduce [[KV cache]] memory by exploiting inherent redundancy across [[attention heads]]. While traditional methods like [[Multi-Query Attention (MQA)]] and [[Grouped-Query Attention (GQA)]] reduce the number of heads to save memory, they can often lead to a reduction in model capacity. 

LRKV introduces a more nuanced approach: each layer employs a shared full-rank KV projection that is augmented with low-rank, head-specific residuals. This mechanism provides a continuous, controllable trade-off between total parameter sharing and complete head independence, allowing the model to retain high representational power while minimizing memory overhead.

## Key Findings

Extensive testing on models ranging from 128M to 6.3B parameters reveals several critical advantages:

*   **Memory Efficiency:** LRKV utilizes only 45% to 53% of the [[KV cache]] memory required by standard [[Multi-Head Attention (MHA)]].
*   **Training Speed:** The architecture reaches equivalent baseline quality 18% to 25% faster than standard methods when measured in training steps.
*   **Competitive Accuracy:** LRKV consistently achieves lower test loss compared to MHA, MQA, GQA, and [[Multi-Head Latent Attention (MLA)]].

## Benchmark Performance

Following supervised midtraining, LRKV-based models have demonstrated superior performance across a wide array of downstream [[machine-learning]] benchmarks. Notably, the architecture achieved peak scores in complex reasoning and coding tasks, including [[ARC-Challenge]], [[MMLU]], [[GSM8K]], and [[HumanEval]]. This indicates that the low-rank compression of the key-value space does not compromise the fundamental reasoning capabilities of the [[Transformer]] architecture.