---
title: "FVD: Inference-Time Alignment of Diffusion Models via Fleming-Viot Resampling"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.06779"
tags: [diffusion-models, inference-time-alignment, sequential-monte-carlo, generative-ai]
category: machine-learning
---

# FVD: Inference-Time Alignment of Diffusion Models via Fleming-Viot Resampling

**Fleming-Viot Diffusion (FVD)** is a novel inference-time alignment method designed to optimize [[Diffusion Models]] without the need for retraining or expensive [[Value Function Approximation]]. The method specifically targets the "diversity collapse" phenomenon frequently encountered in [[Sequential Monte Carlo (SMC)]]-based diffusion samplers.

## The Problem: Diversity Collapse
In traditional [[SMC]] sampling, models often rely on multinomial resampling schemes. Under strong selection pressure—where the goal is to maximize a specific reward—these schemes tend to favor a small number of high-reward trajectories. This leads to a loss of sample variety, known as lineage or diversity collapse, where the generated outputs become repetitive and fail to represent the full breadth of the underlying distribution.

## The FVD Solution
Drawing inspiration from the [[Fleming-Viot process]] used in population dynamics, FVD introduces a specialized birth-death mechanism for diffusion alignment. Instead of standard multinomial resampling, FVD utilizes:

*   **Reward-Based Survival:** Individual trajectories are evaluated based on reward signals.
*   **Stochastic Rebirth Noise:** To prevent trajectories from collapsing into a single deterministic path (especially when rewards are only approximate), FVD integrates stochastic noise during the "rebirth" phase.
*   **Trajectory Support Preservation:** This mechanism allows the sampler to explore reward-tilted distributions effectively while maintaining the broader support of the original generative model.

## Performance and Scalability
FVD is designed to be fully parallelizable, allowing it to scale efficiently with additional inference-time computation. Empirical results demonstrate significant advantages over existing baselines:

*   **Visual Quality:** On the [[DrawBench]] benchmark, FVD achieved a 7% improvement in **ImageReward**.
*   **Fidelity:** In class-conditional tasks, it improved the [[Fréchet Inception Distance (FID)]] by approximately 14–20%.
*   **Efficiency:** FVD is up to 66 times faster than traditional value-based optimization approaches, making it a highly practical solution for high-fidelity [[Generative AI]] applications.