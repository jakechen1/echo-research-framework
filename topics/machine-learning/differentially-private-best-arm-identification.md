---
title: Differentially Private Best-Arm Identification
created: 2024-05-22
source: https://arxiv.org/abs/2406.06408
tags: [differential privacy, bandits, machine learning, privacy-preserving, sample complexity]
category: machine-learning
---

# Differentially Private Best-Arm Identification

The research paper "Differentially Private Best-Arm Identification" explores the critical intersection of [[Multi-Armed Bandits]] and [[Differential Privacy]] (DP). As [[Machine Learning]] applications increasingly interact with sensitive datasets—specifically in the design of [[Clinical trials]], [[Hyperparameter tuning]], and user-facing [[User studies]]—the need for algorithms that provide utility while maintaining data anonymity becomes paramount.

## Problem Overview

The study focuses on the Best-Arm Identification (BAI) problem under two fundamental privacy models:
*   **$\epsilon$-Local Differential Privacy**: Where noise is added by the data source itself.
*   **$\epsilon$-Global Differential Privacy**: Where a central aggregator applies noise to the collected data.

The authors aim to quantify the "price of privacy" by deriving lower bounds on the [[Sample Complexity]] required to solve the BAI problem with fixed confidence while adhering to these privacy constraints.

## Key Discoveries: The Two Privacy Regimes

A primary contribution of this work is the identification of two distinct operational regimes based on the level of privacy applied:

1.  **High-Privacy Regime**: In this state, the hardness of the problem is driven by a coupled effect between the privacy parameter and novel information-theoretic quantities, specifically involving [[Total Variation]] distance.
2.  **Low-Privacy Regime**: As the privacy requirement relaxes, the lower bounds transition to match the standard, non-private lower bounds known in classical bandit theory.

## Proposed Algorithms

To bridge the gap between privacy and utility, the paper proposes two specialized algorithms:

*   **CTB-TT**: An algorithm tailored for $\epsilon$-local DP. By utilizing a private mean estimator based on the [[Randomised Response]] technique, this method achieves asymptotic optimality.
*   **AdaP-TT***: An algorithm designed for $\epsilon$-global DP. This approach uses an adaptive, arm-dependent episode structure and incorporates the [[Laplace mechanism]] (adding Laplace noise) to ensure a robust privacy-utility trade-off. The expected sample complexity of AdaP-TT* asymptotically reaches the theoretical lower bound up to a multiplicative constant.

Ultimately, this research provides a mathematical framework for implementing privacy-preserving decision-making in environments where data sensitivity is a primary constraint.