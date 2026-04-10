---
title: LLM-Generated Fault Scenarios for Evaluating Perception-Driven Lane Following in Autonomous Edge Systems
created: 2024-05-22
source: https://arxiv.org/abs/2604.07362
tags: [autonomous_driving, edge_computing, fault_injection, computer_vision, generative_ai]
category: ai
---

# LLM-Generated Fault Scenarios for Evaluating Perception-Driven Lane Following in Autonomous Edge Systems

The paper addresses a critical bottleneck in the deployment of [[Autonomous Vehicles]] on [[Edge Computing]] platforms: the inability to perform comprehensive, real-time safety validation due to severe hardware resource constraints. Traditional validation methods typically rely on static datasets or manual [[Fault Injection]], which often fail to capture the unpredictable, diverse environmental hazards encountered during real-world deployment.

## The Proposed Framework

To bridge this gap, the authors introduce a **decoupled offline-online fault injection framework**. This architecture splits the computational burden into two distinct stages to ensure that high-fidelity testing does not compromise the efficiency of the target edge device.

### 1. The Offline Phase
In this phase, the heavy lifting of scenario generation is performed on powerful, non-edge hardware. The researchers employ two types of generative models:
*   [[Large Language Models]] (LLMs): Used to semantically generate structured and complex fault scenarios.
*   [[Latent Diffusion Models]] (LDMs): Used to synthesize high-fidelity sensor degradations, such as simulating fog, rain, or lens obstructions, onto clean sensor data.

### 2. The Online Phase
The complex dynamics generated offline are distilled into a pre-computed lookup table. This allows the [[Edge AI]] device to perform real-time, fault-aware inference using a lightweight method, bypassing the need to run heavy generative models locally.

## Experimental Findings

The framework was extensively validated using a [[ResNet18]] model dedicated to lane-following tasks across 460 different fault scenarios. The results highlighted a significant "robustness gap":

*   **Baseline Performance:** On clean, unobstructed data, the model achieved an $R^2$ of approximately 0.85.
*   **Degradation Under Faults:** When subjected to the LLM-generated scenarios, the Root Mean Square Error (RMSE) increased by as much as 99%.
*   **Localization Failure:** Under specific conditions like simulated fog, the accuracy of localization (within a 0.10m threshold) dropped drastically to just 31.0%.

## Conclusion

The study concludes that evaluating [[Machine Learning]] models solely on standard, clean datasets provides a false sense of security. For reliable [[Computer Vision]] in autonomous systems, validation must include the complex, synthesized environmental degradations that characterize real-world edge deployment.