---
title: Convergence of Byzantine-Resilient Gradient Tracking via Probabilistic Edge Dropout
created: 2024-05-22
source: https://arxiv.org/abs/2604.00449
tags: [Byzantine-resilience, Distributed Optimization, Gradient Tracking, Machine Learning, Robustness]
category: machine-learning
---

# Convergence of Byzantine-Resilient Gradient Tracking via Probabilistic Edge Dropout

The paper "Convergence of Byzantine-Resilient Gradient Tracking via Probabilistic Edge Dropout" addresses a critical vulnerability in [[Distributed Optimization]]: the presence of [[Byzantine Agents]]. In decentralized networks, adversarial agents can transmit arbitrary, malicious messages intended to destabilize the global consensus and prevent the convergence of [[Machine Learning]] models.

### The GT-PD Framework

To combat these threats, the authors introduce **Gradient Tracking with Probabilistic Edge Dropout (GT-PD)**. Unlike traditional robust aggregation methods that often destroy the [[Doubly Stochastic]] mixing structure necessary for efficient convergence, GT-PD employs a dual-layered defense:

1.  **Self-Centered Projection**: A universal defense layer that clips all incoming messages to a specific radius ($\tau$) around the receiving agent, effectively bounding the maximum impact of any single adversarial perturbation.
2.  **Probabilistic Edge Dropout**: A decentralized rule driven by a dual-metric trust score. This mechanism stochastically removes communication edges associated with nodes flagged by the trust metric, effectively isolating malicious actors without disrupting the underlying network topology.

### Addressing Persistent Attacks (GT-PD-L)

In scenarios where Byzantine agents cannot be completely isolated (partial isolation), the authors propose **GT-PD-L**. This variant utilizes a **Leaky Integration** strategy. By applying a leaky integrator to the tracking process, the algorithm can control the accumulation of tracking errors caused by persistent, stealthy perturbations, ensuring the system still achieves linear convergence to a bounded neighborhood.

### Experimental Results

The efficacy of the GT-PD-L method was tested using the [[MNIST]] dataset against various [[Adversarial Attacks]], including:
*   **Sign Flip**
*   **ALIE (Attack on Local Information and Edge-weights)**
*   **Inner Product Manipulation**

The results demonstrate that GT-PD-L provides superior robustness, outperforming the standard coordinate-wise trimmed mean by up to 4.3 percentage points, particularly when facing sophisticated stealth attacks. This research provides a significant advancement in securing decentralized [[Neural Networks]] against adversarial manipulation.