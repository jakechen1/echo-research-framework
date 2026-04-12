---
title: CAKE: Cloud Architecture Knowledge Evaluation of Large Language Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.05755
tags: [benchmarking, LLM, cloud-native, software-engineering]
category: ai, technology
---

# CAKE: Cloud Architecture Knowledge Evaluation of Large Language Models

The **CAKE** benchmark is a specialized evaluation framework designed to assess the proficiency of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) in the domain of [[cloud-native]] software architecture. As LLMs increasingly transition into "co-pilot" roles within [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|software engineering]], CAKE addresses the lack of standardized benchmarks capable of measuring deep, structural architectural understanding.

## Benchmark Design
CAKE comprises 188 expert-validated questions distributed across five core cloud-native topics. The benchmark utilizes a revised version of [[blooms-taxonomy|Bloom's Taxonomy]] to categorize questions into four distinct cognitive levels:
*   **Recall**: Basic retrieval of architectural concepts.
*   **Analyze**: Deconstructing complex architectural components.
*   **Design**: Synthesizing architectural solutions and patterns.
*   **Implement**: Applying architectural principles to practical, executable scenarios.

## Methodology
The researchers evaluated 22 different model configurations, ranging from 0.5B to 70B parameters, across four major [[a-mathematical-theory-of-evolution-for-self-designing-ais|AI]] model families. To ensure robust evaluation, the study employed two distinct testing formats:
1.  **Multiple-Choice Questions (MCQs)**: Evaluated using a three-run majority voting system to identify consistent pattern recognition.
2.  **Free-Response (FR)**: Scored using the [[beyond-llm-as-a-judge-deterministic-metrics-for-multilingual-generative-text-eva|LLM-as-a-judge]] methodology to assess generative depth.

## Key Findings
The study revealed several critical insights into how model scale and prompting techniques affect architectural knowledge:
*   **Accuracy Plateaus**: MCQ accuracy reaches an impressive 99.2%, but this performance tends to plateau once models exceed 3B parameters.
*   **Scaling Laws**: Unlike MCQs, free-response scores scale steadily alongside model size across all cognitive levels.
*   **Evaluation Discrepancy**: The two formats capture different dimensions of knowledge; MCQs approach a performance ceiling, whereas FR continues to effectively differentiate the capabilities of larger models.
*   **Augmentation Effects**: While [[reasoning-augmentation|reasoning augmentation]] (e.g., "+think" techniques) improves the quality of free-response answers, [[tool-augmentation|tool augmentation]] (+tool) can actually degrade performance in smaller-scale models.

These findings underscore the necessity of using diverse evaluation formats to accurately capture the nuances of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] models applied to complex [[cake-cloud-architecture-knowledge-evaluation-of-large-language-models|cloud architecture]] tasks.