---
title: Sparse Max-Affine Regression
created: 2024-05-22
source: https://arxiv.org/abs/2411.02225
tags: [machine-learning, optimization, statistics, sparse-learning]
category: machine-learning
---

# Sparse Max-Affine Regression

**Sparse Max-Affine Regression** introduces a novel algorithmic framework for variable selection within convex piecewise linear regression models. The model is characterized by the maximum of $k$ affine functions, expressed as:

$$x \mapsto \max_{j \in [k]} \langle a_j^\star, x \rangle + b_j^\star$$

where $\{ a_j^\star\}_{j=1}^k$ and $\{b_j^\star\}_{j=1}^k$ represent the ground-truth weight vectors and intercepts, respectively. The primary goal is to perform effective [[Feature Selection]] in high-dimensional environments where the number of dimensions $d$ far exceeds the number of observations.

### Sparse Gradient Descent (Sp-GD)

The paper proposes **Sparse Gradient Descent (Sp-GD)** as a robust solution for this optimization problem. The authors provide a non-asymptotic local convergence analysis for Sp-GD under sub-Gaussian noise conditions. When the covariate distribution adheres to sub-Gaussianity and anti-concentration properties, Sp-GD achieves an $\epsilon$-accurate estimate using $\mathcal{O}(\max(\epsilon^{-2}\sigma_z^2,1)s\log(d/s))$ observations. In the ideal, noise-free case, the algorithm enables exact parameter recovery with only $\mathcal{O}(s\log(d/s))$ observations, demonstrating significant efficiency in [[High-Dimensional Statistics]].

### Initialization and RMD

To ensure convergence, the research details a specialized initialization scheme. This process utilizes [[Sparse Principal Component Analysis]] (Sparse PCA) to estimate the subspace spanned by the weight vectors $\{ a_j^\star\}_{j=1}^k$, followed by an $r$-covering search to estimate the remaining model parameters. 

Furthermore, the paper introduces **Real Maslov Dequantization (RMD)**, a transformative technique used to convert sparse generalized polynomials into sparse max-affine models. The error decay rate