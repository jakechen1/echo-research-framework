---
title: Bias Redistribution in Visual Machine Unlearning: Does Forgetting One Group Harm Another?
created: 2024-05-23
source: https://arxiv.org/abs/2604.08111
tags: [machine-learning, machine-unlearning, algorithmic-fairness, CLIP, computer-vision]
category: machine-learning
author: wiki-pipeline
dc.title: "Bias Redistribution in Visual Machine Unlearning: Does Forgetting One Group Harm Another?"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/bias-redistribution-in-visual-machine-unlearning-does-forgetting-one-group-harm-.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Bias Redistribution in Visual Machine Unlearning

The research paper **"Bias Redistribution in Visual Machine Unlearning: Does Forgetting One Group Harm Another?"** explores a critical, overlooked dimension of [[an-illusion-of-unlearning-assessing-machine-unlearning-through-internal-represen|Machine Unlearning]]: the impact on [[Algorithmic Fairness]]. While machine unlearning is essential for complying with privacy frameworks like [[GDPR]] and [[CCPA]], this study investigates whether the process of selectively forgetting training data inadvertently reshapes and amplifies biases within a model's [[geometric-organization-of-cognitive-states-in-transformer-embedding-spaces|Embedding Space]].

### Experimental Methodology
The researchers utilized [[eclipse-a-composable-pipeline-for-predicting-ecdna-formation-evolution-and-thera|CLIP]] models (specifically ViT/B-32, ViT-L/14, and ViT-B/16) to assess zero-shot classification performance on the [[CelebA]] dataset. The study focused on intersectional groups defined by the intersection of age and gender. To evaluate the efficacy and side effects of unlearning, three distinct methods were analyzed:

*   [[Prompt Erasure]]
*   [[Prompt Reweighting]]
*   [[Refusal Vector]]

The study measured success using per-group accuracy shifts, demographic parity gaps, and a specific "redistribution score."

### Key Findings: The Redistribution Phenomenon
The study's primary contribution is the identification of the **bias redistribution phenomenon**. The authors demonstrate that unlearning a specific demographic group does not eliminate the underlying bias; instead, it redistributes that bias to other correlated groups. 

Notably, the research found that redistribution occurs significantly along gender boundaries rather than age boundaries. For instance, removing the "Young Female" group consistently caused a performance shift toward the "Old Female" group across all model scales. This suggests that [[computer-vision|Computer Vision]] models possess a gender-dominant structural bias that persists and even shifts during the unlearning process.

### Implications for [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]
While the [[Refusal Vector]] method showed promise in reducing redistribution, it struggled with achieving complete data erasure and caused significant degradation in the performance of retained data. The findings conclude that current unlearning techniques are insufficient because they fail to account for the underlying geometry of the model's embeddings. To prevent the unintended amplification of bias in remaining datasets, future developments in [[an-illusion-of-unlearning-assessing-machine-unlearning-through-internal-represen|Machine Unlearning]] must incorporate strategies that respect the structural relationships within the latent space.