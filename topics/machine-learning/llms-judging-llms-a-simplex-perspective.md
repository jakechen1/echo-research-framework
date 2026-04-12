---
title: LLMs Judging LLMs: A Simplex Perspective
created: 2024-05-23
source: https://arxiv.org/abs/2505.21972
tags: [LLM-as-a-judge, Bayesian-inference, uncertainty-quantification, probability-simplex]
category: machine-learning
---

# LLMs Judging LLMs: A Simplex Perspective

The practice of using [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) to evaluate the outputs of other models—often referred to as "LLM-as-a-judge"—has become a standard approach in [[beyond-behavior-why-ai-evaluation-needs-a-cognitive-revolution|AI evaluation]]. Because manual human grading is expensive and slow, researchers increasingly rely on LLMs to provide scores for free-form text. However, this paper explores the mathematical risks inherent in treating LLM judges as ground truth.

## The Uncertainty Problem

The authors identify a critical distinction between two types of error in automated evaluation:

1. [[aleatoric-uncertainty-medical-image-segmentation-estimation-via-flow-matching|Aleatoric uncertainty]]: The inherent randomness and sampling variability in the evaluation process.
2. [[epistemic-uncertainty|Epistemic uncertainty]]: The uncertainty regarding the actual quality and accuracy of the judge itself.

Current evaluation frameworks primarily account for sampling variability but often ignore the uncertainty regarding whether the judge is "correct." This oversight assumes that judges are perfectly accurate, an assumption that may fail in complex or nuanced tasks.

## The Simplex Perspective

The paper introduces a novel geometric framework to study this problem. For any $M$-level scoring system, both the LLM judges and the candidates can be represented as points on an $(M-1)$-dimensional [[probability-simplex|probability simplex]]. 

By treating ranking as a geometric problem, the researchers provide mathematical proofs for several key observations:
* **Complexity and Accuracy:** The study provides a formal basis for the "folk wisdom" that binary scoring ($M=2$) is significantly more effective and robust than multi-level scoring ($M>2$).
* **Geometric Identifiability:** Using geometric concepts, such as triangle areas within the simplex, the authors demonstrate the conditions under which rankings can be reliably identified.

## Bayesian Improvements

To address the lack of robustness in traditional methods, the authors propose a [[bayesian-inference|Bayesian inference]] approach. They design geometric priors that explicitly encode epistemic uncertainty about judge quality. 

Experimental results across various LLM benchmarks demonstrate that while LLM-based rankings are robust in many scenarios, they are not universally reliable. The authors' Bayesian method achieves substantially higher coverage rates than existing procedures, highlighting that modeling the uncertainty of the judge is essential for trustworthy [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] evaluation.