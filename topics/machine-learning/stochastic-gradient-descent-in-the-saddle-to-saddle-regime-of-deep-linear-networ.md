---
title: Stochastic Gradient Descent in the Saddle-to-Saddle Regime of Deep Linear Networks
created: 2024-05-22
source: https://arxiv.org/abs/2604.06366
tags: [SGD, Deep Learning Theory, Langevin Dynamics, Neural Network Training]
category: machine-learning
---

# Stochastic Gradient Descent in the Saddle-to-Saddle Regime of Deep Linear Networks

## Overview
[[deep-linear-networks|Deep Linear Networks]] (DLNs) serve as vital, analytically tractable models used to investigate the complex training dynamics inherent in larger [[deep-neural-networks|Deep Neural Networks]]. A documented phenomenon in DLNs is the "saddle-to-saddle" transition, where optimization trajectories move between different saddle points. While the behavior of deterministic [[multirate-stein-variational-gradient-descent-for-efficient-bayesian-sampling|Gradient Descent]] in this regime is well-understood, the precise impact of the stochastic noise introduced by [[stochastic-gradient-descent-in-the-saddle-to-saddle-regime-of-deep-linear-networ|Stochastic Gradient Descent]] (SGD) on these dynamics has remained a significant unknown in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] theory.

## Theoretical Framework
This research investigates the dynamics of SGD specifically during the training phase within the saddle-to-saddle regime. The authors model the training progression as [[stochastic-langevin-dynamics|Stochastic Langevin Dynamics]], characterized by anisotropic and state-dependent noise. 

By applying the mathematical assumption that weights are both aligned and balanced, the study derives an exact decomposition of the network's dynamics. This process reduces the complex multidimensional problem into a simplified system of one-dimensional, per-mode [[stochastic-differential-equations|Stochastic Differential Equations]] (SDEs).

## Key Findings
The study provides several critical insights into the relationship