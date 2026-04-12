---
title: Why Can't I Open My Drawer? Mitigating Object-Driven Shortcuts in Zero-Shot Compositional Action Recognition
created: 2024-05-22
source: https://arxiv.org/abs/2601.16211
tags: [ai, machine-learning, computer-vision, action-recognition]
category: ai
---

# Why Can't I Open My Drawer?

The research paper "Why Can't I Open My Drawer?" investigates a fundamental flaw in [[zero-shot-compositional-action-recognition|Zero-Shot Compositional Action Recognition]] (ZS-CAR). The core objective of ZS-CA R is to enable models to identify novel action sequences—specifically new combinations of verbs and objects—by leveraging previously observed primitives (e.g., seeing "open door" and "close drawer" to understand "open drawer").

## The Problem: Object-Driven Shortcuts

The authors identify a significant failure mode known as "object-driven shortcuts." In these scenarios, models fail to recognize the actual motion or [[quantifying-the-spatiotemporal-dynamics-of-engineered-cardiac-microbundles|temporal dynamics]] of an action. Instead, they rely on the presence of specific object classes to "guess" the verb. For instance, if a model identifies a "drawer," it may predict the verb "open" based solely on the object's identity, ignoring the actual temporal evidence of the motion.

This shortcut learning is primarily driven by:
* **Sparse Compositional Supervision**: A lack of diverse examples during training.
* **Learning Asymmetry**: The imbalance in how models learn verb-object relationships.

As a result, models overfit to training co-occurrence patterns, leading to poor [[a-canonical-generalization-of-obdd|generalization]] when encountering unseen compositions where the verb and object do not traditionally pair.

## The Proposed Solution: RCORE

To combat these shortcuts, the paper proposes **RCORE** (Robust COmpositional REpresentations). RCORE aims to decouple the object identity from the action motion through two novel components:

1.  **Co-occurrence Prior Regularization (CPR)**: This method introduces explicit supervision for unseen compositions. It treats frequent training co-occurrences as "hard negatives," regularizing the model to prevent it from over-relying on historical statistical biases.
2.  **Temporal Order Regularization for Composition (TORC)**: This component enforces [[temporal-order-sensitivity|temporal-order sensitivity]]. It compels the model to focus on the temporal grounding of verbs, ensuring that the sequence of motion is prioritized over the static objects present in the scene.

## Results

Evaluations conducted on the [[sth-com|Sth-com]] and [[ek100-com|EK100-com]] datasets demonstrate that RCORE effectively reduces the impact of object-driven shortcuts. By shifting the model's focus toward temporal evidence, the framework achieves superior performance in recognizing entirely new action-object combinations.