---
title: Self-Distilled RLVR
created: 2026-04-03
source: https://arxiv.org/abs/2604.03128
tags: [reinforcement-learning, large-language-models, self-distillation, training-stability]
category: machine-learning
---

# Self-Distilled RLVR (RLSD)

[[self-distilled-rlvr|Self-Distilled RLVR]], or **RLSD**, is an advanced training paradigm designed to optimize the reinforcement learning process for [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). The methodology addresses the fundamental tension between learning signal density and signal reliability in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] training.

## The Training Dilemma

In the pursuit of efficient LLM evolution, researchers typically navigate between two suboptimal paradigms:

*   **On-Policy Distillation (OPD) and Self-Distillation (OPSD