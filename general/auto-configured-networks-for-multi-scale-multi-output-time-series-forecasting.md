---
title: Auto-Configured Networks for Multi-Scale Multi-Output Time-Series Forecasting
created: 2024-05-22
source: https://arxiv.org/abs/2604.07610
tags: [ai, machine-learning, time-series, neural-architecture-search, optimization]
category: machine-learning
author: wiki-pipeline
dc.title: "Auto-Configured Networks for Multi-Scale Multi-Output Time-Series Forecasting"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/auto-configured-networks-for-multi-scale-multi-output-time-series-forecasting.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Auto-Configured Networks for Multi-Scale Multi-Output Time-Series Forecasting

The research paper "Auto-Configured Networks for Multi-Scale Multi-Output Time-Series Forecasting" introduces an advanced framework designed to optimize [[auto-configured-networks-for-multi-scale-multi-output-time-series-forecasting|Time-Series Forecasting]] in complex industrial environments. In many industrial applications, sensors provide asynchronous signals, and models are required to predict multiple outputs simultaneously. A significant challenge in deploying these models is the inherent trade-off between prediction accuracy and the computational complexity required for edge or real-time deployment.

### Core Architecture: MS-BCNN
To handle the complexities of multi-scale temporal patterns, the authors propose the **Multi-Scale Bi-Branch Convolutional Neural Network (MS-BCNN)**. This architecture utilizes two distinct processing branches:

1.  **Short-kernel branch:** Optimized to capture high-frequency, local fluctuations within the dataset.
2.  **Long-kernel branch:** Optimized to capture long-term trends and seasonal patterns.

This dual-branch approach allows the model to effectively perform multi-output regression by observing temporal data at varying resolutions, making it robust to the irregular sampling common in industrial telemetry.

### Automated Configuration and Search
The primary innovation of this work is the integration of [[automated-machine-learning|Automated Machine Learning]] (AutoML) with multi-objective optimization. The researchers unified alignment operators, architectural decisions, and [[can-llms-beat-classical-hyperparameter-optimization-algorithms-a-study-on-autore|Hyperparameter Optimization]] into a single, hierarchical-conditional mixed configuration space.

To navigate this vast search space, the paper introduces the **Player-based Hybrid Multi-Objective Evolutionary Algorithm (PHMOEA)**. Rather than searching for a single optimal model, PHMOEA is designed to approximate the **Pareto frontier**. This allows the framework to output a "Pareto set" of models, representing the mathematically optimal trade-off between prediction error and model complexity.

### Experimental Results
The framework was evaluated using hierarchical synthetic benchmarks and a real-world **sintering dataset**. The results demonstrate that the auto-configuration approach significantly outperforms existing baselines under the same computational budget. By producing a Pareto set, the framework offers engineers flexible deployment choices, allowing them to select a model that fits specific hardware constraints without sacrificing peak performance.