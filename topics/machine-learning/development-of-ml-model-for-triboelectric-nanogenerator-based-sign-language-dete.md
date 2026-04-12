---
title: Development of ML model for triboelectric nanogenerator based sign language detection system
created: 2024-05-23
source: https://arxiv.org/abs/2604.06220
tags: [machine-learning, wearable-technology, signal-processing, assistive-technology]
category: machine-learning
---

# Development of ML model for triboelectric nanogenerator based sign language detection system

## Overview
The research addresses the critical challenges in [[sign-language-recognition|Sign Language Recognition]] (SLR), focusing on bridging the communication gap between the deaf and hearing communities. While vision-based SLR is common, it often suffers from physical constraints, computational overhead, and problems with occlusion. This paper proposes a hardware-software integrated approach using a custom [[development-of-ml-model-for-triboelectric-nanogenerator-based-sign-language-dete|Triboelectric Nanogenerator]] (TENG) based sensor glove.

## Methodology
The study evaluates various [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] and [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] architectures using multivariate time-series data harvested from five integrated flex sensors. The benchmark includes:
* Traditional algorithms (e.g., [[random-forest|Random Forest]])
* Feedforward Neural Networks
* [[how-long-short-term-memory-artificial-neural-network-synthetic-data-and-fine-tun|Long Short-Term Memory]] (LSTM) temporal models
* A specialized **MFCC CNN-LSTM** architecture

The proposed architecture utilizes Mel-frequency cepstral coefficients (MFCC) to extract frequency-domain features. These features are processed through independent convolutional branches for each sensor before being fused, allowing the system to handle complex spatial-temporal patterns.

## Key Findings
The results demonstrate a significant performance leap when moving from classical algorithms to specialized deep learning architectures:
* **Accuracy:** The MFCC CNN-LSTM achieved **93.33% accuracy**, a 23-point improvement over the best-performing traditional model (Random Forest at 70.38%).
* **Precision:** The proposed model reached **95.56% precision**.
* **Temporal Optimization:** Ablation studies showed that a 50-timestep window provides the best trade-off between temporal context and training volume, outperforming 100-timestep windows (84.13% vs 58.06%).
* **Robustness:** The use of [[data-augmentation|Data Augmentation]] techniques, such as noise injection and time warping, was found to be essential for the model's ability to generalize across different users.

## Implications
By mapping temporal variations into execution-speed-invariant spectral representations, this research provides a robust framework for [[wearable-technology|Wearable Technology]]. This advancement is a significant step forward in the development of sophisticated [[assistive-technology|Assistive Technology]] for real-time gesture recognition.