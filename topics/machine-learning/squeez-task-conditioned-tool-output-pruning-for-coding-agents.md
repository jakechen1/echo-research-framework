---
title: "Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.04979"
tags: [ai, machine-learning, technology, coding-agents, token-optimization]
---

# Squeez: Task-Conditioned Tool-Output Pruning for Coding Agents

[[Coding Agents]] often struggle with efficiency when interacting with complex environments. A primary bottleneck is the redundant consumption of long tool observations; during software engineering tasks, agents frequently receive massive outputs from tools (such as compilers, file system navigators, or linters) where only a minuscule fraction of the information is relevant to the agent's next decision.

## Overview

**Squeez** is a specialized framework designed to implement **task-conditioned tool-output pruning**. The fundamental goal of Squeez is to analyze a specific task query alongside a tool output to identify and extract the smallest possible "verbatim evidence block" required for the agent to proceed. By isolating only the necessary evidence, Squeez minimizes the downstream computational burden on the [[Large Language Model]].

## Methodology

The researchers developed a new benchmark to train and evaluate this pruning capability, consisting of 11,477 examples. These examples were architected using interactions from [[SWE-bench]] and synthetic data representing multi-ecosystem tool outputs. To implement the pruning mechanism, the team utilized **LoRA** (Low-Rank Adaptation) to fine-tune a [[Qwen 3.5 2B]] model.

## Key Results

The performance of Squeez demonstrates significant advancements in [[Token Optimization]] and [[Information Retrieval]]:

*   **Efficiency:** Squeez successfully removed **92% of input tokens** while maintaining high-fidelity information.
*   **Accuracy:** The model achieved a **0.86 recall** and a **0.80 F1 score**.
*   **Model Comparison:** The fine-tuned 2B model significantly outperformed the much larger [[Qwen 3.5 35B]] in a zero-shot configuration, surpassing it by 11 recall points.
*   **Baseline Superiority:** Squeez outperformed all standard heuristic pruning baselines by a wide margin.

## Implications

By drastically reducing the amount of data processed by the [[Context Window]], Squeez offers a scalable solution for the next generation of autonomous software engineering agents. This reduction in token usage directly translates to lower latency and reduced computational costs in large-scale [[Artificial Intelligence]] deployments.