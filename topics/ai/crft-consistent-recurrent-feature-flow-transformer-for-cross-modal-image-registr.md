---
title: CRFT: Consistent-Recurrent Feature Flow Transformer for Cross-Modal Image Registration
created: 2024-05-23
source: https://arxiv.org/abs/2604.05689
tags: [computer-vision, transformers, image-registration, multimodal-learning]
---

# CRFT: Consistent-Recurrent Feature Flow Transformer

The **Consistent-Recurrent Feature Flow Transformer (CRFT)** is an advanced, unified coarse-to-fine framework designed to solve the complexities of [[cross-modal-image-registration|Cross-Modal Image Registration]]. By leveraging [[transformer-architecture|Transformer Architecture]], CRFT establishes a modality-independent feature flow representation, allowing for robust alignment between images from different sensing modalities.

### Architectural Overview

The CRFT framework operates through a hierarchical approach to ensure both global alignment and local precision:

*   **Coarse Stage**: The model identifies global spatial correspondences by utilizing multi-scale feature correlation. This stage provides the necessary foundation for initial alignment.
*   **Fine Stage**: To address localized discrepancies, the fine stage employs hierarchical feature fusion and adaptive spatial reasoning to refine the registration at a granular level.

A pivotal innovation within CRFT is the **iterative discrepancy-guided attention mechanism**. When paired with a **Spatial Geometric Transform (SGT)**, this mechanism enables recurrent refinement of the flow field. This iterative process allows the network to progressively capture subtle spatial inconsistencies and enforce strict feature-level consistency. This design is particularly effective at handling large affine and scale variations, ensuring structural coherence is maintained across disparate image types.

### Applications and Impact

The