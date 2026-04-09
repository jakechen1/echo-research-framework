---
title: "The Stepwise Informativeness Assumption: Why are Entropy Dynamics and Reasoning Correlated in LLMs?"
created: 2024-05-22
source: https://arxiv.org/abs/2604.06192
tags: [entropy, LLM, reasoning, machine-learning, SIA]
category: machine-learning
---

# The Stepwise Informativeness Assumption

The paper investigates a fundamental puzzle in the study of [[Large Language Models]] (LLMs): the robust correlation between internal entropy dynamics—measured within the model's predictive distribution—and external correctness relative to ground-truth answers. While it has been empirically observed that entropy-based signals can track [[reasoning]] performance, the underlying mechanism explaining *why* these internal signals align with truth has remained largely uncharacterized.

### The Stepwise Informativeness Assumption (SIA)

To address this, the authors propose the **Stepwise Informativeness Assumption (SIA)**. This formal framework suggests that the correlation arises because [[autoregressive]] models achieve correct reasoning by accumulating information about the true answer through answer-informative prefixes. Specifically, the SIA states that as the generation process progresses, the reasoning prefixes are expected to accumulate information that is increasingly relevant to the final answer.

The authors provide a theoretical foundation for this assumption, demonstrating that SIA emerges naturally from [[maximum-likelihood estimation]] (MLE) when models are trained on human reasoning traces. Furthermore, the paper highlights that standard [[fine-tuning]] and [[reinforcement learning]] pipelines act to reinforce these informative dynamics, strengthening the link between token generation and information gain.

### Empirical Evidence and Signatures

The research derives observable "signatures" of SIA, which link conditional answer entropy dynamics directly to the correctness of the output. To validate these signatures, the study was performed across several rigorous reasoning benchmarks, including:

*   **GSM8K** (Mathematical reasoning)
*   **ARC** (Science questions)
*   **SVAMP** (Algebraic word problems)

The findings were consistent across a wide variety of modern, open-weight [[Large Language Models]], including **Gemma-2**, **LLaMA-3.2**, **Qwen-2.5**, **DeepSeek**, and **Olmo** variants. The results confirm that correct reasoning traces exhibit distinct, characteristic patterns in conditional answer entropy, proving that the training process inherently optimizes for the accumulation of answer-relevant information.