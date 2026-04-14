---
title: Are Stochastic Multi-objective Bandits Harder than Single-objective Bandits?
created: 2024-05-23
source: https://arxiv.org/abs/2604.07096
tags: [multi-objective bandits, stochastic bandits, reinforcement learning, pareto optimality, optimization]
category: machine-learning
---

# Are Stochastic Multi-objective Bandits Harder than Single-objective Bandits?

The study of [[are-stochastic-multi-objective-bandits-harder-than-single-objective-bandits|Multi-objective bandits]] has gained significant momentum due to its broad applicability in complex decision-making tasks where rewards are represented as multi-dimensional vectors rather than single scalar values. This transition from scalar to vector rewards necessitates the use of [[pareto-order-relations|Pareto order relations]] and introduces the concept of [[pareto-regret|Pareto regret]].

### The Research Problem
A long-standing debate in [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] concerns whether the added complexity of multiple objectives makes optimization fundamentally more difficult. In the context of [[adversarial-bandits|Adversarial bandits]], recent findings have shown that Pareto regret is no larger than classical single-objective regret. However, the stochastic setting presented a much more ambiguous picture. Prior research suggested that in [[stochastic-bandits|Stochastic bandits]], Pareto regret might increase as the dimensionality of the rewards increases, hinting at a fundamental increase in computational or statistical difficulty.

### Key Findings
This paper provides a definitive resolution to this question. The authors demonstrate that in the stochastic setting, Pareto regret is actually governed by the maximum sub-optimality gap \(g^\dagger\). Specifically, they prove that the regret is of the order \(\Omega(\frac{K\log T}{g^\dagger})\). This suggests that while the dimensionality plays a role, the difficulty is tied to the gap between the optimal and sub-optimal arms rather than a simple additive complexity of the dimensions.

### Proposed Methodology
To achieve this bound, the researchers developed a new algorithm that reaches an optimal Pareto regret of \(O(\frac{K\log T}{g^\dagger})\). The algorithm's architecture relies on a nested two-layer [[improving-semantic-uncertainty-quantification-in-language-model-question-answeri|Uncertainty Quantification]] mechanism. Key components include:

*   **Two-Layer Estimators:** The use of both [[upper-confidence-bound|Upper Confidence Bound]] (UCB) and [[lower-confidence-bound|Lower Confidence Bound]] (LCB) estimators to track uncertainty across both arms and objectives.
*   **Top-Two Racing Strategy:** A method for efficient arm selection.
*   **Uncertainty-Greedy Rule:** A specific rule for dimension selection designed to balance [[exploration-machine-learning|Exploration (Machine Learning)]] and exploitation.

### Experimental Validation
Through comprehensive numerical experiments, the paper validates that the proposed algorithm maintains the predicted regret guarantees and demonstrates significant performance gains over existing benchmark methods in the field of [[mathematical-optimization|Mathematical Optimization]].