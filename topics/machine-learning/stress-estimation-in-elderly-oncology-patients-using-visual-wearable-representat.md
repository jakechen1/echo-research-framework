---
title: Stress Estimation in Elderly Oncology Patients Using Visual Wearable Representations and Multi-Instance Learning
created: 2024-05-23
source: https://arxiv.org/abs/2604.06990
tags: [machine-learning, oncology, wearables, bioinformatics, cardiology]
category: machine-learning
---

# Stress Estimation in Elderly Oncology Patients

In the field of [[Cardio-oncology]], monitoring psychological stress is vital for managing the long-term side effects of cancer treatments. Traditionally, stress is assessed using periodic [[Patient-Reported Outcome Measures (PROMS)]], which lack the continuity required for real-time clinical surveillance. This article explores a novel approach to continuous stress estimation using multimodal [[Wearable Technology]] in an elderly [[Breast Cancer]] cohort.

## Methodology

The research utilizes data from the CARDIOCARE study, integrating streams from two primary devices:
* **Smartwatches:** To capture physical activity and sleep architectures.
* **Chest-worn Sensors:** To provide continuous [[Electrocardiogram (ECG)]] data.

A significant technical challenge in this study is the weakly supervised nature of the dataset. A single [[Perceived Stress Scale (PSS)]] score is mapped to a large duration of unlabeled sensor windows. To resolve this, the researchers transformed heterogeneous sensor data into visual representations.

The computational backbone of the system is **Tiny-BioMoE**, a lightweight, pretrained [[Mixture-of-Experts]] architecture. This model embeds the visual representations into 192-dimensional vectors. These embeddings are then aggregated using [[Multi-Instance Learning (MIL)]] with an attention-based mechanism. This allows the model to identify specific high-stress patterns within the