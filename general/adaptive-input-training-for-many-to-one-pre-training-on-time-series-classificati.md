---
title: ADAPTive Input Training for Many-to-One Pre-Training on Time-Series Classification
created: 2024-05-22
source: https://arxiv.org/abs/2604.08398
tags: [time-series, self-supervised-learning, foundation-models, pre-training]
category: machine-learning
author: wiki-pipeline
dc.title: "ADAPTive Input Training for Many-to-One Pre-Training on Time-Series Classification"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/adaptive-input-training-for-many-to-one-pre-training-on-time-series-classificati.md
dc.language: en
dc.rights: CC-BY-4.0
---

# ADAPTive Input Training for Many-to-One Pre-Training on Time-Series Classification

The paper "ADAPTive Input Training for Many-to-One Pre-Training on Time-Series Classification" introduces a novel framework designed to overcome the current limitations of [[Self-supervised learning]] within the field of [[adversarial-robustness-of-time-series-classification-for-crystal-collimator-alig|Time-series classification]].

### The Challenge of Heterogeneity
Recent advancements in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine learning]] have demonstrated the power of "one-to-many" pre-training, where a model is trained on a single large dataset and subsequently fine-tuned on various downstream tasks. However, this approach struggles with "many-to-one" scenarios—where a model attempts to learn from multiple diverse datasets simultaneously. 

In the time-series domain, the primary obstacle is the extreme heterogeneity of the data. Different datasets often possess wildly different input sizes and channel dimensions. This discrepancy makes it mathematically and computationally difficult to perform efficient, mixed-batch pre-training, which is a fundamental requirement for developing true [[a-family-of-open-time-series-foundation-models-for-the-radio-access-network|Foundation models]] for temporal data.

### The ADAPT Paradigm
To address this, the researchers propose **ADAPT** (AD