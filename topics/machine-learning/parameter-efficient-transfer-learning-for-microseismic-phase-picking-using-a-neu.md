---
title: Parameter-Efficient Transfer Learning for Microseismic Phase Picking Using a Neural Operator
created: 2024-05-23
source: https://arxiv.org/abs/2512.13197
tags: [seismology, neural operator, transfer learning, microseismic, deep learning, geophysics]
category: machine-learning
---

# Parameter-Efficient Transfer Learning for Microseismic Phase Picking Using a Neural Operator

## Overview
[[parameter-efficient-transfer-learning-for-microseismic-phase-picking-using-a-neu|Seismic phase picking]] is a fundamental process for [[microseismic-monitoring|microseismic monitoring]] and effective [[subsurface-imaging|subsurface imaging]]. While manual processing is unfeasible for modern, large-scale sensor arrays, [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] has provided automated alternatives. However, most existing models are optimized for high [[signal-to-noise-ratio|Signal-to-Noise Ratio]] (SNR) earthquake catalogs and often fail when applied to [[explainable-ai-for-microseismic-event-detection|microseismic]] datasets, which are typically characterized by sparse geometries and limited labeled data.

## Methodology
This research presents a method to adapt the **Phase Neural Operator (PhaseNO)**—a model designed for seismic applications—to microseismic environments using [[a-parameter-efficient-transfer-learning-approach-through-multitask-prompt-distil|Transfer Learning]] and [[loft-parameter-efficient-fine-tuning-for-long-tailed-semi-supervised-learning-in|Parameter-Efficient Fine-Tuning]] (PEFT). 

The researchers utilized a model pre-trained on a massive dataset of over 57,000 earthquake and noise records. The core innovation involves fine-tuning only a tiny fraction (**3.6%**) of the model's parameters. This adaptation was executed using a minimal calibration set consisting of only 200 labeled, noisy microseismic recordings sourced from [[hydraulic-fracturing|hydraulic fracturing]] settings. This approach allows the network to retain its fundamental spatiotemporal representations learned from large-scale earthquake data while specializing in the specific noise profiles of microseismic events.

## Performance and Results
The efficiency and accuracy of the adapted model were benchmarked against several established methods, including:
* Traditional [[stalta|STA/LTA]] (Short-Term Average/Long-Term Average) workflows.
* State-of-the-art deep learning architectures, specifically [[phasenet|PhaseNet]] and [[eqtransformer|EQTransformer]].

The results indicated that the adapted PhaseNO model significantly improved performance, achieving up to a **30% absolute improvement** in F1 scores and accuracy across three independent microseismic datasets. The model consistently outperformed both the original pre-trained PhaseNO and the existing state-of-the-art deep learning models.

## Conclusion
The proposed workflow offers a highly practical tool for the [[geophysics|Geophysics]] industry. By demonstrating that a large-scale model can be successfully deployed in data-limited environments with minimal parameter updates, this study provides a scalable solution for real-time monitoring in complex industrial applications.