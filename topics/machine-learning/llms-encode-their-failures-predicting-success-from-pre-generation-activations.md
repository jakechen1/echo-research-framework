---
title: LLMS Encode Their Failures: Predicting Success from Pre-Generation Activations
created: 2024-05-22
source: https://arxiv.org/abs/2602.09924
tags: [LLM, inference-efficiency, mechanistic-interpretability, machine-learning]
category: machine-learning
---

# LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations

The research paper **"LLMs Encode Their Failures: Predicting Success from Pre-Generation Activations"** explores whether [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) possess internal signals that can predict their own performance accuracy before the text generation process begins. As the field moves toward using [[extended-reasoning|Extended Reasoning]] and increased [[inference-time-compute|Inference-time Compute]] to solve complex problems, the ability to identify which tasks actually require high-compute models is essential for [[inference-efficiency|Inference Efficiency]].

## Core Research Findings

The study investigates whether the likelihood of a model's success is recoverable from its [[internal-representations|Internal Representations]] (activations) prior to generation. Key findings include:

* **Predictive Power of Activations:** By training [[linear-probes|Linear Probes]] on pre-generation activations, the researchers were able to predict success on complex mathematics and coding tasks. These probes substantially outperformed traditional [[surface-features|Surface Features]], such as input length or TF-IDF vectors.
* **Model-Specific Difficulty:** Using the E2H-AMC dataset, the study identified a distinction between [[human-difficulty|Human Difficulty]] and a model-specific notion of difficulty. Interestingly, this gap between human intuition and model internal metrics tends to increase as models utilize more extended reasoning capabilities.
* **Model Routing:** The researchers demonstrated a practical application for these probes through [[model-routing|Model Routing]]. By using predictive signals to route queries across a pool of models, they achieved a reduction in [[inference-cost|Inference Cost]] by up to 70% on the MATH dataset, while maintaining or even exceeding the performance of the highest-performing single model.

## Implications for [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]

This research suggests that [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models contain latent information regarding their own competency. This discovery has significant implications for the development of more sustainable and cost-effective [[ai-infrastructure|AI Infrastructure]], as it provides a mechanism to bypass expensive reasoning processes for tasks that the model is already "aware" it can solve easily.

## Related Resources
* **Code Repository:** [https://github.com/KabakaWilliam/llms_know_difficulty](https://github.com/KabakaWilliam/llms_know_difficulty)
* **Topic:** [[a-multi-level-causal-intervention-framework-for-mechanistic-interpretability-in-|Mechanistic Interpretability]]
* **Topic:** [[computational-complexity|Computational Complexity]]