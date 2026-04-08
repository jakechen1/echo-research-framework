---
title: Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills
created: 2024-05-23
source: https://arxiv.org/abs/2604.05333
tags: [AI, Retrieval-Augmented-Generation, Autonomous-Agents, Graph-Neural-Networks]
category: ai
---

# Graph of Skills (GoS)

The paper **"Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills"** addresses a critical bottleneck in the advancement of [[Autonomous Agents]]: the management of expanding large-scale skill libraries. As agents are increasingly tasked with interacting with complex environments—such as web browsers, personal applications, and intricate software interfaces—the number of reusable "skills" can grow into the thousands.

## The Problem of Scale

Traditional approaches to agentic workflows often rely on loading the entire available skill set into the [[Context Window]] of a [[Large Language Model]] (LLM). However, as skill libraries scale, this method becomes unsustainable due to several key challenges:

* **Context Saturation:** Exceeding the model's maximum token capacity.
* **Increased Latency:** Higher computational overhead during processing.
* **Cost and Hallucination:** Rising inference costs and an increased likelihood of model errors when navigating irrelevant information.

## The Graph of Skills (GoS) Framework

To mitigate these issues, the authors introduce **Graph