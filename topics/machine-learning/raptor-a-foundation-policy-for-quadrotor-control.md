---
title: "RAPTOR: A Foundation Policy for Quadrotor Control"
created: 2024-05-22
source: "https://arxiv.org/abs/2509.11481"
tags: [robotics, machine-learning, control-theory, automation]
category: machine-learning
---

# RAPTOR: A Foundation Policy for Quadrotor Control

The **RAPTOR** framework introduces a novel approach to achieving high adaptability in [[Robotics]] through a foundation policy designed specifically for quadrotor control. Traditionally, control systems trained via [[Reinforcement Learning]] (RL) suffer from extreme specialization, making them highly susceptible to failure when encountering the [[Sim2Real gap]] or even minor hardware variations.

## The Challenge of Overfitting
Most modern [[Neural Network]] policies are highly optimized for specific environments. Even slight changes in mass, motor type, or propeller geometry often necessitate intensive [[System Identification]] and retraining. This lack of generalization prevents robots from operating flexibly in real-world, unstructured environments, where hardware changes are common.

## The RAPTOR Method
RAPTOR utilizes a highly efficient, end-to-end policy capable of zero-shot adaptation. The core innovation lies in its training methodology, known as [[Meta-Imitation Learning]]. The researchers trained 1,000 distinct "teacher" policies, each optimized via RL for a specific quadrotor configuration. These specialized teachers were then distilled into a single, compact "student" policy.

To enable [[In-context Learning]], the architecture incorporates recurrence within the hidden layer. This allows the policy to sense environmental changes and adapt its control logic in real-time—within milliseconds—without the need for external retraining or manual parameter updates.

## Key Performance Indicators
The efficiency and versatility of the policy are remarkable:
* **Parameter Efficiency:** The policy is a tiny, three-layer architecture containing only 2,084 parameters.
* **Hardware Diversity:** The system was tested on 10 different real-world quadrotors ranging from 32g to 2.4kg, spanning various motor types (brushed vs. brushless) and flight controllers (PX4, Betaflight, etc.).
* **Robustness:** The policy demonstrated extreme resilience under wind disturbances, physical "poking," and varying propeller types (2/3/4-blade).

By treating quadrotor control as a meta-learning problem, RAPTOR provides a significant blueprint for creating more resilient, general-purpose autonomous agents capable of navigating the complexities of the physical world.