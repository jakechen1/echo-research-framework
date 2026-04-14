---
title: From Incomplete Architecture to Quantified Risk: Multimodality LLM-Driven Security Assessment for Cyber-Physical Systems
created: 2024-05-23
source: https://arxiv.org/abs/2604.05674
tags: [ASTRAL, Cyber-Physical Systems, LLM, Security Assessment, Risk Management]
category: [ai, technology]
---

# From Incomplete Architecture to Quantified Risk: Multimodal LLM-Driven Security Assessment for Cyber-Physical Systems

The security of [[cyber-physical-systems|Cyber-Physical Systems]] (CPS) is frequently undermined by a lack of accurate architectural documentation. Due to the inherent complexity of integrating diverse subsystems and the persistence of legacy technologies, many systems suffer from "architectural incompleteness." These gaps in [[knowledge-management|knowledge management]] prevent practitioners from identifying critical system dependencies, attack surfaces, and potential risk propagation pathways, making reliable [[security-assessment|security assessment]] nearly impossible.

## The ASTRAL Framework

To address the challenges posed by fragmented or absent documentation, this paper introduces **ASTRAL** (Architecture-Centric Security Threat Risk Assessment using LLMs). ASTRAL is an architecture-centric security assessment technique implemented via a prototype tool powered by [[faithful-first-reasoning-planning-and-acting-for-multimodal-llms|Multimodal LLMs]]. 

The primary objective of ASTRAL is to assist practitioners in reconstructing and analyzing CPS architectures by synthesizing system representations from disparate and often unstructured data sources. The framework utilizes several advanced [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] techniques to achieve high-fidelity reconstruction:

*   **[[prompt-chaining|Prompt Chaining]]**: To execute complex, multi-step architectural reasoning tasks.
*   **[[cross-domain-few-shot-learning-for-hyperspectral-image-classification-based-on-m|Few-shot Learning]]**: To enable the model to recognize specific architectural patterns and dependencies with minimal training examples.
*   **Architectural Modeling**: Integrating LLM reasoning with formal models to support adaptive threat identification.

## Impact on Risk Management

A significant innovation of the ASTRAL approach is its ability to move beyond qualitative analysis toward **[[quantitative-risk-estimation|Quantitative Risk Estimation]]**. By leveraging the reasoning capabilities of LLMs, the tool provides a structured way to evaluate how threats might propagate through a reconstructed architecture.

The effectiveness of the approach was validated through an ablation study across multiple CPS case studies and an evaluation involving 14 experienced [[cybersecurity]] practitioners. The results demonstrate that ASTRAL is a reliable tool for supporting architecture-centric assessments, ultimately enabling more informed and data-driven decisions in [[cyber-risk-management|cyber risk management]].