---
title: Isokinetic Flow Matching for Pathwise Straightening of Generative Flows
created: 2024-05-22
source: https://arxiv.org/abs/2604.04491
tags: [generative-models, flow-matching, regularization, sampling-efficiency]
category: machine-learning
---

# Isokinetic Flow Matching for Pathwise Straightening of Generative Flows

In the evolving landscape of [[Generative AI]], [[Flow Matching]] (FM) has emerged as a powerful framework for constructing linear conditional probability paths. However, a fundamental limitation persists: the learned marginal velocity field inevitably exhibits strong curvature. This curvature is an inherent result of trajectory superposition, where overlapping paths create complex dynamics. This phenomenon introduces significant numerical truncation errors during discretization, which serves as a major bottleneck for high-speed, few-step sampling in [[Diffusion Models]].

To address this challenge, the paper introduces [[Isokinetic Flow Matching]] (Iso-FM). This method serves as a lightweight, Jacobian-free dynamical regularizer designed specifically for the pathwise straightening of [[Generative Flows]]. The primary goal of Iso-FM is to penalize pathwise acceleration, thereby reducing the complexity