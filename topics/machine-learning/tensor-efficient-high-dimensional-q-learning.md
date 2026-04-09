---
title: Tensor-Efficient High-Dimensional Q-learning
created: 2024-05-22
source: https://arxiv.org/abs/2511.03595
tags: [reinforcement-learning, tensor-decomposition, q-learning, complexity-reduction]
category: machine-learning
---

# Tensor-Efficient High-Dimensional Q-learning

High-dimensional [[Reinforcement Learning]] (RL) face significant bottlenecks due to the "curse of dimensionality," where the number of state-action pairs grows exponentially with the problem size. This complexity leads to massive computational overhead and notoriously low sample efficiency. While [[Deep Q-Networks]] (DQN) and other neural-network-based approaches have demonstrated success in complex environments, they often fail to explicitly exploit the inherent structural patterns of the underlying tasks.

## The TEQL Framework

The paper introduces **Tensor-Efficient Q-Learning (TEQL)**, a method designed to leverage the latent structures found in high-dimensional control tasks. Many high-dimensional value functions exhibit a low-rank structure; TEQL exploits this by representing the Q-function as a low-rank [[CP Decomposition]] (CANDECOMP/PARAFAC) tensor over discretized state-action spaces. By utilizing [[Tensor Decomposition]], the model achieves a highly parameter-efficient representation compared to standard dense architectures.

## Key Innovations

TEQL introduces two primary mechanisms to enhance learning stability and efficiency:

1.  **Error-Uncertainty Guided Exploration (EUGE):** Traditional exploration often relies on simple epsilon-greedy strategies or visit counts. EUGE integrates the tensor approximation error with visit frequencies to guide action selection. This allows the agent to focus exploration on regions where the model's structural approximation is most uncertain.
2.  **Frequency-Aware Regularization:** To prevent the instability often seen in high-dimensional updates, TEQL incorporates a regularization technique that accounts for the frequency of state-action visits, ensuring smoother convergence during the learning process.

## Experimental Results

Benchmark tests on classic control tasks demonstrate that TEQL outperforms both matrix-based [[Low-rank Approximation]] methods and standard [[Deep Reinforcement Learning]] baselines. Under matched parameter budgets, TEQL shows significantly higher sample efficiency, making it an ideal candidate for [[Resource-Constrained AI]] applications where the cost of environment interaction is high.