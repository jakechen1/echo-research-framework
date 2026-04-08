---
title: LLM 'benchmark' as a 1v1 RTS game where models write code controlling the units
created: 2024-05-22
source: https://yare.io/ai-arena
tags: [LLM, Benchmarking, RTS, Autonomous Agents, Coding]
category: ai, technology
---

# LLM-RTS Benchmark: Competitive Code-Based Agent Evaluation

The proposed benchmark represents a significant paradigm shift in how we evaluate [[Large Language Models]] (LLMs). Traditional [[Machine Learning]] benchmarks typically rely on static datasets—such as MMLU or GSM8K—which measure pattern recognition, linguistic accuracy, and mathematical reasoning within a closed-loop text environment. In contrast, this new approach utilizes a [[Real-Time Strategy]] (RTS) environment where models compete in a 1v1 format.

In this benchmark, the primary metric for success is not merely text generation, but the ability to produce functional, executable code. Each model is tasked with writing scripts that control game units, manage resources, and execute tactical maneuvers within a dynamic game engine. This transforms the evaluation from a standard prompting task into a complex [[Automated Programming]] challenge involving high-level strategic planning and low-level implementation.

The significance of this method lies in its ability to test "agentic" capabilities. To succeed in an RTS environment, a model must demonstrate:

1.  **Temporal Reasoning:** Understanding the long-term consequences of immediate actions within a continuous time stream.
2.  **Strategic Planning:** Developing a coherent strategy that can adapt to the unpredictable movements of an opponent.
3.  **Error Correction:** The ability to iterate on code that may fail during execution due to environmental complexities.

By treating the benchmark as an interactive competition, researchers can observe emergent behaviors and complex strategies that remain hidden during standard text-only evaluation. This methodology bridges the gap between [[Artificial Intelligence]]-driven text generation and the development of true autonomous agents capable of interacting with complex, changing simulations. This approach effectively integrates principles of [[Reinforcement Learning]] into the evaluation pipeline, where the ultimate reward is victory within the simulated combat arena.