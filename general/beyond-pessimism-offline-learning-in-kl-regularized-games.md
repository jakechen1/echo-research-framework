---
title: Beyond Pessimism: Offline Learning in KL-regularized Games
created: 2024-05-22
source: https://arxiv.org/abs/2604.06738
tags: [[offline-learning, zero-sum-games, KL-regularization, sample-complexity, machine-learning
author: wiki-pipeline
dc.title: "Beyond Pessimism: Offline Learning in KL-regularized Games"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/beyond-pessimism-offline-learning-in-kl-regularized-games.md
dc.language: en
dc.rights: CC-BY-4.0
---

## Overview

The paper "Beyond Pessimism: Offline Learning in KL-regularized Games" addresses a fundamental tension in [Multi-Agent Reinforcement Learning (MARL)]]: the conflict between the need for [[Pessimistic Offline RL]] to avoid distribution shift and the necessity of strategic exploration to find a [[Nash Equilibrium]] in competitive environments. While traditional offline reinforcement learning relies heavily on conservatism to mitigate the risks of [[actions|Out-of-Distribution (OOD) Actions]], this paper proposes that such extreme pessimism can be counterproductive in [[Zero-Sum Games]], where overly conservative policies fail to account for the strategic dynamics of an opponent.

The authors introduce a framework centered on [[KL-regularization]], shifting the objective from purely penalizing uncertain actions to optimizing a regularized version of the game where the agent's policy is incentivized to remain close to the [[Behavior Policy]] via [[Kullback–Leibler divergence]]. This approach aims to provide better [[Sample Complexity]] guarantees and more stable convergence in [[Markov Games]].

## The Limitation of Pessimism in Games

In single-agent [[epistemic-robust-offline-reinforcement-learning|Offline Reinforcement Learning]], the primary challenge is the "overestimation bias" caused by evaluating actions not present in the dataset. Standard algorithms, such as [[Conservative Q-Learning (CQL)]], address this by applying a lower bound to the value function, effectively being "pessimistic" about unseen transitions.

However, applying this logic to [[Competitive Games]] introduces several critical failures:

1.  **Strategic Collapse**: In a [[Zero-Sum Game]], if an agent is too pessimistic about unseen actions, it may converge to a sub-optimal, overly passive strategy. This prevents the agent from discovering the "best response" to an opponent's potential moves, effectively ignoring the potential for high-reward strategic maneuvers.
2.  **Equilibrium Distortion**: The introduction of heavy penalties on OOD actions alters the underlying game structure. The learned equilibrium is no longer a true [[Nash Equilibrium]] of the original game but rather an equilibrium of a "shrunken" game where many strategic options have been artificially suppressed.
- **Failure to Model Opponent Dynamics**: Pessimism focuses on the agent's own uncertainty about the environment, but in games, the "environment" includes the opponent. Over-penalizing actions can lead to a failure to model the [[Stochastic Game]] dynamics accurately, as the agent avoids the very actions necessary to test the opponent's stability.

## The KL-Regularized Framework

The core thesis of the paper is that [[KL-regularization]] offers a mathematically principled alternative to pure pessimism. Instead of applying an additive penalty to the [[Q-function]], the authors propose an objective that optimizes a regularized value function where the divergence between the learned policy ($\pi$) and the behavior policy ($\mu$) is explicitly controlled.

### Mathematical Intuition
The framework utilizes a regularized objective of the form:
$$\max_{\pi} \min_{\pi_{opp}} \mathbb{E}_{a \sim \pi, a_{opp} \sim \pi_{opp}} [Q(s, a, a_{opp})] - \beta D_{KL}(\pi || \mu)$$

By using the [[adaptive-symmetrization-of-the-kl-divergence|KL-divergence]] as a regularizer, the agent is encouraged to maximize its expected utility while staying within a "trust region" defined by the density of the offline dataset. This ensures that:
*   **Distributional Alignment**: The agent does not stray into regions of the state-action space where the variance of the [[Bellman Operator]] is too high.
*   **Smoothness**: Unlike the "hard" boundaries created by pessimistic penalties, KL-regularization provides a smooth gradient that allows for gradual shifts away from the behavior policy as more evidence is gathered.
*   **Information Preservation**: The agent retains the strategic structure of the original game, as the regularization does not fundamentally change the reward landscape, but rather constrains the search space.

## Complexity and Convergence

A significant contribution of the work is the analysis of [[Sample Complexity]] within this regularized framework. The authors demonstrate that the error in the learned [[Value Function]] is bounded by a term proportional to the [[adaptive-symmetrization-of-the-kl-divergence|KL-divergence]] between the learned policy and the behavior policy.

### Convergence in Markov Games
The paper provides a proof sketch for the convergence of [[Policy Gradient]] methods under KL-regularization in the offline setting. It shows that if the regularization parameter $\beta$ is scaled appropriately with the size of the dataset, the learned policy converges to a neighborhood of the true [[Nash Equilibrium]]. This is a significant improvement over pessimistic methods, which often exhibit much larger error bounds due to the "aggressive" nature of the value-function underestimation.

### Robustness to Dataset Bias
The authors demonstrate that the KL-regularized approach is more robust to "narrow" datasets. In scenarios where the [[Behavior Policy]] is highly deterministic (e.g., a dataset consisting of a single expert trajectory), the KL-regularizer naturally transitions the agent into a more conservative mode, preventing the "divergence" typically seen in [[Off-Policy Evaluation]] (OPE) when using standard Q-learning.

## Empirical Results

The paper evaluates the proposed method against state-of-the-art offline RL algorithms, including [[CQL]], [[IQL (Implicit Q-Learning)]], and [[TD3+BC]], across several benchmark environments:

*   **Multi-Agent Atari**: In competitive settings, the KL-regularized agent maintained a higher win rate against evolving opponents compared to CQL, which tended to exhibit "stagnant" behavior.
*   **Rock-Paper-Scissors (Offline)**: In a purely strategic setting with limited data, the KL-regularized approach successfully recovered the equilibrium, whereas pessimistic agents failed to move away from the biased behavior policy.
*   **Grid-World Games**: The authors showed that the proposed method achieves lower [[regret-aware-policy-optimization-environment-level-memory-for-replay-suppression|Regret]] in environments where the opponent's strategy is partially hidden or stochastic.

## Implications for Future Research

The findings presented in "Beyond Pessimism" suggest a paradigm shift in how we approach [[corruption-robust-offline-multi-agent-reinforcement-learning-from-human-feedback|Offline Multi-Agent Reinforcement Learning]]. The move from "avoidance-based" learning to "distribution-aware" optimization opens several research avenues:

1.  **Adaptive Regularization**: Developing methods to dynamically adjust the $\beta$ parameter (the regularization strength) based on the local density of the dataset.
2.  **Communication-Augmented Games**: Exploring how KL-regularization handles agents that can communicate, where the "behavior policy" includes not just actions but also messages.
3.  **Integration with [[Model-Based RL]]**: Combining the stability of KL-regularized games with the sample efficiency of [[Dyna-style]] architectures.

## See Also

*   [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]]
*   [[Game Theory]]
*   [[Distributional Reinforcement Learning]]
*   [[Exploration-Exploitation Trade-off]]
*   [[Robust Reinforcement Learning]]
