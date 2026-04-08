---
title: "LSRM: High-Fidelity Object-Centric Reconstruction via Scaled Context Windows"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.05182"
tags: [ai, machine-learning, computer-vision, 3d-reconstruction]
category: [ai, machine-learning]
---

# LSRM: High-Fidelity Object-Centric Reconstruction

The **Large Sparse Reconstruction Model (LSRM)** is a novel framework introduced to study how scaling [[Transformer]] context windows impacts feed-forward [[3D Reconstruction]]. While contemporary object-centric methods offer robust reconstruction capabilities, they historically struggle to match the fine-grained texture and appearance recovery achieved by [[Dense-view Optimization]]. LSRM bridges this gap by substantially expanding the number of active object and image tokens within the model's context window.

## Core Innovations

To facilitate effective scaling without incurring prohibitive computational costs, the LSRM architecture introduces three primary technical contributions:

1.  **Coarse-to-Fine Pipeline**: The model employs an efficient pipeline that focuses computational resources on the most informative regions of an object by predicting sparse, high-resolution residuals.
2.  **3D-Aware Spatial Routing**: Moving away from standard attention scores, LSRM utilizes a spatial routing mechanism based on explicit geometric distances. This establishes much more accurate 2D-3D correspondences, which is critical for high-fidelity geometry.
3.  **Block-Aware Sequence Parallelism**: To manage the massive, dynamic, and sparse workloads across distributed hardware, the authors implemented a custom strategy utilizing an **All-gather-KV protocol**. This allows for efficient balancing of tokens across multiple GPUs.

## Benchmarks and Results

The architectural improvements in LSRM allow it to handle **20x more object tokens** and over **2x more image tokens** than previous state-of-the-art (SOTA) methods. Extensive testing on novel-view synthesis benchmarks reveals significant quantitative gains, specifically a **2.5 dB higher PSNR** and a **40% lower LPIPS** compared to existing models.

In the domain of [[Inverse Rendering]], LSRM demonstrates consistent improvements in recovering intricate textures and complex geometries. Its performance in these tasks matches or exceeds the capabilities of traditional dense-view optimization, marking a significant advancement in [[Computer Vision]] and [[Neural Rendering]] technologies.