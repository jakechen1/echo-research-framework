---
title: Amortized Safe Active Learning for Real-Time Data Acquisition
created: 2024-05-22
source: https://arxiv.org/abs/2501.15458
tags: [active-learning, neural-networks, gaussian-processes, safety-critical-ai, real-time-systems]
category: [ai, machine-learning]
---

# Amortized Safe Active Learning for Real-Time Data Acquisition

The research paper **"Amortized Safe Active Learning for Real-Time Data Acquisition"** addresses a critical bottleneck in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] deployment: the computational latency of [[almab-dc-active-learning-multi-armed-bandits-and-distributed-computing-for-seque|Active Learning]] (AL) in safety-critical, real-time environments. 

### The Problem: Computational Latency
Traditional Safe Active Learning (AL) schemes are designed to learn unknown systems while respecting safety constraints during data acquisition. Current state-of-latency methods frequently rely on [[gaussian-processes|Gaussian Processes]] (GPs) to model both the task and the safety boundaries. However, these methods require repeated GP updates and complex constrained optimization at every step of the acquisition process. This massive computational overhead makes them unsuitable for real-time applications, such