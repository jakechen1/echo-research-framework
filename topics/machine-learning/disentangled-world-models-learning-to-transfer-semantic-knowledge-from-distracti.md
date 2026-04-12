---
title: Disentangled World Models: Learning to Transfer Semantic Knowledge from Distracting Videos for Reinforcement Learning
created: 2024-05-22
source: https://arxiv.org/abs/2503.08751
tags: [ai, machine-learning, reinforcement-learning, representation-learning, computer-vision]
category: [ai, machine-learning]
---

# Disentangled World Models (DisWM)

The paper **"Disentangled World Models: Learning to Transfer Semantic Knowledge from Distracting Videos for Reinforcement Learning"** addresses a fundamental bottleneck in [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL): low [[sample-efficiency|Sample Efficiency]] in environments subject to significant variations. While [[disentangled-representation-learning|Disentangled Representation Learning]] has been proposed to help agents manage these variations, existing methods typically lack prior knowledge of the world, starting their learning process from scratch.

## Overview of DisWM

The authors introduce **Disentangled World Models (DisWM)**, an interpretable, model-based RL framework designed to bridge the gap between passive visual observation and active environmental interaction. The core innovation lies in the ability to extract and transfer semantic knowledge from "distracting" videos—sequences that may not contain task-specific actions but offer rich, underlying semantic variations.

## Methodology

The DisWM framework operates through a multi-stage pipeline involving **[[latent-distillation|Latent Distillation]]** and flexible constraints:

1.  **Offline Pretraining**: The process begins with an action-free video prediction model trained on unlabeled, distracting videos. By using disentanglement regularization, the model learns to identify and separate underlying semantic features without the need for explicit task rewards or actions.
2.  **Knowledge Transfer**: The semantic intelligence captured during the offline phase is transferred to a functional [[causalvae-as-a-plug-in-for-world-models-towards-reliable-counterfactual-dynamics|World Model]] via latent distillation. This allows the agent to start its learning process with a pre-existing understanding of environmental dynamics.
3.  **Online Adaptation**: During the online phase, the agent interacts with the target environment, incorporating actual actions and rewards. This interaction enriches the data diversity, which serves to further strengthen the model's disentangled representation through adaptive constraints.

## Conclusion

By leveraging semantic knowledge from non-task-specific video data, DisWM provides a pathway for agents to achieve superior performance in complex, non-stationary environments. Experimental results validate that this approach outperforms traditional benchmarks, demonstrating the power of using large-scale, unstructured visual data to bootstrap effective [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] agents.