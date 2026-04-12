---
title: "Vero: An Open RL Recipe for General Visual Reasoning"
created: 2024-05-24
source: "https://arxiv.org/abs/2604.04917"
tags: [ai, machine-learning, vision-language-models, reinforcement-learning, open-source]
category: [ai, machine-learning, technology]
---

# Vero: An Open RL Recipe for General Visual Reasoning

**Vero** is a family of fully open-weight [[aligned-vector-quantization-for-edge-cloud-collabrative-vision-language-models|Vision-Language Models]] (VLMs) designed to bridge the gap between proprietary, closed-source reasoning pipelines and the [[battle-for-wesnoth-open-source-turn-based-strategy-game|Open-Source]] community. The project addresses a critical transparency issue in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]: while current state-of-the-art VLMs demonstrate incredible visual reasoning across charts, science, and spatial tasks, the specific [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL) recipes and datasets used to train them are often hidden behind corporate walls.

## Technical Architecture

The methodology behind Vero focuses on scaling [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] through diverse data and specialized reward structures. The researchers introduced **Vero-600K**, a massive dataset comprising 600,000 samples curated from 59 distinct datasets. To handle the difficulty of varying output formats across different types of visual tasks, the team implemented **task-routed rewards**. This allows the model to process heterogeneous answer formats—ranging from simple classification to complex,-structured scientific interpretations—within a unified training framework.

## Performance and Benchmarking

Vero demonstrates significant improvements over existing open-weight architectures. Using **Qwen3-VL-8B-Instruct** as a base model, the Vero training regimen allowed it to outperform the specialized **Qwen3-VL-8B-Thinking** model on 23 out of 30 benchmarks within the **VeroEval** suite. On average, the researchers observed a performance increase of 3.6 to 5.3 points across a wide range of challenging visual reasoning benchmarks.

## Key Research Findings

The study provides critical insights into the nature of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] scaling for visual reasoning:

* **Diversity as a Driver:** Systematic ablations revealed that different task categories (e.g., spatial vs. scientific) elicit qualitatively different reasoning patterns.
* **Limited Transferability:** Training on isolated task categories leads to poor transferability, suggesting that broad, multi-domain data coverage is the primary catalyst for strong RL scaling.
* **Open Access:** In a commitment to transparency, the developers have released all associated data, code, and models to the public.