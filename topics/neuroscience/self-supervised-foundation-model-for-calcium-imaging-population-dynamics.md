---
title: Self-Supervised Foundation Model for Calcium-imaging Population Dynamics
created: 2024-05-22
source: https://arxiv.org/abs/2604.04958
tags: [CalM, Calcium Imaging, Neural Dynamics, Self-Supervised Learning, Foundation Models]
category: neuroscience
---

# Self-Supervised Foundation Model for Calcium-imaging Population Dynamics

The **CalM** model represents a significant advancement in the field of [[Neuroscience]], introducing a self-supervised [[Foundation Model]] specifically engineered for analyzing [[Calcium-imaging]] data. Traditional methodologies for interpreting neural activity are often limited by their task-specific nature, which restricts their utility when transitioning between different research objectives. CalM addresses this bottleneck by learning robust, generalizable representations directly from neuronal calcium traces without the need for manual labels.

## Architecture and Methodology

The architecture of CalM is centered around a specialized **dual-axis [[Autoregressive Transformer]]**. The pretraining framework is composed of two primary components designed to handle the complexity of neural populations:

1.  **Neural Tokenizer**: A high-performance component that maps single-neuron traces into a shared, discrete vocabulary. This process allows the model to compress high-dimensional continuous signals into manageable tokens suitable for large-scale processing.
2.  **Dual-Axis Modeling**: Unlike standard transformers that focus primarily on sequential temporal data, CalM models dependencies across both the **neural axis** (capturing interactions between different neurons within a population) and the **temporal axis** (capturing how activity evolves over time).

##