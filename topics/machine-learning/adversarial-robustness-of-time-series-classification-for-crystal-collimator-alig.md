---
title: Adversarial Robustness of Time-Series Classification for Crystal Collimator Alignment
created: 2024-05-22
source: https://arxiv.org/abs/2604.06289
tags: [machine-learning, adversarial-robustness, particle-physics, time-series-analysis]
category: machine-learning
---

# Adversarial Robustness of Time-Series Classification for Crystal Collimator Alignment

This article explores the vulnerabilities and defenses of [[Convolutional Neural Networks]] (CNNs) utilized in the high-precision environment of [[CERN]]'s [[Large Hadron Collider (LHC)]]. The primary application involves the automated alignment of crystal collimators by classifying data streams from [[Beam-loss Monitor]] (BLM) sensors.

## Problem Statement
The alignment process depends on analyzing [[Time-Series]] data generated during crystal rotation. While these CNNs are highly effective at pattern recognition, they are susceptible to adversarial attacks—small, intentional perturbations that can trick the model into incorrect classifications. In the context of the LHC, such misclassifications could lead to improper collimator settings, potentially endangering beam stability.

## Methodology
A major hurdle in the [[Formal Verification]] of these models is the complex, non-linear preprocessing required for raw sensor data, including z-normalization and padding. To bridge this gap, the researchers developed a **preprocessing-aware wrapper**. This differentiable layer integrates normalization and padding constraints directly into the model pipeline, allowing existing [[Machine Learning]] robustness frameworks to interact with the deployed system.

The study utilizes established benchmarking tools, specifically [[Foolbox]] and the [[Adversarial Robustness Toolbox (ART)]], to estimate robustness and validate the pipeline against gradient-based attacks.

## Key Contributions and Results
*   **Adversarial Fine-Tuning:** By implementing [[Adversarial Training]] techniques, the authors achieved an increase in robust accuracy of up to **18.6%** without sacrificing the model's performance on clean, undistorted data.
*   **Sequence-Level Robustness:** The research extends beyond individual data windows to analyze sliding-window classification. The authors identified that adversarial perturbations can create "adversarial sequences" that compromise temporal robustness.
*   **Temporal Persistence:** The study observed that misclassifications induced by adversarial attacks tend to persist across