---
title: Operator Learning for Surrogate Modeling of Wave-Input Forces from Sea Surface Waves
created: 2024-05-22
source: https://arxiv.org/abs/2604.06433
tags: [DeepONet, Surrogate Modeling, SWAN, Hydrodynamics, Oceanography, Machine Learning]
category: machine-learning
---

# Operator Learning for Surrogate Modeling of Wave-Induced Forces from Sea Surface Waves

The prediction of [[storm-surge-prediction|Storm Surge Prediction]] and changes in water elevation relies heavily on understanding "wave setup"—the process by which wave-induced energy transfers to currents. A critical component of this process is the calculation of **radiation stress**, which introduces momentum flux into circulation models. Traditionally, achieving accuracy requires coupling circulation models with complex [[numerical-wave-models|Numerical Wave Models]] such as **SWAN** (Simulating WAves Nearshore). However, the extreme computational cost of these numerical models often forces researchers to run wave models at much coarser temporal resolutions than circulation models, leading to potential inaccuracies in coupled simulations.

## The DeepONet Approach

This research investigates the implementation of [[deep-operator-networks|Deep Operator Networks]] (DeepONets) as a high-efficiency [[hybrid-fourier-neural-operator-for-surrogate-modeling-of-laser-processing-with-a|Surrogate Modeling]] alternative to the SWAN model. Unlike standard neural networks that map vectors to vectors, DeepONets are designed to learn operators, allowing them to approximate continuous mappings between function spaces. This capability is essential for replacing complex physical solvers in the field of [[hydrodynamics|Hydrodynamics]].

## Experimental Methodology

The proposed surrogate model was rigorously tested across several environments to ensure robustness:
* **Dimensionality Tests:** The model was evaluated on three distinct 1-D and 2-D steady-state numerical examples.
* **Parameter Variability:** Testing included highly variable boundary wave conditions and fluctuating wind fields.
* **Real-World Application:** The researchers applied the model to a realistic numerical simulation of steady-state wave activity at Duck, North Carolina.

## Results and Significance

The DeepONet surrogate achieved consistently high accuracy in predicting two critical physical metrics:
1. The components of the **radiation stress gradient**.
2. The **significant wave height** across representative scenarios.

By demonstrating that operator learning can accurately mimic the outputs of the SWAN model with significantly reduced computational overhead, this study provides a pathway for more frequent, high-resolution coupled simulations. This advancement is crucial for improving the real-time accuracy of coastal flood forecasting and long-term environmental monitoring in the context of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] applications for ocean engineering.