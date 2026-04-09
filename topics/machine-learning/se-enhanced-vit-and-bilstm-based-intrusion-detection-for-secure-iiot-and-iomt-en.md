---
title: SE-Enhanced ViT and BiLSTM-Based Intrusion Detection for Secure IIoT and IoMT Environments
created: 2024-05-23
source: https://arxiv.org/abs/2604.06254
tags: [Intrusion Detection, Deep Learning, IIoT, IoMT, Transformers]
category: machine-learning
---

# SE-Enhanced ViT and BiLSTM-Based Intrusion Detection for Secure IIoT and IoMT Environments

## Overview
As the scale of interconnected devices continues to expand within [[Industrial Internet of Things (IIoT)]] and [[Medical Internet of Things (MIoT)]] ecosystems, the necessity for timely and accurate [[Cybersecurity]] threat detection has become a critical challenge. This article explores a novel framework designed to enhance [[Intrusion Detection Systems (IDS)]] through a hybrid deep learning architecture.

## Methodology
The study proposes an advanced architecture known as **SE ViT-BiLSTM**. The fundamental innovation lies in the modification of the standard [[Vision Transformer (ViT)]] architecture. Specifically, the researchers replaced the traditional multi-head attention mechanism with [[Squeeze-and-Excitation (SE) Attention]]. This modification aims to improve computational efficiency and feature recalibration.

To better capture the sequential and temporal dependencies inherent in network traffic patterns, the model integrates [[Bidirectional Long Short-Term Memory (BiLSTM)]] layers. Furthermore, to address the common problem of class imbalance in network datasets, the framework utilizes data-balancing techniques, including:
* [[SMOTE]] (Synthetic Minority Over-sampling Technique)
* [[RandomOverSampler]]

## Experimental Results
The model was evaluated using two prominent benchmark datasets: [[EdgeIIoT]] and [[CICIoT2024]]. The performance was measured both before and after applying data-balancing techniques to assess the impact of feature weighting and oversampling.

### Key Performance Metrics
The SE ViT-BiLSTM model demonstrated superior performance compared to existing [[Machine Learning]] approaches:

| Dataset | Condition | Accuracy | Latency (sec/inst) |
| :--- | :--- | :--- | :--- |
| **EdgeIIoT** | Unbalanced | 99.11% | 0.00032 |
| **EdgeIIoT** | Balanced | 99.33% | 0.00035 |
| **CICIoT2024** | Unbalanced | 96.10% | 0.00053 |
| **CICIoT2024** | Balanced | 98.16% | 0.00014 |

## Conclusion
The integration of [[Squeeze-and-Excitation]] attention with [[BiLSTM]] and [[Vision Transformers]] provides a highly efficient solution for real-time threat detection. The extremely low latency observed across all tests suggests that this model is highly suitable for deployment in resource-constrained environments within [[IIoT]] and [[IoMT]] infrastructures.