---
title: Towards Accurate and Calibrated Classification: Regularizing Cross-Entropy From A Generative Perspective
created: 2024-05-23
source: https://arxiv.org/abs/2604.06689
tags: [Generative Cross-Entropy, Machine Learning, Calibration, Deep Learning, Long-tail Learning]
category: machine-learning
---

# Towards Accurate and Calibrated Classification: Regularizing Cross-Entropy From A Generative Perspective

The paper addresses a critical challenge in [[Machine Learning]]: the inherent conflict between high predictive accuracy and reliable [[Calibration]] in [[Deep Neural Networks (DNNs)]]. Modern architectures frequently suffer from excessive overconfidence, a phenomenon largely attributed to [[Overfitting]] during the minimization of [[Negative Log-Likelihood (NLL)]]. While existing solutions like [[Focal Loss]] attempt to mitigate this issue, they often introduce a regressive trade-off by reducing overall classification accuracy.

To resolve this, the authors propose a novel approach: **Generative Cross-Entropy (GCE)**. The core innovation lies in leveraging the complementary strengths of both [[Generative Models]] and [[Discriminative Classifiers]]. By focusing on the maximization of $p(x|y)$, GCE acts as a cross-entropy variant augmented with a class-level confidence regularizer. The researchers demonstrate that under certain mild conditions, GCE remains a strictly proper scoring rule, ensuring a mathematically sound foundation for training.

Empirical evaluations across standard benchmarks—including [[CIFAR-10/