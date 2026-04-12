---
title: "CRAFT: Video Diffusion for Bimanual Robot Data Generation"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.03552"
tags: [robotics, diffusion-models, data-augmentation, sim2real, computer-vision]
category: [ai, machine-learning, technology]
---

# CRAFT: Video Diffusion for Bimanual Robot Data Generation

[[unfolder-for-mac-–-a-3d-model-unfolding-tool-for-creating-papercraft|CRAFT]] (Canny-guided Robot Data Generation using Video Diffusion Transformers) is an innovative framework designed to overcome the data scarcity bottleneck in [[bimanual-robot-learning|Bimanual Robot Learning]]. Traditionally, learning complex dual-arm manipulation policies requires extensive real-world demonstrations, which are prohibitively expensive and often lack the visual diversity necessary for robust generalization across different viewpoints, lighting, and object configurations.

### Methodology

The core innovation of CRAFT lies in its ability to transform low-fidelity, simulator-generated trajectories into high-fidelity, photorealistic manipulation videos. The framework utilizes [[video-diffusion-transformers|Video Diffusion Transformers]] conditioned on edge-based structural cues. By applying Canny edge detection to trajectories produced in a simulator, the researchers create structural templates that guide the diffusion process. This ensures that the generated video maintains temporal coherence and remains strictly aligned with the underlying physical actions (action labels) of the simulated robot.

### Key Capabilities

CRAFT provides a unified [[data-augmentation|Data Augmentation]] pipeline that supports several critical transformations:
* **Visual Variation:** Adjusting lighting, background textures, and camera viewpoints to increase environmental robustness.
* **Object Reconfiguration:** Altering object poses and configurations to expand the dataset's complexity.
* **Cross-Embodiment Transfer:** Enabling the synthesis of data that can be applied across different robot morphologies.
* **Multi-View Synthesis:** Generating consistent views from multiple perspectives to improve spatial awareness in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] models.

### Impact on [[sim2real|Sim2Real]]

By leveraging pre-trained diffusion models, CRAFT effectively bridges the [[sim2real|Sim2Real]] gap. It allows researchers to start with only a few real-world demonstrations and expand them into a massive, visually diverse dataset without the need to physically replay trajectories on a real robot. Experimental results indicate that CRAFT-generated data significantly improves success rates in bimanual tasks compared to straightforward data scaling or traditional augmentation, marking a significant advancement in [[ai-driven-marine-robotics-emerging-trends-in-underwater-perception-and-ecosystem|Robotics]] and [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]].