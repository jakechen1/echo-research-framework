---
title: Generative optimal transport via forward-backward HJB matching
created: 2024-05-22
source: https://arxiv.org/abs/2604.07762
tags: [generative_models, optimal_transport, stochastic_control, hjb_equation, machine_learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Generative optimal transport via forward-backward HJB matching"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/generative-optimal-transport-via-forward-backward-hjb-matching.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Generative optimal and backward HJB matching

The research paper, "Generative optimal transport via forward-backward HJB matching," introduces a mathematical framework for controlling the evolution of many-body stochastic systems. Specifically, it addresses the problem of driving a system from a disordered reference state to a structured target ensemble, a task fundamental to [[generative-modeling-of-granular-flow-on-inclined-planes-using-conditional-flow-m|Generative Modeling]] and [[fast-and-interpretable-protein-substructure-alignment-via-optimal-transport|Optimal Transport]].

## The Problem of Reversing Relaxation

In statistical mechanics, natural relaxation—driven by diffusion—typically moves from a structured target toward a disordered state. The core scientific question addressed here is how to identify the minimum-work stochastic process that reverses this relaxation. 

The primary computational hurdle in such problems is that computing the optimal process usually requires pre-existing knowledge of trajectories that already sample