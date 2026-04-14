---
title: "CuraLight: Debate-Guided Data Curation for LLM-Centered Traffic Signal Control"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.05663"
tags: [Traffic Signal Control, Large Language Models, Reinforcement Learning, Intelligent Transportation Systems]
category: [ai, technology]
---

# CuraLight: Debate-Guided Data Curation for LLM-Centered Traffic Signal Control

CuraLight is a novel framework designed to advance [[curalight-debate-guided-data-curation-for-llm-centered-traffic-signal-control|Traffic Signal Control]] (TSC) within the domain of [[intelligent-transportation-systems|Intelligent Transportation Systems]] (ITS). As urban centers face increasing challenges regarding congestion and emissions, the integration of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) into traffic management offers a path toward more adaptive and interpretable control strategies.

### The Challenge in Modern TSC
Current approaches utilizing [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL) and LLMs face several critical bottlenecks:
* **Limited Interpretability:** Traditional RL agents often operate as "black boxes."
* **Data Scarcity:** A lack of sufficient, high-quality interaction data for diverse traffic scenarios.
* **Poor Generalization:** Difficulty in adapting to heterogeneous intersection layouts and varying traffic flows.

### The CuraLight Framework
CuraLight introduces an LLM-centered architecture that leverages an RL agent to assist in the fine-tuning of an LLM-based controller. The framework operates through two primary mechanisms:

1. **RL-Assisted Exploration:** An RL agent explores various traffic environments to generate high-quality interaction trajectories. These trajectories are then converted into structured prompt-response pairs, enabling the use of [[imitation-learning|Imitation Learning]] to fine-tune the LLM.
2. **Debate-Guided Curation:** To ensure the quality of the training data, the framework utilizes a multi-LLM ensemble deliberation system. This system engages in structured "debates" to evaluate candidate signal timing actions, providing preference-aware supervision signals that refine the training process.

### Experimental Results
The effectiveness of CuraLight was tested using the SUMO simulator, applying heterogeneous real-world networks from Jinan, Hangzhou, and Yizhuang. The results demonstrate significant improvements over state-of-the-art baselines:
* **Average Travel Time:** Reduced by 5.34%.
* **Average Queue Length:** Reduced by 5.14%.
* **Average Waiting Time:** Reduced by 7.04%.

By combining RL-driven exploration with a sophisticated debate-based supervision mechanism, CuraLight provides a scalable, interpretable, and highly efficient solution for modern [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] applications in urban infrastructure management.