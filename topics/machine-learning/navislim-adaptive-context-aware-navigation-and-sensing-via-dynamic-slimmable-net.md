---
title: "NaviSlim: Adaptive Context-Aware Navigation and Sensing via Dynamic Slimmable Networks"
created: 2024-05-22
source: https://arxiv.org/abs/2407.01563
tags: [ai, machine-learning, technology, micro-drones, edge-computing]
category: ai, technology
---

# NaviSlim

**NaviSlim** is an innovative class of neural navigation models designed specifically for small-scale [[autonomous-vehicles|Autonomous Vehicles]], such as [[micro-drones|Micro-drones]]. The primary challenge addressed by this research is the severe limitation of computing power and energy reservoirs found in miniature aerial platforms, which typically prevents the deployment of heavy, state-of-the-art [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] models required for complex autonomous operations.

## Architecture and Mechanism

The core contribution of NaviSlim is a gated [[slimmable-neural-network|Slimmable Neural Network]] architecture. Unlike traditional [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]] that utilize a static architecture regardless of the environment, NaviSlim can dynamically select a "slimming factor." This allows the model to autonomously scale its computational complexity in response to the current context, including:
* Environmental difficulty
* Current flight trajectory
* Specific navigation goals

This adaptive scaling optimizes both [[execution-time|Execution Time]] and energy consumption by reducing the computational load during simpler flight phases.

## Dynamic Sensor Fusion

Beyond computational optimization, NaviSlim introduces a novel approach to [[multi-modal-sensor-fusion-using-hybrid-attention-for-autonomous-driving|Sensor Fusion]]. While existing methods often require switching between different neural networks to handle different sensor inputs, NaviSlim can dynamically adjust the power levels of onboard sensors. This allows the system to reduce energy consumption and minimize the time spent on sensor acquisition without the overhead of model switching.

## Experimental Results

The researchers evaluated the NaviSlim models using the [[microsoft-airsim|Microsoft AirSim]] robust simulation environment. The results demonstrated significant efficiency gains compared to static neural networks designed for worst-case scenarios:
* **Model Complexity:** Achieved a dynamic reduction in complexity between 57% and 92%.
* **Sensor Utilization:** Optimized sensor power usage between 61% and 80%.

By bridging the gap between complex [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] requirements and the hardware constraints of [[multi-turn-reasoning-llms-for-task-offloading-in-mobile-edge-computing|Edge Computing]], NaviSlim provides a scalable framework for the future of autonomous aerial exploration and surveillance.