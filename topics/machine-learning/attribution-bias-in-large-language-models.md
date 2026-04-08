---
title: Attribution Bias in Large Language Models
created: 2024-05-22
source: https://arxiv.org/abs/2604.05224
tags: [ai, machine-learning, bias, fairness, LLM]
category: ai
---

# Attribution Bias in Large Language Models

As [[Large Language Models]] (LLMs) become increasingly integrated into [[Information Retrieval]] systems and search engines, the ability to accurately attribute content to its original creator is paramount. The paper "Attribution Bias in Large Language Models" investigates the systemic failures of these models in maintaining proper authorship credits.

## AttriBench: A Balanced Benchmark

A primary contribution of this research is the introduction of **AttriBench**, the first benchmark dataset designed to be both fame- and demographically-balanced. Previous benchmarks often conflated the popularity of an author with their demographic identity, making it impossible to isolate specific biases. By explicitly balancing author fame against demographics, AttriBench allows for a controlled investigation into how [[Machine Learning]] models exhibit [[Algorithmic Bias]] based on race, gender, and intersectional identities.

## Observed Failures in LLMs

The researchers evaluated 11 widely used LLMs, including frontier models, and identified two significant areas of concern:

1.  **Accuracy Disparities:** The study found large, systematic disparities in attribution accuracy. Models perform inconsistently across different racial and gender groups, revealing deep-seated biases in how information is credited.
2.  **The Suppression Phenomenon:** The paper introduces the concept of "suppression"—a distinct failure mode where the model entirely omits attribution even when the authorship information is explicitly provided in the input. This suppression is not random; it is widespread and unevenly distributed across demographic groups, meaning standard accuracy metrics may fail to capture the true extent of the harm.

## Conclusion and Future Directions

The research positions quote attribution as a critical benchmark for evaluating [[Representational Fairness]] in artificial intelligence. To develop trustworthy [[Technology]], developers must address not only simple accuracy errors but also the complex, socio-demographic patterns of information suppression that undermine the integrity of automated knowledge retrieval.