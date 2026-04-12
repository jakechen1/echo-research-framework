---
title: Rectified Schrödinger Bridge Matching for Few-Step Visual Navigation
created: 2024-05-22
source: https://arxiv.org/abs/2604.05673
tags: [RSBM, Visual Navigation, Schrödinger Bridge, Embodied AI, Robotics]
category: machine-learning
---

# Rectified Schrödinger Bridge Matching for Few-Step Visual Navigation

The paper "Rectified Schrödinger Bridge Matching for Few-Step Visual Navigation" introduces a novel framework designed to address the latency bottleneck in [[towards-provable-probabilistic-safety-for-scalable-embodied-ai-systems|Embodied AI]]. While generative models like [[diffhdr-re-exposing-ldr-videos-with-video-diffusion-models|Diffusion Models]] and [[schrdinger-bridges|Schrödinger Bridges]] (SB) are excellent at capturing the multi-modal distributions necessary for complex [[robotic-control|Robotic Control]], they typically require a high number of integration steps to ensure accuracy. This computational overhead poses a critical barrier to real-time autonomous navigation.

### The RSBM Framework

The authors propose **Rectified Schrödinger Bridge Matching (RSBM)**. The core innovation lies in exploiting a shared velocity-field structure between standard Schrödinger Bridges ($\varepsilon=1$, representing maximum-entropy transport) and deterministic [[fast-and-interpretable-protein-substructure-alignment-via-optimal-transport|Optimal Transport]] ($\varepsilon\to 0$, similar to [[conditional-flow-matching-for-physics-constrained-inverse-problems-with-finite-t|Conditional Flow Matching]]). This transition is controlled by a single entropic regularization parameter, $\varepsilon$.

The research establishes two fundamental properties that enable this efficiency:

1.  **Velocity Structure Invariance**: The conditional velocity field maintains the same functional form across the entire $\varepsilon$ spectrum. This allows a single neural network to effectively serve all regularization strengths.
2.  **Variance Reduction**: The authors prove that reducing $\varepsilon$ linearly decreases the conditional velocity variance. This reduction enables much more stable and efficient [[ordinary-differential-equation|Ordinary Differential Equation]] (ODE) integration.

### Performance and Impact

RSBM utilizes a learned conditional prior to shorten the transport distance, operating at an optimized intermediate $\varepsilon$ that balances multi-modal coverage with path straightness. 

Empirical evaluations demonstrate that while standard bridges require 10 or more integration steps to converge, RSBM achieves a **92% success rate** and over **94% cosine similarity** using only **3 integration steps**. Crucially, this performance is achieved without the need for complex distillation or multi-stage training. This advancement significantly narrows the gap between high-fidelity generative policies and the low-latency demands of real-world robotic deployment.