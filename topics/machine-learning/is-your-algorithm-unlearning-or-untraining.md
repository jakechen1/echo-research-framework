---
title: Is your algorithm unlearning or untraining?
created: 2024-05-22
source: https://arxiv.org/abs/2604.07962
tags: [machine learning, machine unlearning, data privacy, algorithmic disambiguation]
category: machine-learning
---

# Is your algorithm unlearning or untraining?

The paper "Is your algorithm unlearning or untraining?" explores a fundamental ambiguity within the field of [[Machine Learning]], specifically regarding the nomenclature used to describe the removal of information from trained models. As [[Artificial Intelligence]] scales and datasets grow, the ability to "delete" specific data points or behaviors has become a central research priority, often grouped under the umbrella of [[Machine Unlearning]].

The authors argue that the literature has become "overloaded" with a single term that actually covers two fundamentally different mathematical problems. To resolve this, they propose a formal distinction between two distinct objectives:

### 1. Untraining
**Untraining** is a localized, specific operation. The primary goal is to reverse the specific influence that a given "forget set" had on the model during its initial training phase. The focus is strictly on the individual examples provided in the set, aiming to revert the model to a state as if those specific data points had never been processed.

### 2. Unlearning
**Unlearning** is a generalized, conceptual operation. In this context, the "forget set" serves merely as a proxy or a signal to remove an entire underlying [[Probability Distribution]] or concept from the model. The objective is not just to remove the specific data points, but to erase the broader behavior, pattern, or concept that those examples represent (e.g., removing a specific character's personality or toxic linguistic patterns).

### Implications for Research
The authors suggest that failing to distinguish between these two processes leads to several systemic issues in [[Algorithmic Research]]:
* **Inappropriate Metrics**: Using the same evaluation standards for both tasks can lead to highly skewed or misleading results.
* **Invalid Baselines**: Comparing an "untraining" algorithm to an "unlearning" benchmark creates a false sense of efficacy.
* **Interpretability Issues**: Without clear definitions, it becomes difficult to determine if a model