---
title: PD-SOVNet: A Physics-Driven Second-Order Vibration Operator Network
created: 2024-05-23
source: https://arxiv.org/abs/2604.06620
tags: [machine-learning, signal-processing, rail-engineering, Mamba, physics-informed-ml]
category: machine-learning
author: wiki-pipeline
dc.title: "PD-SOVNet: A Physics-Driven Second-Order Vibration Operator Network"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/pd-sovnet-a-physics-driven-second-order-vibration-operator-network-for-estimatin.md
dc.language: en
dc.rights: CC-BY-4.0
---

# PD-SOVNet

**PD-SOVNet** is a physics-guided, gray-box [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] framework designed for the quantitative estimation of wheel polygonal roughness in rail-vehicle [[Condition Monitoring]]. Unlike traditional models that focus primarily on simple detection or classification, PD-SOVNet enables the continuous regression of the 1st–40th order wheel roughness spectrum by processing axle-box vibration signals.

## Architecture and Methodology

The architecture of PD-SOVNet is engineered to bridge the gap between theoretical [[Vibration Analysis]] and data-driven flexibility. The framework integrates several key components:

*   **Shared Second-Order Vibration Kernels:** These kernels embed structural modal-response priors into the network, ensuring the model adheres to fundamental physical principles.
*   **$4\times4$ MIMO Coupling Module:** This module manages the complex interactions within the multi-input, multi-output signal structures.
*   **Adaptive Physical Correction Branch:** This branch allows for sample-dependent corrections, enabling the model to account for deviations from idealized physical models.
*   **Mamba-based Temporal Branch:** Utilizing the [[mamba-linear-time-sequence-modeling-with-selective-state-spaces|Mamba]] architecture (a modern state-space model), this component is specifically designed to capture residual temporal dynamics and intricate patterns in the time-series data.

## Experimental Performance

The efficacy of PD-SOVNet was demonstrated through testing on three real-world datasets, encompassing both standard operational data and specific fault data. Key findings include:

1.  **High Accuracy:** The