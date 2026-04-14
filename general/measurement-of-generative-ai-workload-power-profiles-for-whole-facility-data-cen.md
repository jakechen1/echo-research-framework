---
title: "Measurement Of Generative AI Workload Power Profiles For Whole Facility Data Cen"
category: machine-learning
created: 2026-04-12
author: wiki-pipeline
dc.title: "Measurement Of Generative AI Workload Power Profiles For Whole Facility Data Cen"
dc.creator: wiki-pipeline
dc.date: 2026-04-12
dc.type: Text
dc.format: text/markdown
dc.identifier: general/measurement-of-generative-ai-workload-power-profiles-for-whole-facility-data-cen.md
dc.language: en
dc.rights: CC-BY-4.0
---

title: Measurement of Generative AI Workload Power Profiles for Whole-Facility Data Center Infrastructure Planning
created: 2023-10-27
source: https://arxiv.org/abs/2604.07345
tags: [ai, machine-learning, technology, energy-efficiency, data-centers]
category: technology

# Measurement of Generative AI Workload Power Profiles for Whole-Facility Data Center Infrastructure Planning

The rapid expansion of [[synthetic-trust-attacks-modeling-how-generative-ai-manipulates-human-decisions-i|Generative AI]] has introduced unprecedented computational demands, significantly increasing the energy footprint of modern [[concentrated-siting-of-ai-data-centers-drives-regional-power-system-stress-under|Data Centers]]. A critical barrier to sustainable expansion is the lack of accessible, high-resolution power consumption data; much of the current information remains proprietary or lacks the granularity required for effective long-term infrastructure planning.

## Methodology

This research introduces a novel methodology designed to bridge the gap between individual workload power consumption and whole-facility energy demand. Utilizing the high-performance computing (HPC) infrastructure at NLR, which is equipped with [[NVIDIA H100]] GPUs, the study captured power usage at an extremely high resolution of 0.1 seconds. The research specifically targets the various stages of the [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] lifecycle, including:

*   **Model Training**
*   **Fine-tuning**
*   **Inference**

To ensure scientific reproducibility and standardization, the study utilized industry-standard benchmarks. Specifically, **MLCommons** benchmarks were used to characterize training and fine-tuning workloads, while **vLLM** benchmarks were employed to profile inference tasks.

## Scaling and Infrastructure Impact

A major contribution of this work is the development of a bottom-up, event-driven energy model. This model allows researchers to scale high-resolution power profiles from a single workload up to the level of an entire facility. By capturing the realistic temporal fluctuations driven by AI workloads and specific user behaviors, the model provides a highly accurate representation of energy demand.

The dataset produced by this study is made publicly available to aid the broader scientific community. The implications of this research are vital for the future of [[Energy Infrastructure]] planning, particularly regarding:

1.  **Grid Connection**: Managing the stability of the electrical grid during peak AI demand.
2.  **On-site Generation**: Planning for localized renewable energy integration.
3.  **Distributed Microgrids**: Optimizing the management of autonomous, localized power networks.

This work serves as a foundational step toward building more sustainable, energy-aware computing ecosystems in the era of large-scale AI.