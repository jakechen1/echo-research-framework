---
title: "Interpretation Of Crystal Energy Landscapes With Kolmogorov Arnold Networks"
category: machine-learning
created: 2026-04-12
---

title: Interpretation of Crystal Energy Landscapes with Kolmogorov-Arnold Networks
created: 2024-05-22
source: https://arxiv.org/abs/2604.04636
tags: [Kolmogorov-Arnold Networks, Materials Informatics, Interpretability, Crystal Stability]
category: machine-learning

# Interpretation of Crystal Energy Landscapes with Kolmogorov-Arnold Networks

The characterization of [[crystalline-energy-landscapes|Crystalline Energy Landscapes]] is a fundamental requirement for predicting the thermodynamic stability, electronic structure, and functional behavior of new materials. While modern [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] has significantly accelerated property prediction, most implementations rely on "black-box" models. This lack of transparency limits the ability of researchers to derive new scientific laws or physical insights from the model's predictions.

## The KAN Approach

To bridge the gap between predictive accuracy and scientific interpretability, this research introduces [[hardware-oriented-inference-complexity-of-kolmogorov-arnold-networks|Kolmogorov-Arnold Networks]] (KANs) as an alternative to traditional [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]]. Unlike conventional architectures that utilize fixed activation functions, KANs employ learnable functions. This architectural difference allows the network to reveal the underlying physical relationships within the crystal data more transparently.

The study specifically presents the **Element-Weighted KAN**, a composition-only model. This model has achieved state-of-the-art accuracy across large-scale datasets in predicting several critical material properties, including:
*   Formation energy
*   Band gap
*   Work function

## Discovering Chemical Trends

A primary advantage of the KAN framework is its ability to act as a tool for scientific discovery. Without being provided with explicit physical constraints or manual feature engineering, the model successfully uncovered interpretable chemical trends that align with the [[periodic-table|Periodic Table]] and the principles of [[quantum-mechanics|Quantum Mechanics]]. 

Through the use of embedding