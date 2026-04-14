---
title: Towards Accurate and Calibrated Classification: Regularizing Cross-Entropy From A Generative Perspective
created: 2024-05-23
source: https://arxiv.org/abs/2604.06689
tags: [Generative Cross-Entropy, Machine Learning, Calibration, Deep Learning, Long-tail Learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Towards Accurate and Calibrated Classification: Regularizing Cross-Entropy From A Generative Perspective"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/towards-accurate-and-calibrated-classification-regularizing-cross-entropy-from-a.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Towards Accurate and Calibrated Classification: Regularizing Cross-Entropy From A Generative Perspective

The paper addresses a critical challenge in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]: the inherent conflict between high predictive accuracy and reliable [[calibration-of-a-neural-network-ocean-closure-for-improved-mean-state-and-variab|Calibration]] in [[Deep Neural Networks (DNNs)]]. Modern architectures frequently suffer from excessive overconfidence, a phenomenon largely attributed to [[mitigating-structural-overfitting-a-distribution-aware-rectification-framework-f|Overfitting]] during the minimization of [[Negative Log-Likelihood (NLL)]]. While existing solutions like [[Focal Loss]] attempt to mitigate this issue, they often introduce a regressive trade-off by reducing overall classification accuracy.

To resolve this, the authors propose a novel approach: **Generative Cross-Entropy (GCE)**. The core innovation lies in leveraging the complementary strengths of both [[approximately-equivariant-recurrent-generative-models-for-quasi-periodic-time-se|Generative Models]] and [[Discriminative Classifiers]]. By focusing on the maximization of $p(x|y)$, GCE acts as a cross-entropy variant augmented with a class-level confidence regularizer. The researchers demonstrate that under certain mild conditions, GCE remains a strictly proper scoring rule, ensuring a mathematically sound foundation for training.

Empirical evaluations across standard benchmarks—including [[CIFAR-10/