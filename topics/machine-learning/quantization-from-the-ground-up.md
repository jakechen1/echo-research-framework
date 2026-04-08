---
title: Quantization from the ground up
created: 2024-05-22
source: https://ngrok.com/blog/quantization
tags: [quantization, deep-learning, model-compression, efficiency]
category: machine-learning
---

# Quantization from the ground up

Quantization is a critical optimization technique in [[Machine Learning]] used to enhance the efficiency and deployment capabilities of [[Neural Networks]]. At its core, the process involves mapping a large set of continuous, high-precision values—typically 32-bit floating-point numbers ([[FP32]])—to a smaller, discrete set of lower-precision values, such as 8-bit integers ([[INT8]]).

As the scale of [[Artificial Intelligence]] models continues to grow, particularly with the advent of [[Large Language Models (LLMs)]], the memory and computational overhead required for [[Inference]] has become a significant bottleneck. Quantization addresses this by reducing the model's memory footprint and increasing [[Computational Throughput]]. By utilizing lower precision, sophisticated models can be migrated from massive data centers to [[Edge Computing]] environments and mobile hardware.

There are two primary methodologies used in the industry:

1.  **[[Post-Training Quantization (PTQ)]]**: This technique is applied to a model that has already been fully trained. While PTQ is computationally efficient and easy to implement, aggressive reduction in bit-width can lead to a measurable degradation in [[Model Accuracy]].
2.  **[[Quantization-Aware Training (QAT)]]**: This approach incorporates the effects of quantization into the training process itself. By simulating the rounding errors and precision loss during the forward pass, the [[Deep Learning]] model learns to compensate for the discretization, resulting in much higher fidelity at low bit-widths.

The ultimate goal of quantization is [[Model Compression]] without sacrificing the utility of the underlying architecture. While the trade-off between precision and speed is a central challenge, mastering quantization is essential for the future of scalable, sustainable, and ubiquitous [[Technology]] deployment.