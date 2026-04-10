---
title: Mitigating Distribution Sharpening in Math RLVR via Distribution-Aligned Hint Synthesis and Backward Hint Annealing
created: 2024-05-22
source: https://arxiv.org/abs/2604.07747
tags: [reinforcement-learning, llm, mathematical-reasoning, optimization]
category: ai, machine-learning
---

# Mitigating Distribution Sharpend in Math RLVR

The paper "**Mitigating Distribution Sharpening in Math RLVR via Distribution-Aligned Hint Synthesis and Backward Hint Annealing**" addresses a critical bottleneck in training [[Large Language Models (LLMs)]] for mathematical reasoning using [[Reinforcement Learning with Verifiable Rewards (RLVR)]].

## The Problem: Distribution Sharpening

While RLVR excels at improving single-attempt accuracy (pass@1) for complex math problems, it often leads to **distribution sharpening**. This phenomenon narrows the model's solution coverage, meaning that while the model becomes more "certain" about one correct path, its performance on large-$k$ sampling (pass@high-k) degrades. This occurs because the model loses the diversity of reasoning paths necessary to explore various solution trajectories.

Furthermore, while using "hints" can make difficult problems trainable, traditional hint-based approaches suffer from two major flaws:
1.  **Teacher-Student Mismatch:** The hints provided by a "teacher" model do not align with the current distribution of the "student" model.
2.  **Exposure Bias:** The model becomes overly dependent on hints, failing to perform when evaluated in a no-hint environment.

## Proposed Solutions

To resolve these issues, the researchers introduced two novel components:

### 1. Distribution-Aligned Hint Synthesis (DAHS)
[[Distribution-Aligned Hint Synthesis (DAHS)]] mitigates the distribution mismatch by constructing verified teacher hints that are specifically conditioned on the student-style responses. This ensures the guidance provided is pedagogically relevant to the model's current learning state.

### 2. Backward Hint Annealing (BHA)
[[Backward Hint Annealing (BHA)]] addresses the need for hint removal. The method anneals hint exposure across different difficulty buckets. By implementing per-question hint dropout, the framework ensures that the model continues to receive unassisted updates, preventing a permanent reliance on scaffolds and preparing the model for no-hint [[Inference]] evaluation.

## Experimental Results

The researchers evaluated the method using the [[DAPO Training Framework]] on several [[AIME Benchmarks]] (AIME24, AIME25, and AIME26). Using models such as [[Qwen3-1.7B-Base]] and [[Llama-3.2-1B-Instruct]], the study found:

*   **Qwen3-1.7B-Base:** Significant improvements were observed in both pass@1 and pass@2048 metrics.
*   **Llama-3.2-1B-Instruct:** Gains were primarily concentrated in the large-$k$ regime.

The study concludes that [[scaffolded learning]] is most effective when it provides necessary learning signals during early training stages and is systematically removed before final deployment.