---
title: BacPrep: Lessons from Deploying an LLM-Based Bacalaureat Assessment Platform
created: 2024-05-22
source: https://arxiv.org/abs/2506.04989
tags: [LLM, EdTech, Automated Grading, Gemini, Machine Learning]
category: [ai, technology]
author: wiki-pipeline
dc.title: "BacPrep: Lessons from Deploying an LLM-Based Bacalaureat Assessment Platform"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/bacprep-lessons-from-deploying-an-llm-based-bacalaureat-assessment-platform.md
dc.language: en
dc.rights: CC-BY-4.0
---

# BacPrep: Lessons from Deploying an LLM-Based Bacalaureat Assessment Platform

**BacPrep** is an experimental [[Educational Technology]] platform designed to bridge the gap in access to quality exam preparation for the Romanian Bacalaureat. By utilizing [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs), the platform aims to provide automated, accessible, and free feedback to students, particularly those in remote or underserved geographical areas.

## Overview
The platform serves as a testing ground for the efficacy of [[Automated Assessment]] in high-stakes educational contexts. Using official exam questions from the previous five years, BacPrep leverages the **Gemini 2.5 Flash** model to facilitate a responsive user experience during its initial data collection phase. To date, the platform has processed over 100 student submissions in subjects such as [[Computer Science]] and [[Romanian Language]].

## Key Technical Challenges
The deployment of BacPrep acted as a stress test for current [[synthetic-trust-attacks-modeling-how-generative-ai-manipulates-human-decisions-i|Generative AI]] capabilities in academic grading. The research identified several significant failure modes:

*   **Stochastic Inconsistency:** Grading results exhibited high variance across multiple model runs of the same input.
*   **Computational Errors:** The model demonstrated difficulty with arithmetic precision, specifically when aggregating fractional components of a total score.
*   **Context Degradation:** A noticeable decline in reasoning performance was observed when the model was presented with large, complex prompt contexts.
*   **Rubric Misalignment:** The LLM frequently failed to respect subject-specific weightings and complex grading rubrics.
*   **Logical Dissonance:** Instances were recorded where the qualitative feedback provided by the model directly contradicted the numerical score it assigned.

## Proposed Architecture Redesign
To address these limitations, the researchers propose a shift toward a more modular [[optimizing-llm-prompt-engineering-with-dspy-based-declarative-learning|Prompt Engineering]] strategy. The redesigned architecture focuses on:

1.  **Subject-Level Decomposition:** Breaking down complex grading tasks into smaller, specialized prompts.
2.  **Specialized Graders:** Implementing distinct, subject-specific agents to ensure better adherence to specific rubrics.
3.  **Median-Selection Strategy:** Utilizing multiple inference runs and selecting the median score to mitigate [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] variance and instability.

The next critical milestone for BacPrep involves rigorous validation against human-graded benchmarks to ensure pedagogical accuracy.