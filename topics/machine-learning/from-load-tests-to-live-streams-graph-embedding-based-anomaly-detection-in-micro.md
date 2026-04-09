---
title: From Load Tests to Live Streams: Graph Embedding-Based Anomaly Detection in Microservice Architectures
created: 2024-05-22
source: https://arxiv.org/abs/2604.06448
tags: [anomaly detection, microservices, graph neural networks, machine learning, observability]
category: machine-learning
---

# From Load Tests to Live Streams

The research paper "From Load Tests to Live Streams" addresses a critical challenge in managing large-scale [[Microservice Architectures]]: the discrepancy between simulated [[Load Testing]] environments and the unpredictable traffic patterns of real-world live streaming events. Using [[Prime Video]] as a primary case study, the authors demonstrate that while traditional stress tests validate system capacity, they often fail to replicate the unique service behaviors and dependencies triggered during high-concurrency events like [[Thursday Night Football]].

## Methodology

To address this gap, the authors propose an unsupervised [[Anomaly Detection]] system capable of identifying under-represented services. The technical core of the approach involves generating node-level graph embeddings through a hybrid architecture known as **GCN-GAE** ([[Graph Convolutional Network]] and [[Graph Autoencoder]]). 

The process follows several key steps:
1. **Graph Construction**: The system builds directed, weighted service graphs representing the microservice ecosystem at a minute-level resolution.
2. **Feature Learning**: The GCN-GAE architecture learns complex structural representations (embeddings) of the service dependencies.
3. **Similarity Analysis**: The system flags anomalies by calculating the [[Cosine Similarity]] between the embeddings derived from controlled load tests and those captured during live streaming events.

## Performance and Results

The researchers introduced a synthetic anomaly injection framework to evaluate the system's efficacy in a controlled setting. The experimental results indicate high reliability, though they highlight specific areas for improvement in [[Distributed Systems]] monitoring:

* **Precision**: 96% 
* **False Positive Rate**: 0.08%
* **Recall**: 58%

While the remarkably low false-positive rate makes the system highly actionable for engineers, the lower recall suggests that current propagation assumptions may miss certain complex anomaly types.

## Significance

This work provides a foundational methodology for improving observability in [[Cloud Computing]] environments. By shifting from simple threshold-based monitoring to deep-learning-based structural analysis, the system offers a path toward more resilient and self-healing microservice ecosystems.