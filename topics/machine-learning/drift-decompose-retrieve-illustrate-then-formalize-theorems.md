---
title: "DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems"
created: 2024-05-23
source: "https://arxiv.org/abs/2510.10815"
tags: [autoformalization, LLM, theorem-proving, retrieval-augmented-generation, mathlib]
category: ai
---

# DRIFT: Decompose, Retrieve, Illustrate, then Formalize Theorems

The **DRIFT** framework represents a significant advancement in the field of [[autoformalization|Autoformalization]], specifically addressing the challenges faced by [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) when converting informal mathematical statements into formal, machine-verifiable code.

## The Challenge of Autoformalization

A primary obstacle in [[theorem-proving|Theorem Proving]] is the gap between natural, informal mathematical language and the rigid, primitive syntax of formal languages like [[sfbd-omni-bridge-models-for-lossy-measurement-restoration-with-limited-clean-sam|Lean]]. Traditional [[contradictions-in-context-challenges-for-retrieval-augmented-generation-in-healt|Retrieval-Augmented Generation]] (RAG) methods often attempt to query mathematical libraries using the raw informal statement. However, these methods frequently fail because informal text lacks a direct, one-to-one mapping to the specialized lemmas and theorems found in libraries such as [[mathlib|Mathlib]].

## The DRIFT Framework

To bridge this gap, DRIFT introduces a multi-stage pipeline designed to make mathematical retrieval more tractable:

1.  **Decompose**: The framework breaks down complex, informal mathematical statements into smaller, more manageable "sub-components."
2.  **Retrieve**: By using these decomposed components, the system performs a more targeted search for relevant premises within mathematical libraries, reducing noise.
3.  **Illustrate**: DRIFT retrieves "illustrative theorems" that serve as templates, helping the model understand how the retrieved premises should be applied in a formal context.
4.  **Formalize**: The final stage utilizes the decomposed structure and illustrative examples to produce the formal mathematical representation.

## Performance and Benchmarks

The effectiveness of DRIFT has been validated across several rigorous datasets, including [[proofnet|ProofNet]], [[connf|ConNF]], and [[minif2f|MiniF2F]]. Key findings include:

*   **Retrieval Accuracy**: On the ProofNet benchmark, DRIFT nearly doubled the F1 score compared to the standard [[dpr|DPR]] (Dense Passage Retrieval) baseline.
*   **Robustness**: The framework demonstrated exceptional performance on out-of-distribution data in the ConNF benchmark, showing significant improvements when using advanced models like [[gpt-4|GPT-4]] and [[deepseek-v3|DeepSeek-V3]].
*   **Model-Adaptive Insights**: The research highlights that retrieval success is heavily dependent on the specific "knowledge boundaries" of the LLM being used, suggesting that future [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] research should focus on adaptive retrieval strategies tailored to specific model capabilities.