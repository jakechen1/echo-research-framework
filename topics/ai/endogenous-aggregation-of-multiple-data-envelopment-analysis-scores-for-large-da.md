---
title: Endogenous Aggregation of Multiple Data Envelopment Analysis Scores for Large Data Sets
created: 2024-05-22
source: https://arxiv.org/abs/2510.20052
tags: [[Data Envelopment Analysis]], [[Efficiency Evaluation]], [[Optimization]], [[Operations Research]], [[Regularization]]
category: technology
---

# Endogenous Aggregation of Multiple DEA Scores

This article details a novel methodological approach for performing dynamic efficiency evaluation across multiple organizational dimensions using [[Data Envelopment Analysis]] (DEA). The research addresses the computational challenges of large-scale datasets while providing a framework for generating both dimension-specific and aggregate efficiency scores.

## Methodology

The researchers introduce two regularized DEA models designed to handle complex datasets containing both desirable and undesirable outputs. These models are engineered to enhance discriminatory power through the use of a regularization parameter.

1.  **Slack-Based Measure (SBM):** This approach calculates an aggregate efficiency score first and then distributes that score across the various dimensions of the organization.
2.  **Goal Programming Slack-Based Measure (GP-SBM):** This is a linearized version of a nonlinear model that operates in reverse; it estimates the efficiency of individual dimensions first and subsequently derives an aggregate score.

Both models are designed to be scalable, making them suitable for large-scale problem settings where efficiency must be measured across disparate metrics.

## Case Study: Healthcare Application

To validate the effectiveness of these models, the authors applied their approach to a longitudinal study of twelve hospitals in Ontario, Canada. The study analyzed data from a 24-month period between January 2018 and December 2019. The evaluation focused on three theoretically grounded dimensions of organizational effectiveness:

*   **Technical Efficiency**
*   **Clinical Efficiency**
*   **Patient Experience**

## Findings and Significance

The numerical results demonstrate that both the SBM and GP-SBM models outperform conventional [[Performance Benchmarking]] methods. While traditional methods typically evaluate dimensions in isolation before performing aggregation, the proposed models are significantly better at capturing the underlying correlations among input and output variables. This integrated approach provides a more accurate and holistic view of organizational performance, particularly in multi-dimensional environments like healthcare administration.