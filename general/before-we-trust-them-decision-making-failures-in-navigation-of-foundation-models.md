---
title: Before We Trust Them: Decision-Making Failures in Navigation of Foundation Models
created: 2024-05-23
source: https://arxiv.org/abs/2601.05529
tags: [navigation, reliability, foundation models, spatial reasoning, safety, AI evaluation]
categories: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "Before We Trust Them: Decision-Making Failures in Navigation of Foundation Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/before-we-trust-them-decision-making-failures-in-navigation-of-foundation-models.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Before We Trust Them: Decision-Making Failures in Navigation of Foundation Models

The research paper "Before We Trust Them: Decision-Making Failures in Navigation of Foundation Models" identifies a critical discrepancy between the reported success rates of [[a-family-of-open-time-series-foundation-models-for-the-radio-access-network|Foundation Models]] and their actual reliability in [[cadence-context-adaptive-depth-estimation-for-navigation-and-computational-effic|navigation]]-related decision-making. The authors argue that high-level performance metrics often mask profound underlying vulnerabilities that could lead to catastrophic failures in real-world applications.

## Methodology
To expose these gaps, the researchers utilized six diagnostic tasks distributed across three distinct spatial reasoning settings:
1. **Reasoning under complete spatial information.**
2. **Reasoning under incomplete spatial information.**
3. **Reasoning under safety-relevant information.**

## Key Findings
The study reveals that current evaluation metrics are insufficient for capturing the "brittleness" of large-scale models. A primary concern is that a high success rate does not equate to a functional understanding of spatial structures. 

* **Lack of Spatial Understanding:** In path-planning tasks involving unknown cells, GPT-5 demonstrated a 93% success rate. However, the study found that the failure cases were not random; they exhibited a fundamental lack of the structural [[spatial reasoning]] necessary for reliable navigation.
* **Model Regression:** The research found that newer iterations of models are not inherently more reliable. Specifically, in emergency-evacuation simulations, Gemini-2.5 Flash achieved only 67% accuracy, a significant regression from Gemini-2.0 Flash, which performed at 100% under identical conditions.
* **Critical Error Modes:** Across all tested models, the researchers identified several recurring failure types, including [[hallucinated reasoning]], [[structural collapse]], [[constraint violations]], and highly [[unsafe decisions]].

## Conclusion
The authors conclude that the field must move away from aggregate success metrics and toward a [[failure-focused analysis]]. To ensure the safe deployment of [[autonomous systems]], a more granular and rigorous evaluation framework is required to address the fundamental cognitive gaps identified in current [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] architectures.