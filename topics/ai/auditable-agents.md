---
title: Auditable Agents
created: 2024-05-22
source: https://arxiv.org/abs/2604.05485
tags: [ai, security, accountability, autonomous-agents]
category: ai
---

# Auditable Agents

As [[Large Language Models]] evolve into [[Agentic Systems]] capable of calling tools, querying databases, and triggering external side effects, the paradigm of AI safety is shifting. While traditional safety research focuses on preventing harmful actions, the rise of agents necessitates a focus on **answerability**. If an agent performs an irreversible action in the real world, the critical question is no longer just "how do we stop it?" but "how do we hold it accountable?"

## The Pillars of Oversight

The research distinguishes between three interconnected concepts essential for managing autonomous behavior:

*   **Accountability**: The capacity to determine compliance with regulations and assign responsibility for specific outcomes.
*   **Auditability**: The underlying system property that provides the necessary technical foundation for accountability.
*   **Auditing**: The active process of reconstructing agent behavior through the analysis of trustworthy evidence.

The central thesis of the work is that accountability is impossible in any agent system that lacks inherent auditability.

## Dimensions of Auditability

To move beyond theoretical discussion, the authors define five operational dimensions for measuring agent auditability:

1.  **Action Recoverability**: The ability to reconstruct the sequence of events.
2.  **Lifecycle Coverage**: Ensuring monitoring spans the entire operational lifespan of the agent.
3.