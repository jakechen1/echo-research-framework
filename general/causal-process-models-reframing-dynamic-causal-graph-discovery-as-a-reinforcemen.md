---
title: "Causal Process Models: Reframing Dynamic Causal Graph Discovery as a Reinforcement Learning Problem"
created: 2024-05-24
source: https://arxiv.org/abs/2507.13920
tags: [causal inference, reinforcement learning, world models, graph neural networks, computer vision]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "Causal Process Models: Reframing Dynamic Causal Graph Discovery as a Reinforcement Learning Problem"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/causal-process-models-reframing-dynamic-causal-graph-discovery-as-a-reinforcemen.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Causal Process Models (CPMs)

The paper **"Causal Process Models: Reframing Dynamic Causal Graph Discovery as a Reinforcement Learning Problem"** introduces a novel architecture designed to address the limitations of static [[Causal Inference]] models. Traditional neural models of causality typically assume a fixed, static causal graph. However, this fails to capture the reality of physical environments where causal relationships—such as collisions or attachments between objects—emerge and dissolve dynamically over time.

## Overview of the Causal Process Framework

To bridge this gap, the authors propose the **Causal Process Framework** and its neural implementation, **Causal Process Models (CPMs)**. The core objective is to learn sparse, time-varying causal graphs directly from visual observations. Unlike previous [[openglt-a-comprehensive-benchmark-of-graph-neural-networks-for-graph-level-tasks|Graph Neural Networks]] that rely on dense, permanent connectivity, CPMs explicitly construct causal edges only when objects are actively interacting.

### Reinforcement Learning Integration

The primary innovation lies in treating the construction of dynamic interaction graphs as a [[a-multi-agent-reinforcement-learning-framework-for-public-health-decision-analys|Multi-Agent Reinforcement Learning]] (MARL) problem. In this framework, specialized agents act as decision-makers that sequentially evaluate pairs of objects to determine if a causal connection exists at a specific timestep. This approach allows the model to maintain high [[a-multi-level-causal-intervention-framework-for-mechanistic-interpretability-in-|Interpretability]] by focusing only on relevant, active interactions.

## Technical Innovations

The CPM architecture utilizes a structured representation that factorizes object and force vectors into three learned, semantically meaningful dimensions:

1.  **Mutability**: Captures the capacity for an object's state to change.
2.  **Causal Relevance**: Measures the influence an object exerts on its environment.
3.  **Control Relevance**: Determines the degree of influence an agent can exert over an object.

By decomposing vectors this way, the model achieves automatic discovery of meaningful encodings from raw data, which is essential for robust [[causalvae-as-a-plug-in-for-world-models-towards-reliable-counterfactual-dynamics|World Models]].

## Performance and Results

Empirical evaluations demonstrate that CPMs significantly outperform dense graph baselines on physical prediction tasks. The advantages are most notable in:
*   **Long-horizon prediction**: Maintaining accuracy over extended sequences.
*   **Scalability**: Handling increasing object counts without the computational explosion associated with dense connectivity.
*   **Efficiency**: Leveraging sparsity to reduce the computational overhead of tracking interactions.

This research marks a significant step forward in developing more efficient and biologically inspired models for [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] in complex, dynamic environments.