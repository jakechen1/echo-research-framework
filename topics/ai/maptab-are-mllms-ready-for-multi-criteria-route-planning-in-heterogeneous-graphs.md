---
title: "MapTab: Are MLLMs Ready for Multi-Criteria Route Planning in Heterogeneous Graphs?"
created: 2024-05-22
source: https://arxiv.org/abs/2602.18600
tags: [benchmarking, MLLM, route-planning, multimodal-learning, artificial-intelligence]
category: ai
---

# MapTab: Are MLL．Models Ready for Multi-Criteria Route Planning in Heterogeneous Graphs?

MapTab is a specialized multimodal benchmark designed to rigorously evaluate the reasoning capabilities of [[Multimodal Large Language Models]] (MLLMs) when faced with multi-criteria constraints. As the field moves toward [[Artificial General Intelligence]] (AGI), MapTab addresses a critical gap: the lack of benchmarks capable of testing how models process information from heterogeneous sources—specifically map images and structured tabular data—to solve complex spatial problems.

## Benchmark Structure

The MapTab framework utilizes two primary scenarios to test model performance:

1.  **Metromap**: A large-scale dataset covering metro networks from 160 cities across 52 countries.
2.  **Travelmap**: A dataset featuring 168 representative tourist attractions spanning 19 countries.

To complete a task, an MLLM must perceive visual cues from map images and effectively ground them with attributes found in tabular formats. The benchmark evaluates how well models can optimize routes based on four essential decision-making dimensions: **Time**, **Price**, **Comfort**, and **Reli