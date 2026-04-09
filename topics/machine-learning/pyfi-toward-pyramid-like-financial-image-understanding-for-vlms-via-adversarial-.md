---
title: "PyFi: Toward Pyramid-like Financial Image Understanding for VLMs via Adversarial Agents"
created: 2024-05-24
source: https://arxiv.org/abs/2512.14735
tags: [ai, machine-learning, VLMs, financial-ai, adversarial-learning, computer-vision]
---

# PyFi

**PyFi** is a novel framework designed to advance [[Vision Language Models]] (VLMs) in the specialized domain of financial image understanding. The framework introduces a "pyramid-like" reasoning approach, allowing models to navigate through question chains that progress from simple visual perception to complex, expert-level financial analysis.

## Core Components

### PyFi-600K Dataset
The foundation of the framework is the **PyFi-600K** dataset, which consists of 600,000 question-answer pairs. The dataset is structured as a reasoning pyramid:
* **The Base:** Comprises questions requiring fundamental visual perception (e.g., identifying numbers or text in a chart).
* **The Apex:** Contains high-complexity questions that demand deep [[Machine Learning]]-driven expertise and multi-step financial reasoning.

### PyFi-adv Mechanism
To ensure scalability without the need for manual human annotation, the researchers implemented **PyFi-adv**. This is a multi-agent adversarial mechanism operating under the [[Monte Carlo Tree Search]] (MCTS) paradigm. The process involves two competing entities:
1. **Challenger Agent:** Tasked with generating increasingly difficult question chains to probe the limits of the model.
2. **Solver Agent:** Tasked with answering the generated questions.

This adversarial interplay allows for the automated, synthetic generation of high-quality, hierarchical training data.

## Experimental Results
The researchers applied the PyFi framework to fine-tune the **Qwen2.5-VL** model series (3B and 7B parameters). By training on the structured reasoning chains, the models learned to decompose complex financial queries into simpler, sequential sub-questions. 

The performance improvements were significant:
* **Qwen2.5-VL-3B:** Achieved an average accuracy increase of **19.52%**.
* **Qwen2.5-VL-7B:** Achieved an average accuracy increase of **8.06%**.

## Related Topics
* [[Artificial Intelligence]]
* [[Computer Vision]]
* [[Large Language Models]]
* [[Financial Technology]]