---
title: SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents
created: 2024-05-22
source: https://arxiv.org/abs/2604.07791
tags: [AI, Reinforcement Learning, Agentic Learning, Tool-use]
category: ai, machine-learning
---

# SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents

## Overview
**SEARL** is an innovative framework designed to facilitate the development of **self-evolving agents**. As the paradigm of [[Artificial Intelligence]] shifts toward agentic learning—where models improve by synthesizing new tools and accumulating explicit experiences—SEARL provides a structured approach to autonomous learning without the massive computational overhead typically required by modern [[Large Language Models (LLMs)]].

## The Challenge of Sparsity and Scale
Current advancements in [[Reinforcement Learning with Verifiable Rewards (RLVR)]] have shown promise in single-turn reasoning. However, two major challenges persist in the pursuit of self-evolving agents:
1. **Deployment Constraints:** Prevailing methods often necessitate large-scale LLMs or complex multi-agent frameworks, which are impractical for deployment in resource-constrained environments.
2. **Reward Sparsity:** Agents frequently operate under "outcome-based" reward structures, receiving feedback only upon task completion. This lack of intermediate feedback makes it difficult for the agent to correlate specific actions with successful results.

## The SEARL Framework
To address these limitations, the SEARL framework introduces a **Tool-Memory** based architecture. Instead of relying solely on direct interaction experiences, SEARL constructs a structured experience memory that integrates the **planning** and **execution** phases of a task.

Key innovations include:
* **Structured Experience Memory:** By integrating planning with execution, SEARL creates a robust state abstraction. This allows the agent to recognize patterns and facilitate [[Tool-use]] reuse across different, but analogous, contexts.
* **Reward Densification:** The framework utilizes inter-trajectory correlations to transform sparse, end-of-task feedback into denser, more informative reward signals.
* **Knowledge Extraction:** SEARL enables agents to extract explicit knowledge from historical data, allowing for continuous evolution through synthesized tools and accumulated expertise.

## Experimental Validation
The SEARL framework was evaluated on complex [[Knowledge Reasoning]] and [[Mathematics]] tasks. The experimental results demonstrate that SEARL achieves significantly more efficient and practical learning compared to existing methods, proving its viability for high-