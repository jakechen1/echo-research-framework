---
title: Harnessing Hyperbolic Geometry for Harmful Prompt Detection and Sanitization
created: 2024-05-23
source: https://arxiv.org/abs/2604.06285
tags: [ai-safety, hyperbolic-geometry, vlms, anomaly-detection, security]
category: ai
---

# Harnessing Hyperbolic Geometry for Harmful Prompt Detection and Sanitization

The research paper "Harnessing Hyperbolic Geometry for Harmful Prompt Detection and Sanitization" addresses a critical security vulnerability in [[Vision-Language Models]] (VLMs): the susceptibility to malicious prompts designed to trigger unsafe or harmful content. While VLMs are foundational for tasks like image synthesis and retrieval, their ability to align textual and visual information makes them targets for [[Adversarial Attacks]] that bypass traditional safety mechanisms.

Existing defenses typically rely on blacklist filters, which are easily circumvented, or heavy classifier-based systems, which are computationally expensive and fragile against embedding-level manipulations. To resolve these issues, the authors propose a dual-component framework.

### Hyperbolic Prompt Espial (HyPE)
HyPE acts as a lightweight [[Anomaly Detection]] mechanism. Rather than relying on Euclidean space, HyPE leverages the unique properties of [[Hyperbolic Geometry]] to model the structured distribution of benign prompts. By utilizing the hierarchical nature of hyperbolic space, the system can identify harmful prompts as outliers within the embedding space with high precision and minimal computational overhead.

### Hyperbolic Prompt Sanitization (HyPS)
Building upon the detection capabilities of HyPE, HyPS provides a method for remediation. This component utilizes explainable attribution methods to pinpoint specific harmful tokens within a prompt. Once identified, HyPS selectively modifies these words to neutralize unsafe intent. A primary advantage of this approach is that it preserves the original semantics of the user's prompt, maintaining the