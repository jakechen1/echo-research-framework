---
title: "Emergent Social Transmission Of Model Based Representations Without Inference"
category: neuroscience
created: 2026-04-12
---

title: Emergent social transmission of model-based representations without inference
created: 2024-05-23
source: https://arxiv.org/abs/2604.05777
tags: [social learning, reinforcement learning, cognitive science, cultural evolution]
category: ai, machine-learning, neuroscience

# Emergent social transmission of model-based representations without inference

The research paper "Emergent social transmission of model-based representations without inference" explores a fundamental question in [[cognitive-science|Cognitive Science]]: how can complex, structural knowledge about an environment be passed between individuals through simple [[social-learning|Social Learning]] mechanisms, without the need for computationally expensive [[mentalizing|Mentalizing]]?

## The Problem of Cognitive Load
In studying human intelligence, it is often assumed that we rely on the ability to infer the hidden beliefs and intentions of others. However, this "mind-reading" capability is computationally costly. An alternative perspective, rooted in [[cultural-evolution|Cultural Evolution]], suggests that complex cultural knowledge can be transmitted through simple behavioral cues and environmental observations, bypassing the need for deep social reasoning.

## Methodology
The researchers employed [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] simulations to test this hypothesis. They created an environment that was reconfigurable, presenting a challenge to a "naïve agent" searching for rewards. The study compared two distinct learning modes:
1. **Asocial Learning:** The agent learns purely through individual trial and error.
2. **Social Learning:** The agent observes an "expert" agent.

Crucially, the learner was programmed to avoid any form of mentalizing. Instead of attempting to infer the expert's internal states, the learner used simple heuristics, such as mimicking observed actions or boosting its own value representations based on the expert's successful behaviors.

## Key Findings
The simulations revealed that simple, non-inferential cues are sufficient to drive the transmission of complex information:
* **Representation Convergence:** Even without mentalizing, the learner's internal environmental representations converged toward those of the expert.
* **Model-Based Advantage:** The most significant benefits were observed in agents utilizing [[model-based-learning|Model-based learning]]. These agents showed accelerated learning rates and developed more "expert-