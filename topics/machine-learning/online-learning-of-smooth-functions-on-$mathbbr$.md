---
title: Online learning of smooth functions on $\mathbb{R}$
created: 2024-05-22
source: https://arxiv.org/abs/2604.03525
tags: [online learning, function estimation, adversarial learning, mathematical analysis]
category: machine-learning
---

# Online learning of smooth functions on $\mathbb{R}$

The research paper "Online learning of smooth functions on $\mathbb{R}$" investigates the theoretical limits of [[adversarial online learning]] when estimating real-valued functions over an infinite domain. The study focuses on smooth function classes, denoted as $\mathcal{G}_q$, where the $L^q$ norm of the function's derivative is bounded.

## The Problem of Ill-Posedness
A central contribution of this work is the discovery that the standard model of online regression is inherently ill-posed on the unbounded real line $\mathbb{R}$. The authors demonstrate that for any $p \ge 1$ and $q > 1$, an adversary can strategically select a sequence of queries $x_t$ to force the cumulative $p$-loss to diverge to infinity. This instability arises because the adversary can exploit the "smoothness" of the function class by placing queries in regions far from all previous observations, making error control impossible under standard conditions.

## Proposed Learning Scenarios
To address this obstruction, the paper analyzes three modified learning frameworks designed to limit the influence of queries that are spatially isolated from the existing dataset