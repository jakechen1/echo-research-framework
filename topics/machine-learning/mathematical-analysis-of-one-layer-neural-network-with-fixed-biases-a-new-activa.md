---
title: "Mathematical analysis of one-layer neural network with fixed biases, a new activation function and other observations"
created: 2024-05-24
source: https://arxiv.org/abs/2604.07715
tags: [neural-networks, activation-functions, machine-learning, mathematical-analysis, gradient-descent]
category: machine-learning
---

# Mathematical analysis of one-layer neural network with fixed biases, a new activation function and other observations

This research paper provides a rigorous [[Mathematical Analysis]] of a simplified one-hidden-layer [[Neural Network]] architecture. The study focuses on models utilizing [[ReLU]] activation functions characterized by fixed biases and one-dimensional input and output structures. By investigating both continuous and discrete versions of this specific model, the researchers establish critical proofs regarding the stability and efficiency of the learning process.

A primary contribution of the research is the formal proof of convergence when utilizing the $L^2$ squared loss function under a [[Gradient Descent]] procedure. Beyond convergence, the authors provide mathematical evidence for the "spectral bias" property within this specific learning framework, exploring the intricate relationships between the spectrum of certain operators and the progression of the learning process. This provides a deeper theoretical understanding of how different frequency components are prioritized during training in small-scale models.

The analysis also evaluates the fundamental structural properties that [[Activation Functions]] should possess to facilitate efficient learning. Building upon these observations, the paper proposes a novel alternative activation function: the **Full-wave Rectified Exponential function (FReX)**. The authors provide a detailed discussion on the convergence behavior of gradient descent when applying FReX, offering a new potential tool for [[Machine Learning]] optimization and [[Artificial Intelligence]] architecture design.

Ultimately, the