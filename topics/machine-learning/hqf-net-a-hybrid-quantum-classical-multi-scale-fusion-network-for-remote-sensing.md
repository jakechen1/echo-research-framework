---
title: HQF-Net: A Hybrid Quantum-Classical Multi-Scale Fusion Network for Remote Sensing Image Segmentation
created: 2024-05-22
source: https://arxiv.org/abs/2604.06715
tags: [Quantum Machine Learning, Computer Vision, Remote Sensing, Hybrid Neural Networks, Deep Learning]
categories: [ai, machine-learning, technology]
---

# HQF-Net

**HQF-Net** (Hybrid Quantum-Classical Multi-Scale Fusion Network) is an advanced architectural framework designed to enhance [[Semantic Segmentation]] within the field of [[Remote Sensing]]. The primary challenge in remote sensing is the ability to capture both fine-grained spatial details and high-level semantic context within highly complex, multi-scale scenes.

## Architecture and Methodology

HQF-Net utilizes a hybrid approach that merges classical [[Deep Learning]] strengths with [[Quantum Computing]] innovations. The network architecture is built upon a frozen DINOv3 [[Vision Transformer]] (ViT-L/16) backbone, which provides robust multi-scale semantic guidance. This backbone is integrated with a customized [[U-Net]] architecture via a **Deformable Multiscale Cross-Attention Fusion (DMCAF)** module, which facilitates more effective feature interaction across scales.

To optimize feature refinement and information flow, the framework introduces two specialized quantum-inspired components:

*   **Quantum-enhanced Skip Connections (QSkip):** These connections are engineered to improve the transition of spatial information through the decoder layers.
*   **Quantum Bottleneck with Mixture-of-Experts (QMoE):** This utilizes an adaptive routing mechanism that integrates complementary local, global, and directional quantum circuits. This allows the model to dynamically weight different quantum features based on the input complexity.

## Performance Benchmarks

Experimental evaluations conducted on three major remote sensing datasets demonstrate the superiority of the HQF-Net design:

1.  **LandCover.ai:** Achieved a Mean Intersection over Union (mIoU) of 0.8568 and an overall accuracy of 96.87%.
2.  **OpenEarthMap:** Attained a 71.82% mIoU.
3.  **SeasoNet:** Reached an mIoU of 55.28% with a 99.37% overall accuracy.

## Conclusion

The success of HQF-Net suggests that structured hybrid quantum-classical processing is a highly promising direction for [[Computer Vision]] tasks. By leveraging the strengths of both paradigms, the network provides a scalable solution for complex image analysis under the constraints of near-term quantum hardware.