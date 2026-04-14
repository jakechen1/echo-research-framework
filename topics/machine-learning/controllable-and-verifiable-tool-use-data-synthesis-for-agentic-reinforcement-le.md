---
title: Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning
created: 2024-05-23
source: https://arxiv.org/abs/2604.09813
tags: [ai, machine-learning, technology, reinforcement-learning, synthetic-data]
---

# Controllable and Verifiable Tool-Use Data Synthesis for Agentic Reinforcement Learning

### Overview
The research introduces **COVERT**, a novel two-stage pipeline designed to bridge the gap between static dataset generation and the dynamic requirements of [[Reinforcement Learning]] (RL). While existing [[Synthetic Data]] methods are optimized for offline [[Supervised Fine-Tuning]] (SFT), training [[Agentic AI]] requires executable environments capable of providing verifiable, reward-checkable feedback during online rollouts.

### The COVERT Pipeline
The COVERT architecture focuses on generating high-fidelity, complex environments through two primary phases:

1.  **Self-Evolving Synthesis:** The first stage utilizes multi-level validation to generate reliable base trajectories. This ensures that the fundamental tool-use patterns are accurate before complexity is introduced.
2.  **Oracle-Preserving Augmentation:** The second stage systematically increases environmental difficulty. Crucially, it uses "oracle-preserving" techniques—meaning that while the environment becomes harder, the underlying ground truth (the correct tool calls and final answers) remains intact. Augmentations include:
    *   **Distractor Tools:** Introducing irrelevant tools to test selection precision.
    *   **Ambiguity:** Crafting indirect or vague user queries.
    *   **Noisy Feedback:** Introducing erroneous or multi-format tool outputs to train error detection.

### Reward Computation and Verifiability
A significant challenge in [[Machine Learning]] for agents is the "reward signal" problem. COVERT enables automatic reward computation via **reference matching** for standard tasks and **judge-assisted verification** for complex behaviors, such as