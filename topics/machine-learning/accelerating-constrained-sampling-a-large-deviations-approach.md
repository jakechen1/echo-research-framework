---
title: Accelerating Constrained Sampling: A Large Deviations Approach
created: 2024-05-22
source: https://arxiv.org/abs/2506.07816
tags: [sampling, Langevin dynamics, large deviations, machine learning, optimization]
category: machine-learning
---

# Accelerating Constrained Sampling: A Large Deviations Approach

The challenge of sampling from a target probability distribution within a constrained domain is a fundamental problem in several computational disciplines, particularly in [[machine learning]] and [[computational statistics]]. When sampling is restricted to a specific subset of a domain, traditional algorithms must be adapted to account for boundary constraints.

## Background: Langevin Dynamics

Existing literature has proposed various methods to handle these constraints, such as **Projected Langevin Monte Carlo (PLMC)**, which is based on the discretization of **Reflected Langevin Dynamics (RLD)**. A more complex evolution of this method is the **Skew-Reflected Non-reversible Langevin Dynamics (SRNLD)**. This approach incorporates a skew-symmetric matrix into the dynamics to leverage non-reversibility, which has the potential to drive the system toward the target distribution more efficiently.

However, a significant practical hurdle remains: determining how to design the skew-symmetric matrix to achieve optimal performance. Without a principled approach to this design, the benefits of non-reversibility may be lost to computational inefficiency.

## The Large Deviations Approach

This paper addresses the design problem by utilizing the [[Large Deviation Principle]] (LDP). The researchers establish an LDP for the empirical measure of SRN