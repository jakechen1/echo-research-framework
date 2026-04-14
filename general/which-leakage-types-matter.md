---
title: Which Leakage Types Matter?
created: 2024-05-22
source: https://arxiv.org/abs/2604.04199
tags: [machine-learning, data-science, model-evaluation, data-leakage]
category: machine-learning
author: wiki-pipeline
dc.title: "Which Leakage Types Matter?"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/which-leakage-types-matter.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Which Leakage Types Matter?

In the field of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]], the concept of [[data-leakage-in-automotive-perception-practitioners-insights|Data Leakage]] is often discussed as a singular error. However, recent research (arXiv:2604.04199) provides a systematic evaluation of four distinct leakage classes, revealing that the impact of these errors varies significantly depending on the specific mechanism involved.

## Study Overview
The researchers conducted twenty-eight within-subject counterfactual experiments across 2,047 [[Tabular Datasets]], supplemented by a boundary experiment on 129 temporal datasets. The study aimed to quantify the severity of four specific leakage classes by measuring changes in performance metrics, specifically AUC.

## The Four Classes of Leakage

### Class I: Estimation Leakage
This class involves improper [[Feature Scaling]], such as fitting scalers on the entire dataset rather than only the training split. The study found this type of leakage to be negligible, with all tested conditions producing a $|\Delta\text{AUC}| \leq 0.005$.

### Class II: Selection Leakage
This category involves "peeking" at test results or "seed cherry-picking" to optimize model performance. This was found to be the most substantial form of leakage, accounting for approximately 90% of the measured effect. The researchers concluded that this is primarily a result of [[Noise Exploitation]], which artificially inflates reported model scores.

### Class III: Memorization Leakage
The impact of this class is directly correlated with [[Model Capacity]]. The severity scales from $d_z = 0.37$ in simple models like [[Naive Bayes]] to $d_z = 1.11$ in more complex models like [[Decision Trees]].

### Class IV: Boundary Leakage
This type of leakage remains largely "invisible" when researchers utilize standard [[Random Cross-Validation]] (CV) techniques.

## Conclusion
The findings suggest that traditional pedagogical emphases in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] may be inverted. While textbooks often warn against normalization/estimation leakage, the study demonstrates that **Selection Leak