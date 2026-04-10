---
title: "Conservation Law Breaking at the Edge of Stability: A Spectral Theory of Non-Convex Neural Network Optimization"
created: 2024-05-22
source: https://arxiv.org/abs/2604.07405
tags: [ai, machine-learning, optimization, neural-networks, spectral-theory]
category: ai, machine-learning
---

# Conservation Law Breaking at the Edge of Stability

A central enigma in [[Machine Learning]] is the apparent efficiency of [[Gradient Descent]] in solving [[Non-Convex Optimization]] problems, despite the theoretical complexity of such landscapes being NP-hard. The research presented in this article provides a mathematical framework to understand this stability through the lens of conservation laws and [[Spectral Theory]].

### $L_1$ Conservation Laws in Gradient Flow
The study demonstrates that during continuous gradient flow in $L$-layer [[ReLU]] networks (specifically those without bias), certain $L_1$ conservation laws are preserved. These laws, defined as $C_l = \|W_{l+1}\|_F^2 - \|W_l\|_F^2$, effectively constrain the optimization trajectory to lower-dimensional manifolds, preventing the errant movement typically expected in high-dimensional, non-convex spaces.

### Symmetry Breaking in Discrete Optimization
While these laws hold during continuous flow, the transition to discrete-step [[Gradient Descent]] introduces a phenomenon known as "drift." This drift breaks the conservation laws, with the magnitude of the break scaling by $\eta^\alpha$, where the exponent $\alpha$ fluctuates between $1.1$ and $1.6$ depending on the specific architecture and loss function. The authors decompose this drift as $\eta^2 \cdot S(\eta)$, utilizing a closed-form spectral crossover formula to track mode coefficients.

### The Role of Cross-Entropy and the Hessian
The research highlights how [[Cross-Entropy Loss]] acts as a self-regularizing mechanism. The concentration of softmax probabilities drives exponential compression within the [[Hess