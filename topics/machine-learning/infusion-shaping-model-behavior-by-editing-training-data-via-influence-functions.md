---
title: Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions
created: 2024-05-22
source: https://arxiv.org/abs/2602.09987
tags: [influence-functions, data-poisoning, model-interpretability, machine-learning]
category: machine-learning
---

# Infusion: Shaping Model Behavior by Editing Training Data via Influence Functions

**Infusion** is a specialized framework designed to manipulate the behavior of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models by applying subtle, targeted edits to training datasets. While [[infusion-shaping-model-behavior-by-editing-training-data-via-influence-functions|Influence Functions]] are traditionally utilized to attribute a model's specific outputs back to individual training documents, the Infusion framework reverses this logic. It explores the capacity to craft specific perturbations in existing training data that induce desired changes in model behavior through strategic parameter shifts.

## Methodology

The Infusion framework utilizes scalable approximations of influence functions to compute minimal edits to training documents. Unlike standard [[data-poisoning|Data Poisoning]] techniques that rely on injecting new, explicit examples of a target behavior, Infusion modifies a tiny fraction of the existing corpus. By calculating precise perturbations, the framework can steer the model's learned parameters toward a target state using only minor adjustments to the underlying data distribution.

## Experimental Results

The researchers evaluated Infusion across both [[computer-vision|Computer Vision]] and [[natural-language-processing|Natural Language Processing]] domains, yielding several key insights:

* **Vision Efficiency:** In experiments using CIFAR-10, the researchers demonstrated that editing as little as 0.2% of the training documents (100 out of 45,000) could achieve performance competitive with baseline methods that use larger sets of explicit examples.
* **Architectural Transferability:** A significant finding is that these poisoned edits can transfer across different architectures. For example, edits designed for a [[hybrid-resnet-1d-bigru-with-multi-head-attention-for-cyberattack-detection-in-in|ResNet]] model were found to affect a [[Convolutional Neural Network