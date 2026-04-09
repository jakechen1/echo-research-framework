---
title: VertAX: a differentiable vertex model for learning epithelial tissue mechanics
created: 2024-05-22
source: https://arxiv.org/abs/2604.06896
tags: [VertAX, JAX, Epithelial Tissue, Differentiable Programming, Morphogenesis, Inverse Design]
category: machine-learning, biology, technology
---

# VertAX

**VertAX** is a specialized computational framework designed for the differentiable modeling of confluent [[Epithelial Tissues]] using a [[Vertex Model]] approach. Built on the [[JAX]] library, the framework provides researchers with the tools to simulate and learn the complex mechanical interactions that drive tissue-scale reshaping and [[Morphogenesis]].

## Overview

Traditional vertex models are highly effective at capturing the local mechanical interactions among cells. However, these models often involve a vast array of tunable parameters, making the processes of [[Parameter Inference]] and optimization computationally intensive. VertAX addresses this by introducing a framework that supports **automatic differentiation**, **GPU acceleration**, and **end-to-end bilevel optimization**. 

Because VertAX is implemented using pure Python, it allows for the definition of arbitrary energy and cost functions. This flexibility enables seamless integration with existing [[Machine Learning]] pipelines, allowing researchers to move between forward simulation and inverse mechanical design within a single unified ecosystem.

## Core Functionalities

The developers demonstrate the utility of VertAX across three representative computational tasks:

1.  **Forward Modeling:** Simulating the dynamic, time-dependent reshaping of tissues during development.
2.  **Mechanical Parameter Inference:** Utilizing experimental data to back-calculate the underlying physical properties of a tissue.
3.  **Inverse Design:** The optimization of mechanical parameters to achieve specific, pre-defined tissue-scale behaviors.

## Technical Contributions

A key highlight of the research is the benchmarking of three distinct differentiation strategies:
*   **Automatic Differentiation:** Standard gradient computation used in modern deep learning.
*   **Implicit Differentiation:** A method focused on gradients through steady-state or equilibrium systems.
*   **Equilibrium Propagation:** A strategy that approximates gradients using repeated forward, adjoint-free simulations.

The study demonstrates that [[Equilibrium Propagation]] can effectively approximate gradients, providing a vital pathway for extending complex, inverse biophysical problems to non-differentiable simulators with minimal additional engineering effort. This bridges the gap between high-fidelity [[Cell Biology]] simulations and gradient-based optimization.