---
title: Improving ML Attacks on LWE with Data Repetition and Stepwise Regression
created: 2024-05-22
source: https://arxiv.org/abs/2604.03903
tags: [cryptography, machine-learning, lattice-based, lwe, security, cryptanalysis]
category: machine-learning
author: wiki-pipeline
dc.title: "Improving ML Attacks on LWE with Data Repetition and Stepwise Regression"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/improving-ml-attacks-on-lwe-with-data-repetition-and-stepwise-regression.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Improving ML Attacks on LWE with Data Repetition and Stepwise Regression

The paper "Improving ML Attacks on LWE with Data Repetition and Stepwise Regression" (arXiv:2604.03903) presents significant advancements in using [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] to perform [[Cryptanalysis]] on the [[Learning with Errors (LWE)]] problem. LWE is a foundational mathematical problem used in the development of [[Lattice-based Cryptography]], which is a primary candidate for securing communications in a post-quantum era.

## Context and Problem Statement
In its simplest iteration involving binary secrets, the LWE problem can be viewed as a version of the [[Subset Sum Problem]] modified by the addition of error terms. Prior research has demonstrated that [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models can be trained to recover secrets in cases involving binary, ternary, and other small-scale secrets. Specifically, previous studies (e.g., Nolte et al., 2024) showed success in recovering secrets with up to three active bits within the "cruel region," particularly when samples were pre-processed using [[BKZ]] algorithms. However, these attacks were largely limited to very sparse secrets.

## Proposed Methodology
This research explores how to extend the reach of these attacks to recover denser, more complex secrets. The authors propose two primary improvements:

1.  **Data Repetition and Scaling**: The authors demonstrate that employing larger training sets and utilizing repeated examples allows models to successfully tackle denser secret distributions. 
2.  **Stepwise Regression**: The paper introduces a [[improving-ml-attacks-on-lwe-with-data-repetition-and-stepwise-regression|Stepwise Regression]] technique specifically designed to recover the "cool bits" of the secret, providing a refinement stage that enhances the precision of the initial ML-based guess.

## Key Findings
The study identifies a critical empirical observation: a **power-law relationship** exists between the success of model-based recovery attempts, the total size of the dataset, and the number of repeated examples used during training. 

These findings suggest that the security margins of LWE-based primitives may be more vulnerable to large-scale, data-intensive [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] training than previously assumed, particularly as dataset availability and computational power continue to scale.