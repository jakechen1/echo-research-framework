---
title: Inference-Time Scaling of Diffusion Language Models via Trajectory Refinement
created: 2024-05-22
source: https://arxiv.org/abs/2507.08390
tags: [diffusion models, generative AI, particle gibbs sampling, machine learning, inference optimization]
categories: [ai, machine-learning]
---

# Inference-Time Scaling of Diffusion Language Models via Trajectory Refinement

This paper explores novel methods for enhancing the performance of [[Discrete Diffusion Models]] during the inference phase, specifically focusing on steering generation toward desired rewards without the need for costly retraining. While [[Autoregressive Language Models]] currently dominate the field, diffusion-based architectures are emerging as powerful alternatives capable of matching performance through large-scale training. However, achieving precise inference-time control remains a significant challenge.

## The PG-DLM Approach

Existing methods for reward-guided generation typically rely on resampling or filtering within a single denoising trajectory. These approaches optimize rewards step-by-step but lack the ability to refine the entire sequence globally. To address this limitation, the authors introduce **Particle Gibbs Sampling for Diffusion Language Models (PG-DLM)**.

PG-DLM utilizes a [[Markov Chain]] approach constructed over full denoising trajectories. By applying a conditional [[Sequential Monte Carlo]] kernel, the algorithm enables trajectory-level refinement. This transition from step-wise optimization to trajectory-level reassessment allows the model to correct errors that occur early in the denoising process.

## Key Innovations and Scaling

The primary contribution of this work is the introduction of a new **scaling axis**: the number of refinement iterations. Unlike prior methods that primarily scale by increasing the number of parallel samples (which eventually yields diminishing returns), PG-DLM demonstrates that increasing the number of refinement iterations continues to drive performance gains.

Additional benefits include:
* **Adaptive Compute Allocation:** The framework allows for computational efficiency by performing extra refinement iterations only when the initial trajectory quality is low.
* **Theoretical Robustness:** The authors provide mathematical derivations for convergence guarantees and variance bounds.

## Empirical Results

The effectiveness of PG-DLM is demonstrated through significant accuracy improvements on complex reasoning tasks. On the [[GSM8K]] benchmark, the model achieved a baseline accuracy of 90.07% using an average of 2.9 particles. By increasing the computational budget to 16 particles via trajectory refinement, the accuracy rose to **94.47%**, outperforming existing reward-guided generation methods under similar compute budgets.