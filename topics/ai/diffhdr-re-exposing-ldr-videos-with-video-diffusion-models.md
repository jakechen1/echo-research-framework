---
title: DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.06161
tags: [computer-vision, generative-ai, video-processing]
category: ai, technology
---

# DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models

The digital video landscape is largely dominated by 8-bit [[Low Dynamic Range (LDR)]] formats. A significant drawback of these formats is the irreversible loss of scene radiance due to quantization and highlight saturation. This loss of detail in extreme light regions prevents accurate mapping to [[High Dynamic Range (HDR)]] displays and severely restricts the ability of editors to perform meaningful re-exposure in post-production.

## Overview

**DiffHDR** is a generative framework designed to bridge the gap between LDR and HDR video. Unlike traditional dynamic range expansion techniques that often produce artifacts in overexposed or underexposed areas, DiffHDR formulates the LDR-to-HDR conversion as a **generative radiance inpainting** task. By utilizing the latent space of a pre-trained [[Video Diffusion Model]], the framework can synthesize realistic, plausible details in regions where data was previously lost.

## Technical Approach

The framework implements several advanced methodologies to ensure high-fidelity reconstruction:

*   **Log-Gamma Color Space**: To handle the vast luminance range of HDR, the model operates within the Log-Gamma color space, which facilitates better management of extreme brightness levels.
*   **Spatio-Temporal Priors**: By leveraging the learned weights of a [[Diffusion Model]], DiffHDR utilizes spatio-temporal generative priors. This ensures that the newly synthesized pixels are not only visually accurate but also temporally stable across video frames.
*   **Controllable Synthesis**: The framework allows for highly customized re-exposure through [[Text-to-Video]] guidance or the use of reference images, providing artists with granular control over the final aesthetic.

## Training Methodology

A major bottleneck in training HDR-related models is the scarcity of paired LDR-HDR video datasets. To solve this, the researchers developed a synthetic pipeline that creates high-quality training data by projecting HDRI maps onto moving geometry, simulating realistic motion and lighting changes.

## Conclusion

Extensive testing demonstrates that DiffHDR significantly outperforms current state-of-the-art approaches. The model achieves superior **radiance fidelity** and maintains much higher temporal stability, creating HDR videos that offer professional-grade latitude for color grading and re-exposure.