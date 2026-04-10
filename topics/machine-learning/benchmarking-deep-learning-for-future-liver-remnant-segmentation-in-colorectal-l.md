---
title: Benchmarking Deep Learning for Future Liver Remnant Segmentation in Colorectal Liver Metastasis
created: 2024-05-22
source: https://arxiv.org/abs/2604.07999
tags: [medical imaging, deep learning, surgical planning, segmentation, oncology]
category: ai, machine-learning, biology, technology
---

# Benchmarking Deep Learning for Future Liver Remnant Segmentation in CRLM

## Overview
In the clinical management of [[Colorectal Liver Metastases (CRLM)]], the accurate segmentation of the [[Future Liver Remnant (FLR)]] is a critical prerequisite for surgical planning. Precise identification of the FLR is essential to prevent post-hepatectomy liver failure, a high-risk complication following resection. 

Despite the potential for [[Deep Learning]] to automate this process, the task remains technically demanding. Automation is hindered by the complex anatomical boundaries of the liver, convoluted hepatic vasculature, and the presence of diffuse metastatic lesions. Historically, the field has been limited by a lack of high-fidelity, validated datasets for training and evaluation.

## Dataset and Methodology
This research addresses the data bottleneck by manually refining 197 volumes from the public CRLM-CT-Seg dataset. This effort establishes the first open-source, validated benchmark specifically designed for FLR segmentation tasks.

The study implemented a comparative analysis of different [[Medical Image Segmentation]] strategies, focusing on two primary architectures:
*   **Cascaded Strategies:** A sequential pipeline (Liver $\rightarrow$ CRLM $\rightarrow$ FLR).
*   **End-to-End (E2E) Strategies:** A single-pass approach.

The researchers benchmarked three state-of-the-art models: [[nnU-Net]], [[SwinUNETR]], and [[STU-Net]].

## Key Findings
The benchmarking process revealed significant differences in model performance and error handling:
*   **Optimal FLR Segmentation:** The cascaded