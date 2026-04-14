---
title: Faithful-First Reasoning, Planning, and Acting for Multimodal LLMs
created: 2024-05-22
source: https://arxiv.org/abs/2511.08409
tags: [ai, machine-learning, multimodal, hallucination]
---

# Faithful-First Reasoning, Planning, and Acting for Multimodal LLMs

The paper "Faithful-First Reasoning, Planning, and Acting for Multimodal LLMs" addresses a critical challenge in the evolution of [[multimodal-large-language-models-for-multi-subject-in-context-image-generation|Multimodal Large Language Models]] (MLLMs): the phenomenon of **unfaithfulness**. In many current models, the generated reasoning chains often drift away from the provided visual evidence or end in predictions that fundamentally contradict the intermediate logic presented by the model.

### The RPA Framework

To address these discrepancies, the authors introduce the **Faithful-First Reasoning, Planning, and Acting (RPA)** framework. The framework is designed to treat faithfulness as a core guiding principle during both the training and inference phases. It consists of two primary integrated components:

*   **FaithEvi**: This component acts as a supervisor, providing both step-wise