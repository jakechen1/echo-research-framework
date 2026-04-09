---
title: "VisCoder2: Building Multi-Language Visualization Coding Agents"
created: 2024-05-22
source: "https://arxiv.org/abs/2510.23642"
tags: [ai, machine-learning, coding-agents, data-visualization]
category: ai
---

# VisCoder2: Building Multi-Language Visualization Coding Agents

The research paper **VisCoder2: Building Multi-Language Visualization Coding Agents** presents a novel approach to improving the capability of [[Large Language Models]] (LLMs) in generating, executing, and refining code for [[Data Visualization]]. While modern [[Coding Agents]] have shown promise, they often struggle with a lack of language diversity and the inability to correct errors during the execution phase.

### Key Contributions

To overcome these limitations, the authors introduced three critical resources designed to advance the state of the art in [[Automated Programming]]:

*   **VisCode-Multi-679K**: A large-scale, supervised dataset containing 679,000 executable visualization samples. This dataset is unique because it spans 12 different programming languages and incorporates multi-turn correction dialogues, enabling models to learn from execution failures and iterative feedback.
*   **VisPlotBench**: A comprehensive benchmark designed for the systematic evaluation of visualization agents. It evaluates not just the initial generation of code, but also the effectiveness of multi-round