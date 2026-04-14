---
title: Scaling Coding Agents via Atomic Skills
created: 2024-05-23
source: https://arxiv.org/abs/2604.05013
tags: [AI, Reinforcement Learning, Software Engineering, LLM]
category: ai, technology
author: wiki-pipeline
dc.title: "Scaling Coding Agents via Atomic Skills"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/scaling-coding-agents-via-atomic-skills.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Scaling Coding Agents via Atomic Skills

The research paper "Scaling Coding Agents via Atomic Skills" introduces a transformative paradigm for training [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) specialized in software engineering. Traditionally, coding agents have been trained using composite benchmarks—complex, end-to-end tasks like bug fixing. However, the authors argue that this method results in task-specific overfitting, where an agent performs well on known benchmarks but fails to generalize to novel, complex software problems.

### The Atomicity Paradigm
To resolve the limitations of task-level optimization, the authors propose a shift toward mastering "atomic skills." They formalize five fundamental, composable skills that act as the basis vectors for all complex software engineering:

1.  **Code Localization**: Pinpointing the exact location of errors or required changes.
2.  **Code Editing**: Performing precise modifications to existing source code.
3.  **Unit-Test Generation**: Creating automated tests to ensure functional correctness.
4.  **Issue Reproduction**: Successfully recreating the conditions that trigger a reported bug.
5.  **Code Review**: Analyzing code for quality, efficiency, and standards.

By treating these as individual, granular units, the model can learn a more robust foundation that is not tied to the specific context of a single large-scale task.

### Methodology and Performance
The researchers utilized joint [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL) to scale these agents. This approach allows for the simultaneous optimization of all five skills, preventing the "negative interference" or trade-offs often encountered when training on heterogeneous datasets.

The experimental results demonstrate a significant breakthrough. The proposed training paradigm improved average performance by **18.7%** across both the five atomic skills and five composite tasks. Notably, the advancements in atomic mastery transferred effectively to complex, unseen domains, including [[synthetic-sandbox-for-training-machine-learning-engineering-agents|Machine Learning Engineering]], [[Code Refactoring]], and [[security|Code Security]]. This suggests that scaling via granular, foundational capabilities is a more effective path toward creating highly capable, generalized [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]-driven software engineers.