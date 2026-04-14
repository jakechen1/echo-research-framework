---
title: Inside-Out: Measuring Generalization in Vision Transformers Through Inner Workings
created: 2024-05-24
source: https://arxiv.org/abs/2604.08192
tags: [vision-transformers, generalization, distribution-shift, circuit-discovery, machine-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Inside-Out: Measuring Generalization in Vision Transformers Through Inner Workings"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/inside-out-measuring-generalization-in-vision-transformers-through-inner-working.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Inside-Out: Measuring Generalization in Vision Transformers Through Inner Workings

## Overview
Evaluating the reliability of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models under [[learning-stable-predictors-from-weak-supervision-under-distribution-shift|Distribution Shift]] is a critical challenge, especially in high-stakes industries where labeled target data is often unavailable. The paper "Inside-Out" proposes a paradigm shift in model evaluation: moving from output-centric metrics to an analysis of the model's internal mechanisms.

## The Limitation of Traditional Metrics
Current proxy metrics, such as model confidence or accuracy-on-the-line, focus primarily on the final output of a model. These methods are often unreliable because they ignore the underlying causal processes that generate those predictions. A model may produce high-confidence outputs while its internal logic fails to adapt to new data distributions, leading to catastrophic failures in deployment.

## The "Inside-Out" Approach
The authors introduce a novel perspective by using the model's internal "**circuits**"—the causal interactions between internal representations—as a predictive metric for [[a-canonical-generalization-of-obdd|Generalization]]. By utilizing [[differentiable-logical-programming-for-quantum-circuit-discovery-and-optimizatio|Circuit Discovery]], the researchers extract the structural logic of [[inside-out-measuring-generalization-in-vision-transformers-through-inner-working|Vision Transformers]] to observe how information flows through the architecture.

The paper introduces two specific, label-free metrics designed for practical deployment scenarios:

1.  **Dependency Depth Bias**: Intended for the **pre-deployment** phase. This metric allows researchers to compare different models and select the one with the highest potential for success on unlabeled target datasets.
2.  **Circuit Shift Score**: Intended for the