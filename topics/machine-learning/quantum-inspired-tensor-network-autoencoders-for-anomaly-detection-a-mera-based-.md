---
title: Quantum-Inspired Tensor Network Autoencoders for Anomaly Detection: A MERA-Based Approach
created: 2024-05-22
source: https://arxiv.org/abs/2604.06541
tags: [tensor-networks, autoencoders, particle-physics, anomaly-detection, machine-learning]
---

# Quantum-Inspired Tensor Network Autoencoders for Anomaly Detection

In the field of [[particle physics]], identifying rare phenomena within [[collider jets]] remains a critical challenge for modern experiments. The research paper "Quantum-Inspired Tensor Network Autoencoders for Anomaly Detection: A MERA-Based Approach" investigates whether a specific [[tensor networks]] architecture can provide a superior inductive bias for tasks involving [[anomaly detection]].

## Architecture and Methodology

The core innovation presented is a [[machine learning]] architecture inspired by the [[Multi-scale Entanglement Renormalization Ansatz]] (MERA). This approach is motivated by the physical reality of jets, which are generated through a branching cascade process. Because of this process, the internal structure of a jet is naturally organized across different angular and momentum scales.

The proposed MERA-inspired [[autoencoder]] is designed to compress information hierarchically. Unlike a standard [[tree-tensor-network]] (TTN), which focuses purely on coarse-grained compression, the MERA architecture includes "disentangling" layers. These layers allow the model to reorganize short-range correlations before the information is compressed into a lower-dimensional representation. This allows the model to handle the multi-scale nature of the input data more effectively than flat architectures.

## Experimental Findings

The researchers compared this MERA-based approach against several [[deep learning]] benchmarks, including:
*   Dense [[autoencoders]]