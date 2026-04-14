---
title: "ADOPT: Adaptive Dependency-Guided Joint Prompt Optimization for Multi-Step LLM Pipelines"
created: 2024-05-23
source: "https://arxiv.org/abs/2510.24933"
tags: [prompt-optimization, LLM, machine-learning, automation]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "ADOPT: Adaptive Dependency-Guided Joint Prompt Optimization for Multi-Step LLM Pipelines"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/adopt-adaptive-dependency-guided-joint-prompt-optimization-for-multi-step-llm-pi.md
dc.language: en
dc.rights: CC-BY-4.0
---

# ADOPT

**ADOPT** (Adaptive Dependency-Guided Joint Prompt Optimization) is a specialized framework designed to solve the challenges of optimizing [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) used within [[pipeline|Multi-step Pipelines]]. While multi-step architectures enable models to execute complex reasoning and task-oriented workflows, the process of "joint optimization"—tuning the prompts for every step in the sequence simultaneously—is remarkably difficult. 

### The Challenge of Multi-Step Optimization
In complex pipelines, the primary obstacles to effective optimization are two-fold:
1. **Missing Step-Level Supervision**: It is often difficult to know exactly which intermediate step caused a failure in the final output.
2. **Inter-step Dependencies**: The performance of a subsequent step is heavily reliant on the quality of the output from the preceding step, creating a complex web of dependencies.

### The ADOPT Framework
ADOPT introduces an adaptive method to navigate these dependencies through several key technical innovations:

* **Gradient Decomposition**: The framework analyzes the dependency between each individual LLM step and the ultimate task goal. It constructs a **global textual gradient** based on errors found in the final output and then decomposes this into **step-level local textual gradients**. This provides the optimizer with highly precise signals for updating local prompts.
* **Decoupled Architecture**: ADOPT separates the estimation of optimization signals from the actual prompt updating process. This decoupling allows the framework to be integrated flexibly with various existing single-prompt optimizers.
* **Shapley-based Resource Allocation**: To prevent computational waste, ADOPT utilizes a strategy based on the [[provably-adaptive-linear-approximation-for-the-shapley-value-and-beyond|Shapley Value]] from [[Game Theory]]. This allows the system to adaptively identify and allocate optimization resources to the "high-impact" steps that contribute most to the pipeline's success.

### Experimental Results
Evaluations conducted on structurally diverse pipelines and real-world datasets demonstrate that ADOPT is both robust and highly effective. The framework consistently outperforms existing [[sprig-improving-large-language-model-performance-by-system-prompt-optimization|Prompt Optimization]] baselines, establishing a new standard for managing complex, interconnected [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] workflows.