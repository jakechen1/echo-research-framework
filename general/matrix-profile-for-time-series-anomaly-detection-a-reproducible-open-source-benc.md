---
title: Matrix Profile for Time-Series Anomaly Detection: A Reproducible Open-Source Benchmark on TSB-AD
created: 2024-05-22
source: https://arxiv.org/abs/2604.02445
tags: [Matrix Profile, Anomaly Detection, Time-Series, Open-Source, TSB-AD]
category: machine-learning
author: wiki-pipeline
dc.title: "Matrix Profile for Time-Series Anomaly Detection: A Reproducible Open-Source Benchmark on TSB-AD"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/matrix-profile-for-time-series-anomaly-detection-a-reproducible-open-source-benc.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Matrix Profile for Time-Series Anomaly Detection: A Reproducible Open-Source Benchmark on TSB-AD

This technical report introduces the **Matrix Profile for Anomaly Detection (MMPAD)**, an open-source implementation designed to provide a reproducible reference for [[matrix-profile-for-anomaly-detection-on-multidimensional-time-series|Matrix Profile]] (MP) methods within the [[TSB-AD]] benchmark framework. The research focuses on leveraging the scalable and interpretable nature of distance-based algorithms to solve complex [[matrix-profile-for-time-series-anomaly-detection-a-reproducible-open-source-benc|Time-Series Anomaly Detection]] tasks.

### Core Methodology

While the vanilla nearest-neighbor profile serves as a foundational tool for identifying patterns, the authors demonstrate that achieving high-tier performance on modern benchmarks requires sophisticated architectural design. The MMPAD system integrates several advanced components to handle the complexities of both [[Univariate Time Series]] and [[prism-lightweight-multivariate-time-series-classification-through-symmetric-mult|Multivariate Time Series]]:

1.  **Pre-sorted Multidimensional Aggregation**: Optimized processing of multidimensional data to maintain efficiency across large-scale datasets.
2.  **Exclusion-zone-aware k-Nearest Neighbor (kNN) Retrieval**: A specialized mechanism designed to identify repeated anomalies. By incorporating an exclusion zone, the system prevents redundant detection of the same anomalous event, a common pitfall in standard kNN-based approaches.
3.  **Moving-Average Post-processing**: A refinement step used to smooth detection results and enhance the precision of identified anomalies.

### Contributions to the Field

The primary objective of this work is to establish a reliable, open-source baseline for the [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] community. The report provides comprehensive documentation regarding hyperparameter configurations tailored for the specific tracks within the [[TSB-AD]] benchmark. 

Furthermore, the authors provide a rigorous analysis of how the system performs across diverse dataset characteristics, offering insights into the strengths and limitations of