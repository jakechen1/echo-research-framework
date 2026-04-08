---
title: "Cobblestone: A Divide-and-Conquer Approach for Automating Formal Verification"
created: 2024-05-22
source: https://arxiv.org/abs/2410.19940
tags: [formal verification, proof synthesis, large language models, Coq, automated reasoning]
categories: [ai, machine-learning, technology]
---

# Cobblestone

**Cobblestone** is an innovative framework designed to automate the process of [[Formal Verification]] using a "divide-and-conquer" strategy. While proof assistants like [[Coq]] are essential for ensuring the mathematical correctness of software and hardware, they traditionally require significant manual effort and specialized expertise. Although [[Machine Learning]] has introduced new possibilities for [[Proof Synthesis]], existing [[Large Language Models]] (LLMs) often struggle to prove complex properties and can introduce unsound logic.

## Methodology

The core innovation of Cobblestone lies in its iterative decomposition approach. Rather than relying on an LLM to generate a single, end-to-end proof, Cobblestone utilizes the LLM to generate potential proof candidates that serve to break the primary theorem into smaller, simpler sub-problems. The framework follows a specific lifecycle:

1.  **Decomposition**: An LLM proposes potential proof structures or strategies.
2.  **Sub-problem Identification**: The system uses these proposals to split the main goal into manageable parts.
3.  **Verification and Iteration**: The system automatically identifies which sub-parts have been successfully proven and focuses subsequent iterations on the remaining unproven segments.

A defining characteristic of Cobbletone is its commitment to **soundness**. Despite the inherent unreliability and "hallucination" tendencies of LLMs, the framework ensures that the final assembled proof is mathematically rigorous and verified by the underlying proof assistant.

## Performance and Efficiency

Evaluations performed on various open-source [[Coq]] benchmarks demonstrate that Cobblestone is highly efficient. The framework has shown the ability to outperform:
*   State-of-the-art non-LLM automated tools.
*   Current leading LLM-based proof synthesis tools.

In terms of resource consumption, Cobblestone is remarkably cost-effective, with an average execution cost of only **$1.25** and an average duration of **14.7 minutes**. 

## Human-AI Collaboration

Cobblestone is not limited to fully autonomous operation. It is designed to integrate external inputs, such as lemmas or structural hints provided by a human user or an external automated tool. When provided with an "oracle" (external guidance), the system's success rate increases significantly, proving up to 58% of theorems. This capability highlights the potential of using [[Artificial Intelligence]] to augment, rather than replace, human expertise in [[Software Engineering]].