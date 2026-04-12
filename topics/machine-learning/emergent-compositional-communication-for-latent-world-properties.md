---
title: Emergent Compositional Communication for Latent World Properties
created: 2024-05-22
source: https://arxiv.org/abs/2604.03266
tags: [multi-agent-systems, representation-learning, self-supervised-learning, computer-vision]
category: ai, machine-learning
---

# Emergent Compositional Communication for Latent World Properties

The research paper **"Emergent Compositional Communication for Latent World Properties"** investigates the ability of [[strategic-persuasion-with-trait-conditioned-multi-agent-systems-for-iterative-le|Multi-Agent Systems]] to extract discrete, compositional representations of unobservable physical properties from frozen video features. The study explores whether communication pressure alone can force agents to encode latent attributes—such as [[elasticity|Elasticity]], friction, and mass ratio—without explicit supervision or property labels.

## Methodology
The researchers employed a [[gumbel-softmax|Gumbel-Softmax]] bottleneck to mediate communication between agents. Through a process of [[iterated-learning|Iterated Learning]], the agents developed protocols that are "positionally disentangled," meaning different parts of the message correspond to specific physical attributes. The study utilized frozen video backbones to observe how pre-existing [[self-supervised-learning|Self-Supervised Learning]] features influence the emergence of communication.

## Key Findings
* **High Compositionality:** In configurations with four agents, 100% of experimental seeds achieved near-perfect compositionality (PosDis=0.999), demonstrating that the communication structure is highly robust.
* **The Role of Perceptual Priors:** The choice of vision backbone significantly impacts communicable information. [[dinov2|DINOv2]] was found to be superior for spatially-oriented tasks (e.g., ramp physics), whereas [[v-jepa-2|V-JEPA 2]] dominated in tasks requiring an understanding of dynamics (e.g., collision physics). This suggests that the [[perceptual-prior|Perceptual Prior]] of the