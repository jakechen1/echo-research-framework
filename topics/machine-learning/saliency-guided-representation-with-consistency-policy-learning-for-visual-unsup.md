---
title: Saliency-Guided Representation with Consistency Policy Learning for Visual Unsupervised Reinforcement Learning
created: 2024-05-23
source: https://arxiv.org/abs/2604.05931
tags: [reinforcement-learning, unsupervised-learning, computer-vision, robotics]
category: [ai, machine-learning]
---

# Saliency-Guided Representation with Consistency Policy Learning (SRCP)

The paper introduces **Saliency-Guided Representation with Consistency Policy Learning (SRCP)**, a novel framework designed to enhance [[Unsupervised Reinforcement Learning]] (URL) in high-dimensional, visual environments. The research specifically targets the limitations of [[Successor Representations (SR)]], a prominent paradigm used to build generalist agents capable of [[Zero-shot Generalization]] to unseen tasks without additional supervision.

## The Problem: Scaling SR to Visual Environments

While [[Successor Representations]] are highly effective in low-dimensional, structured settings, they face significant hurdles when applied to complex [[Computer Vision]] tasks. The authors identify two primary bottlenecks in existing visual SR methods:

1.  **Suboptimal Representations**: Standard SR objectives often fail to distinguish between critical environmental dynamics and irrelevant background noise. This leads to representations that attend to "dynamics-irrelevant" regions, resulting in inaccurate successor measures and degraded performance during task generalization.
2.  **Policy Modeling Difficulties**: Flawed representations hinder the ability of SR-based policies to model multi-modal, skill-conditioned action distributions. This makes it difficult to ensure high levels of [[Skill Controllability]] within the agent.

## The SRCP Solution

To overcome these challenges, the SRCP framework proposes a specialized architecture that decouples representation learning from successor training. The framework