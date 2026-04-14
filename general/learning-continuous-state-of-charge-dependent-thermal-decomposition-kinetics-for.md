---
title: "Learning Continuous State Of Charge Dependent Thermal Decomposition Kinetics For"
category: machine-learning
created: 2026-04-12
author: wiki-pipeline
dc.title: "Learning Continuous State Of Charge Dependent Thermal Decomposition Kinetics For"
dc.creator: wiki-pipeline
dc.date: 2026-04-12
dc.type: Text
dc.format: text/markdown
dc.identifier: general/learning-continuous-state-of-charge-dependent-thermal-decomposition-kinetics-for.md
dc.language: en
dc.rights: CC-BY-4.0
---

title: Learning continuous state of charge dependent thermal decomposition kinetics for Li-ion cathodes using KA-CRNNs
created: 2024-05-23
source: https://arxiv.org/abs/2512.15628
tags: [machine-learning, lithium-ion batteries, thermal runaway, neural networks, battery safety]
category: machine-learning

# Learning continuous SOC-dependent thermal decomposition kinetics using KA-CRNNs

The study of [[Thermal runaway]] in [[Lithium-ion batteries]] is a critical frontier in improving [[Battery Safety]]. A primary driver of exothermic behavior during battery abuse is the [[learning-continuous-state-of-charge-dependent-thermal-decomposition-kinetics-for|State of Charge]] (SOC). Historically, predictive models for [[kinetic-mamba-mamba-assisted-predictions-of-stiff-chemical-kinetics|Chemical Kinetics]] have relied on scalar parameters calculated at fixed or discrete SOC levels. This limitation prevents models from accurately capturing the continuous shifts in kinetic behavior that occur as a battery discharges or charges, which is vital for understanding exothermic behavior under true abuse conditions.

## The KA-CRNN Framework
To overcome these limitations, the implementation of the [[Kolmogorov-Arnold Chemical Reaction Neural Network]] (KA-CRNN) framework offers a revolutionary solution. Unlike standard [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] approaches that act as black boxes, the KA-CRNN is "physics-encoded." By embedding a mechanistically informed reaction pathway directly into the network architecture, the model can learn continuous and realistic SOC-dependent exothermic cathode-electrolyte interactions.

## Methodology and Implementation
The researchers utilized [[Differential Scanning Calorimetry]] (DSC) data to train the model. The architecture is specifically designed to represent critical thermodynamic and kinetic parameters—including activation energies, pre-exponential factors, and enthalpies—as continuous, fully interpretable functions of the SOC. This enables the model to bridge the gap between discrete experimental observations and the continuous electrochemical states encountered during real-world usage.

## Results and Significance
The framework was validated using several cathode types, including NCA, NM, and NMA. The models successfully reproduced heat-release features across all SOC levels and provided deep, interpretable insights into the mechanisms of oxygen release and phase transformation. 

This approach serves as a foundation for future developments in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] applied to [[adversarially-and-distributionally-robust-virtual-energy-storage-systems-via-the|Energy Storage]]. By extending kinetic parameter dependencies to other environmental and electrochemical variables, the KA-CRNN framework supports more accurate monitoring and prediction of thermal events in next-generation power systems.