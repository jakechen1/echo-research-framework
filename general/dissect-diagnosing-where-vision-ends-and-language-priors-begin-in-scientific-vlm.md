---
title: "DISSECT: Diagnosing Where Vision Ends and Language Priors Begin in Scientific VLMs"
created: 2024-05-22
source: https://arxiv.org/abs/2604.06250
tags: [VLM, benchmark, chemistry, biology, multimodal-learning, artificial-intelligence]
categories: [ai, machine-learning, drug-discovery, biology]
author: wiki-pipeline
dc.title: "DISSECT: Diagnosing Where Vision Ends and Language Priors Begin in Scientific VLMs"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/dissect-diagnosing-where-vision-ends-and-language-priors-begin-in-scientific-vlm.md
dc.language: en
dc.rights: CC-BY-4.0
---

# DISSECT: Diagnosing Where Vision Ends and Language Priors Begin in Scientific VLMs

The paper introduces **DISSECT**, a specialized diagnostic benchmark designed to investigate the "perception-integration gap" in [[aligned-vector-quantization-for-edge-cloud-collabrative-vision-language-models|Vision-Language Models]] (VLMs). This gap refers to a specific failure mode where a model successfully extracts visual information (perception) but fails to process that information during complex reasoning tasks (integration).

### The DISSECT Benchmark
Comprising 12,000 questions, DISSECT focuses on two critical scientific domains: [[predicting-activity-cliffs-for-autonomous-medicinal-chemistry|Chemistry]] (7,000 questions) and [[neurobiology|Biology]] (5,000 questions). Unlike standard benchmarks that provide a single accuracy score, DISSECT employs five distinct input modes to decompose model performance into recognizable metrics:

*   **Vision+Text**: The standard multimodal input.
*   **Text-Only**: Measuring the model's reliance on [[dissect-diagnosing-where-vision-ends-and-language-priors-begin-in-scientific-vlm|Language Priors]].
*   **Vision-Only**: Testing raw visual extraction capabilities.
*   **Human Oracle**: Using human-provided text descriptions as ground truth.
*   **Model Oracle**: A novel protocol where the VLM first verbalizes the image content and then performs reasoning based on its own text description.

### Key Research Findings
The study evaluated 18 different VLMs, uncovering several critical insights into the current state of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]:

1.  **Domain Complexity**: [[predicting-activity-cliffs-for-autonomous-medicinal-chemistry|Chemistry]] presents a much more rigorous test of genuine visual reasoning than [[neurobiology|Biology]], as it is less susceptible to being solved via linguistic shortcuts.
2.  **The Integration Bottleneck**: Open-source models frequently exhibit the perception-integration gap. They perform significantly better when reasoning from their own verbalized descriptions (Model Oracle) than from raw images, exposing a failure to "think" about what they "see."
3.  **The Frontier of Capability**: Closed-source models have largely mitigated this gap, suggesting that bridging the transition from visual extraction to logical integration is the primary differentiator between current open-source and closed-source [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] architectures.

### Conclusion
The "Model Oracle" protocol introduced in this paper offers a model-agnostic method for researchers to diagnose exactly where a VLM’s reasoning process breaks down, making it a vital tool for the advancement of [[Scientific AI]].