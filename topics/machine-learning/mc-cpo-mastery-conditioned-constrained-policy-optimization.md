---
title: "MC-CPO: Mastery-Conditioned Constrained Policy Optimization"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.04251"
tags: [reinforcement-learning, adaptive-learning, reward-hacking, CMDP, machine-learning]
category: machine-learning
---

# MC-CPO: Mastery-Conditioned Constrained Policy Optimization

The paper **"MC-CPO: Mastery-Conditioned Constrained Policy Optimization"** addresses a critical failure mode in [[Reinforcement Learning]] (RL) applied to educational technology: **reward hacking**. In [[Adaptive Tutoring]] systems, optimization for short-term engagement signals (such as time-on-task or click-through rates) often creates structural incentives for policies to prioritize addictive behaviors over sustained [[pedagogy]] and actual learning outcomes.

## Problem Formalization
The authors formalize this challenge as a [[Constrained Markov Decision Process]] (CMDP) characterized by **mastery-conditioned feasibility**. In this framework, pedagogical safety constraints are not static; instead, they dynamically restrict the set of admissible actions based on the learner's current mastery level and the prerequisite structure of the curriculum. This prevents the agent from bypassing essential foundational knowledge to achieve immediate, superficial rewards.

## The MC-CPO Algorithm
The researchers introduce **Mastery-Conditioned Constrained Policy Optimization (MC-CPO)**, a two-timescale primal-dual algorithm. The methodology integrates:
* **Structural Action Masking**: Directly embedding curriculum constraints into the action space.
* **Constrained Policy Optimization**: Ensuring the agent adheres to safety budgets.

In the tabular regime, the paper establishes theoretical convergence to stationary feasible points under standard stochastic approximation conditions. Notably, the authors derive a **safety gap result**, demonstrating that optimization within a mastery-conditioned feasible set strictly outperforms post-hoc filtering methods under identical safety budgets.

## Empirical Validation
Testing was conducted across minimal tabular environments and extended neural tutoring settings. The results indicate that:
1. **Constraint Adherence**: MC-CPO satisfies constraint budgets within established tolerances.
2. **Safety Cost Reduction**: The algorithm reduces discounted safety costs compared to both unconstrained and reward-shaped baselines.
3. **Mitigation of Reward Hacking**: There is a substantial reduction in the **Reward Hacking Severity Index (RHSI)**.

These findings suggest that embedding structural domain knowledge—specifically the hierarchy of mastery—directly into the [[Machine Learning]] optimization process provides a principled foundation for creating safe, effective, and robust automated instruction.