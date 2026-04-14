---
title: "FP4 Explore, BF16 Train: Diffusion Reinforcement Learning via Efficient Rollout Scaling"
created: 2024-05-22
source: https://arxiv.arg/abs/2604.06916
tags: [reinforcement-learning, diffusion-models, quantization, efficiency, computer-vision]
category: ai
---

# FP4 Explore, BF16 Train: Diffusion Reinforcement Learning via Efficient Rollout Scaling

The research paper introduces **Sol-RL** (Speed-of-light RL), a novel two-stage [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL) framework designed to optimize the alignment of [[diffhdr-re-exposing-ldr-videos-with-video-diffusion-models|diffusion models]] with human preferences without the prohibitive computational costs typically associated with large-scale rollouts.

## The Challenge of Rollout Scaling

In the post-training phase of text-to-image models, a common strategy to improve alignment is increasing the "rollout group size." This involves generating a larger number of candidate images to better capture the distribution of human preferences. However, for foundational models such as [[flux1-12b|FLUX.1-12B]] and [[sd35-l|SD3.5-L]], the computational burden of generating these massive candidate pools is immense. While [[3dturboquant-training-free-near-optimal-quantization-for-3d-reconstruction-model|quantization]] (specifically using FP4) offers a way to increase throughput, traditional quantized pipelines often suffer from performance degradation that compromises the [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] optimization process.

## The Sol-RL Framework

To solve the tension between efficiency and training integrity, Sol-RL proposes a decoupling of the exploration and optimization phases:

1.  **Stage 1: FP4 Exploration**: The framework uses [[fp4-quantization|FP4 quantization]] via high-throughput NVFP4 arithmetic to execute rapid rollouts. This stage focuses on generating an expansive candidate pool and identifying a highly contrastive subset of samples.
2.  **Stage 2: BF16 Optimization**: The selected high-quality candidates are regenerated using [[bf16-precision|BF16 precision]]. The policy optimization occurs exclusively on these high-fidelity samples, ensuring the model maintains the accuracy and stability of a standard training pipeline.

## Key Results and Impact

By integrating this algorithm-hardware synergy, Sol-RL allows researchers to leverage the speed of [[low-precision-arithmetic|low-precision arithmetic]] for discovery while reserving high-precision arithmetic for learning. Extensive experiments on models including [[sana|SANA]], [[flux1|FLUX.1]], and [[sd35-l|SD3.5-L]] demonstrate that:

*   **Efficiency**: Training convergence can be accelerated by up to **4.64×**.
*   **Fidelity**: The framework maintains the training integrity and alignment performance of traditional BF16 pipelines.
*   **Scalability**: It unlocks the ability to utilize massive rollout scaling at a fraction of the original computational cost.