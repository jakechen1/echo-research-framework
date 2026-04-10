---
title: "GIRL: Generative Imagination Reinforcement Learning via Information-Theoretic Hallucination Control"
created: 2024-05-22
source: https://arxiv.org/abs/2604.07426
tags: [reinforcement-learning, model-based-rl, world-models, hallucination-control, deep-learning]
category: machine-learning
---

# GIRL: Generative Imagination Reinforcement Learning

**GIRL** (Generative Imagination Reinforcement Learning) is a novel framework designed to address a fundamental failure mode in [[Model-based Reinforcement Learning]] (MBRL): the accumulation of modeling errors during long-horizon planning. In traditional MBRL, agents optimize policies by simulating trajectories within a learned [[World Models]] environment. However, as these "imagined" rollouts extend, small prediction errors compound, causing the latent trajectories to drift away from the real training manifold—a phenomenon often referred to as "hallucination."

### Key Innovations

GIRL introduces two primary mechanisms to stabilize the imagination process:

1.  **Cross-Modal Grounding**: To prevent the model from predicting physically implausible states, GIRL utilizes a grounding signal derived from a frozen [[Foundation Models]] architecture, specifically [[DINOv2]]. This anchors the latent transition prior to a semantically consistent embedding space, effectively penalizing predictions that deviate from known visual features.
2.  **Uncertainty-Adaptive Trust-Region**: The framework implements a bottleneck that interprets the KL regularizer as a Lagrange multiplier within a constrained optimization problem. This mechanism restricts imagination drift by calibrating the learning region based on **Expected Information Gain** and a **Relative Performance Loss** signal, ensuring the agent remains within a "trusted" zone of the model's accuracy.

### Theoretical and Empirical Impact

The authors provide a rigorous theoretical foundation by re-deriving a **value-gap bound** using the Performance Difference Lemma and Integral Probability Metrics. This derivation is particularly significant because the bound remains informative even as the discount factor approaches one, directly connecting the optimization objective to real-environment regret.

Experimental results across several benchmark suites—including [[DeepMind Control]], Adroit Hand Manipulation, and Meta-World—demonstrate the effectiveness of the approach. Compared to [[DreamerV3]], GIRL reduces latent rollout drift by between 38% and 61%. Additionally, the framework outperforms [[TD-MPC2]] in environments characterized by sparse rewards and high-contact dynamics. For deployment efficiency, a distilled-prior variant is also introduced to reduce inference overhead.