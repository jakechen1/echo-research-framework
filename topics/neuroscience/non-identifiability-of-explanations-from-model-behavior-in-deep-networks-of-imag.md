---
title: Non-identifiability of Explanations from Model Behavior in Deep Networks of Image Authenticity Judgments
created: 2024-05-22
source: https://arxiv.org/abs/2604.07254
tags: [ai, interpretability, computer-vision, cognitive-science]
category: ai
---

# Non-identifiability of Explanations from Model Behavior

The study "Non-identifiability of Explanations from Model Behavior in Deep Networks of Image Authenticity Judgments" investigates the fundamental gap between a model's ability to predict human behavior and its ability to explain the underlying mechanisms of that behavior. While [[deep-neural-networks|Deep Neural Networks]] (DNNs) can achieve high accuracy in predicting human ratings of image authenticity, the research demonstrates that these models do not necessarily utilize the same features or cues as humans.

## Methodology

To evaluate the robustness of [[explainable-ai-for-microseismic-event-detection|Explainable AI]] (XAI), researchers applied lightweight regression heads to several pretrained [[line-llm-based-iterative-neuron-explanations-for-vision-models|Vision Models]], including VGG architectures, EfficientNetB3, and Barlow Twins. The team utilized various [[attribution-maps|Attribution Maps]] techniques to identify predictive features, including:

*   [[grad-cam|Grad-CAM]]
*   [[lime|LIME]]
*   Multiscale pixel masking

## Key Findings

The research uncovered significant discrepancies in how different architectures achieve predictive success:

1.  **Feature Misalignment:** Certain models, specifically VGG-based architectures, reached high predictive performance by tracking [[q-probe-scaling-image-quality-assessment-to-high-resolution-via-context-aware-ag|image quality]] rather than authenticity-specific variance. This renders their attribution maps irrelevant to the actual task of authenticity judgment.
2.  **Architecture Inconsistency:** While attribution maps remained stable within a single architecture (particularly for [[efficientnetb3|EfficientNetB3]]), there was minimal agreement in attribution across different model architectures, even when models exhibited similar predictive performance.
3.  **Ensemble Benefits:** The study found that [[ensemble-learning|Ensemble Learning]] could improve the prediction of human authenticity judgments and enable more effective image-level attribution via pixel masking.

## Conclusion and Implications

The study concludes that deep networks can successfully predict human-like behavior without producing identifiable or human-aligned explanations. These findings serve as a critical warning for [[computational-neuroscience|Computational Neuroscience]] and [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] researchers: [[post-hoc-explanations|post hoc explanations]] derived from successful behavioral models should be treated as weak evidence for identifying the true underlying [[cognitive-mechanisms|cognitive mechanisms]] of human perception.