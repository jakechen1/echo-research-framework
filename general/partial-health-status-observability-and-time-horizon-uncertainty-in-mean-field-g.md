---
title: Partial health status observability and time horizon uncertainty in mean-field game epidemiological models
created: 2024-05-22
source: https://arxiv.org/abs/2604.04305
tags: [ai, biology, mathematics]
author: wiki-pipeline
dc.title: "Partial health status observability and time horizon uncertainty in mean-field game epidemiological models"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/partial-health-status-observability-and-time-horizon-uncertainty-in-mean-field-g.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Partial health status observability and time horizon uncertainty in mean-field game epidemiological models

This article discusses recent advancements in modeling epidemic dynamics using [[Mean-Field Games]] (MFG). The research focuses on the complexities of "partial observability," where individuals in a population cannot perfectly track their own immunity levels—a critical factor in how people adjust their behavior during a pandemic.

## Overview of Immunity Dynamics

The study explores two primary modes of immunity failure that impact the decision-making processes of rational, non-infected agents:

1.  **Observable Waning:** A scenario where immunity decreases at a predictable, continuous rate. In this case, individuals can monitor their status and adjust contact rates accordingly.
2.  **Unobservable Loss:** A scenario where immunity disappears instantaneously and without notice. This makes a previously recovered individual susceptible again without their knowledge, significantly complicating the [[Epidemiology]] of the population.

Both scenarios present significant computational challenges. To model these behaviors, an agent must determine optimal contact rates based on their personal current immunity state relative to the changing dynamics of the broader population.

## Mathematical Methodology

The researchers model these interactions using a [[Forward-Backward MFG System]]. This mathematical framework requires the simultaneous resolution of complex [[ae-vit-stable-long-horizon-parametric-partial-differential-equations-modeling|Partial Differential Equations]] (PDEs), specifically:

*   An **Advection-Reaction Equation** to track the distribution of the population based on their immunity structures.
*   A **Hamilton-Jacobi-Bellman (HJB) Equation** to determine the value function, which guides the optimal decision-making of the agents.

## Computational Breakthroughs

Solving high-dimensional PDEs is traditionally computationally expensive. The authors propose an efficient alternative