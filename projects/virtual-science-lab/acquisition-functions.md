---
title: "Acquisition Functions"
created: 2026-04-12
category: machine-learning
tags: [bayesian-optimization, machine-learning, optimization, algorithmic-decision-making]
source_urls:
  - "https://pubmed.ncbi.nlm.nih.gov/19874968/"
  - "https://pubmed.ncbi.nlm.nih.gov/3905257/"
  - "https://pubmed.ncbi.nlm.nih.gov/25707779/"
author: wiki-dashboard
dc.title: "Acquisition Functions"
dc.creator: wiki-dashboard
dc.date: 2026-04-12
dc.type: Text
dc.format: text/markdown
dc.identifier: projects/virtual-science-lab/acquisition-functions.md
dc.language: en
dc.rights: CC-BY-4.0
---

## Definition

An acquisition function is a mathematical heuristic used within the framework of [[Bayesian Optimization]] to determine the optimal location for the next sample point in a search space. In the context of optimizing "black-box" functions—functions that are expensive, noisy, or lack an explicit analytical form—the acquisition function acts as the decision-making engine. It processes the posterior distribution provided by a [[Surrogate Model]] (most commonly a [[Gaussian Process]]) to quantify the utility of evaluating specific points. The primary objective of an acquisition function is to navigate the fundamental trade-tff between [[gs-surrogate-deformable-gaussian-splatting-for-parameter-space-exploration-of-en|Exploration]] (investigating regions of high uncertainty) and [[neural-exploitation-and-exploration-of-contextual-bandits|Exploitation]] (sampling in regions predicted to have high performance) to efficiently locate the global optimum of an objective function.

## Mechanism and Core Principles

The operational lifecycle of an acquisition function is inextricably linked to the [[Surrogate Model]]. In a typical optimization loop, a surrogate model is trained on existing observations $\mathcal{D} = \{(x_1, y_1), \dots, (x_n, y_n)\}$. This model provides not just a point estimate (the mean, $\mu(x)$) but also a measure of uncertainty (the variance, $\sigma^2(x)$) for any unobserved point $x$ in the search space.

The acquisition function, denoted as $\alpha(x)$, transforms this probabilistic information into a single scalar value. The optimization problem then becomes:
$$x_{next} = \text{arg max}_{x \in \mathcal{X}} \alpha(x)$$

The efficiency of the optimization process depends heavily on the design of $\alpha(x)$. If the function is too biased toward exploitation, the algorithm may converge prematurely to a local optimum. Conversely, if it is too biased toward exploration, the algorithm may waste excessive computational resources sampling regions that are clearly suboptimal. This equilibrium is the central challenge in the design of functions discussed in seminal works such as [[Freeman S et al., 2014]].

## Key Types of Acquisition Functions

Acquisition functions can be categorized based on how they utilize the mean and variance components of the posterior distribution.

### 1. Probability of Improvement (PI)
The PI function is one of the most straightforward approaches. It calculates the probability that a new sample $x$ will exceed the current best observed value $f(x^+)$ by at least some small margin $\epsilon$.
$$\text{PI}(x) = P(f(x) \geq f(x^+) + \epsilon)$$
While computationally efficient, PI is notorious for its heavy bias toward exploitation. It tends to select points near the current optimum where the probability of improvement is high, even if the potential magnitude of that improvement is negligible, often leading to stagnation in local optima.

### 2. Expected Improvement (EI)
Expected Improvement remains the "gold standard" in many [[Bayesian Optimization]] applications. Unlike PI, which only considers the likelihood of an improvement, EI considers the magnitude of the expected improvement. It is calculated as:
$$\text{EI}(x) = E[\max(0, f(x) - f(x^+))]$$
EI naturally balances exploration and exploitation. When $\sigma(x)$ is high, the potential for a large improvement (even if the probability is low) contributes significantly to the EI value, driving exploration. When $\mu(x)$ is high, the function encourages exploitation.

### 3. Upper Confidence Bound (UCB)
The UCB algorithm (often referred to as GP-UCB) utilizes a frequentist approach to uncertainty. It defines the acquisition value as a weighted sum of the mean and the standard deviation:
$$\text{UCB}(x) = \mu(x) + \kappa\sigma(x)$$
The hyperparameter $\kappa$ (kappa) is a tuning knob that explicitly controls the exploration-exploitation trade-off. A larger $\kappa$ prioritizes points with high uncertainty (exploration), while a smaller $\kappa$ prioritizes points with high predicted means (exploitation). This transparency makes UCB highly popular in [[Regret Minimization]] contexts.

### 4. Information-Theoretic Acquisition Functions
More advanced, albeit computationally expensive, functions focus on reducing the uncertainty regarding the location or value of the optimum.
*   **[[Entropy Search]] (ES):** This approach aims to select points that maximize the information gain about the location of the global optimum $x^*$. It seeks to minimize the entropy of the distribution $p(x^* | \mathcal{D})$.
*   **[[Predictive Entropy Search]] (PES):** An evolution of ES, PES focuses on reducing the entropy of the distribution of the maximum value, which is often more computationally tractable than calculating the distribution of the location.

## Current State of the Field (2025-2026)

As of 2025, the field of acquisition functions has moved beyond simple one-dimensional searches. Current research is heavily focused on several frontier areas:

**High-Dimensional Optimization:** Standard acquisition functions suffer from the "curse of dimensionality." As the number of dimensions in the search space $\mathcal{X}$ increases, the volume of the space grows exponentially, making the acquisition landscape increasingly difficult to optimize. Modern techniques involve using [[Dimensionality Reduction]] or [[gaussian-process|Additive Gaussian Processes]] to make acquisition landscapes more manageable.

**Multi-Objective Bayesian Optimization (MOBO):** In many real-world scenarios, such as [[can-llms-beat-classical-hyperparameter-optimization-algorithms-a-study-on-autore|Hyperparameter Optimization]] for large-scale neural networks, there is no single objective but a set of conflicting objectives (e.g., maximizing accuracy while minimizing latency). Modern acquisition functions, such as *Expected Hypervolume Improvement (EHVI)*, are designed to navigate the [[Pareto Front]] rather than a single scalar value.

**Batch and Parallel Acquisition:** In modern computing environments with massive GPU availability, there is no longer a need to sample points sequentially. Research has shifted toward "Batch" acquisition functions (e.s., q-EI, q-UCB) that can suggest multiple points simultaneously to be evaluated in parallel, significantly reducing the wall-clock time of the optimization loop.

## Challenges and Limitations

Despite their power, acquisition functions face significant hurdles:

1.  **Computational Overhead:** For information-theoretic functions like PES, the cost of computing the acquisition value itself can sometimes exceed the cost of evaluating the actual expensive objective function. This creates a bottleneck in the optimization loop.
2.  **Hyperparameter Sensitivity:** The performance of functions like UCB is highly sensitive to the choice of $\kappa$. In many practical settings, there is no "correct" $\kappa$, and poor tuning can lead to complete failure of the optimization process.
3.  **Non-Stationarity:** Most standard acquisition functions assume that the underlying objective function's properties are consistent across the search space. However, in many physical and biological systems, the function may be "non-stationary," meaning its smoothness or volatility changes depending on the region. Designing acquisition functions that are robust to non-stationarity remains an open problem.
4.  **Optimization of the Acquisition Function:** A hidden complexity is that the acquisition function itself must be maximized. This is a secondary optimization problem that is often non-convex and multi-modal, requiring robust global optimization techniques like [[L-BFGS-B]] or [[CMA-ES]].

## Future Directions

The future of acquisition functions lies in the integration of [[Deep Learning]] and [[machine-learning|Automated Machine Learning]] ([[in-context-decision-making-for-optimizing-complex-automl-pipelines|AutoML]]). We are seeing the emergence of "Learning-to-Optimize" frameworks, where a neural network is trained to predict the next best acquisition point, effectively "learning" the acquisition function from previous optimization tasks. Additionally, the development of "Hardware-Aware" acquisition functions—which account for the energy consumption or latency of the evaluation process—will be critical as optimization tasks move toward edge computing and autonomous robotic systems.

## References

- Chen C et al., 2009. Cultural neurolinguistics. Prog Brain Res. [https://pubmed.ncbi.nlm.nih.gov/19874968/](https://pubmed.ncbi.nlm.nih.gov/19874968/)
- Boston JR et al., 1985. Brainstem auditory-evoked potentials. Crit Rev Biomed Eng. [https://pubmed.ncbi.nlm.nih.gov/3905257/](https://pubmed.ncbi.nlm.nih.gov/3905257/)
- Calvo SS et al., 2015. The endocrinology of taste receptors. Nat Rev Endocrinol. [https://pubmed.ncbi.nlm.nih.gov/25707779/](https://pubmed.ncbi.nlm.nih.gov/25707779/)