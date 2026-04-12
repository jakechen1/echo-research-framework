---
title: Fraud Detection System for Banking Transactions
created: 2024-05-22
source: https://arxiv.org/abs/2604.07952
tags: [fraud-detection, machine-learning, fintech, cybersecurity]
category: machine-learning
---

# Fraud Detection System for Banking Transactions

The rapid expansion of [[digital-payment|Digital Payment]] ecosystems has significantly increased the surface area for financial crime. As the scale and complexity of online transactions grow, the sophistication of attack strategies has risen, making traditional rule-based detection methods increasingly obsolete.

## The Challenge of Class Imbalance
A critical difficulty in detecting financial fraud is the significant disparity between genuine and fraudulent transactions, a phenomenon known as [[class-imbalance|Class Imbalance]]. In most banking datasets, fraudulent transactions are statistically rare. Without specialized intervention, [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models tend to favor the majority class, leading to high accuracy metrics that fail to capture the actual presence of fraud.

## The Proposed Framework
This research introduces a structured framework for fraud prevention following the [[crisp-dm|CRISP-DM]] (Cross-Industry Standard Process for Data Mining) methodology. The study utilizes the [[paysim|PaySim]] synthetic financial transaction dataset, which provides a realistic simulation of mobile money movements to facilitate rigorous testing.

To address the scarcity of fraud instances, the researchers implemented [[SM