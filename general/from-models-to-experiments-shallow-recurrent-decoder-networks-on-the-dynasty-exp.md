---
title: "From Models To Experiments: Shallow Recurrent Decoder Networks on the DYNASTY Experimental Facility"
created: 2024-05-22
source: https://arxiv.org/abs/2503.08907
tags: [machine-learning, state-estimation, nuclear-engineering, fluid-dynamics, deep-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "From Models To Experiments: Shallow Recurrent Decoder Networks on the DYNASTY Experimental Facility"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/from-models-to-experiments-shallow-recurrent-decoder-networks-on-the-dynasty-exp.md
dc.language: en
dc.rights: CC-BY-4.0
---

# From Models To Experiments: Shallow Recurrent Decoder Networks on the DYNASTY Experimental Facility

This article explores the implementation of **Shallow Recurrent Decoder** networks within the context of the **DYNASTY Experimental Facility**. These networks represent a novel paradigm in [[pdanse-particle-based-data-driven-nonlinear-state-estimation-from-nonlinear-meas|State Estimation]], specifically designed to synthesize sparse, real-world observations with high-dimensional, model-generated data.

## Overview of Shallow Recurrent Decoder Networks

The Shallow Recurrent Decoder architecture provides several transformative advantages over standard [[Data-Driven Methods]] in complex physical systems. Key features include:

* **Sensor Sparsity:** The ability to reconstruct the full dynamics of a physical system using as few as three sensors, even if they are selected at random.
* **Compressed Training:** The network can be trained on data spanned by a reduced basis, significantly lowering the computational burden.
* **Observable Reconstruction:** A single, easily measurable field variable can be used to reconstruct coupled, spatio-temporal fields that are otherwise unobservable.
* **Low Configuration Overhead:** The architecture requires minimal hyper-parameter tuning compared to traditional [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] models.

## Application to the DYNASTY Facility

While the efficacy of this architecture has been demonstrated in simulated environments (such as modeling [[Nuclear Reactor]] dynamics), applying these models to real-world experimental hardware remains a critical challenge. This work addresses this gap by applying the architecture to the **DYNASTY facility** at Politecnico di Milano.

The DYNASTY facility is designed to study the natural circulation of internally heated fluids, which is a fundamental mechanism for [[Generation IV Nuclear Reactors]], specifically [[Circulating Fuel Reactors]]. 

## Methodology and Validation

To validate the architecture, the study utilizes a dual-approach:
1. **High-Fidelity Simulation:** The **RELAP5** code is employed to generate comprehensive, high-fidelity datasets representing complex fluid dynamics.
2. **Experimental Integration:** Real-time temperature measurements, extracted directly from the DYNASTY facility, are used as inputs for the state estimation process.

The ultimate goal of this research is to provide a rigorous validation of the Shallow Recurrent Decoder architecture for use in large-scale engineering systems, proving its capability to provide accurate, real-time [[graph-neural-ode-digital-twins-for-control-oriented-reactor-thermal-hydraulic-fo|Digital Twin]] capabilities for critical infrastructure.