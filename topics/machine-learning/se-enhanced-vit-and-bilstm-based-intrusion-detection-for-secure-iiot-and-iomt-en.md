---
title: SE-Enhanced ViT and BiLSTM-Based Intrusion Detection for Secure IIoT and IoMT Environments
created: 2024-05-23
source: https://arxiv.org/abs/2604.06254
tags: [Intrusion Detection, Deep Learning, IIoT, IoMT, Transformers]
category: machine-learning
---

# SE-Enhanced ViT and BiLSTM-Based Intrusion Detection for Secure IIoT and IoMT Environments

## Overview
As the scale of interconnected devices continues to expand within [[industrial-internet-of-things-iiot|Industrial Internet of Things (IIoT)]] and [[medical-internet-of-things-miot|Medical Internet of Things (MIoT)]] ecosystems, the necessity for timely and accurate [[cybersecurity|Cybersecurity]] threat detection has become a critical challenge. This article explores a novel framework designed to enhance [[intrusion-detection-systems-ids|Intrusion Detection Systems (IDS)]] through a hybrid deep learning architecture.

## Methodology
The study proposes an advanced architecture known as **SE ViT-BiLSTM**. The fundamental innovation lies in the modification of the standard [[vision-transformer-vit|Vision Transformer (ViT)]] architecture. Specifically, the researchers replaced the traditional multi-head attention mechanism with [[squeeze-and-excitation-se-attention|Squeeze-and-Excitation (SE) Attention]]. This modification aims to improve computational efficiency and feature recalibration.

To better capture the sequential and temporal dependencies inherent in network traffic patterns, the model integrates [[bidirectional-long-short-term-memory-bilstm|Bidirectional Long Short-Term Memory (BiLSTM)]] layers. Furthermore, to address the common problem of class imbalance in network datasets, the framework utilizes data-balancing techniques, including:
* [[smote|SMOTE]] (Synthetic Minority Over-sampling Technique)
* [[randomoversampler|RandomOverSampler]]

## Experimental Results
The model was evaluated using two prominent benchmark datasets: [[edgeiiot|EdgeIIoT]] and [[ciciot2024|CICIoT2024]]. The performance was measured both before and after applying data-balancing techniques to assess the impact of feature weighting and oversampling.

### Key Performance Metrics
The SE ViT-BiLSTM model demonstrated superior performance compared to existing [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] approaches:

| Dataset | Condition | Accuracy | Latency (sec/inst) |
| :--- | :--- | :--- | :--- |
| **EdgeIIoT** | Unbalanced | 99.11% | 0.00032 |
| **EdgeIIoT** | Balanced | 99.33% | 0.00035 |
| **CICIoT2024** | Unbalanced | 96.10% | 0.00053 |
| **CICIoT2024** | Balanced | 98.16% | 0.00014 |

## Conclusion
The integration of [[squeeze-and-excitation|Squeeze-and-Excitation]] attention with [[se-enhanced-vit-and-bilstm-based-intrusion-detection-for-secure-iiot-and-iomt-en|BiLSTM]] and [[inside-out-measuring-generalization-in-vision-transformers-through-inner-working|Vision Transformers]] provides a highly efficient solution for real-time threat detection. The extremely low latency observed across all tests suggests that this model is highly suitable for deployment in resource-constrained environments within [[se-enhanced-vit-and-bilstm-based-intrusion-detection-for-secure-iiot-and-iomt-en|IIoT]] and [[se-enhanced-vit-and-bilstm-based-intrusion-detection-for-secure-iiot-and-iomt-en|IoMT]] infrastructures.