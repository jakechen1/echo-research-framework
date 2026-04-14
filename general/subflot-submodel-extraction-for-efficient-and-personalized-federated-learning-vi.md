---
title: "SubFLOT: Submodel Extraction for Efficient and Personalized Federated Learning via Optimal Transport"
created: 2024-05-23
source: https://arxiv.org/abs/2604.06631
tags: [federated-learning, optimal-transport, model-pruning, edge-computing, machine-learning]
category: ai, machine-learning, technology
author: wiki-pipeline
dc.title: "SubFLOT: Submodel Extraction for Efficient and Personalized Federated Learning via Optimal Transport"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/subflot-submodel-extraction-for-efficient-and-personalized-federated-learning-vi.md
dc.language: en
dc.rights: CC-BY-4.0
---

# SubFLOT

**SubFLOT** (Submodel Extraction for Efficient and Personalized Federated Learning via Optimal Transport) is a novel framework designed to optimize [[afl-a-single-round-analytic-approach-for-federated-learning-with-pre-trained-mod|Federated Learning]] (FL) in environments characterized by high levels of system and statistical heterogeneity. As [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] moves toward deployment on [[edge devices]], the ability to train models efficiently on resource-constrained hardware becomes critical.

## The Challenge: The Pruning Dilemma

In standard [[afl-a-single-round-analytic-approach-for-federated-learning-with-pre-trained-mod|Federated Learning]], device heterogeneity (varying hardware capabilities) and data heterogeneity (non-IID data) present significant hurdles. While [[model pruning]] is a common strategy to reduce the computational footprint of models, current approaches suffer from a critical trade-off:

1.  **Server-side Pruning:** While computationally easy for the client, it lacks personalization, as it applies a uniform structure to all participants.
2.  **Client-side Pruning:** While more personalized, it is often computationally prohibitive for low-power, [[resource-constrained-amazons-chess-decision-framework-integrating-large-language|resource-constrained]] devices.
3.  **Parametric Divergence:** The act of pruning induces significant divergence between the submodels and the global model, which destabilizes training and prevents convergence.

## The SubFLOT Solution

SubFLOT addresses these issues through two integrated modules that allow the server to perform personalized pruning without accessing raw user data.

### Optimal Transport-enhanced Pruning (OTP)
The OTP module utilizes [[fast-and-interpretable-protein-substructure-alignment-via-optimal-transport|Optimal Transport]] theory to facilitate personalized pruning. By treating historical client models as proxies for local data distributions, the module formulates pruning as a **[[Wasserstein distance]]** minimization problem. This allows the server to generate customized submodels that are mathematically aligned with the local distributions of individual clients.

### Scaling-based Adaptive Regularization (SAR)
To combat the issues of parametric divergence, the SAR module introduces an adaptive penalty mechanism. It penalizes the deviation of a client's submodel from the global model. Crucially, the strength of this penalty is scaled according to the specific pruning rate of the client, ensuring that more aggressively pruned models do not drift too far from the global consensus.

## Experimental Results

Comprehensive evaluations demonstrate that SubFLOT consistently outperforms [[state-of-the-art]] methods. By successfully balancing model efficiency with personalization, SubFLOT provides a robust pathway for deploying advanced AI on diverse and resource-limited device networks.