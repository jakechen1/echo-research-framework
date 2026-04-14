---
title: A Decomposition Perspective to Long-context Reasoning for LLMs
created: 2024-05-22
source: https://arxiv.org/abs/2604.07981
tags: [LLM, Long-context, Reinforcement Learning, Artificial Intelligence, Machine Learning]
category: ai
---

## Overview

The paper "A Decomposition Perspective to Long-context Reasoning for LLMs" addresses a critical bottleneck in the evolution of [[large-language-models-llms|Large Language Models (LLMs)]]: the difficulty of maintaining coherent reasoning over extended input sequences. While [[$pi^2$-structure-originated-reasoning-data-improves-long-context-reasoning-abili|Long-context reasoning]] is essential for many real-world applications, the authors argue that current research lacks a granular understanding of the internal complexities that make these tasks challenging.

## Methodology: From Holistic to Atomic

The primary contribution of this research is moving away from a holistic view of reasoning. Instead, the authors propose decomposing long-context reasoning into a collection of fundamental "atomic skills." By identifying these individual components, the researchers can more accurately pinpoint where models fail during complex inference tasks.

To operationalize this theory, the study employs a two-step process:
1. **Dataset Synthesis**: The authors automatically generate a suite of pseudo-datasets. Each dataset is specifically designed to target and isolate a specific atomic skill, providing a controlled environment for training.
2. **Skill Sharpening**: Using these targeted datasets, the researchers apply [[reinforcement-learning-rl|Reinforcement Learning (RL)]] to the model. The objective is to sharpen the model's proficiency in each specific atomic skill, under the premise that improving individual components will lead to a synergistic improvement in general reasoning.

## Experimental Results

The effectiveness of this decomposition approach was tested across a wide array of [[evgeoqa-benchmarking-llms-on-dynamic-multi-objective-geo-spatial-exploration|Benchmark]] suites, including Loogle, Loong, LongBench-v2, BrowscompLong, Ruler-qa2, and MRCR. 

The results demonstrate a significant performance uplift. The proposed method outperformed established strong baselines by an average margin of 7.7%, raising the average performance score from 46.3% to 54.0%. These findings suggest that targeted, skill-based optimization is a highly potent strategy for advancing the capabilities of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models in handling complex, long-form data.