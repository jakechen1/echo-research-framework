---
title: "CAAP: Capture-Aware Adversarial Patch Attacks on Palmprint Recognition Models"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.06987"
tags: [adversarial_attacks, palmprint_recognition, computer_vision, security]
category: ai
author: wiki-pipeline
dc.title: "CAAP: Capture-Aware Adversarial Patch Attacks on Palmprint Recognition Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/caap-capture-aware-adversarial-patch-attacks-on-palmprint-recognition-models.md
dc.language: en
dc.rights: CC-BY-4.0
---

# CAAP: Capture-Aware Adversarial Patch Attacks on Palmprint Recognition Models

## Overview
Palmprint recognition serves as a critical component in modern [[Biometrics]], particularly within industries requiring high-security [[biometric-access-control-for-private-galleries|Access Control]] and contactless [[Payment Systems]]. The technology relies on the highly discriminative textures of skin ridges and creases. However, the deployment of [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] models in these security-critical applications introduces significant risks regarding [[explainability-guided-adversarial-attacks-on-transformer-based-malware-detectors|Adversarial Attacks]].

Recent research has identified a gap in current [[computer-vision|Computer Vision]] security: most existing studies focus on digital-domain perturbations and fail to account for the physical-world distortions—such as lighting changes and texture blurring—that occur during the actual capture of a palmprint. To bridge this gap, the **CAAP** (Capture-Aware Adversarial Patch) framework was developed.

## The CAAP Framework
CAAP is designed to create a universal, reusable adversarial patch that remains effective despite the variations introduced during physical acquisition. The framework introduces several innovative components:

*   **Cross-Shaped Patch Topology:** To effectively disrupt the long-range texture continuity of palmprints, CAAP uses a cross-shaped structure. This topology provides broader spatial coverage compared to standard patches while maintaining a low pixel budget.
*   **ASIT (Input-Conditioned Patch Rendering):** This module enables the patch to be rendered specifically in response to input characteristics.
*   **RaS (Stochastic Capture-Aware Simulation):** This module simulates the unpredictable distortions and noise encountered during real-world physical imaging.
*   **MS-DIFE (Feature-Level Identity-Disruptive Guidance):** This provides targeted guidance at the feature level to maximize the disruption of identity-linked features.

## Experimental Findings
Testing conducted on the **Tongji**, **IITD**, and **AISEC** datasets demonstrates that CAAP achieves powerful untargeted and targeted attack success rates. Notably, the attack shows high [[Cross-Model Transferability]], meaning the patch can successfully deceive different neural network architectures. 

The study also highlights that while [[nearest-neighbor-projection-removal-adversarial-training|Adversarial Training]] can provide some protection, it is insufficient to fully eliminate the threat of physically realizable attacks. These findings underscore a critical need for more robust [[security|Cybersecurity]] defenses in biometric recognition systems.

## Related Resources
*   [Official arXiv Paper](https://arxiv.org/abs/2604.06987)
*   [Implementation Code (GitHub)](https://github.com/ryliu68/CAAP)