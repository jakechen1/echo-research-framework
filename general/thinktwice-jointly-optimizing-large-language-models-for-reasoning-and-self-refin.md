---
title: ThinkTwice: Jointly Optimizing Large Language Models for Reasoning and Self-Refinement
created: 2024-05-22
source: https://arxiv.org/abs/2604.01591
tags: [LLM, GRPO, Reinforcement Learning, Mathematical Reasoning, Self-Correction]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "ThinkTwice: Jointly Optimizing Large Language Models for Reasoning and Self-Refinement"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/thinktwice-jointly-optimizing-large-language-models-for-reasoning-and-self-refin.md
dc.language: en
dc.rights: CC-BY-4.0
---

# ThinkTwice: Jointly Optimizing Large Language Models for Reasoning and Self-Refinement

**ThinkTwice** is a novel two-phase optimization framework designed to enhance the capabilities of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) in both complex [[do-mllms-really-understand-space-a-mathematical-reasoning-evaluation|mathematical reasoning]] and autonomous [[self-refinement]]. Developed to improve the accuracy of model outputs through iterative processing, the framework is built upon the foundation of [[Group Relative Policy Optimization]] (GRPO).

### Overview
The core innovation of ThinkTwice lies in its dual-phase training approach. Unlike traditional methods that focus solely on the initial generation of an answer, ThinkTwintce jointly optimizes the model for two distinct tasks:
1. **Problem Solving**: The model is optimized to arrive at a correct solution to a reasoning problem.
2. **Self-Refinement**: The model is optimized to examine and refine its own previously generated solutions.

A significant advantage of this framework is its reliance on a [[binary correctness reward]]. This allows the model to learn from error detection without requiring expensive [[critique annotations]] or specialized correctness signals, making the training pipeline much more scalable.

### Experimental Results
The effectiveness of ThinkTwice has been demonstrated across several mathematical reasoning benchmarks using model families including [[Qwen3-4B]] and [[Olmo3-7B]]. On the [[AIME]] (American Invitational Mathematics Examination) benchmark, ThinkTwice showed substantial improvements over traditional [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL) baselines. Specifically, on the Qwen3-4B model, the framework outperformed standard GRPO by 5 percentage points in initial reasoning and by 11.5 percentage points when measured via pass@4 after a single self-refinement step.

### Training Dynamics
Analysis of the [[training dynamics]] reveals an emergent "rectify-then-fortify" curriculum. In the early stages of training, the optimization process primarily serves to **rectify** errors (correcting incorrect initial attempts). As the model matures, the process shifts toward **fortifying** the model's ability to preserve already-correct solutions, ensuring that the refinement process does not degrade existing accuracy. This research establishes a principled methodology for [[Reinforcement Learning from Verifiable Rewards]] (RLVR).