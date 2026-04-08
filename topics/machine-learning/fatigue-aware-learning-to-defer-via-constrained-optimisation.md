---
title: Fatigue-Aware Learning to Defer via Constrained Optimisation
created: 2024-05-22
source: https://arxiv.org/abs/2604.00904
tags: [machine-learning, human-ai collaboration, optimization, neural networks, automation]
category: machine-learning
---

# Fatigue-Aware Learning to Defer via Constrained Optimisation

The research paper "Fatigue-Aware Learning to Defer via Constrained Optimisation" addresses a critical flaw in current [[Learning to Defer (L2D)]] frameworks: the assumption of static human performance. In practical [[Human-AI Collaboration]] scenarios, human experts are subject to performance degradation caused by cognitive workload and fatigue, a factor traditionally ignored by automated delegation models.

## The FALCON Framework

The authors propose **FALCON** (*Fatigue-Aware Learning to Defer via Constrained Optimisation*), a novel method designed to explicitly model the fluctuating performance of human experts. Unlike traditional L2D approaches that treat the human responder as a constant reliability factor, FALCON incorporates psychologically grounded fatigue curves to predict how accuracy diminishes as cumulative workload increases.

To manage this complexity, the paper formulates the L2D problem as a [[Constrained Markov Decision Process (CMDP)]]. The decision-making state within this model is multi-dimensional, encompassing:

*   **Task-specific features:** The inherent difficulty or characteristics of the input data.
*   **Cumulative human workload:** The historical tally of tasks assigned to the human, used to estimate current fatigue levels.

The optimization process is executed using **PPO-Lagrangian training**, a variation of [[Proximal Policy Optimization (PPO)]], which allows the system to optimize for overall accuracy while strictly adhering to predefined human-AI cooperation budgets.

## Benchmarking and Results

To evaluate the robustness of FALCON, the researchers introduced **FA-L2D**, a new benchmark designed to simulate various fatigue dynamics—ranging from near-static performance to rapid, high-intensity degradation.

Key experimental findings include:
*   **Superior Performance:** FALCON consistently outperforms existing state-of-the-art L2D methods across various coverage levels.
*   **Zero-Shot Generalization:** The model demonstrates an ability to generalize to unseen experts with different fatigue patterns without the need for additional retraining.
*   **Optimal Coordination:** The study proves that adaptive human-AI decision-making provides a significant advantage over either purely autonomous AI or purely human-driven systems when coverage lies between 0 and 1.

This work represents a significant step toward creating more resilient and biologically-aware [[Artificial Intelligence]] systems capable of working alongside humans in high-stakes, long-duration environments.