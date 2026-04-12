---
title: First-Mover Bias in Gradient Boosting Explanations: Mechanism, Detection, and Resolution
created: 2024-05-22
source: https://arxiv.org/abs/2603.22346
tags: [SHAP, Gradient Boosting, Explainable AI, Multicollinearity, Model Stability]
category: [ai, machine-learning, technology]
---

# First-MOC Bias in Gradient Boosting

**First-Mover Bias** is a mechanistic phenomenon identified in [[first-mover-bias-in-gradient-boosting-explanations-mechanism-detection-and-resol|Gradient Boosting]] where the sequential nature of residual fitting leads to a path-dependent concentration of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|SHAP]] feature importance. This bias serves as a primary contributor to [[attribution-instability|attribution instability]], particularly when models are subjected to high levels of [[multicollinearity]].

## The Mechanism of Instability
The core of the issue lies in the sequential dependency chain of the boosting process. As the model fits residuals step-by-step, the features selected in early iterations capture a disproportionate amount of importance. The research highlights a significant "scaling trap": increasing the complexity of a single model—creating a **Large Single Model (LSM