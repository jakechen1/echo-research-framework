---
title: "ELC: Evidential Lifelong Classifier for Uncertainty Aware Radar Pulse Classification"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.06958"
tags: [radar, uncertainty-quantification, lifelong-learning, signal-processing, deep-learning]
categories: [ai, machine-learning, technology]
---

# ELC: Evidential Lifelong Classifier

The **Evidential Lifelong Classifier (ELC)** is an advanced computational framework designed to improve the reliability of [[Radar Pulse Classification]] in the high-stakes domain of [[Electromagnetic Warfare]]. In modern electronic warfare, situational awareness depends on the ability to identify RF emitters accurately; however, standard [[Deep Neural Networks]] (DNNs) face two primary obstacles: the inability to learn new pulse types without forgetting old ones and a lack of mechanism to communicate prediction confidence.

## Methodology

The ELC architecture addresses these challenges by integrating [[Uncertainty Quantification]] with [[Lifelong Learning]]. The framework employs [[Evidence Theory]] to model [[Epistemic Uncertainty]], allowing the system to distinguish between known patterns and new, unseen signals. 

The system utilizes a specific strategy known as **Learn-Prune-Share**. This mechanism allows the model to:
* **Learn** new pulse classes incrementally.
* **Prune** redundant parameters to maintain efficiency.
* **Share** features across tasks to prevent catastrophic forgetting.

The paper compares the ELC against a [[Bayesian Lifelong Classifier (BLC)]], which relies on Shannon entropy for uncertainty estimation. While BLC provides a measure of probability, it lacks the robust "ignorance" modeling provided by the ELC’s evidential approach.

## Performance and Selective Prediction

A critical feature of the ELC is **selective prediction**. By setting uncertainty thresholds, the classifier can proactively reject predictions deemed unreliable. This is particularly vital in environments with a low [[Signal-to-Noise Ratio (SNR)]].

Experimental results on synthetic radar and [[RF Fingerprinting]] datasets demonstrate significant advantages:
* In extremely noisy conditions (down to -20 dB SNR), the ELC's selective prediction improved recall by up to **46%** compared to the BLC.
* The ELC demonstrates a stronger correlation between predicted confidence and actual correctness.

By enabling the model to "express ignorance," the ELC increases the overall trustworthiness of automated decision-support systems in dynamic electromagnetic environments.