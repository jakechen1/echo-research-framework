---
title: "Fairness Evaluation And Inference Level Mitigation In Llms"
category: machine-learning
created: 2026-04-12
---

title: Fairness Evaluation and Inference Level Mitigation in LLMs
created: 2024-05-22
source: https://arxiv.org/abs/2510.18914
tags: [LLM, fairness, neural pruning, inference-time, bias mitigation]
category: [ai, machine-learning, technology]

# Fairness Evaluation and Inference Level Mitigation in LLMs

Large [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) often exhibit undesirable behaviors embedded within their internal representations. These behaviors include [[algorithmic-bias|Algorithmic Bias]], inconsistency drift, and the amplification of harmful content. Such issues are particularly prevalent during extended conversational sequences, where unwanted patterns can propagate and intensify through multi-turn dialogues.

### Limitations of Current Approaches
Historically, efforts to mitigate these negative outputs have focused on training-time or data-centric methods. While effective in some scenarios, these approaches are heavily limited by several factors:
* **Computational Cost:** Retraining or refining datasets