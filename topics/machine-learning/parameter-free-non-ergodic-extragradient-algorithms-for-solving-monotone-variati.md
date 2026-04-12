---
title: Parameter-free non-ergodic extragradient algorithms for solving monotone variational inequalities
created: 2024-05-22
source: https://arxiv.org/abs/2604.07662
tags: [optimization, machine-learning, algorithms, variational-inequalities]
---

# Parameter-free non-ergodic extragradient algorithms

The research paper "Parameter-free non-ergodic extragradient algorithms for solving monotone variational inequalities" introduces a novel class of algorithms designed to solve [[monotone-variational-inequalities|monotone variational inequalities]] (VIs). VIs serve as a unified mathematical framework essential for solving [[convex-minimization|convex minimization]], [[equilibrium-computation|equilibrium computation]], and [[convex-concave-saddle-point-problems|convex-concave saddle-point problems]].

### The Challenge of Stepsize Selection
While extragradient-type methods are among the most effective first-order algorithms for these problems, their practical utility is often limited by the difficulty of stepsize selection. Most existing theoretical literature focuses on the convergence of ergodic averages (the average of all previous iterates). However, in practical computational applications, the performance of the "last iterate" is often a much more significant indicator of success. 

Furthermore, existing guarantees for last-iterate convergence typically rely on fixed stepsizes that require knowledge of global smoothness information. In many real-world scenarios, such global information is difficult to estimate or simply non-existent.

### Proposed Solution
The authors develop a set of parameter-free extragradient methods that provide non-asymptotic last-iterate guarantees for constrained monotone VIs. The core contributions include:

* **Global Lipschitz Operators:** For operators that are globally Lipschitz, the proposed algorithm achieves an $o(1/\sqrt{T})$ last-iterate convergence rate.
* **Local Lipschitz Extension:** The framework is extended to [[locally-lipschitz-operators|locally Lipschitz operators]] through the implementation of a [[backtracking-line-search|backtracking line search]]. Crucially, this extension preserves the parameter-free nature of the algorithm while achieving the same convergence rate, making it applicable to complex problem classes where global smoothness is unrealistic.

### Empirical Validation
The efficacy of these algorithms was demonstrated through various numerical experiments across several high-impact domains:
* [[bilinear-matrix-games|Bilinear matrix games]]
* [[lasso|LASSO]] regression
* [[minimax-group-fairness|Minimax group fairness]]
* State-of-the-art [[maximum-entropy-sampling|maximum entropy sampling]] relaxations

The results indicate that these parameter-free methods not only show strong last-iterate performance but also provide significant improvements over existing optimization methods in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] and computational mathematics.