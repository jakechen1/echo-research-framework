---
title: "This Treatment Works, Right? Evaluating LLM Sensitivity to Patient Question Framing in Medical QA"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.05051"
tags: [ai, machine-learning, technology, RAG, medical QA, robustness]
author: wiki-pipeline
dc.title: "This Treatment Works, Right? Evaluating LLM Sensitivity to Patient Question Framing in Medical QA"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/this-treatment-works-right-evaluating-llm-sensitivity-to-patient-question-framin.md
dc.language: en
dc.rights: CC-BY-4.0
---

# This Treatment Works, Right? Evaluating LLM Sensitivity to Patient Question Framing in Medical QA

## Overview
This research investigates the reliability of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) when used for [[Medical Question Answering]] (QA). As patients increasingly rely on [[a-mathematical-theory-of-evolution-for-self-designing-ais|AI]] to interpret complex health data, the sensitivity of these models to how a question is phrased—known as "prompt sensitivity"—presents a significant risk to clinical safety.

## Methodology
The study employed a controlled [[contradictions-in-context-challenges-for-retrieval-augmented-generation-in-healt|Retrieval-Augmented Generation]] (RAG) environment. To ensure maximum control and eliminate errors stemming from poor retrieval, the researchers used expert-selected documents derived from [[Clinical Trials]] abstracts as the ground truth.

The researchers analyzed a dataset of 6,614 query pairs, focusing on two specific dimensions of query variation:
1.  **Question Framing**: The use of positive vs. negative phrasing (e.g., "Does this treatment help?" vs. "Does this treatment fail to help?").
2.  **Language Style**: The use of technical medical terminology vs. plain, layperson language.

The study evaluated the response consistency across eight different state-of-the-art LLMs.

## Key Findings
The experimental results reveal critical vulnerabilities in model stability:

*   **Framing Sensitivity**: The most significant finding was that "framing effects" drive inconsistency. Pairs of questions with opposing frames (positive vs. negative) were significantly more likely to produce contradictory clinical conclusions than pairs using the same frame.
*   **Multi-turn Amplification**: The-inconsistency issue is exacerbated during multi-turn conversations. The study found that sustained, persuasive prompting during a dialogue increases the likelihood of the model deviating from the provided evidence.
*   **Language Style Neutrality**: Interestingly, the researchers found no significant interaction between the framing of the question and the complexity of the language style used.

## Implications for [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]
The results demonstrate that LLM responses in medical contexts can be systematically manipulated through phrasing alone, even when the underlying evidence remains constant. This lack of [[adversarial-robustness-of-deep-state-space-models-for-forecasting|Robustness]] suggests that current RAG-based systems may not be suitable for high-stakes medical applications without new evaluation criteria designed to measure "phrasal invariance." Development of more stable, evidence-grounded architectures remains a primary challenge for the field.