---
title: BWTA: Accurate and Efficient Binarized Transformer by Algorithm-Hardware Co-design
created: 2024-05-23
source: https://arxiv.org/abs/2604.03957
tags: [quantization, transformer, cuda, machine-learning, efficiency]
categories: [ai, machine-learning, technology]
---

# BWTA: Accurate and Efficient Binarized Transformer by Algorithm-Hardware Co-design

**BWTA** (Binary Weights & Ternary Activations) is a novel framework designed to enable ultra-low-bit [[3dturboquant-training-free-near-optimal-quantization-for-3d-reconstruction-model|Quantization]] in [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|Transformer]] architectures without the typical-heavy loss in accuracy or lack of hardware acceleration. The research employs an algorithm-hardware co-design approach to bridge the gap between extreme compression and practical deployment.

## Problem Statement
While ultra-low-bit quantization offers massive potential for reducing the computational footprint of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models, two primary obstacles exist:
1. **Accuracy Degradation:** Traditional binarization often suffers from "zero-point distortion," leading to significant performance drops.
2. **Hardware Inefficiency:** Existing low-bit methods often lack optimized [[foundry-template-based-cuda-graph-context-materialization-for-fast-llm-serving-c|CUDA]] kernels, preventing real-world speedups on modern GPUs.

## Proposed Solution

### Algorithmic Innovation
The authors introduce the **BWTA quantization scheme**, which utilizes binary weights paired with ternary activations. By projecting minute values to zero, the method minimizes distortion and preserves the model's representational integrity. To facilitate training, the paper proposes **Smooth Multi-Stage Quantization**. This training strategy utilizes a *Levelwise Degradation Strategy* and a *Magnitude-Alignment Projection Factor* to ensure the model achieves stable and fast convergence during the transition from full-precision to extreme low-bit states.

### Hardware Optimization
To unlock the theoretical efficiency of BWTA, the researchers developed a specialized **BWTA MatMul CUDA kernel**. This kernel implements:
* **Bit-packing:** Instruction-level parallel bit-packing to maximize throughput.
* **Comprehensive Kernels:** Optimized implementations for both binary and ternary matrix multiplications across linear and attention operators.

## Experimental Results

### Accuracy
BWTA demonstrates remarkable stability across different scales:
* **BERT:** Approaches full-precision performance, with an