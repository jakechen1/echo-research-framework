---
title: "SUPERNOVA: Eliciting General Reasoning in LLMs with Reinforcement Learning on Natural Instructions"
created: 2024-05-24
source: https://arxiv.org/abs/2604.08477
tags: [AI, RLVR, LLM, Data Curation, Reasoning, Machine Learning]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "SUPERNOVA: Eliciting General Reasoning in LLMs with Reinforcement Learning on Natural Instructions"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/supernova-eliciting-general-reasoning-in-llms-with-reinforcement-learning-on-nat.md
dc.language: en
dc.rights: CC-BY-4.0
---

# SUPERNOVA

**SUPERNOVA** is a specialized data curation framework designed to bridge the gap between formal domain reasoning and general-purpose reasoning in [[Large Language Models (LLMs)]]. While [[Reinforcement Learning with Verifiable Rewards (RLVR)]] has demonstrated transformative success in structured domains such as mathematics and [[Computer Programming]], its application to general reasoning—encompassing tasks like [[Causal Inference]] and temporal reasoning—has been hindered by a lack of high-quality, verifiable training data.

## Overview

The core innovation of SUPERNOVA lies in its ability to adapt existing instruction-tuning datasets that contain expert-annotated ground truths into formats suitable for RLVR. The researchers conducted over 100 controlled reinforcement learning experiments to identify the most effective strategies for data design. The study focused on three critical variables:

1.  **Source Task Selection:** Determining which initial datasets provide the best foundation for training.
2.  **Task Mixing Strategies:** Optimizing the balance of different reasoning types during the learning process.
3.  **Synthetic Interventions:** Utilizing automated methods to enhance the quality of the training data.

## Key Findings

The research highlights that the process of task selection is highly sensitive; specifically, selecting tasks based on their performance relative to individual target tasks is significantly more effective than using strategies based on overall average performance. 

When implemented, the SUPERNOVA framework significantly outperforms industry-standard baselines, such as [[Qwen3.5]], on several rigorous benchmarks, including:
*   **BBEH** (achieving relative improvements of up to 52.8% across various model scales)
*   **Zebralogic**
*   **MMLU-Pro**

## Impact

By providing a principled approach to [[curalight-debate-guided-data-curation-for-llm-centered-traffic-signal-control|Data Curation]], SUPERNOVA offers a scalable methodology for expanding the reasoning capabilities of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] models. The framework demonstrates that the bottleneck for general reasoning is not necessarily the RL algorithm itself, but the strategic utilization of human-annotated resources to create verifiable learning environments.

## External Resources
*   **Code and Data:** [GitHub - asuvarna31/supernova](https://github.com/asuvarna31/supernova)
*   **Original Paper:** [arXiv:2604.08477](https://arxiv.org/abs/2604.08477)