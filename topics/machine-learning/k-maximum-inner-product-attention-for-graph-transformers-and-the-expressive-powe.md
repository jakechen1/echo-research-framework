---
title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive Power of GraphGPS
created: 2024-05-22
source: https://arxiv.org/abs/2604.03815
tags: [ai, machine-learning, graph-neural-networks, scalability]
category: machine-learning
---

# k-Maximum Inner and Product Attention for Graph Transformers and the Expressive Power of GraphGPS

The research paper introduces **k-Maximum Inner Product (k-MIP) attention**, a specialized mechanism designed to overcome the scalability bottlenecks inherent in traditional [[Graph Transformers]]. While traditional [[Graph Neural Networks]] (GNNs) are often limited by phenomena such as [[oversquashing]] and difficulty modeling long-range dependencies, standard Transformer architectures are constrained by the quadratic computational and memory complexity of the all-to-all [[Attention Mechanism]].

## The k-MIP Mechanism

To balance computational efficiency with model effectiveness, the authors propose the k-