---
title: "OASIC: Occlusion-Agnostic and Severity-Informed Classification"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.04012"
tags: [computer-vision, occlusion, anomaly-detection, deep-learning]
category: [ai, machine-learning, technology]
---

# OASIC: Occlusion-Agnostic and Severity-Informed Classification

**OASIC** (Occlusion-Agnostic and Severity-Informed Classification) is a specialized framework designed to overcome the fundamental challenges posed by severe object occlusions in [[Computer Vision]]. In real-world environments, occlusions degrade the performance of [[Machine Learning]] models through two primary drivers: the permanent loss of visible object features and the introduction of distracting visual patterns from the occluder itself.

### Methodology

The OASIC approach implements a dual-layered strategy to mitigate these two root causes:

1.  **Distraction Removal (Test-Time Masking)**: To address the interference caused by occluders, the framework treats occluding patterns as visual anomalies. At test-time, these patterns are identified and masked out. This process is "occlusion-agnostic," meaning it does not rely on knowing the specific type of object causing the obstruction, but rather focuses on the anomaly relative to the target object.
2.  **Severity-Informed Training**: To address the loss of visual information, the model is trained using random masking at various levels of intensity. A key discovery of the research is that the "severity" of an occlusion (the degree to which information is missing) can be estimated during test-time. Furthermore, the researchers found that a model optimized for a specific degree of occlusion performs significantly better on similar levels of occlusion.

### Key Innovations and Results

Rather than relying on a single, generalized model, OASIC employs an adaptive selection strategy. It estimates the severity of the occlusion in a new image and then selects the specific model from its suite that was optimized for that exact degree of severity.

The experimental results demonstrate the robustness of this strategy. The combination of gray masking and adaptive model selection improved the $\text{AUC}_\text{occ}$ by **+18.5** compared to standard training on occluded images, and by **+23.7** compared to traditional fine-tuning on unoccluded datasets. This makes OASIC a significant advancement for [[Artificial Intelligence]] applications in unpredictable or cluttered environments.