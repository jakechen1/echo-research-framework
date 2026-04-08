---
title: Brittlebench: Quantifying LLM robustness via prompt sensitivity
created: 2024-05-22
source: https://arxiv.org/abs/2603.13285
tags: [LLM, Robustness, NLP, Evaluation, Machine Learning]
category: ai, machine-learning
---

# Brittlebench: Quantifying LLM robustness via prompt sensitivity

## Overview
**Brittlebench** is a novel theoretical framework and evaluation pipeline designed to measure the sensitivity of [[Large Language Models]] (LLMs) to variations in input prompts. The research addresses a critical flaw in current [[Artificial Intelligence]] evaluation methodologies: the reliance on clean, static benchmarks that fail to account for the "noise" inherent in real-world human interactions.

## The Problem of Prompt Brittleness
Standard [[Machine Learning]] benchmarks often use perfectly formatted queries, which leads to an overestimation of a model's true capability. In real-world applications, users frequently provide inputs containing typos, grammatical errors, or alternative phrasing. This phenomenon, known as "brittleness," refers to a model's failure to maintain consistent performance when the semantic meaning remains unchanged but the surface-level text varies.

## Methodology: The Brittlebench Pipeline
The researchers developed Brittlebench to disentangle "data-induced difficulty" from "prompt-related variability." The pipeline applies **semantics-preserving perturbations** to established benchmarks. By introducing controlled changes—such as paraphrasing or adding minor errors—to existing datasets, the framework quantifies how much a model's accuracy fluctuates based solely on the phrasing of the prompt.

## Key Findings
The study reveals significant vulnerabilities in both open-weight and commercial frontier models:
* **Performance Degradation:** LLM performance can drop by as much as 12% when subjected to semantic-preserving perturbations.
* **Ranking Instability:** The relative performance ranking of different models is highly unstable; even a single perturbation alters the leaderboards in 63% of test cases.
* **Variance Contribution:** In many instances, prompt-related variability accounts for up to 50% of the total performance variance observed in a model.

## Conclusion
Brittlebench demonstrates that current [[Natural Language Processing]] (NLP) evaluation metrics are insufficient for capturing the true reliability of models. The findings highlight an urgent need for the development of more robust [[Neural Networks]] and evaluation protocols that prioritize stability against input noise.