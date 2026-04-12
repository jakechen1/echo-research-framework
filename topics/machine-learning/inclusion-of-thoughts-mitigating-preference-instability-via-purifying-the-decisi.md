---
title: "Inclusion-of-Thoughts: Mitigating Preference Instability via Purifying the Decision Space"
created: 2024-05-22
source: https://arxiv.org/abs/2604.04944
tags: [LLM, Reasoning, Machine Learning, NLP, Self-Filtering]
category: [ai, machine-learning]
---

# Inclusion-of-Thoughts: Mitigating Preference Instability via Purifying the Decision Space

In the evaluation of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs), [[multiple-choice-questions|Multiple-choice questions]] (MCQs) serve as a primary benchmark for measuring cognitive accuracy. However, a persistent issue in these evaluations is the presence of "plausible distractors"—incorrect options designed to mimic the correct answer. These distractors often induce "preference instability," a phenomenon where the model's internal reasoning oscillates erratically between the correct answer and incorrect, yet convincing, alternatives.

To address this, the paper introduces **Inclusion-of-Thoughts (IoT)**, a progressive self-filtering strategy. The core objective of IoT is to mitigate the cognitive load placed on the model by reducing the complexity of the decision space. Unlike standard prompting methods, IoT works to reconstruct the MCQ by systematically filtering out irrelevant or low-probability options, essentially "purifying" the decision space to focus the model's attention on the most competitive candidates.

### Key Contributions

*   **Decision Space Purification:** IoT stabilizes the model's internal preference by removing noise (distractors) that leads to reasoning instability.
*   **Enhanced Interpretability:** By explicitly documenting the filtering process, the method provides a transparent view of how the model identifies and discards certain options, improving the [[a-multi-level-causal-intervention-framework-for-mechanistic-interpretability-in-|Interpretability]] of the model's decision-making logic.
*   **Performance Gains:** Empirical evaluations across various domains—including [[arithmetic-reasoning|Arithmetic reasoning]], [[commonsense-reasoning|Commonsense reasoning]], and specialized educational benchmarks—show that IoT significantly boosts the effectiveness of [[tool-mcot-tool-augmented-multimodal-chain-of-thought-for-content-safety-moderati|Chain-of-Thought]] (CoT) prompting.
*   **Computational Efficiency:** The strategy is designed to operate with minimal computational overhead, making it an efficient addition to existing [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] inference pipelines.

By refining the focus of the model through intelligent filtration, IoT offers a robust framework for improving the reliability and stability of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] in complex, multi-option reasoning tasks.