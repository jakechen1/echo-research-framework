---
title: "Feddetox Robust Federated Slm Alignment Via On Device Data Sanitization"
category: machine-learning
created: 2026-04-12
---

title: "FedDetox: Robust Federated SLM Alignment via On-Device Data Sanitization"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.06833"
tags: [Federated Learning, AI Safety, Small Language Models, Data Sanitization]
categories: [ai, machine-learning, technology]

# FedDetox: Robust Federated SLIM Alignment via On-Device Data Sanitization

## Overview
As high-quality public datasets become increasingly scarce, [[afl-a-single-round-analytic-approach-for-federated-learning-with-pre-trained-mod|Federated Learning]] (FL) has become a critical pathway for leveraging valuable private user data while maintaining strict privacy standards. However, a significant emerging threat in this domain is "unintended data poisoning." This occurs when the private, local datasets on client devices contain toxic or unsafe information, which can inadvertently degrade the safety alignment of the global model during the federated training process.

**FedDetox** is a newly proposed robust framework designed to address this vulnerability, specifically optimized for [[small-language-models|Small Language Models]] (SLMs) deployed on resource-constrained [[multi-turn-reasoning-llms-for-task-offloading-in-mobile-edge-computing|Edge Computing]] devices.

## Methodology
The FedDetox framework implements a dual-stage strategy to sanitize data at the source before it can impact the global model:

1.  **Knowledge Distillation**: To ensure that even lightweight models can perform complex safety checks, the framework employs [[geometric-limits-of-knowledge-distillation-a-minimum-width-theorem-via-superposi|Knowledge Distillation]]. It transfers advanced safety alignment capabilities from large-scale, "teacher" [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] into lightweight "student" classifiers. These student models are small enough to reside and execute on edge hardware without significant computational overhead.
2.  **On-Device Sanitization**: During the federated human preference alignment phase, edge clients use these student classifiers to identify unsafe samples. Instead of simply deleting the data—which would reduce the amount of training signal available—FedDetox replaces toxic content with specialized **refusal templates**. This mechanism effectively transforms potential "poison" into positive safety signals, training the model to recognize and refuse harmful prompts.

## Conclusion
Experimental results demonstrate that FedDetox maintains model safety at levels comparable to centralized training baselines. Crucially, the framework achieves this protection without compromising the general utility of the model, providing a scalable solution for safe and robust [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] in decentralized environments.