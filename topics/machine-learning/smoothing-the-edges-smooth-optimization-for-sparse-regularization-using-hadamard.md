---
title: Smoothing the Edges: Smooth Optimization for Sparse Regularization using Hadamard Overparametrization
created: 2023-10-27
source: https://arxiv.org/abs/2307.03571
tags: [optimization, sparsity, deep learning, neural networks, machine learning]
category: machine-learning
---

# Smoothing the Edges: Smooth Optimization for Sparse Regularization using Hadamard Overparametrization

The paper "Smoothing the Edges" introduces a novel mathematical framework designed to address the inherent difficulties in optimizing non-smooth and potentially non-convex objectives, particularly those used for achieving [[structured-sparsity|structured sparsity]]. Traditionally, optimization problems involving sparsity-inducing regularizers rely on specialized solvers tailored to specific models. This research proposes a method that enables fully differentiable and approximation-free optimization, making it seamlessly compatible with the [[multirate-stein-variational-gradient-descent-for-efficient-bayesian-sampling|gradient descent]] paradigm used in modern [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|deep learning]].

## Core Methodology

The central innovation of this work is a technique termed [[hadamard-overparametrization|Hadamard Overparametrization]]. This process utilizes an "optimization transfer" consisting of two primary components:
1. **Parameter Overparameterization**: Selecting and expanding specific parameters within the model.
2. **Penalty Transformation**: Implementing a change of penalties such that a smooth surrogate regularization in the overparameterized space induces the intended non-smooth, sparse regularization in the base parameter space.

## Theoretical Contributions

A significant achievement of this research is the formal proof of equivalence between the surrogate objective and the original sparse objective. The authors demonstrate that the two problems possess identical [[global-minima|global minima]] and, crucially, matching [[local-minima|local minima]]. This equivalence is vital for practical applications, as it guarantees that the smoothness introduced during optimization does not lead to the creation of spurious solutions or false optima. 

Furthermore, the theoretical framework establishes broader implications regarding the matching of local minima for arbitrary, and potentially unregularized, objectives, contributing significant insights to the field of [[mathematical-optimization|mathematical optimization]].

## Applications and Results

The authors provide a comprehensive review of various sparsity-inducing parametrizations across multiple scientific disciplines and propose several enhancements to their scope. To validate their theory, the researchers conducted numerical experiments across a variety of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] tasks. The results demonstrate the effectiveness of the approach in both [[high-dimensional-regression|high-dimensional regression]] and the training of [[sparse-neural-networks|sparse neural networks]], proving that the method maintains accuracy and efficiency while benefiting from the ease of smooth optimization.