---
title: On the Mirage of Long-Range Dependency, with an Application to Integer Multiplication
created: 202    24-05-22
source: https://arxiv.org/abs/2603.29069
tags: [long-range-dependency, neural-networks, algorithmic-learning, representation-learning]
category: ai, machine-learning
---

# On the Mirage of Long-Range Dependency, with an Application to Integer Multiplication

The research paper *"On the Mirage of Long-Range Dependency, with an Application to Integer Multiplication"* challenges a foundational assumption in [[Machine Learning]]: the idea that certain computational tasks possess intrinsic [[Long-Range Dependency]] (LRD).

### The Problem of Carry Chains
In the context of [[Integer Multiplication]], it has long been believed that the task is difficult for [[Neural Networks]] because of the $O(n)$ dependency created by "carry chains." In a standard 1D bit-string representation, a single bit change can propagate through the entire sequence, necessitating a model capable of capturing distant relationships.

### The "Mirage" Hypothesis
The authors argue that this LRD is not an intrinsic property of multiplication but a "mirage" produced by the choice of **computational spacetime**—essentially, how the input data is laid out for the model. 

The authors provide a constructive proof by re-representing two $n$-bit binary integers as a 2D outer-product grid. Under this 2D representation, the complex long-range multiplication process collapses into a simple $3 \times 3$ local neighborhood operation.

### Comparative Performance of Architectures
The study compares the efficiency and generalization capabilities of various architectures using this 2D approach:

*   **[[Neural Cellular Automata]] (NCA):** Using a minimal set of only 321 learnable parameters, the NCA achieved perfect **length generalization**, performing multiplication up to $683\times$ the range seen during training.
*   **[[Transformer]] Architectures:** Models such as the standard [[Transformer]] (6,625 parameters) and [[Transformer with RoPE]] failed to achieve comparable generalization.
*   **[[Mamba]] (SSMs):** Even advanced [[State Space Models]] designed for efficient long-sequence modeling failed to match the performance of the localized NCA.

### Implications for [[Artificial Intelligence]]
The findings suggest a paradigm shift in how we approach [[Computational Complexity]] in deep learning. The authors conclude that any task currently diagnosed as requiring long-range dependency should first be scrutinized to determine if the dependency is **intrinsic** to the mathematical task or merely an artifact of the chosen data representation.