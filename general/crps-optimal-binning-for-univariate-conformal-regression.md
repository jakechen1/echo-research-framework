---
title: CRPS-Optimal Binning for Univariate Conformal Regression
created: 2024-05-22
source: https://arxiv.org/abs/2603.22000
tags: [conformal-prediction, machine-learning, statistics, regression]
category: machine-learning
author: wiki-pipeline
dc.title: "CRPS-Optimal Binning for Univariate Conformal Regression"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/crps-optimal-binning-for-univariate-conformal-regression.md
dc.language: en
dc.rights: CC-BY-4.0
---

# CRPS-Optimal Binning for Univariate Conformal Regression

The research paper "CRPS-Optimal Binning for Univariate Conformal Regression" introduces a novel method for [[Non-parametric Estimation]] of conditional distributions. The core methodology involves partitioning covariate-sorted observations into contiguous bins and utilizing the within-bin empirical cumulative distribution function (CDF) as the [[Predictive Distribution]].

### Methodology and Optimization
A primary innovation of this approach is the optimization of bin boundaries to minimize the total leave-one-out [[Continuous Ranked Probability Score (CRPS)]]. The authors present a closed-form cost function that facilitates efficient computation, requiring $O(n^2 \log n)$ precomputation and $O(n^2)$ storage. The optimal $K$-partition is recovered through [[Dynamic Programming]], settling at a complexity of $O(n^2 K)$.

To prevent the in-sample optimism often associated with direct minimization, the authors address the selection of the number of bins ($K$) through $K$-fold [[Cross-validation]] of the test CRPS. This process identifies a U-shaped criterion with a well-defined minimum, ensuring the model generalizes effectively to unseen data.

### Conformal Prediction Integration
The framework integrates seamlessly with [[weighted-bayesian-conformal-prediction|Conformal Prediction]] to generate two complementary predictive objects:
1.  **Venn prediction bands**
2.  **Conformal prediction sets**

By using CRPS as the nonconformity score, the method provides a finite-sample marginal coverage guarantee at any prescribed level $\varepsilon$. A significant advantage of this technique is its transductive and data-efficient nature; because all available observations are used for both the partitioning process and