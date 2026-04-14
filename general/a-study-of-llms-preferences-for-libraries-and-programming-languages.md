---
title: A Study of LLMs' Preferences for Libraries and Programming Languages
created: 2024-05-22
source: https://arxiv.org/abs/2503.17181
tags: [LLM, Code Generation, Software Engineering, Bias, Artificial Intelligence]
category: ai, technology
author: wiki-pipeline
dc.title: "A Study of LLMs' Preferences for Libraries and Programming Languages"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/a-study-of-llms-preferences-for-libraries-and-programming-languages.md
dc.language: en
dc.rights: CC-BY-4.0
---

# A Study of LLMs' Preferences for Libraries and Programming Languages

The research paper "A Study of LLMs' Preferences for Libraries and Programming Languages" presents the first empirical investigation into how [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) make critical architectural decisions during [[compiled-ai-deterministic-code-generation-for-llm-based-workflow-automation|Code Generation]]. While traditional evaluations primarily focus on [[Syntactic Validity]] or functional correctness, this study explores the "design choice" aspect—specifically, how models select specific libraries and programming languages to solve problems.

## Research Overview

The study analyzed eight diverse LLMs to identify patterns in their decision-making processes. The researchers sought to determine if models prioritize task-specific optimality or rely on the frequency of patterns found in their training data.

## Key Findings

The study revealed significant biases toward popularity and familiarity over technical suitability:

*   **Library Overuse:** There is a profound tendency for models to default to widely adopted libraries, such as [[NumPy]]. In up to 45% of evaluated cases, the use of these libraries was unnecessary and deviated significantly from the optimal ground-truth solutions.
*   **Language Dominance:** [[openclassgen-a-large-scale-corpus-of-real-world-python-classes-for-llm-research|Python]] remains the overwhelming default choice for the models studied. Even in high-performance project initialization tasks where [[openclassgen-a-large-scale-corpus-of-real-world-python-classes-for-llm-research|Python]] is not the optimal choice, it was selected in 58% of cases.
*   **Neglect of High-Performance Alternatives:** The study found a striking lack of diversity in language selection; for instance, [[synthetic-trust-attacks-modeling-how-generative-ai-manipulates-human-decisions-i|Rust]] was not utilized once in the analyzed high-performance scenarios, despite its potential advantages.

## Implications for [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]

The results highlight a critical "popularity bias" in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]. LLMs tend to prioritize the most frequent patterns seen in their training corpora rather than selecting tools based on the specific performance requirements of a task. 

To mitigate these issues, the authors argue that the field must move toward:
1. **Targeted Fine-tuning:** Developing models that understand the trade-offs between different languages.
2. **Data Diversification:** Reducing the overrepresentation of specific libraries in training sets.
3. **Advanced [[Evaluation Benchmarks]]:** Creating metrics that explicitly measure the fidelity and suitability of language and library selection.