---
title: Expressibility of neural quantum states: a Walsh-complexity perspective
created: 2024-05-22
source: https://arxiv.org/abs/2604.03294
tags: [neural quantum states, walsh complexity, many-body physics, expressibility]
category: machine-learning
---

# Expressibility of neural quantum states: a Walsh-complexity perspective

The research paper "Expressibility of neural quantum states: a Walsh-complexity perspective" addresses a fundamental question in quantum many-body physics: which many-body states can be efficiently represented by modern additive [[Machine Learning]] architectures? While [[Neural Quantum States]] (NQS) have proven to be powerful tools for approximating [[Variational Wavefunctions]], the boundaries of their representational capacity have remained poorly defined.

## Walsh Complexity

To bridge this gap, the authors introduce **Walsh complexity**, a basis-dependent metric that measures how broadly a wavefunction is distributed across various parity patterns. The core discovery is that states characterized by an almost uniform Walsh spectrum are exceptionally difficult to approximate. Specifically, any neural network capable of providing a "good" approximation of such states would require an exponentially large Walsh complexity.

## Limitations of Shallow Architectures

The study demonstrates that shallow additive feed-forward networks are fundamentally limited in their ability to generate high Walsh complexity. Under the "tame regime"—defined by polynomial activation functions and subexponential parameter scaling—these networks fail to capture states with high complexity.

As a primary example, the authors construct a simple dimerized state. Although this state possesses only short-range [[Entanglement]] and can be easily described using a [[Tensor Network]] approach, it possesses maximal Walsh complexity. This discrepancy highlights that traditional metrics of complexity, such as entanglement, do not tell the whole story regarding neural network expressibility.

## The Role of Depth and Activation

The paper provides crucial insights into how network architecture influences performance:

* **Polynomial Activations:** Successful fitting of complex states only occurs when the network depth reaches a logarithmic scale relative to the system size ($N$).
* **$\tanh$ Activations:** The researchers observed a sharp, threshold-like jump in expressibility at a relatively low depth of 3.

Ultimately, the research concludes that Walsh complexity provides an expressibility axis that is complementary to [[Entanglement]]. This distinction clarifies why increasing the depth of additive neural architectures is an essential resource for simulating complex quantum phenomena.