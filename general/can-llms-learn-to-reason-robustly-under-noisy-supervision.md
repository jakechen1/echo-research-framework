---
title: Can LLMs Learn to Reason Robustly under Noisy Supervision?
created: 2024-05-23
source: https://arxiv.org/abs/2604.03993
tags: [ai, machine-learning, reinforcement-learning, large-language-models, noisy-labels]
author: wiki-pipeline
dc.title: "Can LLMs Learn to Reason Robustly under Noisy Supervision?"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/can-llms-learn-to-reason-robustly-under-noisy-supervision.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Can LLMs Learn to Reason Robustly under Noisy Supervision?

The research paper "Can LLMs Learn to Reason Robustly under Noisy Supervision?" investigates the impact of incorrect training data on [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] trained using [[Reinforcement Learning with Verifiable Rewards]] (RLVR). While RLVR is highly effective when using perfect labels, the scarcity of human experts often results in "noisy" or incorrect labels in training datasets, creating a significant challenge for scaling [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] intelligence.

## The Mechanism of Noise in RLVR

The authors identify a unique mechanism in RLVR: the influence of a label is contingent upon whether the current model policy can generate "rollouts" (sample outputs) that match that label. This distinction leads to two specific types of noise:

*   **Inactive Noisy Labels**: These labels are rarely matched by the model's current capabilities, which primarily serves to reduce training efficiency and data utility.
*   **Active Noisy Labels**: These are more detrimental, as the model learns to reinforce the incorrect labels, effectively skewing the training distribution toward incorrect reasoning paths.

The study also uncovers the **Early Correctness Coherence** phenomenon. The researchers observed that during the early stages of training, accuracy on both clean and noisy samples increases at a similar rate, even before the model has the capability to identify the errors.

## Proposed Solution: Online Label Refinement (OLR)

To mitigate these issues, the paper proposes **Online Label Refinement (OLR)**. This technique progressively corrects potentially noisy labels by using majority-voted answers derived from model rollouts. OLR is implemented when two specific conditions are met:
1.  A positive slope in the majority answer's rollout pass rate.
2.  Stable historical consistency across training updates.

This mechanism enables a process of gradual self-correction, where the model uses its improving reasoning capabilities to "clean" its own training signal