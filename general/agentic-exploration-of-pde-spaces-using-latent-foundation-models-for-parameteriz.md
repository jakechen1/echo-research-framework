---
title: Agentic Exploration of PDE Spaces using Latent Foundation Models for Parameterized Simulations
created: 2024-05-22
source: https://arxiv.org/abs/2604.09584
tags: [ai, machine-learning, physics, simulation, automation]
category: ai, machine-learning, technology
author: wiki-pipeline
dc.title: "Agentic Exploration of PDE Spaces using Latent Foundation Models for Parameterized Simulations"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/agentic-exploration-of-pde-spaces-using-latent-foundation-models-for-parameteriz.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Agentic Exploration of PDE Spaces

The paper "Agentic Exploration of PDE Spaces using Latent Foundation Models for Parameterized Simulations" addresses the fundamental challenge of exploring high-dimensional, continuous, and chaotic physical phenomena governed by [[Partial Differential Equations]] (PDEs). Traditionally, the exploration of these spatiotemporal solution spaces has relied on expensive [[Computational Fluid Dynamics]] (CFD) simulations or physical laboratory experiments, which lack the scalability found in discrete domains like [[drug discovery]].

## Methodology

The researchers propose a novel framework that integrates multi-agent [[Large Language Models]] (LLMs) with [[Latent Foundation Models]] (LFMs). The core innovation lies in using the LFM as an on-demand surrogate simulator. This generative model learns compact and disentangled latent representations of flow fields, effectively allowing the continuous parameter space of a PDE to be explored through a differentiable or easily queryable latent manifold.

The system utilizes a hierarchical agent architecture designed for [[Automated Scientific Discovery]]. The agents operate in a closed-loop cycle consisting of:
1. **Hypothesis Generation**: Formulating scientific predictions based on existing data.
2. **Experimentation**: Using the LFM to query arbitrary parameter configurations and boundary conditions.
3. **Analysis**: Interpreting the resulting flow field characteristics.
4. **Verification**: Refining or discarding hypotheses through iterative testing.

This tool-modular interface requires minimal human intervention, allowing the agents to autonomously navigate complex physics landscapes.

## Experimental Results

The framework was validated using the study of flow past tandem cylinders at $Re = 500$. The agentic system autonomously evaluated over 1,600 parameter-location pairs, leading to the discovery of significant physical scaling laws:
* **Two-mode structure**: A regime-dependent pattern observed for minimum displacement thickness.
* **Linear scaling**: A robust relationship discovered for maximum momentum thickness.

Notably, the agents identified a dual-extrema structure that emerges during the transition from the near-wake to the co-shedding regime.

## Significance

By coupling learned physical representations with agentic reasoning, this research establishes a new paradigm for [[Machine Learning]] in the physical sciences. It demonstrates that [[Artificial Intelligence]] can move beyond simple pattern recognition to actively participate in the complex reasoning required for understanding continuous, complex dynamical systems.