---
title: "BTC-LLM: Efficient Sub-1-Bit LLM Quantization via Learnable Transformation and Binary Codebook"
created: 2024-05-22
source: "https://arxiv.org/abs/2506.12040"
tags: [[machine-learning-llm-quantization-neural-networks-compression|"Machine Learning", "LLM", "Quantization", "Neural Networks", "Compression"]]
category: machine-learning
---

# BTC-LLM: Efficient Sub-1-Bit LLM Quantization

The **BTC-LLM** framework represents a significant advancement in the extreme [[lightthinker-from-reasoning-compression-to-memory-management|compression]] of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). While [[binary-neural-networks|Binary Neural Networks]] (BNNs) typically reduce weights to +/-1 to achieve maximal memory and computational efficiency, achieving sub-1-bit precision has historically been difficult due to severe performance degradation and the computational overhead associated with managing sparse masks.

## Challenges in Sub-1-Bit Quantization
Current methods for achieving sub-1-bit compression often rely on [[weight-pruning|weight pruning]] to introduce sparsity. However, these approaches suffer from several critical bottlenecks:
1. **Performance Degradation**: Significant loss in model accuracy during extreme compression.
2. **Mask-Management Overhead**: The computational cost of managing sparse structures.
3. **Hardware Incompatibility**: Difficulties in deploying sparse models efficiently on standard [[ahcq-sam-toward-accurate-and-hardware-compatible-post-training-segment-anything-|hardware]] architectures.

## Technical Innovations
BTC-LLM introduces a novel quantization framework that eliminates the need for sparse masks, enabling efficient inference on standard hardware through two primary innovations:

### 1. Binary Codebook
The framework utilizes a **Binary Codebook** that clusters recurring vectors into compact indices. By leveraging custom distance metrics and sign-based updates, the codebook allows the model to represent complex weight patterns through a streamlined set of indices, significantly reducing the total memory footprint.

### 2. Learnable Transformation
A **Learnable Transformation** layer is implemented to mitigate the impact of weight outliers. This transformation promotes shared sign patterns among binary weights, reducing the influence of extreme values and ensuring that the quantized weights maintain high fidelity to the original model.

## Experimental Performance
Evaluations conducted across the [[llama|LLaMA]], [[qwen|Qwen]], and [[fbi-llm|FBI-LLM]] families demonstrate that BTC-LLM achieves state-of-the-art results in extreme compression ranges (1.11 to 0.7 bits). Most notably, the **LLaMA-2-13B** model, when compressed to 0.8 bits, maintained high performance with only a 3.1% accuracy drop in zero-shot benchmarks, while delivering a **1.6x speedup** over [[fp16|FP16]] precision.