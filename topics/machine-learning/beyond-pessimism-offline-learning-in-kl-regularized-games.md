---
title: Beyond Pessimism: Offline Learning in KL-regularized Games
created: 2024-05-22
source: https://arxiv.org/abs/2604.06738
tags: [offline-learning, zero-sum-games, KL-regularization, sample-complexity, machine-learning
---

## Overview

The paper "Beyond Pessimism: Offline Learning in KL-regularized Games" addresses a fundamental tension in [[multi-agent-reinforcement-learning-marl|Multi-Agent Reinforcement Learning (MARL)]]: the conflict between the need for [[pessimistic-offline-rl|Pessimistic Offline RL]] to avoid distribution shift and the necessity of strategic exploration to find a [[nash-equilibrium|Nash Equilibrium]] in competitive environments. While traditional offline reinforcement learning relies heavily on conservatism to mitigate the risks of [[out-of-distribution-ood-actions|Out-of-Distribution (OOD) Actions]], this paper proposes that such extreme pessimism can be counterproductive in [[zero-sum-games|Zero-Sum Games]], where overly conservative policies fail to account for the strategic dynamics of an opponent.

The authors introduce a framework centered on [[kl-regularization|KL-regularization]], shifting the objective from purely penalizing uncertain actions to optimizing a regularized version of the game where the agent's policy is incentivized to remain close to the [[behavior-policy|Behavior Policy]] via [[kullbackleibler-divergence|Kullback–Leibler divergence]]. This approach aims to provide better [[sample-complexity|Sample Complexity]] guarantees and more stable convergence in [[markov-games|Markov Games]].

## The Limitation of Pessimism in Games

In single-agent [[offline-reinforcement-learning|Offline Reinforcement Learning]], the primary challenge is the "overestimation bias" caused by evaluating actions not present in the dataset. Standard algorithms, such as [[conservative-q-learning-cql|Conservative Q-Learning (CQL)]], address this by applying a lower bound to the value function, effectively being "pessimistic" about unseen transitions.

However, applying this logic to [[competitive-games|Competitive Games]] introduces several critical failures:

1.  **Strategic Collapse**: In a [[zero-sum-game|Zero-Sum Game]], if an agent is too pessimistic about unseen actions, it may converge to a sub-optimal, overly passive strategy. This prevents the agent from discovering the "best response" to an opponent's potential moves, effectively ignoring the potential for high-reward strategic maneuvers.
2.  **Equilibrium Distortion**: The introduction of heavy penalties on OOD actions alters the underlying game structure. The learned equilibrium is no longer a true [[nash-equilibrium|Nash Equilibrium]] of the original game but rather an equilibrium of a "shrunken" game where many strategic options have been artificially suppressed.
- **Failure to Model Opponent Dynamics**: Pessimism focuses on the agent's own uncertainty about the environment, but in games, the "environment" includes the opponent. Over-penalizing actions can lead to a failure to model the [[stochastic-game|Stochastic Game]] dynamics accurately, as the agent avoids the very actions necessary to test the opponent's stability.

## The KL-Regularized Framework

The core thesis of the paper is that [[kl-regularization|KL-regularization]] offers a mathematically principled alternative to pure pessimism. Instead of applying an additive penalty to the [[q-function|Q-function]], the authors propose an objective that optimizes a regularized value function where the divergence between the learned policy ($\pi$) and the behavior policy ($\mu$) is explicitly controlled.

### Mathematical Intuition
The framework utilizes a regularized objective of the form:
$$\max_{\pi} \min_{\pi_{opp}} \mathbb{E}_{a \sim \pi, a_{opp} \sim \pi_{opp}} [Q(s, a, a_{opp})] - \beta D_{KL}(\pi || \mu)$$

By using the [[kl-divergence|KL-divergence]] as a regularizer, the agent is encouraged to maximize its expected utility while staying within a "trust region" defined by the density of the offline dataset. This ensures that:
*   **Distributional Alignment**: The agent does not stray into regions of the state-action space where the variance of the [[bellman-operator|Bellman Operator]] is too high.
*   **Smoothness**: Unlike the "hard" boundaries created by pessimistic penalties, KL-regularization provides a smooth gradient that allows for gradual shifts away from the behavior policy as more evidence is gathered.
*   **Information Preservation**: The agent retains the strategic structure of the original game, as the regularization does not fundamentally change the reward landscape, but rather constrains the search space.

## Complexity and Convergence

A significant contribution of the work is the analysis of [[sample-complexity|Sample Complexity]] within this regularized framework. The authors demonstrate that the error in the learned [[value-function|Value Function]] is bounded by a term proportional to the [[kl-divergence|KL-divergence]] between the learned policy and the behavior policy.

### Convergence in Markov Games
The paper provides a proof sketch for the convergence of [[policy-gradient|Policy Gradient]] methods under KL-regularization in the offline setting. It shows that if the regularization parameter $\beta$ is scaled appropriately with the size of the dataset, the learned policy converges to a neighborhood of the true [[nash-equilibrium|Nash Equilibrium]]. This is a significant improvement over pessimistic methods, which often exhibit much larger error bounds due to the "aggressive" nature of the value-function underestimation.

### Robustness to Dataset Bias
The authors demonstrate that the KL-regularized approach is more robust to "narrow" datasets. In scenarios where the [[behavior-policy|Behavior Policy]] is highly deterministic (e.g., a dataset consisting of a single expert trajectory), the KL-regularizer naturally transitions the agent into a more conservative mode, preventing the "divergence" typically seen in [[off-policy-evaluation|Off-Policy Evaluation]] (OPE) when using standard Q-learning.

## Empirical Results

The paper evaluates the proposed method against state-of-the-art offline RL algorithms, including [[cql|CQL]], [[iql-implicit-q-learning|IQL (Implicit Q-Learning)]], and [[td3bc|TD3+BC]], across several benchmark environments:

*   **Multi-Agent Atari**: In competitive settings, the KL-regularized agent maintained a higher win rate against evolving opponents compared to CQL, which tended to exhibit "stagnant" behavior.
*   **Rock-Paper-Scissors (Offline)**: In a purely strategic setting with limited data, the KL-regularized approach successfully recovered the equilibrium, whereas pessimistic agents failed to move away from the biased behavior policy.
*   **Grid-World Games**: The authors showed that the proposed method achieves lower [[regret|Regret]] in environments where the opponent's strategy is partially hidden or stochastic.

## Implications for Future Research

The findings presented in "Beyond Pessimism" suggest a paradigm shift in how we approach [[offline-multi-agent-reinforcement-learning|Offline Multi-Agent Reinforcement Learning]]. The move from "avoidance-based" learning to "distribution-aware" optimization opens several research avenues:

1.  **Adaptive Regularization**: Developing methods to dynamically adjust the $\beta$ parameter (the regularization strength) based on the local density of the dataset.
2.  **Communication-Augmented Games**: Exploring how KL-regularization handles agents that can communicate, where the "behavior policy" includes not just actions but also messages.
3.  **Integration with [[model-based-rl|Model-Based RL]]**: Combining the stability of KL-regularized games with the sample efficiency of [[dyna-style|Dyna-style]] architectures.

## See Also

*   [[reinforcement-learning|Reinforcement Learning]]
*   [[game-theory|Game Theory]]
*   [[distributional-reinforcement-learning|Distributional Reinforcement Learning]]
*   [[exploration-exploitation-trade-off|Exploration-Exploitation Trade-off]]
*   [[robust-reinforcement-learning|Robust Reinforcement Learning]]
