---
title: Cog-DRIFT: Exploration on Adaptively Reformulated Instances Enables Learning from Hard Reasoning Problems
created: 2024-05-23
source: https://arxiv.org/abs/2604.04767
tags: [LLM, Reinforcement Learning, Curriculum Learning, Reasoning]
categories: [ai, machine-learning]

# Cog-DRIFT

**Cog-DRIFT** is a novel framework designed to overcome the "exploration barrier" in [[Reinforcement Learning]] from Verifiable Rewards (RLVR) for [[Large Language Models]] (LLMs). The primary limitation addressed by this research is the inability of models to learn from extremely complex reasoning problems that are initially too difficult to solve within their current policy, as these problems yield no meaningful reward signal.

## Methodology

The core innovation of Cog-DRIFT is the use of **task reformulation**. Rather than attempting to solve complex, open-ended reasoning tasks directly, the framework transforms these challenges into cognitively simpler variants. These reformulations include:

* **Multiple-choice formats**: Reducing the search space to a set of predefined options.
* **Cloze formats**: Utilizing fill-in-the-blank structures to provide denser learning signals.

These variants are designed to preserve the original correct answer while reducing the effective search space. The framework employs an **adaptive curriculum** that organizes these reformulated instances by difficulty. The training progresses along a spectrum from discriminative tasks to more complex generative tasks. This allows the model to "bootstrap" its learning—acquiring foundational knowledge from easier, structured formats and transferring that intelligence back