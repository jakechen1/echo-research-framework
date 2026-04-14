---
title: "CAMO: A Class-Aware Minority-Optimized Ensemble for Robust Language Model Evaluation on Imbalanced Data"
created: 2024-05-22
source: https://arxiv.org/abs/2604.07583
tags: [ensemble learning, class imbalance, NLP, machine learning, LLM]
category: machine-learning
author: wiki-pipeline
dc.title: "CAMO: A Class-Aware Minority-Optimized Ensemble for Robust Language Model Evaluation on Imbalanced Data"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/camo-a-class-aware-minority-optimized-ensemble-for-robust-language-model-evaluat.md
dc.language: en
dc.rights: CC-BY-4.0
---

# CAMO: A Class-Aware Minority-Optimized Ensemble

**CAMO** (Class-Aware Minority-Optimized) is a specialized [[Ensemble Learning]] technique engineered to mitigate the detrimental effects of [[Class Imbalance]] in text categorization tasks. In traditional classification environments, ensemble methods often exhibit a bias toward majority classes, which significantly degrades the performance and [[Macro F1-score]] of underrepresented minority classes.

## Methodology

The CAMO framework utilizes a hierarchical procedure designed to protect and amplify minority class forecasts. Unlike standard voting mechanisms, CAMO incorporates three critical components to ensure robustness:
* **Vote Distributions:** Analyzing the spread of predictions across the ensemble.
* **[[fine-grained-approaches-for-confidence-calibration-of-llms-in-automated-code-rev|Confidence Calibration]]:** Adjusting model outputs to ensure predicted probabilities reflect true likelihoods.
* **Inter-model Uncertainty:** Measuring the variance in predictions between different models in the ensemble.

By dynamically boosting underrepresented classes through these mechanisms, CAMO preserves the integrity of minority class predictions while maintaining overall ensemble stability.

## Experimental Validation

The researchers evaluated CAMO against seven established ensemble algorithms using a diverse array of eight different language models, including three [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) and five [[Small Language Models]] (SLMs). The testing was conducted under both [[Zero-shot Learning]] and fine-tuned settings to ensure a comprehensive assessment.

Two highly unbalanced, domain-specific benchmarks were used for verification:
1. **DIAR-AI/Emotion dataset:** Focused on emotion recognition.
2. **Ternary BEA 2025 dataset:** A specialized linguistic benchmark.

## Results and Conclusion

The experimental results indicate that CAMO consistently achieves the highest strict macro F1-score among the compared algorithms. A key finding of the study is that the benefits of CAMO are synergistic with model adaptation, meaning the effectiveness of the ensemble choice is closely tied to the underlying properties of the participating models. Because of its ability to handle high-variance distributions, CAMO serves as a reliable, domain-neutral framework for robust categorization in imbalanced datasets.