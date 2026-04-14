---
title: Corruption-robust Offline Multi-agent Reinforcement Learning From Human Feedback
created: 202_05_23
source: https://arxiv.org/abs/2603.28281
tags: [multi-agent reinforcement learning, human feedback, robustness, offline learning, game theory]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "Corruption-robust Offline Multi-agent Reinforcement Learning From Human Feedback"
dc.creator: wiki-pipeline
dc.date: 202_05_23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/corruption-robust-offline-multi-agent-reinforcement-learning-from-human-feedback.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Corruption-robust Offline Multi-agent Reinforcement Learning From Human Feedback

The research paper "Corruption-robust Offline Multi-agent Reinforcement Learning From Human Feedback" addresses a critical vulnerability in [[a-multi-agent-reinforcement-learning-framework-for-public-health-decision-analys|Multi-agent Reinforcement Learning]] (MARL): the impact of adversarial data corruption when utilizing [[corruption-robust-offline-multi-agent-reinforcement-learning-from-human-feedback|Reinforcement Learning from Human Feedback]] (RLHF) in an offline setting. 

## Problem Statement: The Strong-Contamination Model
The authors investigate a "strong-contamination model" within the framework of [[Linear Markov Games]]. In this model, the learning agent relies on a dataset $D$ composed of trajectory-preference tuples. Each preference is recorded as an $n$-dimensional binary label vector, representing the individual preferences of $n$ distinct agents. The core challenge is that an $\epsilon$-fraction of these samples may be arbitrarily corrupted by an adversary, potentially leading to suboptimal or unstable policy convergence.

## Theoretical Contributions
The paper provides mathematical guarantees under two different levels of data coverage:

*   **Uniform Coverage Assumption**: In scenarios where the clean dataset sufficiently represents every policy of interest, the authors introduce a robust estimator. This estimator ensures that the [[Nash equilibrium]] gap is bounded by $O(\epsilon^{1 - o(1)})$.
*   **Unilateral Coverage Assumption**: A more rigorous and challenging setting where the dataset only covers the Nash equilibrium and its single-player deviations. In this regime, the proposed algorithm achieves a bound on the Nash gap of $O(\sqrt{\epsilon})$.

## Computational Tractability and CCE
While the initial robust estimators provide strong theoretical bounds, the authors note that these procedures face [[Intractable Computation]] issues. To bridge the gap between theory and practical application, the paper relaxes the solution concept from a pure Nash equilibrium to [[Coarse Correlated Equilibria (CCE)]]. 

The researchers successfully derive a quasi-polynomial-time algorithm that operates under the unilateral coverage regime, maintaining a CCE gap that scales as $O(\sqrt{\epsilon})$.

## Significance
This paper marks the first systematic treatment of adversarial data corruption within the context of offline MARLHF. By providing algorithmic solutions for both theoretical equilibrium gaps and computational feasibility, it lays the groundwork for developing more resilient [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] systems in multi-agent environments subject to noisy or malicious human feedback.