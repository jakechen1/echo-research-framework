---
title: "Generation time in a discrete epidemic model with asymptomatic carriers: beyond geometric waiting times"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.07309"
tags: [epidemiology, mathematical-modeling, transmission-dynamics, infectious-disease]
category: biology
---

# Generation time in a discrete epidemic model with asymptomatic carriers: beyond geometric waiting times

This research introduces a sophisticated approach to calculating the intervals between successive cases in a transmission chain of [[infectious-diseases|Infectious Diseases]]. Moving away from traditional [[markovian-processes|Markovian processes]] that rely on simplified geometric waiting times, the paper presents a non-Markovian, discrete-time [[analysis-of-non-pharmaceutical-interventions-with-sir-epidemic-models-decreasing|Epidemic Model]] capable of accounting for complex transmission dynamics involving asymptomatic carriers.

## Model Architecture

The proposed model utilizes a compact recursive system to track infectiousness across three primary stages of infection:
1.  [[latent-period|Latent Period]]
2.  [[asymptomatic-phase|Asymptomatic Phase]]
3.  [[symptomatic-phase|Symptomatic Phase]]

A key innovation of this model is the recognition of variable infectiousness. The researchers account for fluctuations in the ability to transmit the pathogen both across different stages of the infection and along the elapsed time within each individual phase.

## Mathematical Derivations

By mathematically rearranging the terms of the [[basic-reproduction-number|Basic Reproduction Number]] ($R_0$)—specifically considering an asymptomatic primary case who may or may not eventually develop symptoms—the authors derived the probability distribution for the [[generation-time-in-a-discrete-epidemic-model-with-asymptomatic-carriers-beyond-g|Generation Time]]. 

The study yields several significant mathematical insights:
*   **Expected Value:** The expected generation time is calculated as a convex combination of the expected generation times occurring before and after the onset of symptoms.
*   **Moment Analysis:** The $n$-th moment of the generation time is mathematically linked to the moments (up to the $n$-th order) of the weighted forward recurrence time at each phase, as well as the moments of the latent and incubation periods. These relationships are weighted by the specific infectiousness of each transmission phase.

## Empirical Simulations

The researchers validated the model using several data-driven epidemic scenarios. To represent the waiting times accurately, they employed [[discrete-weibull-distributions|Discrete Weibull Distributions]]. The analysis of various diseases demonstrated that, with the exception of [[measles|Measles]], most investigated pathogens exhibit moderate variability in their respective generation time distributions. This findings suggest that the model provides a more robust framework for [[epidemiology|Epidemiology]] than models assuming constant or geometrically distributed intervals.