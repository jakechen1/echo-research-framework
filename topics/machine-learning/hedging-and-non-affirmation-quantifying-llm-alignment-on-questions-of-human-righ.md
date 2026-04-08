---
title: Hedging and Non-Affirmation: Quantifying LLM Alignment on Questions of Human Rights
created: 2024-05-22
source: https://arxiv.org/abs/2502.19463
tags: [LLM, Alignment, Bias, Ethics, Machine Learning, Human Rights]
category: ai
---

# Hedging and Non-Affirmation: Quantifying LLM Alignment on Questions of Human Rights

## Overview
This research investigates the phenomena of **hedging** and **non-affirmation** within [[Large Language Models]] (LLMs). These behaviors—where a model avoids clear endorsement or uses cautious, non-committal language—are often considered desirable in subjective or opinion-based contexts to maintain neutrality. However, the authors argue that these behaviors are fundamentally undesirable when discussing [[Human Rights]], which are intended to apply unambiguously to all human beings regardless of group identity.

## Methodology
The study establishes a systematic framework to quantify these behaviors by analyzing unconstrained LLM responses. The researchers evaluated six large proprietary models and one [[Open-weight model]] using a dataset of 4,738 prompts. The scope of the study was extensive, covering 205 different national and stateless ethnic identities. To ensure the findings were not merely a reflection of secondary variables, the study also analyzed the influence of:
* [[Economic Indicators]] (such as GDP)
* Conflict signals/geopolitical instability
* Sovereignty status (statelessness)

## Key Findings
The research highlights a significant failure in [[Model Alignment]] regarding identity-based consistency:
* **Identity-Dependent Bias:** 4 out of the 7 evaluated models exhibited hedging and non-affirmation behaviors that were significantly dependent on the ethnic identity being discussed.
* **Primary Predictor:** While economic and geopolitical factors do influence model responses, the identity of the group itself was identified as the strongest predictor of hedging behavior, outweighing the impact of GDP or conflict status.
* **Consistency:** The observed disparities were robust to various methods of prompt rephrasing, suggesting a deep-seated bias in the models' underlying training or alignment processes.

## Mitigation and Conclusion
To address these disparities, the researchers experimented with [[Machine Learning]] intervention techniques on open-weight models, specifically focusing on **steering** and **orthogonalization** of group identities. The study concludes that **group steering** is the most effective method for debiasing the models across different query types. Notably, this approach is robust and does not lead to significant "downstream forgetting," offering a potential path forward for more equitable [[Ethical AI]] development.