---
title: Grokking as Dimensional Phase Transition in Neural Networks
created: 2024-05-22
source: https://arxiv.org/abs/2604.04655
tags: [grokking, neural-networks, phase-transition, machine-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Grokking as Dimensional Phase Transition in Neural Networks"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/grokking-as-dimensional-phase-transition-in-neural-networks.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Grokking as Dimensional Phase Transition in Neural Networks

[[grokking-as-dimensional-phase-transition-in-neural-networks|Grokking]] refers to a phenomenon in [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]] where a model undergoes an abrupt, sudden transition from simple memorization of training labels to the achievement of [[a-canonical-generalization-of-obdd|Generalization]]. This phenomenon is often difficult to predict via standard training loss metrics, as the transition occurs long after the training error has plateaued.

## The Dimensional Phase Transition
Recent research (arXiv:2604.04655) characterizes the grokking process as a **dimensional phase transition**. By utilizing finite-size scaling of gradient avalanche dynamics across eight distinct model scales, the study identifies a fundamental shift in the effective dimensionality ($D$) of the learning process.

The researchers found that:
*   **Sub-critical Phase:** During the initial memorization stage, the system is sub-diffusive, characterized by $D < 1$.
*   **Super-critical Phase:** At the onset of generalization, the system shifts to a super-diffusive state, characterized by $D > 1$.

This transition exhibits hallmarks of [[Self-Organized Criticality]] (SOC), suggesting that the sudden leap in model performance is a systemic structural shift rather than a gradual refinement of weights.

## Gradient Field Geometry vs. Architecture
A key contribution of this study is the decoupling of the transition from specific [[Neural Network Architecture]] designs. The researchers demonstrated that the observed dimensionality $D$ is a property of the **gradient field geometry** rather than the underlying graph topology. 

To prove this, the study compared real training dynamics against synthetic i.i.d. Gaussian gradients. While the synthetic gradients maintained a stable $D \approx 1$ regardless of the network's structure, real training via [[Backpropagation]] exhibited "dimensional excess." This implies that the correlations generated during the backpropagation process are the primary drivers of the dimensional shift.

## Implications for Artificial Intelligence
These findings provide new insights into the [[Trainability]] of [[Overparameterized Networks]]. By identifying the geometric drivers of the transition, researchers may be able to better predict the onset of generalization and develop new optimization strategies to bypass the prolonged memorization phase in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]-driven [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models.