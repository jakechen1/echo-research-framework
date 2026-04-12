---
title: Explainable AI for microseismic event detection
created: 2024-05-22
source: https://arxiv.org/abs/2510.17458
tags: [XAI, PhaseNet, Seismology, Deep Learning, SHAP]
category: machine-learning
---

# Explainable AI for microseismic event detection

The application of [[deep-neural-networks|Deep Neural Networks]] in [[explainable-ai-for-microseismic-event-detection|microseismic event detection]] has revolutionized [[seismology]], with models such as [[phasenet|PhaseNet]] demonstrating remarkable accuracy. However, the "black-box" nature of these models poses significant challenges for critical applications that require physical justification. This research addresses this gap by applying [[explainable-artificial-intelligence|Explainable Artificial Intelligence]] (XAI) techniques to interpret and refine seismic detection processes.

## Methodology and Interpretation

The study utilizes two primary XAI frameworks to audit the decision-making process of the [[phasenet|PhaseNet]] architecture:

*   **[[grad-cam|Grad-CAM]] (Gradient-weighted Class Activation Mapping):** This technique was employed to visualize the spatial attention of the network. The results confirmed that the model's focus aligns precisely with the arrival of [[p-waves|P-waves]] and [[s-waves|S-waves]].
*   **[[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|SHAP]] (Shapley Additive Explanations):** This method was used to quantify the contribution of specific features to the model's predictions. The [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|SHAP]] analysis revealed that vertical-component amplitudes are the primary drivers for P-phase identification, while horizontal components dominate S-phase picks. Importantly, these findings align perfectly with established [[geophysical]] principles.

## The SHAP-gated Inference Scheme

A significant contribution of this work is the introduction of a [[shap-gated-inference-scheme|SHAP-gated inference scheme]]. Rather than using XAI solely for post-hoc interpretation, the researchers integrated an explanation-based metric directly into the inference pipeline. By combining the model's standard output with a metric derived from [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|SHAP]] values, the system can filter out uncertain detections.

## Results and Impact

In a test conducted on 9,000 waveforms, the SHAP-gated model achieved an **F1-score of 0.98** (precision: 0.99, recall: 0.97), outperforming the baseline [[phasenet|PhaseNet]] F1-score of 0.97. The implementation demonstrated significantly higher robustness to [[signal-noise|signal noise]].

This research provides a scalable template for building trust in [[automated-seismic-detectors|automated seismic detectors]]. It proves that [[from-xai-to-mlops-explainable-concept-drift-detection-with-profile-drift-detecti|XAI]] can transition from a diagnostic tool to a functional component of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] architectures, directly enhancing the reliability and performance of models in high-stakes environments.

**Implementation:** The scripts and implementation used in this study are available at [GitHub/ayratabd/xAI_PhaseNet](https://github.com/ayratabd/xAI_PhaseNet).