---
title: Thompson Sampling for Infinite-Horizon Discounted Decision Processes
created: 2024-05-22
source: https://arxiv.org/abs/2405.08253
tags: [Thompson Sampling, Markov Decision Processes, Reinforcement Learning, Decision Theory, Regret Analysis]
category: machine-learning
---

# Thompson Sampling for Infinite-Horizon Discounted Decision Processes

This paper addresses the theoretical challenges of analyzing [[thompson-sampling-for-infinite-horizon-discounted-decision-processes|Thompson Sampling]] (TS) within the context of discounted, infinite-horizon [[markov-decision-processes|Markov Decision Processes]] (MDPs) that utilize Borel state and action spaces. In these environments, rewards and transitions are governed by unknown parameters, making the task of evaluating adaptive learning algorithms significantly more complex than in finite-state settings.

## The Problem of Regret Measurement

A central contribution of this research is the identification of the limitations of standard [[regret-analysis|Regret Analysis]] in infinite-horizon settings. The authors argue that traditional definitions of regret are inadequate for proper policy evaluation when the timeline is infinite and rewards are discounted. To resolve this, they propose a novel decomposition of the standard expected regret into three distinct, interpretable components:

1.  **Expected Finite-Time Regret**: This aligns with the traditional metrics used to evaluate [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] algorithms over a fixed, finite horizon.
2.  **Expected State Regret**: This term captures the "path dependency" of decisions, measuring how much future performance is compromised because earlier decisions moved the system into less favorable states than an optimal policy would have.
3.  **Expected Residual Regret**: This measures the regret relative to the optimal reward from the current period onward, specifically disregarding the irreversible consequences of past decisions.

To provide an even more granular analysis, the paper introduces **probabilistic residual regret**. This is a sample-path version of the residual regret that captures the remaining loss in future performance conditional on the observed history.

## Key Findings

The paper focuses on the performance of [[thompson-sampling-for-infinite-horizon-discounted-decision-processes|Thompson Sampling]] under these expanded Borel settings. The researchers demonstrate that:

*   The third component of the decomposed regret (expected residual regret) for TS converges to zero **exponentially fast**.
*   Under mild conditions ensuring the existence of relevant limits, the probabilistic counterpart of this metric converges to zero **almost surely**.

Ultimately, the research concludes that [[thompson-sampling-for-infinite-horizon-discounted-decision-processes|Thompson Sampling]] achieves "complete learning" in these complex, infinite-horizon environments, providing a robust mathematical foundation for using sampling-based approaches in continuous state and action spaces.