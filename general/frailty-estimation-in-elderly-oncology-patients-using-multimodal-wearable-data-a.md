---
title: Frailty Estimation in Elderly Oncology Patients Using Multimodal Wearable Data and Multi-Instance Learning
created: 2024-05-22
source: https://arxiv.org/abs/2604.06985
tags: [wearables, oncology, machine-learning, multi-instance-learning, digital-health]
category: machine-learning
author: wiki-pipeline
dc.title: "Frailty Estimation in Elderly Oncology Patients Using Multimodal Wearable Data and Multi-Instance Learning"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/frailty-estimation-in-elderly-oncology-patients-using-multimodal-wearable-data-a.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Frailty Estimation in Elderly Oncology Patients Using Multimodal Wearable Data and Multi-Instance Learning

## Overview
Assessing [[frailty-estimation-in-elderly-oncology-patients-using-multimodal-wearable-data-a|frailty]] and functional decline in elderly [[oncology|oncology]] patients is a critical component in determining treatment tolerance and clinical outcomes. A significant challenge in geriatric oncology is that traditional assessments are typically limited to infrequent clinic visits, which cannot capture the continuous fluctuations in a patient's physiological state. This research proposes a multimodal [[wearable technology]] framework designed to estimate frailty-related functional changes between clinical follow-ups.

## Methodology
The study leverages data from the multicenter CARDIOCARE study, specifically focusing on elderly breast cancer patients. The researchers implemented an innovative attention-based [[Multiple Instance Learning]] (MIL) formulation. This approach is specifically designed to fuse irregular, multimodal wearable instances while accounting for real-world challenges such as data missingness and weak supervision.

The framework integrates two primary data streams:
* **Smartwatch Data:** Monitoring free-living physical activity and sleep features.
* **Chest Strap Data:** Extracting [[detecting-low-left-ventricular-ejection-fraction-from-ecg-using-an-interpretable|ECG]]-derived heart rate variability (HRV) features.

The data is organized into "patient-horizon bags" aligned with the 3-month (M3) and 6-month (M6) follow-up milestones. The model utilizes modality-specific multilayer perceptron (MLP) encoders to aggregate variable-length longitudinal instances. The goal is to predict discretized classes of change from baseline: worsened, stable, or improved, specifically targeting handgrip strength and FACIT-F functional scores.

## Key Findings
Using a subject-independent