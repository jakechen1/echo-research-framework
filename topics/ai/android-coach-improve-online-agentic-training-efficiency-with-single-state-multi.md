---
title: Android Coach: Improve Online Agentic Training Efficiency with Single State Multiple Actions
created: 2024-05-22
source: https://arxiv.org/abs/2604.07277
tags: [android, reinforcement-learning, agentic-training, efficiency, mobile-agents]
category: ai
---

# Android Coach

**Android Coach** is a specialized framework designed to optimize the training of [[Android Agents]] through enhanced [[Reinforcement Learning]] (RL) efficiency. The primary challenge addressed by this research is the prohibitive cost of online training, which is driven by the high latency of mobile emulators and the inherent sample inefficiency of current algorithmic paradigms.

### The Problem: Single State Single Action Bottleneck
Most existing training approaches utilize a **Single State Single Action** paradigm. In this model, the policy is updated using one-to-one state-action pairs gathered from linear, one-way rollouts. This method fails to fully exploit the potential of each expensive emulator state, as the agent moves to a new state immediately after a single action, leaving the potential value of alternative actions for that same state unexamined.

### The Solution: Single State Multiple Actions
Android Coach introduces a shift to a **Single State Multiple Actions** paradigm. This framework allows an agent to sample and evaluate multiple potential actions for a single, captured emulator state. To prevent the need for additional emulator overhead (which would negate the efficiency gains), the framework employs a learned **critic** to estimate the values of these various actions.

To maintain the accuracy of this training signal, the researchers implemented two key components:
1.  **Process Reward Model**: Integrated to ensure the critic serves as a reliable "coach" for the agent.
2.  **Group-wise Advantage Estimator**: A mechanism based on averaged critic outputs used to stabilize policy updates.

### Experimental Results
The effectiveness of Android Coach has been validated through extensive testing against state-of-the-art models. Key achievements include:
*   **Success Rate Improvements**: Achieved a 7.5% increase on **AndroidLab** and an 8.3% increase on **AndroidWorld** compared to UI-TARS-1.5-7B.
*   **Training Efficiency**: Demonstrated a **1.4x higher training efficiency** compared to standard [[Reinforcement Learning]] algorithms such as [[PPO]] and [[GRPO]] when matched at equivalent success rates.

By maximizing the utility of every interaction within the emulator, Android Coach provides a scalable pathway for developing complex, autonomous mobile agents.