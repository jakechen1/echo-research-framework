---
title: Self-Discovered Intention-aware Transformer for Multi-modal Vehicle Trajectory Prediction
created: 2024-05-22
source: https://arxiv.org/abs/2604.07126
tags: [transformer, autonomous-driving, trajectory-prediction, multi-modal, motion-planning]
category: machine-learning
author: wiki-pipeline
dc.title: "Self-Discovered Intention-aware Transformer for Multi-modal Vehicle Trajectory Prediction"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/self-discovered-intention-aware-transformer-for-multi-modal-vehicle-trajectory-p.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Self-Discovered Intention-aware Transformer for Multi-modal Vehicle Trajectory Prediction

## Overview
Predicting vehicle trajectories is a fundamental challenge in the development of [[dvgt-2-vision-geometry-action-model-for-autonomous-driving-at-scale|Autonomous Driving]] and [[Intelligent Transportation Systems]] (ITS). Accurate prediction is essential for safe navigation and collision avoidance in complex, dynamic environments. Traditional [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] approaches have frequently relied on specific [[openglt-a-comprehensive-benchmark-of-graph-neural-networks-for-graph-level-tasks|Graph Neural Networks]] (GNNs) or required explicit, manually labeled intention data, both of which limit the flexibility and scalability of the models in diverse traffic scenarios.

## Methodology
The paper introduces a novel, pure [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|Transformer]]-based network designed for multi-modal trajectory prediction. Unlike previous architectures that rely on fixed graph structures, this model leverages the attention mechanisms of the [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|Transformer]] to consider the interactions between a target vehicle and its neighboring vehicles.

The architecture is built upon a dual-track design:
1. **Trajectory Track**: This module focuses on the precise mathematical prediction of future vehicle paths.
2. **Intention Track**: This module focuses on calculating the likelihood of various driving intentions (e.g., turning, lane changing, or remaining in lane) by analyzing the context provided by surrounding traffic.

A key finding of this study is that separating the spatial reasoning module from the trajectory generation module significantly enhances prediction performance.

## Key Innovations
* **Decoupled Architecture**: By separating spatial feature extraction from temporal trajectory generation, the model achieves higher precision and reduces computational interference between intent recognition and path plotting.
* **Residual Offset Learning**: To handle the complexity of multi-modal futures, the model learns an ordered group of trajectories by predicting residual offsets among $K$ trajectories. This allows the network to represent multiple possible future paths efficiently without exponential increases in complexity.
* **Self-Discovered Intentions**: The model reduces the reliance on human-annotated labels by learning to infer intention likelihood directly from the environmental multi-modal context.

## Applications
This research provides a scalable framework for [[Multi-modal Learning]] in robotics and automotive engineering, specifically impacting motion planning algorithms and real-time decision-making systems in urban mobility.