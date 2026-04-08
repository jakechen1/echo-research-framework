---
title: "From Model-Based Screening to Data-Driven Surrogates: A Multi-Stage Workflow for Exploring Stochastic Agent-Based Models"
created: 2024-05-22
source: https://arxiv.org/abs/2604.03350
tags: [Agent-Based Models, Machine Learning, Sensitivity Analysis, Stochasticity, Surrogate Modeling]
category: machine-learning
---

# From Model-Based Screening to Data-Driven Surrogates

The paper "From Model-Based Screening to Data-Driven Surrogates" addresses the fundamental computational challenges involved in the systematic exploration of [[Agent-Based Models (ABMs)]]. As simulations become more complex, researchers face the "curse of dimensionality" and the inherent [[Stochasticity]] of agent-driven systems, making exhaustive parameter sweeps computationally prohibitive.

## The Multi-Stage Pipeline

The authors propose a novel, two-stage automated pipeline designed to bridge the gap between traditional [[Design of Experiments]] and modern [[Machine Learning]] applications. The workflow is structured as follows:

1.  **Model-Based Screening**: The first stage focuses on dimensionality reduction. Through automated screening, the framework identifies dominant variables within the simulation and assesses the variability of outcomes. This process segments the parameter space, effectively filtering out non-essential parameters and reducing the complexity of the simulation environment.
2.  **Machine Learning Surrogates**: Once the parameter space is refined, the pipeline utilizes [[Surrogate Modeling]] techniques. [[Machine Learning]] models are trained on the data generated during the screening phase to map the remaining nonlinear interaction effects.

## Applications and Findings

Using a [[Predator-Prey Model]] as a case study, the researchers demonstrated that this approach can successfully automate the discovery of "unstable regions." These are specific areas within the parameter space where system outcomes are highly sensitive to nonlinear interactions between multiple variables.

## Conclusion

This framework provides modelers with a rigorous, "hands-off" methodology for conducting [[Sensitivity Analysis]] and large-scale policy testing. By integrating statistical screening with predictive ML models, the workflow enables the exploration of high-dimensional, stochastic simulators that were previously too complex for manual investigation. This has significant implications for any field utilizing complex emergent behavior models, including [[Biology]] and [[Technology]] development.