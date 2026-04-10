---
title: Leveraging Complementary Embeddings for Replay Selection in Continual Learning with Small Buffers
created: 2024-05-22
source: https://arxiv.org/abs/2604.08336
tags: [continual-learning, replay-buffer, self-supervised-learning, machine-learning, computer-vision]
category: machine-learning
---

# Leveraging Complementary Embeddings for Replay Selection in Continual Learning with Small Buffers

[[Catastrophic forgetting]] remains one of the most significant hurdles in the field of [[Continual Learning]] (CL). When training models on a continuous stream of data, the loss of previously learned information—especially under severe memory constraints—can drastically degrade long-term performance. In [[Replay-based Learning]] strategies, the efficiency of the model is heavily dependent on the sample selection strategy used to populate the [[Replay Buffer]].

## The Limitation of Current Approaches
Traditionally, most selection strategies rely on embeddings learned through [[Supervised Learning]] objectives. While effective for class-specific distinctions, these embeddings often fail to capture the broader, class-agnostic semantic features present in the data. These overlooked features are often encoded within [[Self-supervised Learning]] representations, which offer a more holistic view of the underlying data distribution.

## The MERS Method
The paper introduces **Multiple Embedding Replay Selection (MERS)**, a novel approach designed to optimize buffer utilization. Rather than relying on a single feature set, MERS utilizes a graph-based method to integrate both supervised and self-supervised embeddings. By leveraging these complementary datasets, the algorithm can select more representative and semantically rich samples for the buffer.

## Key Findings and Advantages
The research demonstrates that MERS provides consistent improvements over current State-of-the-Art (SOTA) selection strategies. Key benefits include:

* **Efficiency in Low-Memory Regimes:** MERS shows particularly strong performance gains when the [[Replay Buffer]] size is strictly limited.
* **Zero Parameter Overhead:** The method does not require adding new model parameters or increasing the total volume of replayed data.
* **Empirical Success:** Significant performance boosts were observed on standard benchmarks, specifically **CIFAR-100** and **TinyImageNet**.

Because MERS functions as a "drop-in" enhancement, it can be integrated into existing [[Replay-based CL]] algorithms without fundamental architectural changes. This makes it a highly practical solution for [[Machine Learning]] practitioners working under hardware or memory constraints.