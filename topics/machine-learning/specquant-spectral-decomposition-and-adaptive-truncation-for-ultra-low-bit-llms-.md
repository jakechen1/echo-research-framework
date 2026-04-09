---
title: "SpecQuant: Spectral Decomposition and Adaptive Truncation for Ultra-Low-Bit LLMs Quantization"
created: 2024-05-22
source: "https://arxiv.org/abs/2511.11663"
tags: [quantization, LLM, compression, Fourier-transform, machine-learning]
category: machine-learning
---

# SpecQuant

**SpecQuant** is a novel two-stage quantization framework designed to achieve extreme compression in [[Large Language Models]] (LLMs). As the deployment of high-performance models moves toward end-user devices, the necessity for [[ultra-low-bit quantization]]—targeting both weights and activations—has become a primary challenge in [[machine learning]] optimization.

## The Challenge of Extreme Quantization
Standard quantization techniques often struggle with the high variance found in LLM parameters. Specifically, two major hurdles exist:
1. **Activation Outliers:** Extreme values in activations that are difficult to represent in low-bit formats.
2. **Cross-channel Variance:** Significant differences in signal energy across different channels.

## Methodology: The Two-Stage Framework
SpecQuant approaches these challenges through the lens of the [[Fourier frequency domain]]. The framework consists of two primary stages:

### 1. Outlier Smoothing
In the first stage, SpecQuant targets [[activation outliers]]. The method smooths these outliers and transfers their numerical impact into the weight matrix. This redistribution simplifies the quantization process for the subsequent stages by reducing the dynamic range required for activations.

### 2. Spectral Decomposition and Truncation
The second stage applies channel-wise low-frequency [[Fourier truncation]]. This process is predicated on the principle that the most critical information (signal energy) in a model's weights is concentrated in the low-frequency components. By suppressing high-frequency components that often represent noise or negligible detail, SpecQuant improves [[quantization robustness]] without sacrificing essential model logic.

### Adaptive Inference
To support real-time deployment, SpecQuant introduces a lightweight, adaptive truncation module. This module functions during the [[inference]] phase, dynamically adjusting truncation thresholds based on the specific characteristics of each channel, ensuring optimal precision-to-efficiency tradeoffs.

## Performance Results
Empirical evaluations conducted on the [[LLaMA-3 8B]] model demonstrate the framework's efficiency:
* **Accuracy:** Achieves 4-bit quantization for both weights and activations with a zero-shot accuracy gap of only 1.5% compared to full-precision models.
* **Efficiency:** Delivers a 2x increase in [[inference speed]].
* **Memory:** Achieves a 3x reduction in [[memory usage]], making it ideal for edge computing.

## Resources
The implementation of SpecQuant can be found via the following [[GitHub]] repository: [Kishon-zzx/SpecQuant](https://github.com/Kishon-zzx/SpecQuant).