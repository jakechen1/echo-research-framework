---
title: On the Role of Fault Localization Context for LLM-Based Program Repair
created: 2024-05-23
source: https://arxiv.org/abs/2604.05481
tags: [LLM, Software Engineering, Fault Localization, Automated Program Repair, AI]
category: ai, technology
author: wiki-pipeline
dc.title: "On the Role of Fault Localization Context for LLM-Based Program Repair"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/on-the-role-of-fault-localization-context-for-llm-based-program-repair.md
dc.language: en
dc.rights: CC-BY-4.0
---

# On the Role of Fault Localization Context for LLM-Based Program Repair

The research paper "On the Role of Fault Localization Context for LLM-Based Program Repair" investigates the critical relationship between context granularity and the effectiveness of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) in [[Automated Program Repair]] (APR). As [[on-the-role-of-fault-localization-context-for-llm-based-program-repair|Fault Localization]] (FL) serves as a foundational component of the repair pipeline, this study explores how the volume and type of surrounding code information influence repair success.

### Study Overview
The researchers conducted a large-scale empirical study utilizing 500 instances from the [[SWE-bench Verified]] benchmark. Using [[GPT-5-mini]], the team evaluated 61 different configurations, varying the scope of the provided context across three levels: file-level, element-level, and line-level.

### Key Findings
The study's results challenge the prevailing assumption that increasing the amount of surrounding context uniformly improves repair performance. Significant findings include:

* **File-Level Importance:** Determining the correct file is the most significant driver of success, yielding a 15-17x improvement over baselines that lack file-level localization.
* **The Context "Sweet Spot":** The study found that the most successful repairs occurred when the context included approximately 6 to 10 relevant files, suggesting a ceiling to the benefits of expanding file context.
* **Noise Amplification:** While element-level expansion can provide conditional gains, expanding context to the line-level frequently degrades performance. This is attributed to "noise amplification," where excessive, irrelevant code distracts the model from the actual bug.
* **Retrieval Efficiency:** [[LLM-based retrieval]] methods were found to outperform traditional structural heuristics, providing superior results while using fewer tokens and fewer files.

### Conclusion
The study concludes that the most effective [[on-the-role-of-fault-localization-context-for-llm-based-program-repair|Fault Localization]] strategy involves a hybrid approach: utilizing high-level semantic understanding to grasp broad context, paired with precise, low-level localization to pinpoint the error. These insights provide essential guidance for the development of more efficient [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] agents for autonomous [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|Software Engineering]] tasks.