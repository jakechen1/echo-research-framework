---
title: StarVLA: A Lego-like Codebase for Vision-Language-Action Model Developing
created: 2024-05-23
source: https://arxiv.org/abs/2604.05014
tags: [VLA, Robotics, Machine Learning, Open-Source, Computer Vision]
category: ai
---

# StarVLA

StarVLA is an open-source, modular framework specifically designed to address the extreme fragmentation currently hindering research in [[Vision-Language-Action (VLA)]] models. As the development of [[Embodied AI]] requires the seamless integration of perception, language understanding, and physical action, StarVMA provides a unified ecosystem to facilitate the creation of generalist agents.

### Modular Architecture
The core strength of StarVLA lies in its "Lego-like" design. It employs a decoupled architecture where the backbone and the action head can be swapped independently. This structural flexibility allows researchers to utilize diverse [[Vision-Language Models (VLM)]], such as Qwen-VL, or integrate advanced [[World Models]] like Cosmos into a unified training pipeline. This modularity is essential for prototyping new [[Machine Learning]] architectures without the need to rewrite fundamental codebases or incompatible architectures.

### Unified Training and Evaluation
Beyond architecture, StarVLA implements standardized, reusable training strategies, including [[cross-embodiment learning]] and [[multimodal co-training]]. These strategies are designed to work consistently across various robotic