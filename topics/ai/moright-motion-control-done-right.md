---
title: MoRight: Motion Control Done Right
created: 2024-05-22
source: https://arxiv.org/abs/2604.07348
tags: [video-generation, motion-control, computer-vision, causality]
category: ai
---

# MoRight: Motion Control Done Right

**MoRight** is a unified framework designed to advance the field of [[video-generation]] by introducing high-fidelity, controllable motion dynamics. The framework addresses the critical limitations found in current [[computer-vision]] models, specifically regarding the entanglement of camera movement and the lack of physical causality.

## The Problem: Entanglement and Lack of Causality

Existing video generation methods typically suffer from two primary deficiencies:

1.  **Motion Entanglement**: In many current models, the user's attempt to control an object's movement inadvertently alters the camera's viewpoint. This makes it impossible to adjust the camera angle without disrupting the intended object motion.
2.  **Kinematic Displacement**: Most models treat motion as simple pixel displacement rather than understanding the underlying physics. Consequently, they fail to model **[[motion-causality]]**, where a user-driven action should trigger a coherent, reactive response from other objects in the scene.

## The MoRight Solution

MoRight introduces a dual-pronged approach to solve these issues through **disent