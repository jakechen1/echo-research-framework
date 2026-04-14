---
title: Splats under Pressure: Exploring Performance-Energy Trade-offs in Real-Time 3D Gaussian Splatting under Constrained GPU Budgets
created: 2024-05-22
source: https://arxiv.org/abs/2604.07177
tags: [3DGS, GPU, Edge Computing, Neural Rendering, Energy Efficiency]
category: technology
---

# Splats under Pressure

This research addresses the growing need for efficient [[neural-rendering|Neural Rendering]] techniques that can operate effectively outside of high-performance workstation environments. As [[generative-3d-gaussian-splatting-for-arbitrary-resolutionatmospheric-downscaling|3D Gaussian Splatting]] (3DSGS) emerges as a dominant method for photorealistic scene reconstruction, the industry faces a significant bottleneck: the high computational cost of rasterizing massive amounts of Gaussian data on resource-constrained hardware.

### Methodology: GPU Emulation
The study addresses the difficulty of testing fragmented hardware by implementing an emulation-based framework. Rather than relying on an expensive and fragmented testing process across dozens of physical mobile and embedded devices, the researchers utilize a single high-end [[GPU