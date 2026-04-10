---
title: Synthetic Data for any Differentiable Target
created: 2024-05-23
source: https://arxiv.org/abs/2604.08423
tags: [synthetic data, reinforcement learning, data attribution, model alignment]
category: ai, machine-learning
---

# Synthetic Data for any Differentiable Target

The paper "Synthetic Data for any Differentiable Target" explores the fundamental limits of controlling [[Large Language Models]] (LLMs) through the use of [[Synthetic Data]]. The research addresses the central question of whether a target model's behavior can be precisely steered via the optimization of its training distribution rather than direct weight manipulation.

### The Dataset Policy Gradient (DPG)

To solve this, the authors introduce the **Dataset Policy Gradient (DPG)**, a new [[Reinforcement Learning]] (RL) primitive. DPG is designed to optimize synthetic data generators so they produce datasets tailored to a specific, differentiable metric. When these generated examples are used for [[Supervised Fine-Tuning]] (SFT) on a target model, the model exhibits the desired behavior.

The mechanism relies on **data attribution** via higher-order gradients. By using these attribution scores as policy gradient rewards, the authors demonstrate that the DPG approach effectively approximates the true, though computationally intractable, gradient for the synthetic data generator. This allows the generator to learn how to "craft" data that triggers specific responses in the target model.

### Experimental Results

The versatility of the DPG framework was demonstrated through several highly specific tasks. The researchers showed that through SFT on generated data alone, they could manipulate the target model's LM head weights to:
*   Embed a functional **QR code**.
*   Represent a specific numeric pattern (e.g., `67`).
*   Reduce the $\ell^2$ norm of the weights.

Additionally, the study proved that the generator could be trained to perform complex linguistic transformations, such as rephrasing inputs into a new language or generating a specific **UUID**, even when these objectives were absent from the generator's initial input prompts.

### Implications

These findings suggest that DPG is a powerful and flexible technique for [[Model Alignment]] and property shaping. It positions [[Synthetic Data]] not just as a way to augment training sets, but as a primary tool for precise, programmable control over the properties of [[Artificial Intelligence]] models.