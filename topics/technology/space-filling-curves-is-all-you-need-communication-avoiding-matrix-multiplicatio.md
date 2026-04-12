---
title: Space Filling Curves is All You Need: Communication-Avoiding Matrix Multiplication Made Simple
created: 2024-05-23
source: https://arxiv.org/abs/2601.16294
tags: [HPC, GEMM, Algorithms, LLM, Optimization]
category: technology
---

# Space Filling Curves in Matrix Multiplication

The paper "Space Filling Curves is All You Need: Communication-Avoiding Matrix Multiplication Made Simple" presents a breakthrough in optimizing [[general-matrix-multiplication-gemm|General Matrix Multiplication (GEMM)]], which serves as the fundamental computational backbone for both [[high-performance-computing-hpc|High-Performance Computing (HPC)]] and [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]].

### The Problem: The Tuning Bottleneck
Current state-of-the-art vendor libraries rely on highly specialized, hand-tuned parameters—including specific tensor layouts, parallelization schemes, and cache blocking—to maximize throughput. A major drawback of this approach is that these optimal settings are highly dependent on specific hardware architectures and matrix shapes. As a result, an exhaustive tuning process is required for every new platform, which is computationally infeasible in a rapidly evolving hardware