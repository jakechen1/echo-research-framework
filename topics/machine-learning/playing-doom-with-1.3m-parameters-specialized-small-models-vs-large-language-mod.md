---
title: Playing DOOM with 1.3M Parameters: Specialized Small Models vs Large Language Models for Real-Time Game Control
created: 2024-05-24
source: https://arxiv.org/abs/2604.07385
tags: [ai, machine-learning, technology]
---

# Playing DOOM with 1.3M Parameters

The research paper "Playing DOOM with 1.3M Parameters" introduces **SauerkrautLM-Doom-MultiVec**, an extremely lightweight [[Machine Learning]] model designed for high-frequency decision-making in the classic first-person shooter, [[DOOM]]. While contemporary research often focuses on scaling [[Large Language Models]] (LLMs) to hundreds of billions of parameters, this paper demonstrates that a specialized model with only 1.3 million parameters can significantly outperform much larger counterparts in real-time environments.

### Architecture and Methodology
The model utilizes a specialized architecture consisting of a [[ModernBERT]] encoder paired with hash embeddings and depth-aware token representations. To process the game state, the model uses an attention pooling classification head to select optimal game actions derived from ASCII frame representations. Notably, the system operates with a decision latency of just 31ms per frame, meeting the rapid-fire requirements of [[Real-time Control]].

The model was trained on a relatively small dataset of 31,000 human gameplay demonstrations, specifically optimized for the "defend_the_center" scenario.

### Performance Comparison
The study compared SauerkrautLM-Doom-MultiVec against several state-of-the-art LLMs, including [[Nemotron-120B]], [[Qwen3.5-27B]], and [[GPT-4o-mini]]. The results demonstrated a massive disparity in efficiency and skill:

* **Kill Count:** The 1.3M parameter model achieved 178 frags across 10 episodes, whereas the combined total of all tested LLMs was only 13 frags.
* **Behavioral Intelligence:** While the LLMs primarily exhibited evasive behaviors (avoiding enemies), the small specialized model was the only agent capable of actively engaging and defeating enemies.
* **Scaling Efficiency:** Despite being up to 92,000x