---
title: DeCo: Frequency-Decoupled Pixel Diffusion for End-to-End Image Generation
created: 2024-05-22
source: https://arxiv.org/abs/2511.19365
tags: [pixel diffusion, image generation, flow matching, computer vision, transformers]
category: ai, machine-learning, technology
author: wiki-pipeline
dc.title: "DeCo: Frequency-Decoupled Pixel Diffusion for End-to-End Image Generation"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/deco-frequency-decoupled-pixel-diffusion-for-end-to-end-image-generation.md
dc.language: en
dc.rights: CC-BY-4.0
---

# DeCo: Frequency-Decoupled Pixel Diffusion for End-to-End Image Generation

**DeCo** is a novel pixel diffusion framework designed to overcome the computational inefficiencies inherent in existing end-to-end image generation models. While [[diffusion-models|Latent Diffusion Models (LDM)]] have become the industry standard by operating in a compressed latent space, they rely on a [[variational-autoencoders|Variational Autoencoders (VAE)]] which can impose capacity limits on reconstructed details. Conversely, [[deco-frequency-decoupled-pixel-diffusion-for-end-to-end-image-generation|Pixel Diffusion]] aims to generate images directly in pixel space to preserve maximum information, but traditionally suffers from extremely slow training and inference.

### The Core Problem: Frequency Overload
In standard pixel diffusion architectures, a single [[Diffusion Transformers (DiT)]] is typically responsible for modeling both high-frequency signals (textures, sharp edges) and low-frequency semantics (shape, global structure). This dual responsibility forces the transformer to allocate excessive computational resources to fine-grained details that do not necessarily require the same level of semantic complexity as the global composition.

### The DeCo Solution: Frequency Decoupling
The DeCo framework proposes a "frequency-decoupled" approach to separate these tasks:

1.  **Semantic Focus:** The DiT is specialized to model only the low-frequency semantic components of the image. By removing the burden of high-frequency reconstruction, the DiT can focus entirely on structural accuracy.
2.  **Lightweight Detail Synthesis:** A lightweight pixel decoder is introduced to generate high-frequency details. This decoder operates conditioned on the semantic guidance provided by the DiT, ensuring that fine details are contextually appropriate.
3.  **Frequency-Aware Flow-Matching:** The researchers implemented a specialized **frequency-aware flow-matching loss**. This loss function optimizes the training process by emphasizing visually salient frequencies and suppressing insignificant high-frequency noise.

### Performance Benchmarks
Experimental evaluations on [[ImageNet]] demonstrate that DeCo significantly narrows the gap between pixel-space and latent-space diffusion methods. The model achieved state-of-the-art FID scores of 1.62 at 256x256 resolution and 2.22 at 512x512 resolution. Furthermore, in system-level comparisons using the GenEval benchmark, DeCo’s pretrained text-to-image model achieved a leading overall score of 0.86, proving its efficacy in high-fidelity, text-aligned image synthesis.