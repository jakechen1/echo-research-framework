---
title: OpenGLT: A Comprehensive Benchmark of Graph Neural Networks for Graph-Level Tasks
created: 2024-05-22
source: https://arxiv.org/abs/2501.00773
tags: [graph-neural-networks, benchmarking, machine-learning, graph-theory]
category: machine-learning
---

# OpenGLT: A Comprehensive Benchmark of Graph Neural Networks for Graph-Level Tasks

Graphs serve as the fundamental data structure for modeling complex interactions within domains such as [[social-networks|social networks]], [[molecular-structures|molecular structures]], and [[biological-systems|biological systems]]. Within these fields, **graph-level tasks**—which involve predicting properties or labels for entire graphs—are essential for breakthroughs in areas like [[molecular-property-prediction|molecular property prediction]] and subgraph counting.

## The Problem of Evaluation Fragmentation
While [[openglt-a-comprehensive-benchmark-of-graph-neural-networks-for-graph-level-tasks|Graph Neural Networks]] (GNNs) have shown immense promise, their evaluation has historically been inconsistent. Researchers often face limitations due to narrow datasets, insufficient architecture coverage, restricted task scopes, and non-standardized experimental setups. This fragmentation makes it difficult to draw reliable, cross-domain conclusions regarding which models truly perform best.

## The OpenGLT Framework
To address these challenges, the **OpenGLT** framework provides a unified evaluation standard. The framework systematically categorizes GNNs into five distinct architectural types:
* **Node-based GNNs**
* **Hierarchical pooling-based GNNs**
* **Subgraph-based GNNs**
* **Graph learning-based GNNs**
* **Self-supervised learning-based (SSL) GNNs**

The benchmark standardizes testing across four critical domains: **social networks**, **biology**, **chemistry**, and **motif counting**. It evaluates both **classification** and **regression** task types under three real-world scenarios: clean data, noisy data, and imbalanced or few-shot graph settings.

## Key Findings
Through extensive experiments involving 20 models and 26 datasets, the study revealed that no single architecture is universally superior:
1. **Performance Trade-offs:** **Subgraph-based GNNs** excel in [[expressiveness]], while **graph learning-based** and **SSL-based** methods offer superior [[adversarial-robustness-of-deep-state-space-models-for-forecasting|robustness]]. In contrast, **node-based** and **pooling-based** models are the most efficient in terms of computational cost.
2. **Topology-Aware Selection:** The study demonstrates that specific topological features, such as **density** and **centrality**, can act as guides for selecting the most suitable GNN architecture for a specific dataset.

By establishing this unified framework, OpenGLT enables more rigorous scientific progress in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] for graph-structured data.