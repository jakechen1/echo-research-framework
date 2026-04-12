---
title: Primal-Dual Methods for Nonsmooth Nonconvex Optimization with Orthogonality Constraints
created: 2024-05-22
source: https://arxiv.org/abs/2604.04130
tags: [optimization, primal-dual, nonsmooth, nonconvex, algorithmic-complexity]
category: machine-learning, technology
---

# Primal-Dual Methods for Nonsmooth Nonconvex Optimization with Orthogonality Constraints

The research presented in this paper addresses a critical bottleneck in modern [[data-science|Data Science]]: the optimization of problems involving both [[nonsmoothness|Nonsmoothness]] and orthogonality constraints. As high-dimensional datasets grow, the ability to perform efficient [[primal-dual-methods-for-nonsmooth-nonconvex-optimization-with-orthogonality-cons|Nonconvex Optimization]] on structures like the [[stiefel-manifold|Stiefel Manifold]] becomes increasingly vital.

### The Challenge of Orthogonality
While [[riemannian-optimization|Riemannian Optimization]] has emerged as a powerful paradigm for handling orthogonality constraints, the authors identify several significant limitations when these problems become nonsmooth. Current Riemannian methods often face issues regarding:
* **Scalability and Parallelizability:** High computational costs in large-scale settings.
* **Complex Subproblems:** The requirement to solve difficult internal optimization tasks.
* **Numerical Instability:** Cumulative errors that threaten the feasibility of the resulting orthogonal matrices.

### The Proposed Solution
To mitigate these issues, the paper introduces a **retraction-free primal-dual approach**. The authors propose a specialized **linearized smoothing augmented Lagrangian method** specifically engineered for nonsmooth and nonconvex landscapes. 

Unlike traditional methods, this new approach is:
1. **Single-loop:** Reducing the overhead of nested optimization layers.
2. **Subproblem-free:** Eliminating the need to solve complex secondary optimization tasks, which enhances computational speed.

### Theoretical and Numerical Contributions
The paper provides rigorous mathematical foundations for the proposed method. The authors establish an iteration complexity of $O(\epsilon^{-3})$ for finding $\epsilon$-KKT points, a result that matches the best-known performance benchmarks in existing [[riemannian-optimization|Riemannian Optimization]] literature. Furthermore, by applying the [[kurdyka-lojasiewicz-kl-property|Kurdyka-Lojasiewicz (KL) property]], the research demonstrates the asymptotic sequential convergence of the algorithm.

Numerical experiments confirm the practical utility of the method. When tested against state-of-the-art algorithms on both smooth and nonsmooth problems, the proposed primal-dual method demonstrated superior computational efficiency and significantly better scalability, making it a robust candidate for large-scale [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] and [[algorithmic-complexity|Algorithmic Complexity]] applications.