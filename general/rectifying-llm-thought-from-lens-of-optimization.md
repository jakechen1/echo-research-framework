---
title: Rectifying LLM Thought from Lens of Optimization
created: 2024-05-24
source: https://arxiv.org/abs/2512.01925
tags: [LLM, Chain-of-Thought, Reinforcement Learning, Optimization, AI]
category: ai, machine-learning
author: wiki-pipeline
dc.title: "Rectifying LLM Thought from Lens of Optimization"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/rectifying-llm-thought-from-lens-of-optimization.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Rectifying LLM Thought from Lens of Optimization

The paper "Rectifying LLM Thought from Lens of Optimization" addresses a growing challenge in the era of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs): the inefficiency of long [[Chain-of-Thought (CoT)]] prompting. While extended reasoning chains allow models to perform complex deliberation, they are frequently prone to "overthinking"—a phenomenon where the model engages in excessively protracted and suboptimal reasoning steps that do not contribute to the final solution.

## The Optimization Framework

The researchers propose a novel theoretical framework that views the reasoning process through the lens of [[a-firefly-algorithm-for-mixed-variable-optimization-based-on-hybrid-distance-mod|Optimization]]. Instead of treating CoT as a simple sequence of text, the paper frames each individual reasoning step as an update within a [[multirate-stein-variational-gradient-descent-for-efficient-bayesian-sampling|Gradient Descent]] procedure. In this analogy, each step in the chain acts as a step toward the global minimum of a problem-solving objective, where the "loss" represents the distance from the correct answer.

## Introducing RePro

To combat the issues of overthinking and reasoning instability, the authors introduce **RePro** (Rectified Process-level Reward). RePro is designed to refine the reasoning process during the post-training phase. The core of the method lies in a surrogate objective function that evaluates the quality of the "optimization" happening during the CoT. 

RePro employs a dual scoring mechanism to assess two critical dimensions:
1. **Intensity:** Quantifies the meaningfulness of the update provided by a reasoning step.
2. **Stability:** Measures the consistency and reliability of the reasoning trajectory.

These metrics are aggregated into a composite process-level reward. This reward is then integrated into [[Reinforcement Learning with Verifiable Rewards]] (RLVR) pipelines. By using RePro, the training process penalizes steps that introduce noise or unnecessary complexity while rewarding steps that move the model closer to a verifiable solution.

## Experimental Results

The effectiveness of RePro was validated across various [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] benchmarks, specifically targeting mathematics, science, and coding. The experiments demonstrated that RePro consistently enhances reasoning performance and successfully mitigates the detrimental effects of overthinking, leading to more efficient and accurate computational thought processes.