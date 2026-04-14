---
title: Training event-based neural networks with exact gradients via Differentiable ODE Solving in JAX
created: 2024-05-22
source: https://arxiv.org/abs/2603.08146
tags: [Eventax, JAX, Spiking Neural Networks, ODE Solvers, Neuro-inspired Computing]
categories: [ai, machine-learning, neuroscience, technology]
author: wiki-pipeline
dc.title: "Training event-based neural networks with exact gradients via Differentiable ODE Solving in JAX"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/training-event-based-neural-networks-with-exact-gradients-via-differentiable-ode.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Training event-based neural networks with exact gradients via Differentiable ODE Solving in JAX

The paper "Training event-based neural networks with exact gradients via Differentiable ODE Solving in JAX" introduces **Eventax**, a novel computational framework designed to overcome the fundamental limitations of current [[threshold-modulation-for-online-test-time-adaptation-of-spiking-neural-networks|Spiking Neural Networks]] (SNNs) training methodologies.

### The Gradient Trade-off
Historically, gradient-based training for event-based networks has faced a critical dichotomy between two approaches:

1.  **Discrete-time methods**: These utilize [[Surrogate Gradients]] to support arbitrary neuron models, but they introduce gradient bias and constrain spike-time resolution due to fixed time-stepping.
2.  **Continuous-time methods**: These provide exact gradients but are restricted to mathematically simple neuron types (such as the [[Leaky Integrate and Fire (LIF)]] model) because they require analytical expressions for spike times and state evolution.

### The Eventax Framework
Eventax resolves this tension by combining [[Differentiable ODE Solvers]] with event-based spike handling. Built on the [[JAX]] ecosystem and utilizing [[Diffrax]] solvers, the framework computes gradients that are exact with respect to the forward simulation for any neuron model defined by [[Ordinary Differential Equations]] (ODEs).

The framework provides a streamlined API, allowing researchers to specify only the essential components of a model:
*   Neuron dynamics.
*   Spike conditions.
*   Reset rules.

### Biological Fidelity and Benchmarking
Eventax demonstrates significant modeling flexibility, supporting a wide range of architectures and neuron models, including [[Quadratic Integrate-and-fire (QIF)]], [[Exponential integrate-and-fire (EIF)]], [[Izhikevich]], and the [[Event-based Gated Recurrent Unit (EGRU)]]. 

The framework’s utility was demonstrated across multiple benchmarks, including [[MNIST]] and [[Yin-Yang]]. Furthermore, Eventax supports highly complex biological simulations, such as multi-compartment neurons that incorporate models of dendritic spikes found in human layer 2/3 cortical pyramidal neurons. This capability bridges the gap between high-level [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] optimization and high-fidelity [[Neuroscience]] modeling.