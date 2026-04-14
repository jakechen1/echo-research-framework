---
title: CoLoRSMamba: Conditional LoRA-Steered Mamba for Supervised Multimodal Violence Detection
created: 2024-05-22
source: https://arxiv.org/abs/2604.03329
tags: [ai, machine-learning, computer-vision, multimodal-learning, mamba, neural-networks]
category: ai, machine-learning
---

# CoLoRSMamba

**CoLoRSMamba** (Conditional LoRA-Steered Mamba) is a novel multimodal architecture designed for high-precision, efficient supervised violence detection. The model addresses a core challenge in [[computer-vision|Computer Vision]]: the presence of noisy or semantically disconnected audio in real-world video streams, which can often mislead standard multimodal fusion techniques.

## Architecture and Methodology

The architecture utilizes a directional "Video to Audio" approach, integrating [[videomamba|VideoMamba]] and [[audiomamba|AudioMamba]] through a specialized mechanism known as CLS-guided conditional [[evgeoqa-benchmarking-llms-on-dynamic-multi-objective-geo-spatial-exploration|LoRA]] (Low-Rank Adaptation). Unlike traditional models that rely heavily on computationally expensive [[multi-modal-user-interface-control-detection-using-cross-attention|Cross-Attention]] layers, CoLoRSMamba uses the Visual CLS token to influence the audio processing stream directly.

At each layer of the network, the VideoMamba CLS token produces two critical components:
1.  **A channel-wise modulation vector.**
2.  **A stabilization gate.**

These components are used to adapt the AudioMamba projections, specifically targeting the selective parameters of the [[adversarial-robustness-of-deep-state-space-models-for-forecasting|State-Space Models]] (SSMs), namely $\Delta$, $B$, and $C$. By modulating the step-size pathway, the model enables "scene-aware" audio dynamics, allowing the audio features to be conditioned by the visual context without the overhead of token-level attention.

## Training and Evaluation

The training process employs a dual-objective strategy:
*   **Binary Classification:** To identify the presence of violence.
*   **Symmetric AV-InfoNCE:** A contrastive learning objective designed to align clip-level audio and video embeddings in a shared latent space.

To ensure a fair evaluation, the researchers curated specific audio-filtered subsets of the **NTU-CCTV** and **DVD** datasets, focusing on clips where high-quality audio synchronization was available.

## Performance Results

CoLoRSMamba demonstrates significant improvements over standard audio-only, video-only, and multimodal baselines. Key performance metrics include:

| Dataset | Accuracy | F1-V Score |
| :--- | :--- | :--- |
| **NTU-CCTV** | 