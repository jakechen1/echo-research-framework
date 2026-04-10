---
title: "NaviSlim: Adaptive Context-Aware Navigation and Sensing via Dynamic Slimmable Networks"
created: 2024-05-22
source: https://arxiv.org/abs/2407.01563
tags: [ai, machine-learning, technology, micro-drones, edge-computing]
category: ai, technology
---

# NaviSlim

**NaviSlim** is an innovative class of neural navigation models designed specifically for small-scale [[Autonomous Vehicles]], such as [[Micro-drones]]. The primary challenge addressed by this research is the severe limitation of computing power and energy reservoirs found in miniature aerial platforms, which typically prevents the deployment of heavy, state-of-the-art [[Deep Learning]] models required for complex autonomous operations.

## Architecture and Mechanism

The core contribution of NaviSlim is a gated [[Slimmable Neural Network]] architecture. Unlike traditional [[Neural Networks]] that utilize a static architecture regardless of the environment, NaviSlim can dynamically select a "slimming factor." This allows the model to autonomously scale its computational complexity in response to the current context, including:
* Environmental difficulty
* Current flight trajectory
* Specific navigation goals

This adaptive scaling optimizes both [[Execution Time]] and energy consumption by reducing the computational load during simpler flight phases.

## Dynamic Sensor Fusion

Beyond computational optimization, NaviSlim introduces a novel approach to [[Sensor Fusion]]. While existing methods often require switching between different neural networks to handle different sensor inputs, NaviSlim can dynamically adjust the power levels of onboard sensors. This allows the system to reduce energy consumption and minimize the time spent on sensor acquisition without the overhead of model switching.

## Experimental Results

The researchers evaluated the NaviSlim models using the [[Microsoft AirSim]] robust simulation environment. The results demonstrated significant efficiency gains compared to static neural networks designed for worst-case scenarios:
* **Model Complexity:** Achieved a dynamic reduction in complexity between 57% and 92%.
* **Sensor Utilization:** Optimized sensor power usage between 61% and 80%.

By bridging the gap between complex [[Machine Learning]] requirements and the hardware constraints of [[Edge Computing]], NaviSlim provides a scalable framework for the future of autonomous aerial exploration and surveillance.