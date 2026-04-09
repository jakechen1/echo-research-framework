---
title: "TeaLeafVision: An Explainable and Robust Deep Learning Framework for Tea Leaf Disease Classification"
created: 2024-05-22
source: https://arxiv.org/abs/2604.07182
tags: [computer-vision, agriculture, deep-learning, precision-farming]
category: machine-learning
---

# TeaLeafVision

**TeaLeafVision** is an advanced [[Deep Learning]] framework engineered for the automated detection and classification of diseases in tea leaves. Given that tea is the world's second most consumed beverage, the framework addresses the critical need for precise agricultural monitoring to protect global economic stability and crop yield.

## Overview of Methodology
The research focuses on the application of [[Convolutional Neural Networks]] (CNN) to analyze the **teaLeafBD dataset**. This dataset is uniquely challenging as it includes seven distinct classes—one healthy class and six disease-specific classes—captured under diverse field conditions to mirror real-world environmental complexities.

The study evaluated several prominent architectures, identifying three high-performing models:
*   **DenseNet201**: Identified as the superior model, achieving a remarkable test accuracy of **99%**.
*   **MobileNetV2**
*   **InceptionV3**

## Explainability and Model Robustness
To overcome the "black-box" nature of traditional neural networks, TeaLeafVision integrates [[Explainable AI]] (XAI) techniques. These methods are essential for building trust in automated agricultural systems. The framework employs:

1.  **Gradient-weighted Class Activation Mapping (Grad-CAM)**: To provide visual heatmaps indicating which parts of the leaf are driving the classification decision.
2.  **Occlusion Sensitivity Analysis**: To evaluate how the removal of specific features impacts the model's predictive accuracy.
3.  **Adversarial Training**: To enhance the [[Robustness]] of the model against noise and perturbations, ensuring reliable performance in unpredictable outdoor environments.

## Practical Application
Beyond theoretical accuracy, the project emphasizes utility in [[AgTech]]. The researchers have developed a functional prototype designed to leverage these high-accuracy models for real-life tea leaf disease management. This integration of [[Computer Vision]] into agricultural workflows allows for rapid, scalable, and automated disease identification, potentially revolutionizing modern tea cultivation and crop protection strategies.