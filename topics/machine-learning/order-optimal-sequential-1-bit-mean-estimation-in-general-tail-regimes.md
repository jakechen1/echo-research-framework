---
title: Order-Optimal Sequential 1-Bit Mean Estimation in General Tail Regimes
created: 2024-05-23
source: https://arxiv.org/abs/2604.07796
tags: [mean-estimation, 1-bit-communication, adaptive-algorithms, information-theory, sample-complexity]
category: machine-learning
---

# Order-Optimal Sequential 1-Bit Mean Estimation in General Tail Regimes

The study of **Mean Estimation** under extreme communication constraints is a critical frontier in [[statistical-learning-theory|Statistical Learning Theory]]. This research investigates the problem of estimating the mean ($\mu$) of a distribution when communication is restricted to a **1-bit constraint**. In this setting, the estimator only receives a single bit of information per sample, typically indicating whether a sample exceeds a specific, sequentially chosen threshold.

## Methodology

The paper introduces a novel **adaptive mean estimator** designed to function within the $(\epsilon, \delta)$-PAC (Probably Approximately Correct) framework. The estimator operates using randomized threshold queries. The scope of the estimation covers any distribution where the mean is bounded ($\mu \in [-\lambda, \lambda]$) and the $k$-th central moment is bounded ($\mathbb{E}[|X-\mu|^k] \le \sigma^k$) for any fixed $k > 1$. 

The core strength of this approach lies in its **order-optimality** across various tail regimes. 

## Key Findings

### Sample Complexity and Optimality
The researchers demonstrate that the estimator's **sample complexity** is optimal across all specified $k$-value regimes:
* **For $k \neq 2$:** The estimator matches the unquantized [[minimax-lower-bounds|Minimax Lower Bounds]], subject to a small $O(\log(\lambda/\sigma))$ localization cost.
* **For $k = 2$ (Finite Variance):** The estimator incurs an extra multiplicative $O(\log(\sigma/\epsilon))$ penalty. Crucially, the authors provide an [[information-theory|Information Theory]]-based proof showing that this penalty is a fundamental, unavoidable limit of 1-bit quantization.

### The Adaptivity Gap
A significant contribution of this work is the identification of a major **adaptivity gap**. The study proves that any **non-adaptive estimator** (one that does not adjust thresholds based on previous outcomes) suffers from a sample complexity that scales linearly with the search space parameter $\lambda/\sigma$. This makes non-adaptive approaches vastly less efficient than the proposed adaptive algorithm.

## Algorithmic Extensions
Beyond the primary estimator, the paper presents several robust variants:
1. **Unknown Budgeting:** Algorithms that function effectively under an unknown sampling budget.
2. **Scale Adaptivity:** Methods that adapt to an unknown scale parameter $\sigma$, even when provided with loose initial bounds.
3. **Two-Stage Adaptivity:** Variants that achieve high efficiency using only two stages of adaptivity, utilizing more complex 1-bit interval queries.