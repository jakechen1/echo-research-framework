---
title: "Dynamic Attentional Context Scoping: Agent-Triggered Focus Sessions for Isolated Per-Agent Steering in Multi-Agent LLM Orchestration"
created: 2024-05-22
source: "https://arxiv.org/abs/260lar.07911"
tags: [ai, multi-agent systems, context management, llm orchestration, autonomy]
category: ai
---

# Dynamic Attentional Context Scoping (DACS)

**Dynamic Attentional Context Scoping (DACS)** is an architectural mechanism designed to solve the problem of [[context pollution]] within [[Multi-Agent Systems]] (MAS). In complex [[Large Language Models]] (LLM) orchestration, a central orchestrator often manages multiple concurrent agents. As the number of agents ($N$) increases, the orchestrator's [[context window]] becomes saturated with interleaved task states, partial outputs, and competing instructions, which degrades the quality of decision-making and steering.

## The Problem: Context Pollution
In traditional "flat-context" orchestration, every agent's data competes for the same limited attention space. This results in "cross-agent contamination," where the instructions or outputs of Agent A interfere with the processing of Agent B. This interference leads to significant drops in steering accuracy and makes scaling agentic workflows computationally inefficient.

## The DACS Mechanism
DACS introduces an asymmetric, agent-triggered approach to context management. Instead of maintaining a monolithic context, the orchestrator operates in two distinct modes:

1.  **Registry Mode:** The orchestrator maintains a high-level overview of the entire system. Each agent is represented only by a lightweight status summary (limited to $\le$ 200 tokens), allowing the orchestrator to remain responsive to all agents and the user without cluttering the window.
2.  **Focus Mode ($a_i$):** When a specific agent emits a `SteeringRequest`, the orchestrator enters a specialized focus session. The full, high-fidelity context of the requesting agent is injected into the window, while all other agents are compressed back into their minimal registry entries.

This ensures the context window composition is strictly $F(a_i) + R_{-i}$, providing deterministic isolation without the need for complex retrieval or lossy compression of the primary agent's state.

## Experimental Results
Evaluations across 200 experimental trials demonstrate that DACS significantly outperforms standard architectures:

*   **Steering Accuracy:** Achieved 90.0%–98.4% accuracy, compared to only 21.0%–60.0% in flat-context baselines.
*   **Contamination Reduction:** "Wrong-agent contamination" dropped from a peak of 57% to as low as 0%.
*   **Efficiency:** The mechanism achieved context efficiency ratios of up to 3.53x.
*   **Scalability:** The accuracy advantage of DACS grows proportionally with the number of agents ($N$) and the density of decisions ($D$).