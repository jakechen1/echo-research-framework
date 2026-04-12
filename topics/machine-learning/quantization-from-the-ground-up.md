---
title: Quantization from the ground up
created: 2024-05-22
source: https://ngrok.com/blog/quantization
tags: [quantization, deep-learning, model-compression, efficiency]
category: machine-learning
---

# Quantization from the ground up

Quantization is a critical optimization technique in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] used to enhance the efficiency and deployment capabilities of [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]]. At its core, the process involves mapping a large set of continuous, high-precision values—typically 32-bit floating-point numbers ([[fp32|FP32]])—to a smaller, discrete set of lower-precision values, such as 8-bit integers ([[int8|INT8]]).

As the scale of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] models continues to grow, particularly with the advent of [[large-language-models-llms|Large Language Models (LLMs)]], the memory and computational overhead required for [[epistemic-blinding-an-inference-time-protocol-for-auditing-prior-contamination-i|Inference]] has become a significant bottleneck. Quantization addresses this by reducing the model's memory footprint and increasing [[computational-throughput|Computational Throughput]]. By utilizing lower precision, sophisticated models can be migrated from massive data centers to [[multi-turn-reasoning-llms-for-task-offloading-in-mobile-edge-computing|Edge Computing]] environments and mobile hardware.

There are two primary methodologies used in the industry:

1.  **[[post-training-quantization-ptq|Post-Training Quantization (PTQ)]]**: This technique is applied to a model that has already been fully trained. While PTQ is computationally efficient and easy to implement, aggressive reduction in bit-width can lead to a measurable degradation in [[model-accuracy|Model Accuracy]].
2.  **[[quantization-aware-training-qat|Quantization-Aware Training (QAT)]]**: This approach incorporates the effects of quantization into the training process itself. By simulating the rounding errors and precision loss during the forward pass, the [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] model learns to compensate for the discretization, resulting in much higher fidelity at low bit-widths.

The ultimate goal of quantization is [[enec-a-lossless-ai-model-compression-method-enabling-fast-inference-on-ascend-np|Model Compression]] without sacrificing the utility of the underlying architecture. While the trade-off between precision and speed is a central challenge, mastering quantization is essential for the future of scalable, sustainable, and ubiquitous [[us-cities-are-axing-flock-safety-surveillance-technology|Technology]] deployment.