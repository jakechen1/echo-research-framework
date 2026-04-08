---
title: ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference
created: 2024-05-22
source: https://arxiv.org/abs/2508.16703
tags: [ai, machine-learning, technology]
---

# ShadowNPU: System and Algorithm Co-design for NPU-Centric On-Device LLM Inference

The deployment of [[Large Language Models (LLMs)]] on mobile and edge devices is a critical technological advancement for preserving [[User Privacy]] and reducing cloud dependency. However, a significant bottleneck in current [[On-Device AI]] frameworks is the "fallback" phenomenon, where the computationally intensive [[Attention Operator]] is offloaded from the specialized [[Neural Processing Unit (NPU)]] to general-purpose hardware such as the [[CPU]] or [[GPU]].

## The Problem: Quantization and Hardware Fallback
The primary driver for this fallback is the sensitivity of modern [[Quantization]] techniques to error accumulation. When standard frameworks attempt to run quantized attention on an NPU, the precision loss can become unacceptable, forcing the system to revert to the CPU or GPU. This regression results in significant performance degradation, increased latency, and heightened complexity in [[System Scheduling]].

## The Solution: shadowAttn
To address these inefficiencies, the research introduces **shadowAttn**, a system-algorithm co-designed [[Sparse Attention]] module. The fundamental goal of shadowAttn is to maintain an NPU-centric execution flow, minimizing the computational burden placed on the CPU and GPU.

The core innovation lies in using an NPU-based "pilot compute" phase. This phase estimates the importance of specific tokens, allowing the system to calculate attention only on a tiny, highly relevant subset of tokens. By doing so, the overhead of the token estimation process is effectively hidden within the NPU's existing computation cycle.

## Technical Innovations
The shadowAttn framework implements several