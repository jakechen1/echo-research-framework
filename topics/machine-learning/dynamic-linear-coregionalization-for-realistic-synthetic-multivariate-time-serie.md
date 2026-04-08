---
title: Dynamic Linear Coregionalization for Realistic Synthetic Multivariate Time Series
created: 2024-05-24
source: https://arxiv.org/abs/2604.05064
tags: [synthetic-data, multivariate-time-series, dlmc, foundation-models, forecasting]
category: machine-learning, ai, technology
---

# Dynamic Linear Coregionalization for Realistic Synthetic Multivariate Time Series

The paper "Dynamic Linear Coregionalization for Realistic Synthetic Multivariate Time Series" introduces **DynLMC**, a novel framework designed to bridge the gap between synthetic data quality and the structural complexity of real-world [[Multivariate Time Series]].

### The Problem: Static Correlations in Synthetic Data
A primary challenge in training [[Foundation Models for Time Series (FMTS)]] is the scarcity of high-quality, large-scale datasets. While synthetic data generation is a vital solution, most existing generators assume static correlations between different variables (channels). Consequently, these models often fail to capture realistic inter-channel dependencies, such as transient relationships or delayed effects, making them insufficient for training models intended for complex, real-world deployment.

### The Innovation: DynLMC
To address these limitations, the authors propose **DynLMC** (a Dynamic Linear Model of Coregionalization