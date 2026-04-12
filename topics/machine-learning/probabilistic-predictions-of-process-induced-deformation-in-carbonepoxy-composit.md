---
title: "Probabilistic Predictions Of Process Induced Deformation In Carbonepoxy Composit"
category: machine-learning
created: 2026-04-12
---

title: Probabilistic Predictions of Process-Induced Deformation in Carbon/Epoxy Composites Using a Deep Operator Network
created: 2024-05-23
source: https://arxiv.org/abs/2512.13746
tags: [deep-learning, composite-manufacturing, uncertainty-quantification, physics-informed-ml]
category: [ai, machine-learning, technology]

The manufacturing of [[carbonepoxy-composites|Carbon/Epoxy Composites]] is heavily impacted by [[probabilistic-predictions-of-process-induced-deformation-in-carbonepoxy-composit|Process-Induced Deformation]] (PID), a phenomenon where internal residual stresses lead to structural warping and dimensional instability. These stresses arise from the fundamental mismatch in the [[coefficient-of-thermal-expansion|Coefficient of Thermal Expansion]] between the fiber reinforcement and the polymer matrix, as well as the volumetric [[cure-shrinkage|Cure Shrinkage]] characteristic of [[thermoset|Thermoset]] resins during the curing process.

This research introduces a hybrid methodology for predicting and mitigating PID. The foundation of the study is a physics-based, two-mechanism framework that models the interactions between thermal expansion/shrinkage and cure-induced shrinkage. To overcome the computational intensity and time-constraints of traditional [[physics-based-simulation|Physics-based Simulation]], the authors developed a high-speed data-driven surrogate using [[deep-operator-networks|Deep Operator Networks]] (DeepONet).

A significant advancement in this study is the implementation of a [[feature-wise-linear-modulation|Feature-wise Linear Modulation]] (FiLM) DeepONet. This architecture allows the network's branch-network features to be modulated by external variables, such as the initial [[degree-of-cure|Degree of Cure]]. This enables the model to predict complex time histories, including changes in [[viscosity|Viscosity]] and deformation across various [[non-isothermal-cure-cycles|Non-isothermal Cure Cycles]].

Recognizing that experimental measurements are often sparse and limited to specific time instances, the study utilizes [[a-parameter-efficient-transfer-learning-approach-through-multitask-prompt-distil|Transfer Learning]]. The DeepONet is pre-trained on large datasets of high-fidelity simulations and subsequently fine-tuned using targeted, real-world manufacturing data. To ensure the reliability of these predictions under experimental conditions, the framework incorporates [[ensemble-kalman-inversion|Ensemble Kalman Inversion]] (EKI). This allows for comprehensive [[improving-semantic-uncertainty-quantification-in-language-model-question-answeri|Uncertainty Quantification]] and provides a mathematical basis