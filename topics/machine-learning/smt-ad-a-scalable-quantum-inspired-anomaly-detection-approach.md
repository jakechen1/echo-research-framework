---
title: "SMT-AD: a scalable quantum-inspired anomaly detection approach"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.06265"
tags: [machine-learning, quantum-inspired, tensor-networks, anomaly-detection, scalability]
category: machine-learning
---

# SMT-AD: a scalable quantum-inspired anomaly detection approach

SMT-AD, which stands for **Superposition of Multiresolution Tensors for Anomaly Detection**, is a novel [[machine-learning]] framework designed to provide an efficient, highly parallelizable solution for [[anomaly detection]] tasks. Drawing inspiration from [[quantum computing]] architectures, the approach utilizes [[tensor networks]] to model complex data patterns with high computational efficiency.

### Technical Architecture
The core innovation of SMT-AD lies in its use of the superposition of bond-dimension-1 [[matrix product operators]] (MPOs). To process high-dimensional inputs, the architecture employs a **Fourier-assisted feature embedding** technique. One of the most significant advantages of this method is its inherent scalability; unlike many traditional [[neural networks]], the number of learnable parameters in SMT-AD grows only linearly with the feature size, the number of embedding resolutions, and the additional components within the MPO structure. This linear complexity makes it an ideal candidate for processing massive, real-time data streams.

### Performance and Practical Utility
The effectiveness of SMT-AD has been demonstrated on standard benchmark datasets, including datasets involving [[credit card transactions]]. The research indicates that even with minimal configurations, SMT-AD achieves performance levels that are competitive with established [[anomaly