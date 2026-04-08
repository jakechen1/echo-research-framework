---
title: Learned Elevation Models as a Lightweight Alternative to LiDAR for Radio Environment Map Estimation
created: 2024-05-22
source: https://arxiv.org/abs/2604.05520
tags: [6G, Radio Environment Map, Deep Learning, Satellite Imagery, LiDAR, Radio Propagation]
category: machine-learning
---

# Learned Elevation Models as a Lightweight Alternative to LiDAR for Radio Environment Map Estimation

The deployment of next-generation wireless systems, particularly [[6G]], necessitates a deep understanding of signal propagation in complex environments. Because 6G operates at much higher frequency bands, signals are highly sensitive to physical obstructions such as buildings and dense vegetation. To manage this, network planners utilize [[Radio Environment Maps]] (REM) to predict coverage and optimize network topology.

### The Challenge of Traditional REM Estimation
Historically, generating accurate REMs has relied heavily on [[3D Modeling]] using [[LiDAR]]-derived point clouds. While highly accurate, these datasets present significant logistical hurdles:
* **Cost**: Acquiring LiDAR data is expensive.
* **Data Volume**: The datasets are massive, often reaching several gigabytes per km².
* **Latency**: In dynamic urban environments, LiDAR data becomes quickly outdated as new structures are built or vegetation grows.

### The Proposed Two-Stage Framework
To address these inefficiencies, this research proposes a [[Machine Learning]] framework that removes the dependency on 3D data during the inference stage. The process is divided into two distinct phases:

1.  **Elevation Map Generation**: A learned estimator processes standard [[Satellite Imagery]] (RGB) to predict topographical elevation maps. This stage effectively converts 2D imagery into a 2.5D representation of the environment.
2.  **REM Estimation**: The predicted elevation maps, combined with specific antenna parameters, are fed into a [[Convolutional Neural Network]] (CNN) architecture to produce the final radio environment estimate.

### Performance and Implications
The proposed method offers a significant advantage in scalability. By operating on the same input feature space as image-only baselines but adding the predicted elevation layer, the framework improved the Root Mean Square Error (RMSE) by up to 7.8% across various [[CNN]] architectures.

By eliminating the need for 3D data at inference time, this approach provides a practical and lightweight alternative for large-scale [[Radio Propagation]] modeling, enabling more frequent and cost-effective updates to network maps using readily available satellite data.