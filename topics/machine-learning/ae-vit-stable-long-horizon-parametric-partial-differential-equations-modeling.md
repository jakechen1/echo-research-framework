---
title: AE-ViT: Stable Long-Horizon Parametric Partial Differential Equations Modeling
created: 2024-05-22
source: https://arxiv.org/abs/2604.06475
tags: [deep learning, PDEs, vision transformers, reduced order models, physics-informed ML]
category: machine-learning
---

# AE-ViT: Stable Long-Horizon Parametric Partial Differential Equations Modeling

**AE-ViT** is a novel deep learning architecture designed to improve the accuracy and stability of [[Reduced Order Models]] (ROMs) when simulating parametric [[Partial Differential Equations]] (PDEs). As [[Machine Learning]] continues to integrate with [[Computational Fluid Dynamics]], the ability to create efficient surrogate models for complex physical systems becomes increasingly vital.

### The Challenge of PDE Modeling
Traditionally, researchers have utilized two primary approaches to model the evolution of PDEs:
1. **Full-field models:** These attempt to learn the entire solution field. While accurate, they are computationally expensive because they must capture long-range spatial interactions at high resolutions.
2. **Latent-space models:** These use [[Autoencoders]] to compress data into low-dimensional representations. While efficient, these latent vectors often encode purely spatial information, making it difficult for the model to evolve the state accurately over long time horizons.

Furthermore, existing models struggle with "parametric" PDEs, where the trajectory of the system depends on external parameters. Most current architectures fail to account for the differing magnitudes and sensitivities of multiple solution components within a single system.

### The AE-VIt Architecture
The AE-ViT framework proposes a joint model consisting of a convolutional encoder, a [[Transformer]] operating on latent representations, and a decoder for reconstruction. The architecture introduces two key technical innovations:

* **Multi-stage Parameter Injection:** Parameters are injected at multiple stages of the network. This improves the mathematical conditioning of the model, allowing it to better handle the sensitivities of different physical parameters.
* **Coordinate Channel Injection:** By encoding physical coordinates directly into the model, the architecture provides essential spatial context. This allows the [[Transformer]] to dynamically adapt its computations based on the specific parameters governing each unique system.

### Experimental Results
The efficacy of AE-ViT was tested against complex physical simulations, including the **Advection-Diffusion-Reaction** equation and **[[Navier-Stokes]]** flow around a cylinder wake. The results demonstrate that AE-ViT combines the computational efficiency of latent-space evolution with the high fidelity of full-field models. Notably, the model outperforms standard [[Vision Transformers]] (ViTs) and existing latent transformers, reducing the relative rollout error by approximately five times.