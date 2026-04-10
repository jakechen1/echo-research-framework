---
title: Parameter-Efficient Transfer Learning for Microseismic Phase Picking Using a Neural Operator
created: 2024-05-23
source: https://arxiv.org/abs/2512.13197
tags: [seismology, neural operator, transfer learning, microseismic, deep learning, geophysics]
category: machine-learning
---

# Parameter-Efficient Transfer Learning for Microseismic Phase Picking Using a Neural Operator

## Overview
[[Seismic phase picking]] is a fundamental process for [[microseismic monitoring]] and effective [[subsurface imaging]]. While manual processing is unfeasible for modern, large-scale sensor arrays, [[Deep Learning]] has provided automated alternatives. However, most existing models are optimized for high [[Signal-to-Noise Ratio]] (SNR) earthquake catalogs and often fail when applied to [[microseismic]] datasets, which are typically characterized by sparse geometries and limited labeled data.

## Methodology
This research presents a method to adapt the **Phase Neural Operator (PhaseNO)**—a model designed for seismic applications—to microseismic environments using [[Transfer Learning]] and [[Parameter-Efficient Fine-Tuning]] (PEFT). 

The researchers utilized a model pre-trained on a massive dataset of over 57,000 earthquake and noise records. The core innovation involves fine-tuning only a tiny fraction (**3.6%**) of the model's parameters. This adaptation was executed using a minimal calibration set consisting of only 200 labeled, noisy microseismic recordings sourced from [[hydraulic fracturing]] settings. This approach allows the network to retain its fundamental spatiotemporal representations learned from large-scale earthquake data while specializing in the specific noise profiles of microseismic events.

## Performance and Results
The efficiency and accuracy of the adapted model were benchmarked against several established methods, including:
* Traditional [[STA/LTA]] (Short-Term Average/Long-Term Average) workflows.
* State-of-the-art deep learning architectures, specifically [[PhaseNet]] and [[EQTransformer]].

The results indicated that the adapted PhaseNO model significantly improved performance, achieving up to a **30% absolute improvement** in F1 scores and accuracy across three independent microseismic datasets. The model consistently outperformed both the original pre-trained PhaseNO and the existing state-of-the-art deep learning models.

## Conclusion
The proposed workflow offers a highly practical tool for the [[Geophysics]] industry. By demonstrating that a large-scale model can be successfully deployed in data-limited environments with minimal parameter updates, this study provides a scalable solution for real-time monitoring in complex industrial applications.