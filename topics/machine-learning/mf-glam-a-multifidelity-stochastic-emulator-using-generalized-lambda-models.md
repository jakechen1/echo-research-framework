---
title: MF-GLaM: A multifidelity stochastic emulator using generalized lambda models
created: 2024-05-22
source: https://arxiv.org/abs/2507.10303
tags: [machine-learning, stochastic-emulation, surrogate-modeling, multifidelity]
category: machine-learning
---

# MF-GLaM: A multifidelity stochastic emulator using generalized lambda models

The **MF-GLaM** (Multifidelity Generalized Lambda Models) framework introduces a specialized approach to [[hybrid-fourier-neural-operator-for-surrogate-modeling-of-laser-processing-with-a|surrogate modeling]] for [[stochastic-simulators|stochastic simulators]]. In many scientific disciplines, simulators exhibit intrinsic stochasticity caused by unobservable or unmodeled input variables. This results in random outputs even when input conditions remain fixed, making it difficult for traditional deterministic modeling techniques to predict the full [[probability-distribution|probability distribution]] of the outcomes.

## The Challenge of Stochastic Emulation

Accurately characterizing the response distribution of a simulator is computationally intensive. While [[high-fidelity-data|high-fidelity data]] provides the most accurate representation, acquiring enough samples to map the entire distribution is often prohibitively expensive. Traditional [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] approaches often struggle to capture the nuances of the conditional response distribution without massive datasets.

## The MF-GLaM Approach

MF-GLaM addresses this by implementing a [[multifidelity-modeling|multifidelity modeling]] framework. The method aims to enhance limited high-fidelity information by exploiting available data from [[low-fidelity-data|low-fidelity data]] sources. 

The architecture is built upon the **Generalized Lambda Model** (GLaM), which utilizes a flexible, four-parameter [[generalized-lambda-distribution|generalized lambda distribution]] to represent the conditional distribution at each input point. Key features of the MF-GLaM method include:

*   **Non-intrusive implementation:** The model does not require access to the internal stochastic mechanisms of the underlying simulator.
*   **Data efficiency:** It eliminates the need for multiple replications of the same input values, which is a common requirement in traditional stochastic modeling.
*   **Cost-effective scaling:** It leverages lower-fidelity models to augment the predictive power of higher-fidelity models.

## Experimental Results

The efficacy of MF-GLaM has been demonstrated through synthetic complexity tests and a practical application in earthquake modeling. The results indicate that MF-GLaM can achieve higher accuracy than single-fidelity GLaMs at an equivalent computational cost. Furthermore, it can maintain comparable performance levels while significantly reducing the total computational budget, making it a vital tool for complex scientific simulations.