---
title: Replacing Tunable Parameters in Weather and Climate Models with State-Dependent Functions using Reinforcement Learning
created: 2025-05-22
source: https://arxiv.org/abs/2601.04268
tags: [Reinforcement Learning, Climate Modeling, Parametrisation, Multi-agent Systems, Numerical Weather Prediction]
category: machine-learning
---

# Replacing Tunable Parameters in Weather and Climate Models with State-Dependent Functions using Reinforcement Learning

Traditional [[Climate Modeling]] and [[Weather Prediction]] rely heavily on "parametrisations"—mathematical schemes used to represent complex, sub-grid scale processes that the main model resolution cannot capture. Historically, these schemes utilize fixed coefficients that are tuned offline. This approach often leads to persistent model biases because the fixed parameters cannot adapt to the evolving underlying [[Atmospheric Physics]].

## Overview of the Framework

This study proposes a novel framework that replaces these static, tunable parameters with state-dependent functions learned online. By utilizing [[Reinforcement Learning]] (RL), the model learns to update its components as a function of the evolving model state. This allows the simulation to become more adaptive and self-correcting during runtime.

The researchers evaluated the framework across three idealized testbeds:
* **Simple Climate Bias Correction (SCBC)**
* **Radiative-Convective Equilibrium (RCE)**
* **Zonal Mean Energy Balance Model (EBM)**

## Key Findings and Algorithms

The research tested nine different RL algorithms, identifying that **Truncated Quantile Critics (TQC)**, **Deep Deterministic Policy Gradient (DDPG)**, and **Twin Delayed DDPG (TD3)** achieved the highest skill and most stable convergence. 

A significant portion of the study focused on [[Multi-agent Systems]] using a [[Federated Learning]] approach. In the EBM testbed, the researchers found that a six-agent DDPG configuration, utilizing frequent parameter aggregation, produced the lowest area-weighted Root Mean Square Error (RMSE) across the tropics and mid-latitudes.

## Physical Consistency

Crucially, the learned corrections were not merely mathematical artifacts but were physically meaningful:
* **RCE Experiments:** Agents adjusted lapse rates to match vertical temperature errors.
* **EBM Experiments:** Agents modulated radiative parameters to reduce meridional biases and stabilized heating increments to limit long-term drift.

The results suggest that [[Artificial Intelligence]] provides a scalable pathway for integrating online learning within [[Numerical Weather Prediction]] models, potentially reducing the computational burden of manual parameter tuning while increasing model accuracy.