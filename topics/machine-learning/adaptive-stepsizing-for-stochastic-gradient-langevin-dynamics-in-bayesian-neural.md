---
title: Adaptive Stepsizing for Stochastic Gradient Langevin Dynamics in Bayesian Neural Networks
created: 2024-05-23
source: https://arxiv.org/abs/2511.11666
tags: [SGLD, Bayesian Neural Networks, MCMC, Machine Learning, SamAdams]
category: machine-learning
---

# Adaptive Stepsizing for Stochastic Gradient Langevin Dynamics in Bayesian Neural Networks

The research paper "Adaptive Stepsizing for Stochastic Gradient Langevin Dynamics in Bayesian Neural Networks" introduces **SA-SGLD**, a novel algorithmic approach designed to optimize the efficiency of [[Stochastic Gradient Langevin Dynamics]] (SGLD) within the framework of [[Bayesian Neural Networks]] (BNNs).

## Problem Statement

A primary challenge in [[Bayesian Inference]] for large-scale models is the ability to accurately approximate the [[Posterior Distribution]] over parameters. While [[Stochastic Gradient Markov Chain Monte Carlo]] (SGMCMC) methods offer scalability, they are notoriously sensitive to the choice of stepsize. Existing adaptive variants, such as [[pSGLD]], often face a significant trade-off: they can achieve adaptation but frequently fail to sample the correct invariant measure unless expensive and computationally costly divergence correction terms are implemented.

## The SA-SGLD Innovation

Building upon the recently proposed **SamAdams** framework for timestep adaptation, the authors present **SA-SGLD**. This method utilizes a technique known as **time rescaling** to modulate the stepsize dynamically. By monitoring a specific quantity—most commonly the local gradient norm—the algorithm can sense the geometry of the loss landscape.

The mechanism functions as follows:
* **High Curvature Regions:** The algorithm automatically shrinks the stepsize to maintain stability and prevent divergence.
* **Flat Regions:** The algorithm expands the stepsize to accelerate movement through the parameter space, improving the mixing rate.

Crucially, SA-SGLD achieves this adaptation without introducing the algorithmic bias that typically plagues other adaptive [[SGMCMC]] variants, ensuring that the samples remain representative of the true target distribution.

## Experimental Results

The effectiveness of SA-SGLD was validated through several testing environments:
1. **2D Toy Examples:** The method demonstrated superior accuracy in sampling from distributions characterized by high curvature compared to standard SGLD.
2. **Image Classification:** In complex tasks involving BNNs with sharp priors, SA-SGLD showed improved performance and stability.

This advancement represents a significant step forward in making [[Machine Learning]] uncertainty estimation more robust and computationally efficient for high-dimensional data.