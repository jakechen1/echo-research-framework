---
title: Contrastive Decoding Mitigates Score Range Bias in LLM-as-a-Judge
created: 2024-05-22
source: https://arxiv.org/abs/2510.18196
tags: [LLM, Evaluation, Bias Mitigation, Machine Learning, NLP]
category: ai, machine-learning
---

# Contrastive Decoding Mitigates Score Range Bias in LLM-as-a-Judge

The integration of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) as autonomous evaluators—a paradigm known as **LLM-as-a-judge**—has revolutionized how we assess complex tasks like [[summarization|Summarization]]. However, the reliability of using LLMs for direct assessment (assigning scores without a reference text) is hindered by significant systemic errors.

## The Challenge of Score Range Bias

A primary obstacle identified in recent research is **score range bias**. This phenomenon occurs when the numerical outputs of an LLM judge are disproportionately influenced by the pre-defined scoring scales provided in the prompt. Instead of evaluating the intrinsic quality of the content, the model's judgment becomes highly sensitive to the boundaries of the specified range.

Crucially, the research demonstrates that this bias is not an isolated error within specific models. Instead, similar biases are frequently observed among different models within the same [[model-family|Model Family]], suggesting that the susceptibility to range-dependent scoring may be a fundamental characteristic of shared architectural or training lineages.

## Proposed Solution: Contrastive Decoding

To mitigate these inaccuracies, the study introduces the application of [[contrastive-decoding-mitigates-score-range-bias-in-llm-as-a-judge|Contrastive Decoding]] to the evaluation process. This technique aims to decouple the model's qualitative assessment from the mathematical artifacts introduced by the scoring scale.

The results of this approach are substantial. By implementing contrastive decoding, the researchers achieved up to a **11.7% relative improvement** in the [[spearman-correlation|Spearman correlation]] between LLM judgments and actual human assessments across various score ranges.

## Implications for [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]

These findings are critical for the development of trustworthy [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] pipelines. As the industry moves toward automated [[natural-language-processing|Natural Language Processing]] benchmarks, addressing score range bias is essential for ensuring that automated metrics remain a high-fidelity proxy for human intelligence. The success of [[contrastive-decoding-mitigates-score-range-bias-in-llm-as-a-judge|Contrastive Decoding]] provides a scalable pathway toward more robust and objective automated evaluation frameworks.