---
title: Reasoning Through Chess: How Reasoning Evolves from Data Through Fine-Tuning and Reinforcement Learning
created: 202    4-05-24
source: https://arxiv.org/abs/2604.05134
tags: [LLM, Reinforcement Learning, Chess, Reasoning, Supervised Fine-Tuning, Hallucination]
category: ai, machine-learning
---

# Reasoning Through Chess

The research paper "Reasoning Through Chess: How Reasoning Evolves from Data Through Fine-Tuning and Reinforcement Learning" investigates the developmental trajectory of reasoning capabilities within [[Large Language Models]] (LLMs). By using [[Chess]] as a controlled, high-complexity benchmark, the authors study how reasoning emerges as a model moves from [[Supervised Fine-Tuning]] (SFT) to [[Reinforcement Learning]] (RL).

## The Evolution of Reasoning via SFT

The study focuses on how different SFT datasets impact the model's ability to perform subsequent RL. Two primary methodologies were analyzed:

* **Best-Move Prediction:** Training the model to directly predict the single optimal move. While this method achieves the highest performance in downstream RL, it results in **unfaithful reasoning**. This phenomenon occurs when the model's generated reasoning process is logically inconsistent with the move it ultimately selects.
* **Multi-Move Trajectories:** Training the model on sequences of moves (trajectories). This approach yields comparable performance to best-move prediction but promotes **faithful reasoning**, where the internal logic of the model remains consistent with its actions. Furthermore, training on trajectories leads to more stable RL training processes.

## Benefits of Reinforcement Learning

The researchers found that the RL phase provides more than just strategic improvements. Beyond a substantial positive shift in the distribution of move quality, RL serves as a corrective mechanism that reduces [[Hallucination]] rates as a secondary effect. This suggests that RL can refine the reliability of a model's output alongside its accuracy.

## Predictive Metrics and Performance

A key discovery presented in the paper is that specific metrics from the SFT checkpoint—spanning evaluation performance, hallucination rates, and reasoning quality—are highly predictive of the model’s post-RL performance. By leveraging these insights, the authors produced a 7B-parameter model capable of surpassing leading open-source reasoning models in [[Chess]] proficiency.