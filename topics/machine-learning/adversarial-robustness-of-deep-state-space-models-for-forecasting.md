---
title: Adversarial Robustness of Deep State-Space Models for Forecasting
created: 2024-05-22
source: https://arxiv.org/abs/2604.03427
tags: [SSM, Adversarial Machine Learning, Control Theory, Time-Series Forecasting]
category: ai, machine-learning
---

# Adversarial Robustness of Deep State-Space Models for Forecasting

This article explores the security vulnerabilities inherent in [[State-Space Models]] (SSMs) applied to [[Time-Series Forecasting]]. While recent architectures, such as the Spacetime SSM, have demonstrated superior empirical performance on benchmark datasets, their susceptibility to [[Adversarial Attacks]] has remained an understudied gap in the field of [[Machine Learning]].

## Theoretical Foundations

The research establishes a critical link between modern deep architectures and classical estimation theory. Specifically, it proves that a decoder-only Spacetime architecture is capable of representing the optimal [[Kalman Filter]] predictor when the underlying data-generating process is autoregressive. This mathematical property distinguishes Spacetime SSMs from other [[Deep Learning]] models.

To address security concerns, the authors utilize [[Control Theory]] to frame the design of a robust forecaster as a [[Stackelberg Game]]. In this setup, the forecaster acts as the leader, and a stealthy adversary—constrained by a specific detection budget—acts as the follower. The paper proposes [[Adversarial Training]] as a viable solution to mitigate these risks.

## Key Vulnerabilities and Findings

The researchers derive closed-form bounds to quantify adversarial forecasting error. These bounds reveal that three specific architectural dimensions can amplify a model's vulnerability to perturbations:
1. **Open-loop instability**
2. **Closed-loop instability**
3. **Decoder state dimension**

A significant discovery presented in the paper is the extreme effectiveness of [[Model-free Attacks]]. The study demonstrates that adversaries can bypass the need for gradient computations entirely. By exploiting the model's locally linear input-output behavior, these gradient-free attacks on the Monash benchmark datasets resulted in at least 33% more error than standard [[Projected Gradient Descent]] (PGD) attacks. This finding suggests that current defense mechanisms may be insufficient against sophisticated, non-gradient-based adversarial strategies in time-series contexts.