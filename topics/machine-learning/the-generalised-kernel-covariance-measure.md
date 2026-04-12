---
title: The Generalised Kernel Covariance Measure
created: 2024-05-22
source: https://arxiv.org/abs/2604.03721
tags: [machine-learning, statistics, kernel-methods, conditional-independence]
category: machine-learning
---

The [[the-generalised-kernel-covariance-measure|Generalised Kernel Covariance Measure]] (GKCM) represents a significant advancement in [[conditional-independence-ci-testing|Conditional Independence (CI) testing]]. Historically, kernel-based CI tests have relied on embedding variables within [[reproducing-kernel-hilbert-spaces|Reproducing Kernel Hilbert Spaces]] (RKHS) and applying [[kernel-ridge-regression|Kernel Ridge Regression]] (KRR) to evaluate residuals. While theoretically sound, these traditional methods face substantial practical challenges, specifically the high computational cost associated with hyperparameter tuning and the risk of poorly calibrated tests when tuning is bypassed.

The GKCM framework introduces a "regression-model-agnostic" approach to solve these limitations. By decoupling the dependency test from a specific regression architecture, GKCM allows for the integration of a broad class of regression estimators. This flexibility is mathematically grounded in the [[generalised-hilbertian-covariance-measure|Generalised Hilbertian Covariance Measure]] framework (Lundborg et al., 2022), providing a much more versatile toolkit for researchers.

A primary contribution of this research is