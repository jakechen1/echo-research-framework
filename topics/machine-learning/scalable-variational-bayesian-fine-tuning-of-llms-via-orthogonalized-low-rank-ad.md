---
title: Scalable Variable Bayesian Fine-Tuning of LLMs via Orthogonalized Low-Rank Adapters
created: 2024-05-22
source: https://arxiv.org/abs/2604.03388
tags: [LLM, Bayesian Inference, Uncertainty Quantification, PEFT, Machine Learning]
category: machine-learning
---

# Scalable Variational Bayesian Fine-Tuning of LLMs via Orthogonalized Low-Rank Adapters

## Overview
As [[Large Language Models]] (LLMs) are integrated into safety-critical applications, the ability to perform reliable [[Uncertainty Quantification]] (UQ) becomes vital. A major hurdle in modern [[Machine Learning]] is that [[Parameter-Efficient Fine-Tuning]] (PEFT) techniques—while computationally efficient—often lead to model overconfidence. This is particularly problematic when models are fine-tuned on small, domain-specific datasets, leading to a lack of reliable self-assessment regarding decision-making accuracy.

## Limitations of Existing Frameworks
The research identifies two primary shortcomings in current mitigation strategies:
* **Post-hoc Laplace Approximation:** These methods depend heavily on the training trajectory, which can result in suboptimal [[Calibration]] of the model's confidence levels.
* **Standard Variational Bayesian Training:** While theoretically robust, these methods require multiple forward passes through the entire LLM backbone to perform [[Monte Carlo Estimation]]. This creates massive computational overhead, making them impractical for real-time, scalable deployment.

## The PoLAR-VBLL Framework
To bridge the gap between scalability and accuracy, the authors propose **PoLAR-VBLL**. This framework integrates