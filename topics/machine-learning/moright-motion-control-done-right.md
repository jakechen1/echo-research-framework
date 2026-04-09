---
title: MoRight: Motion Control Done Right
created: 2024-05-22
source: https://arxiv.org/abs/2604.07348
tags: [video-generation, computer-vision, causality, motion-control]
categories: [ai, machine-learning, technology]
---

# MoRight: Motion Control Done Right

**MoRight** is a novel unified framework designed to advance the state of the art in [[Video Generation]] and [[Motion Control]]. The framework specifically addresses the persistent challenges of maintaining physical plausibility and user agency when generating motion-driven video content.

## The Problem: Entanglement and Lack of Causality

Current methodologies in [[Computer Vision]] often suffer from two critical limitations when handling user-specified actions:

1.  **Motion Entanglement**: Existing models frequently treat camera movement and object motion as a single, inseparable tracking signal. This makes it nearly impossible for a user to adjust the camera viewpoint without inadvertently altering the trajectory of the objects within the scene.
2.  **Kinematic Displacement vs. Causality**: Many models treat motion as simple pixel displacement. They lack an understanding of **Causality**, meaning they fail to model how an initial movement (e.g., a ball hitting a glass) should trigger a coherent reaction from other objects in the environment.

## The MoRight Solution

MoRight introduces a dual-pronged approach to solve these issues through **disentangled motion modeling**.

### Disentangled Control
MoRight specifies object motion within a canonical static view. Using **temporal cross-view attention**, the framework transfers this motion to any arbitrary target camera viewpoint. This allows for precise, independent control over both the object's trajectory and the camera's perspective.

### Motion Decomposition
The framework decomposes motion into two distinct components:
*   **Active Components**: The primary, user-driven actions.
*   **Passive Components**: The resulting physical consequences or reactions from the environment.

## Inference Capabilities

By modeling the relationship between active and passive motion, MoRight enables two revolutionary modes of [[Artificial Intelligence]] inference:

*   **Forward Reasoning**: Users supply an active motion (e.g., "a hand pushes a cup"), and MoRight predicts the resulting physical consequences (e.g., "the cup tips over and spills").
*   **Inverse Reasoning**: Users specify a desired passive outcome (e.g., "a glass breaking"), and MoRight recovers the plausible driving actions required to cause that outcome.

## Performance

Evaluations across three industry benchmarks demonstrate that MoRight achieves state-of-the-art performance. The model outperforms existing architectures in generation quality, motion controllability, and, most importantly, **interaction awareness**.