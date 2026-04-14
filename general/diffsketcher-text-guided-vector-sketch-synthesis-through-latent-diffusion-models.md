---
title: "DiffSketcher: Text Guided Vector Sketch Synthesis through Latent Diffusion Models"
created: 2024-05-22
source: "https://arxiv.org/abs/2306.14685"
tags: [diffusion-models, vector-graphics, computer-vision, generative-ai]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "DiffSketcher: Text Guided Vector Sketch Synthesis through Latent Diffusion Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/diffsketcher-text-guided-vector-sketch-synthesis-through-latent-diffusion-models.md
dc.language: en
dc.rights: CC-BY-4.0
---

# DiffSketcher: Text Guided Vector Sketch Synthesis through Latent Diffusion Models

## Overview
**DiffSketcher** is a novel algorithmic framework designed to enable the generation of vectorized, free-hand sketches using natural language instructions. While most state-of-the-art [[diffsketcher-text-guided-vector-sketch-synthesis-through-latent-diffusion-models|Latent Diffusion Models]] are trained on rasterized pixel data, DiffSketcher demonstrates that these models possess an inherent capacity to guide the synthesis of parametric [[vector graphics]].

## Technical Approach
The primary innovation of DiffSketcher lies in its ability to bridge the gap between a raster-level diffusion prior and a parametric vector generator. The method focuses on the following technical implementations:

*   **Optimization via SDS Loss:** The system optimizes a collection of [[Bézier curves]] by utilizing an extended [[Score Distillation Sampling (SDS)]] loss. This allows the gradient information from the diffusion model to be applied directly to the parameters of the vector paths.
*   **Attention-Driven Initialization:** To address the high computational latency typically associated with optimizing curves from random noise, the authors introduce a stroke initialization strategy. This strategy leverages the intrinsic **attention maps** of the diffusion model to provide a structural starting point, significantly accelerating the generation process.

## Performance and Results
Experiments indicate that DiffSketcher outperforms existing methods in several key metrics:
1.  **Perceptual Quality:** The synthesized sketches maintain high-fidelity structural integrity and essential visual details.
2.  **Controllability:** The model allows for varying levels of abstraction, moving from detailed sketches to more minimalist representations based on the text prompt.
3.  **Efficiency:** The use of attention-based initialization allows for faster convergence compared to traditional optimization-based vector synthesis.

## Related Topics
*   [[synthetic-trust-attacks-modeling-how-generative-ai-manipulates-human-decisions-i|Generative AI]]
*   [[computer-vision|Computer Vision]]
*   [[Neural Rendering]]
*   [[Text-to-Image Synthesis]]