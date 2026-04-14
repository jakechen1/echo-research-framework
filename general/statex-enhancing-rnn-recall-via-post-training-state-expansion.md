---
title: StateX: Enhancing RNN Recall via Post-training State Expansion
created: 2024-05-23
source: https://arxiv.org/abs/2509.22630
tags: [RNN, StateX, machine-learning, long-context, post-training]
category: machine-learning
author: wiki-pipeline
dc.title: "StateX: Enhancing RNN Recall via Post-training State Expansion"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/statex-enhancing-rnn-recall-via-post-training-state-expansion.md
dc.language: en
dc.rights: CC-BY-4.0
---

# StateX: Enhancing RNN Recall via Post-training State Expansion

StateX is a novel post-training framework designed to address the fundamental limitations of [[Recurrent Neural Networks]] (RNNs) when processing long-range dependencies. While modern architectures, such as [[linear attention]] and [[adversarial-robustness-of-deep-state-space-models-for-forecasting|state-space models]] (SSMs), are highly valued for their efficiency and constant per-token complexity, they face a significant bottleneck: all historical information must be compressed into a fixed-size recurrent state. This inherent compression often leads to degraded [[statex-enhancing-rnn-recall-via-post-training-state-expansion|recall]] performance in tasks that require the precise retrieval of information from distant contexts.

### The Challenge of State Size
Theoretically, the ability of an RNN to recall information is positively correlated with the size of its recurrent state. However, increasing this state size during the initial training phase is computationally prohibitive, as it leads to significantly higher [[training costs]]. Researchers have long sought a way to scale memory capacity without the need for expensive, large-scale retraining from scratch.

### The StateX Framework
StateX introduces an efficient solution by providing a mechanism to expand the states of pre-trained RNNs during a post-training phase. The framework implements specialized architectural modifications tailored for two popular classes of models:
* **Linear Attention**
* **State-Space Models (SSMs)**

The primary innovation of StateX is its ability to scale up the state size with no or negligible increase in the total number of model parameters. By focusing on expanding the hidden state capacity rather than the parameter count of the weights, StateX avoids the traditional computational pitfalls of model scaling.

### Experimental Results
Experiments conducted on models with up to 1.3B parameters demonstrate that StateX effectively enhances both [[graphwalker-graph-guided-in-context-learning-for-clinical-reasoning-on-electroni|in-context learning]] and long-context recall performance. Notably, these gains are achieved without incurring the high costs associated with large-scale training and without compromising the model's existing capabilities on other downstream tasks. This makes StateX a highly scalable approach for optimizing efficient architectures for long-context applications in [[artificial-intelligence-and-the-structure-of-mathematics|artificial intelligence]].