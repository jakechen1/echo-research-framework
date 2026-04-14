---
title: Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills
created: 2024-05-23
source: https://arxiv.org/abs/2604.05333
tags: [AI, Retrieval-Augmented-Generation, Autonomous-Agents, Graph-Neural-Networks]
category: ai
author: wiki-pipeline
dc.title: "Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/graph-of-skills-dependency-aware-structural-retrieval-for-massive-agent-skills.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Graph of Skills (GoS)

The paper **"Graph of Skills: Dependency-Aware Structural Retrieval for Massive Agent Skills"** addresses a critical bottleneck in the advancement of [[claw-eval-toward-trustworthy-evaluation-of-autonomous-agents|Autonomous Agents]]: the management of expanding large-scale skill libraries. As agents are increasingly tasked with interacting with complex environments—such as web browsers, personal applications, and intricate software interfaces—the number of reusable "skills" can grow into the thousands.

## The Problem of Scale

Traditional approaches to agentic workflows often rely on loading the entire available skill set into the [[lsrm-high-fidelity-object-centric-reconstruction-via-scaled-context-windows|Context Window]] of a [[from-large-language-model-predicates-to-logic-tensor-networks-neurosymbolic-offe|Large Language Model]] (LLM). However, as skill libraries scale, this method becomes unsustainable due to several key challenges:

* **Context Saturation:** Exceeding the model's maximum token capacity.
* **Increased Latency:** Higher computational overhead during processing.
* **Cost and Hallucination:** Rising inference costs and an increased likelihood of model errors when navigating irrelevant information.

## The Graph of Skills (GoS) Framework

To mitigate these issues, the authors introduce **Graph