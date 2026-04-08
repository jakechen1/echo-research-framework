---
title: Decocted Experience Improves Test-Time Inference in LLM Agents
created: 2024-05-23
source: https://arxiv.org/abs/2604.04373
tags: [LLM, Machine Learning, Agentic AI, Inference Optimization]
category: ai, machine-learning, technology
---

# Decocted Experience Improves Test-Time Inference in LLM Agents

The research paper "Decocted Experience Improves Test-Time Inference in LLM Agents" presents a novel framework for enhancing the performance of [[Large Language Models]] (LLMs) without the intensive requirement of updating model parameters. While the field has seen significant progress through [[test-time scaling]]—the practice of increasing computation during inference through extended reasoning or search—this paper identifies a critical bottleneck in current methodologies.

### The Problem: Inefficient Scaling
As tasks transition from simple queries to complex [[Agentic AI]] workflows, naive scaling of [[inference-time computation]] (such as increased sampling or tree search) becomes increasingly inefficient. The researchers observe that simply adding more compute often leads to a "wasted budget," where the model explores suboptimal paths that do not contribute to the final solution, particularly in high-complexity environments like [[software engineering]] or web navigation.

### The Solution: Context as a Scaling Axis
The authors propose moving beyond brute-force computation by utilizing **context** as a complementary scaling axis. The central innovation is the concept of **decocted experience**. The term "decocted" refers to the process of extracting the essential "essence" from previous attempts or environmental interactions, rather than providing a raw, noisy history of events.

The research focuses on three pillars of experience augmentation:
1. **Extraction:** Identifying the core lessons and successes/failures from past trajectories.
2. **Organization:** Structuring information into coherent data structures that the model can easily ingest.
3. **Retrieval:** Determining which salient pieces of information are most relevant to the current reasoning step.

### Experimental Results
 The effectiveness of this approach was validated across several high-complexity domains, including:
* **Mathematical Reasoning:** Evaluating logical chain-of-thought stability.
* **Web Browsing:** Testing the ability to navigate dynamic, unstructured environments.
* **Software Engineering:** Executing complex debugging and code generation tasks.

The study concludes that the quality of context construction—specifically the ability to transform raw experience into distilled, actionable knowledge—is the primary driver of performance in modern, experience-augmented agents.