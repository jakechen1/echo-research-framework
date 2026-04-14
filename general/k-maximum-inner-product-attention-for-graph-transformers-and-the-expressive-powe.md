---
title: k-Maximum Inner Product Attention for Graph Transformers and the Expressive Power of GraphGPS
created: 2024-05-22
source: https://arxiv.org/abs/2604.03815
tags: [ai, machine-learning, graph-neural-networks, scalability]
category: machine-learning
author: wiki-pipeline
dc.title: "k-Maximum Inner Product Attention for Graph Transformers and the Expressive Power of GraphGPS"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/k-maximum-inner-product-attention-for-graph-transformers-and-the-expressive-powe.md
dc.language: en
dc.rights: CC-BY-4.0
---

# k-Maximum Inner and Product Attention for Graph Transformers and the Expressive Power of GraphGPS

The research paper introduces **k-Maximum Inner Product (k-MIP) attention**, a specialized mechanism designed to overcome the scalability bottlenecks inherent in traditional [[biscale-gtr-fragment-aware-graph-transformers-for-multi-scale-molecular-represen|Graph Transformers]]. While traditional [[openglt-a-comprehensive-benchmark-of-graph-neural-networks-for-graph-level-tasks|Graph Neural Networks]] (GNNs) are often limited by phenomena such as [[oversquashing]] and difficulty modeling long-range dependencies, standard Transformer architectures are constrained by the quadratic computational and memory complexity of the all-to-all [[Attention Mechanism]].

## The k-MIP Mechanism

To balance computational efficiency with model effectiveness, the authors propose the k-