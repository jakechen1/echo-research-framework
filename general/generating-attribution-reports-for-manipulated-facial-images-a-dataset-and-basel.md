---
title: Generating Attribution Reports for Manipulated Facial Images: A Dataset and Baseline
created: 2024-05-22
source: https://arxiv.org/abs/2412.19685
tags: [ai, computer-vision, multimodal, deepfakes, forensics]
category: ai
author: wiki-pipeline
dc.title: "Generating Attribution Reports for Manipulated Facial Images: A Dataset and Baseline"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/generating-attribution-reports-for-manipulated-facial-images-a-dataset-and-basel.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Generating Attribution Reports for Manipulated Facial Images: A Dataset and Baseline

## Overview
The research paper "Generating Attribution Reports for Manipulated Facial Images: A Dataset and Baseline" introduces a significant evolution in [[Multimedia Forensics]]. Traditionally, detection methods for [[Deepfake]] content have been limited to binary classification (real vs. fake) or pixel-level localization (identifying the area of alteration). This paper addresses the "semantic gap" in forensics by proposing a task that explains the logic behind the manipulation.

## Forgery Attribution Report Generation
The authors introduce a novel multimodal task: **Forgery Attribution Report Generation**. This task requires a model to perform two simultaneous functions:
1.  **Localization ("Where"):** Identifying the specific manipulated regions within an image.
2.  **Explanation ("Why"):** Generating natural language text that describes the editing process and the nature of the manipulation.

By integrating these two components, the framework provides a much deeper level of forensic insight than traditional methods, moving toward a more human-readable form of [[explainable-ai-for-microseismic-event-detection|Explainable AI]] (XAI).

## The MMTT Dataset
To support this new task, the researchers developed the **Multi-Modal Tamper Tracing (MMTT)** dataset. This is a large-scale resource consisting of 152,217 samples. Each sample includes:
*   **Process-derived ground-truth masks** to ensure precise localization training.
*   **Human-authored textual descriptions** that offer linguistic richness and semantic depth regarding the editing steps.

This dataset is intended to drive advancements in [[improving-multimodal-learning-with-dispersive-and-anchoring-regularization|Multimodal Learning]] by providing a high-quality benchmark for both vision and language tasks.

## ForgeryTalker Framework
The paper proposes **ForgeryTalker**, a unified end-to-end architecture. The model utilizes a shared encoder—comprising an image encoder and a Q-former—paired with dual decoders dedicated to mask and text generation. This structure allows for effective cross-modal reasoning.

Experimental evaluations establish ForgeryTalker as a robust baseline, achieving a **59.3 CIDEr** score for report generation and a **73.67 IoU** for localization, setting a new standard for explainable digital forensics.