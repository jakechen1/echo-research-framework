---
title: Extended Hybrid Timed Petri Nets with Semi-Supervised Anomaly Detection for Switched Systems, Modelling and Fault Detection
created: 2024-05-24
source: https://arxiv.org/abs/2604.04051
tags: [hybrid systems, petri nets, anomaly detection, fault detection, machine learning, control theory]
category: machine-learning
author: wiki-pipeline
dc.title: "Extended Hybrid Timed Petri Nets with Semi-Supervised Anomaly Detection for Switched Systems, Modelling and Fault Detection"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/extended-hybrid-timed-petri-nets-with-semi-supervised-anomaly-detection-for-swit.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Extended Hybrid Timed Petri Nets with Semi-Supervised Anomaly Detection

The research paper, "Extended Hybrid Timed Petri Nets with Semi-Supervised Anomaly Detection for Switched Systems, Modelling and Fault Detection," addresses the fundamental challenges in monitoring hybrid physical systems. These systems are uniquely complex because they involve the simultaneous interaction of [[Continuous Dynamics]] and [[Discrete Dynamics]], both of which are susceptible to overlapping fault patterns.

## The ETCPN Model
Traditional fault detection methods often treat discrete and continuous components as separate entities. To bridge this gap, the authors propose an **Extended Timed Continuous Petri Net (ETCPN)**. This model improves upon standard [[extended-hybrid-timed-petri-nets-with-semi-supervised-anomaly-detection-for-swit|Petri Nets]] by introducing marking-dependent flow functions. This innovation allows for an intrinsic coupling between the different dynamics, providing a more accurate representation of how state changes in the discrete layer affect the continuous flow.

## Detection Framework
The proposed framework utilizes a mode-dependent hybrid observer designed to monitor the system's state. A critical component of this design is the use of **Linear Matrix Inequalities (LMIs)** to ensure the observer's stability during arbitrary switching between system modes. A significant advantage of this approach is that the complex LMI calculations can be performed offline, ensuring the framework is computationally efficient enough for real-time [[Automated Monitoring]] and deployment.

The observer functions by generating residuals—mathematical discrepancies between the measured outputs and the estimated outputs. These residuals serve as the primary input for the detection phase.

## Semi-Supervised Anomaly Detection
To eliminate the need for expensive and often unavailable labeled fault datasets, the paper implements [[loft-parameter-efficient-fine-tuning-for-long-tailed-semi-supervised-learning-in|Semi-Supervised Learning]] techniques. The framework trains detection models exclusively on "normal" operational data. The study evaluates three specific algorithms:
* **One-Class SVM (OC-SVM)**
* **Support Vector Data Description (SVDD)**
* **Elliptic Envelope (EE)**

## Conclusion and Results
The experimental simulations, which include discrete, continuous, and hybrid fault scenarios, demonstrate high detection accuracy and rapid convergence. The findings suggest that **OC-SVM** and **SVDD** provide the most effective trade-off between high detection rates and the prevention of false alarms. This unified approach offers a robust solution for complex [[Fault Detection]] in modern industrial and [[Switched Systems]].