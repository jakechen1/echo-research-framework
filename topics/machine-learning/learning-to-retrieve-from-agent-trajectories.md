---
title: Learning to Retrieve from Agent Trajectories
created: 2024-05-22
source: https://arxiv.org/abs/2604.04949
tags: [Information Retrieval, LLM Agents, Machine Learning, Agentic Search]
category: ai, machine-learning, technology
---

# Learning to Retrieve from Agent Trajectories

**Learning to Retrieve from Agent Trajectories** explores a specialized shift in [[Information Retrieval]] (IR) necessitated by the emergence of autonomous [[Large Language Models]] (LLMs). Traditionally, retrieval models have been optimized for human users, utilizing [[Learning-to-Rank]] methods trained on human interaction logs, such as click-through rates and dwell time. However, the rise of agentic search workflows introduces a fundamental mismatch: retrieval is increasingly performed by agents within multi-turn reasoning and action loops, rather than by humans.

## The Problem: Human-Centric Mismatch
In the era of [[Agentic Search]], agents interact with search engines through complex, iterative processes. Traditional training signals (human clicks) do not accurately reflect how an agent consumes information. Because agents use retrieval as a core component of their reasoning, models trained under human-centric assumptions fail to account for the specific way agents issue queries and evaluate documentation utility.

## The LRAT Framework
To address this, the paper introduces **LRAT**, a new training paradigm that leverages agent trajectories as a primary source of supervision. Instead of relying on human behavior, LRAT mines high-quality signals directly from the interaction history of search agents. Key behavioral signals identified in the research include:

*   **Browsing Actions:** Direct engagement with specific documents.
*   **Unbrowsed Rejections:** Instances where an agent explicitly bypasses a document.
*   **Post-browse Reasoning Traces:** The cognitive or logical outputs produced by the agent after processing information.

By using these signals, LRAT implements a weighted optimization approach that incorporates "relevance intensity," allowing the model to understand not just if a document was used, but how critical it was to the agent's reasoning.

## Experimental Results
Extensive testing on [[Deep Research]] benchmarks demonstrates that retrievers trained via LRAT outperform traditional models. The results show significant improvements in:
1.  **Evidence Recall:** The ability to find necessary data points.
2.  **Task Success:** The completion rate of complex, multi-step agent goals.
3.  **Execution Efficiency:** Reducing the computational overhead of unnecessary browsing.

This research suggests that agent trajectories provide a practical, scalable, and highly effective supervision source for the next generation of [[Machine Learning]]-driven retrieval systems.