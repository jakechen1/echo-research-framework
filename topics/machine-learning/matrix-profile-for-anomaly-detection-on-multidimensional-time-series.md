---
title: Matrix Profile for Anomaly Detection on Multidimensional Time Series
created: 2024-05-22
source: https://arxiv.org/abs/2409.09298
tags: [Matrix Profile, Anomaly Detection, Time Series, Machine Learning, Data Mining]
category: machine-learning
---

# Matrix Profile for Anomaly Detection on Multimensional Time Series

The paper "Matrix Profile for Anomaly Detection on Multidimensional Time Series" addresses a significant computational challenge in [[Time Series Data Mining]]. While the [[Matrix Profile]] (MP) has established itself as a powerful tool for detecting patterns and anomalies in univariate sequences, its application to multidimensional data remains complex.

## The Problem of Dimensionality

In standard univariate [[Time Series]] analysis, the Matrix Profile is constructed by storing the pairwise distances between all possible subsequences in an $n \times n$ matrix. However, real-world applications—such as sensor networks in manufacturing plants—often involve multiple concurrent data streams. When dealing with $d$ dimensions, the structural requirement shifts from a simple matrix to an $n \times n \times d$ tensor. This expansion significantly increases the complexity of data storage and processing.

## Proposed Methodology

The research focuses on two primary objectives:
1. **Tensor Condensation**: The authors analyze various mathematical strategies to condense the $n \times n \times d$ tensor into a single, manageable profile vector that retains essential discriminatory features.
2. **Efficient Neighbor Searching**: The paper investigates extending the MP framework to enable efficient $k$-nearest neighbor searches, which is a fundamental requirement for robust [[Anomaly Detection]] (TSAD).

## Experimental Results and Benchmarking

To evaluate the efficacy of their approach, the researchers performed an extensive benchmark comparing the multidimensional Matrix Profile against 19 different baseline [[Machine Learning]] methods. The study utilized 119 multidimensional datasets and tested the algorithms across three distinct learning paradigms:
* [[Unsupervised Learning]]
* [[Supervised Learning]]
* [[Semi-supervised Learning]]

The findings revealed that the Matrix Profile approach is uniquely robust, serving as the only method that consistently delivers high performance across all three learning setups.

## Implementation

For the purpose of transparency and further scientific advancement, the full implementation, including updated evaluations against the TSB-AD benchmark, is publicly available on GitHub at: https://github.com/mcyeh/mmpad_tsb