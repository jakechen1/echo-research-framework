---
title: "TinyNina: A Resource-Efficient Edge-AI Framework for Sustainable Air Quality Monitoring via Intra-Image Satellite Super-Resolution"
created: 2024-05-23
source: https://arxiv.org/abs/2604.04445
tags: [ai, machine-learning, technology, environmental-monitoring]
author: wiki-pipeline
dc.title: "TinyNina: A Resource-Efficient Edge-AI Framework for Sustainable Air Quality Monitoring via Intra-Image Satellite Super-Resolution"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/tinynina-a-resource-efficient-edge-ai-framework-for-sustainable-air-quality-moni.md
dc.language: en
dc.rights: CC-BY-4.0
---

# TinyNina: Edge-AI for Air Quality Monitoring

## Overview
**TinyNina** is a specialized [[pca-driven-adaptive-sensor-triage-for-edge-ai-inference|Edge-AI]] framework designed for high-precision monitoring of [[Nitrogen Dioxide (NO2)]] levels using [[Satellite Imagery]]. The framework addresses a significant bottleneck in [[Environmental Monitoring]]: the limited spatial resolution of standard satellite platforms, such as [[Sentinel-2]], which often lacks the granularity required for detailed urban climate assessment and respiratory health studies.

## Methodology
To overcome the dependency on expensive and often unavailable high-resolution reference datasets, TinyNina implements a novel **intra-image learning paradigm**. This approach utilizes the multi-spectral hierarchy inherent in the Sentinel-2 platform as internal training labels, effectively performing [[naima-semantics-aware-rgb-guided-depth-super-resolution|Super-Resolution]] using the image's own spectral data.

The model architecture is specifically engineered for efficiency and deployment on edge devices through two key components:
*   **Wavelength-specific attention gates**: These ensure that the model preserves critical, pollutant-sensitive spectral features during the upscaling process.
*   **Depthwise separable convolutions**: By replacing standard convolutions, the framework significantly reduces the number of parameters and computational requirements.

## Performance and Efficiency
TinyNina is optimized for **sustainability** and scalability within [[Smart City]] infrastructures. Compared to high-capacity [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] models such as EDSR and RCAN, TinyNina demonstrates:
*   **Ultra-lightweight footprint**: The model consists of only 51K parameters.
*   **Inference Speed**: A **47$\times$ increase in inference speed** compared to heavy-duty architectures.
*   **Computational Efficiency**: A **95% reduction in computational overhead**.
*   **Accuracy**: Validated against 3,276 matched satellite-ground station pairs, achieving a state-of-the-art Mean Absolute Error (MAE) of 7.4 $\mu$g/m$^3$.

## Applications
The framework provides a low-latency, scalable solution for real-time atmospheric monitoring. It is particularly suited for integration into IoT-driven [[Smart City]] networks where real-time tracking of pollutants is essential for managing urban health and climate-related challenges.