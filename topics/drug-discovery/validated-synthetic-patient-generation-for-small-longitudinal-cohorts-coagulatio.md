---
title: Validated Synthetic Patient Generation for Small Longitudinal Cohorts: Coagulation Dynamics Across Pregnancy
created: 2024-05-23
source: https://arxiv.org/abs/2604.07557
tags: [synthetic-data, generative-ai, longitudinal-studies, maternal-health, data-augmentation]
categories: [ai, machine-learning, biology, technology]
---

# Validated Synthetic Patient Generation for Small Longitudinal Cohorts

The scarcity of large longitudinal clinical cohorts represents a significant bottleneck in [[maternal-health|maternal health]], [[rare-diseases|rare diseases]], and early-phase [[targeting-phgdh-for-alzheimers-disease-drug-discovery-strategies|drug-discovery]]. In these domains, datasets are often too small to train reliable [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine-learning]] models, yet expanding these cohorts through manual enrollment is often prohibitively expensive and slow.

## The Stochastic Attention (SA) Framework

To address this gap, the researchers present **multiplicity-weighted Stochastic Attention (SA)**, a generative framework rooted in [[modern-hopfield-network|modern Hopfield network]] theory. Unlike traditional generative models that may struggle with extremely small datasets, the SA framework embeds real patient profiles as memory patterns within a continuous energy landscape.

The framework utilizes **Langevin dynamics** to generate novel synthetic patients by interpolating between these stored patterns. A critical innovation of the SA model is the implementation of per-pattern multiplicity weights. This allows researchers to perform targeted amplification of rare clinical subgroups during the inference phase, effectively "upsampling" specific populations without the need for model retraining.

## Application to Coagulation Dynamics

The framework was validated using a longitudinal dataset of 23 pregnant patients, monitoring 72 biochemical features across three developmental stages: pre-pregnancy baseline, first