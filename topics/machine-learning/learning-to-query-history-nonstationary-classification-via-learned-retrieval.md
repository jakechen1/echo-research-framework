---
title: Learning to Query History: Nonstationary Classification via Learned Retrieval
created: 2024-05-22
source: https://arxiv.org/abs/2604.07027
tags: [machine-learning, nonstationarity, retrieval, classification, time-series]
category: machine-learning
---

# Learning to Query History: Nonstationary Classification via Learned Retrieval

In the field of [[Machine Learning]], [[Nonstationarity]] remains a primary obstacle to the long-term deployment of models. Even when a model demonstrates high accuracy on holdout sets during training, its performance often degrades when the underlying [[Data Distribution]] shifts in a real-world environment. The paper "Learning to Query History: Nonstationary Classification via Learned Retrieval" proposes a novel architectural approach to mitigate this-driven degradation.

### Core Concept: Classification as Time Series Prediction
The authors propose reframing the problem of nonstationary classification as a [[Time Series Prediction]] task. Instead of relying exclusively on the current input $x_t$, the proposed framework conditions the classifier on a sequence of historical labeled examples. This allows the model to "observe" the evolution of the data distribution beyond the initial training cutoff.

### Learned Retrieval Mechanism
To address the computational challenges of processing large historical sequences, the researchers developed a [[Learned Discrete Retrieval]] mechanism. This system uses input-dependent queries to sample the most pertinent historical examples from a larger dataset. 

A significant technical contribution is the implementation of a [[Score-based Gradient Estimator]]. This allows the retrieval mechanism and the classifier to be optimized [[End-to-end]], overcoming the traditional difficulties of backpropagating through discrete sampling operations. Furthermore, this architecture allows the historical corpus to remain on an external [[Filesystem]], ensuring that the entire dataset does not need to be loaded into active memory during training or inference.

### Performance and Scalability
The framework was evaluated using synthetic benchmarks and the [[Amazon Reviews]] '23 dataset (electronics category). The results indicated:
* **Robustness:** Significant improvement in maintaining accuracy during [[Distribution Shift]] compared to standard, static classifiers.
* **Memory Trade-offs:** The [[VRAM]] requirements scale predictably with the length of the historical sequence provided to the model.

While the approach provides high robustness, developers must balance the length of the historical window against the increased [[Computational Complexity]] and memory footprint.