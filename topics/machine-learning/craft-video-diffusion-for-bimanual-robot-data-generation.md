---
title: "CRAFT: Video Diffusion for Bimanual Robot Data Generation"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.03552"
tags: [robotics, diffusion-models, data-augmentation, sim2real, computer-vision]
category: [ai, machine-learning, technology]
---

# CRAFT: Video Diffusion for Bimanual Robot Data Generation

[[CRAFT]] (Canny-guided Robot Data Generation using Video Diffusion Transformers) is an innovative framework designed to overcome the data scarcity bottleneck in [[Bimanual Robot Learning]]. Traditionally, learning complex dual-arm manipulation policies requires extensive real-world demonstrations, which are prohibitively expensive and often lack the visual diversity necessary for robust generalization across different viewpoints, lighting, and object configurations.

### Methodology

The core innovation of CRAFT lies in its ability to transform low-fidelity, simulator-generated trajectories into high-fidelity, photorealistic manipulation videos. The framework utilizes [[Video Diffusion Transformers]] conditioned on edge-based structural cues. By applying Canny edge detection to trajectories produced in a simulator, the researchers create structural templates that guide the diffusion process. This ensures that the generated video maintains temporal coherence and remains strictly aligned with the underlying physical actions (action labels) of the simulated robot.

### Key Capabilities

CRAFT provides a unified [[Data Augmentation]] pipeline that supports several critical transformations:
* **Visual Variation:** Adjusting lighting, background textures, and camera viewpoints to increase environmental robustness.
* **Object Reconfiguration:** Altering object poses and configurations to expand the dataset's complexity.
* **Cross-Embodiment Transfer:** Enabling the synthesis of data that can be applied across different robot morphologies.
* **Multi-View Synthesis:** Generating consistent views from multiple perspectives to improve spatial awareness in [[Artificial Intelligence]] models.

### Impact on [[Sim2Real]]

By leveraging pre-trained diffusion models, CRAFT effectively bridges the [[Sim2Real]] gap. It allows researchers to start with only a few real-world demonstrations and expand them into a massive, visually diverse dataset without the need to physically replay trajectories on a real robot. Experimental results indicate that CRAFT-generated data significantly improves success rates in bimanual tasks compared to straightforward data scaling or traditional augmentation, marking a significant advancement in [[Robotics]] and [[Machine Learning]].