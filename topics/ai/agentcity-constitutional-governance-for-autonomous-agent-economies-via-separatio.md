---
title: "Agentcity Constitutional Governance For Autonomous Agent Economies Via Separatio"
category: artificial-intelligence
created: 2026-04-12
---

title: AgentCity: Constitutional Governance for Autonomous Agent Economies via Separation of Power
created: 2024-05-22
source: https://arxiv.org/abs/2604.07007
tags: [Autonomous Agents, Blockchain Governance, AI Alignment, Decentralized Economy]
category: [ai, technology]

# AgentCity: Constitutional Governance for Autonomous Agent Economies

As [[autonomous-ai-agents|Autonomous AI Agents]] begin to operate across organizational boundaries on the open internet, a significant governance challenge emerges. Agents are increasingly capable of discovering, transacting, and delegating tasks to agents owned by different parties without centralized oversight. This creates a phenomenon known as the **Logic Monopoly**, where the collective behavior of an agent society becomes opaque because no single human can effectively audit or govern the emergent chain of planning, execution, and evaluation.

## The Separation of Power (SoP) Model

To mitigate the risks of the Logic Monopoly, the authors propose the **Separation of Power (SoP)** model. This is a constitutional governance architecture deployed on a [[blockchain-and-ai-securing-intelligent-networks-for-the-future|Blockchain]] designed to break the monopoly through three structural separations:

1.  **Legislation**: Agents formulate operational rules through [[smart-contracts|Smart Contracts]]. In this architecture, the smart contract serves as the actual legislative output that governs all subsequent behavior.
2.  **Execution**: Deterministic software performs the actual tasks, but strictly within the bounds established by the legislative contracts.
3.  **Adjudication**: Humans maintain oversight via a complete ownership chain, ensuring every agent is fundamentally tied to a responsible human principal.

## AgentCity Implementation

The researchers instantiate this model in **AgentCity**, an [[evm-compatible|EVM-compatible]] layer-2 blockchain. AgentCity utilizes a three-tier contract hierarchy comprised of foundational, meta, and operational layers to manage complex agent interactions.

The fundamental thesis of the paper is **alignment-through-accountability**. The researchers argue that if each individual agent is properly aligned with its human owner through a verifiable accountability chain, the emergent behavior of the entire agent collective will naturally converge on human intent—eliminating the need for inefficient top-down, centralized regulations.

## Experimental Results

The SoP model was evaluated through a pre-registered experiment within a "commons production economy." In this setup, agents competed for and shared a finite resource pool to collaboratively produce value. The study successfully demonstrated the stability of this governance model at a scale of 50 to 1,000 agents.