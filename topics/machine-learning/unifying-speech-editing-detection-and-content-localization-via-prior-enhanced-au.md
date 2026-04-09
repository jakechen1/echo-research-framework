---
title: Unifying Speech Editing Detection and Content Localization via Prior-Enhanced Audio LLMs
created: 2024-05-22
source: https://arxiv.org/abs/260             
tags: [speech-editing, audio-llm, deepfake-detection, ai-security]
---

# Unifying Speech Editing Detection and Content Localization via Prior-Enhanced Audio LLMs

The research paper "Unifying Speech Editing Detection and Content Localization via Prior-Enhanced Audio LLMs" introduces a transformative approach to [[Speech Editing Detection]] (SED). Traditional SED techniques often struggle with sophisticated manipulation scenarios, particularly "deletion-type" edits where the manipulated content is entirely absent from the audio signal. Because most existing models rely heavily on frame-level supervision to identify observable acoustic anomalies, they lack the structural reasoning required to detect segments where information has been removed.

## The AiEdit Dataset

To bridge the gap between limited synthetic datasets and realistic threats, the authors introduce **AiEdit**, a large-scale, bilingual dataset comprising approximately 140 hours of audio. Unlike previous benchmarks that rely on manual splicing or limited operations, AiEdit utilizes state-of-the-art end-to-end speech editing systems to simulate realistic addition, deletion, and modification operations. This provides a much more robust and diverse foundation for training [[Machine Learning]] models against modern [[Deepfake Detection]] challenges.

## Proposed Framework

The core innovation of this work lies in reformulating SED as a structured text generation task using [[Audio Large Language Models]] (Audio LLMs). This unification allows the model to perform joint reasoning for both edit type identification and precise content localization. The architecture relies on two primary technical innovations:

*   **Prior-Enhanced Prompting Strategy:** This method enhances the grounding of generative models by injecting word-level probabilistic cues—derived from a frame-level detector—directly into the prompting process. This ensures the model's predictions are anchored in specific acoustic evidence.
*   **Acoustic Consistency-Aware Loss:** The researchers introduced a specialized loss function that explicitly enforces the separation between normal and anomalous acoustic representations within the [[Latent Space]].

## Conclusion

Experimental results demonstrate that this generative framework consistently outperforms existing methods across both detection and localization tasks. By transitioning from simple anomaly detection to a reasoning-based generative approach, the study provides a significant advancement in the field of [[Artificial Intelligence]] security and audio forensics.

**Categories:** ai, machine-learning, technology