---
title: CASE: Cadence-Aware Set Encoding for Large-Scale Next Basket Repurchase Recommendation
created: 2024-05-24
source: https://arxiv.org/abs/2604.06718
tags: [recommender-systems, deep-learning, temporal-modeling, retail-tech, machine-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "CASE: Cadence-Aware Set Encoding for Large-Scale Next Basket Repurchase Recommendation"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/case-cadence-aware-set-encoding-for-large-scale-next-basket-repurchase-recommend.md
dc.language: en
dc.rights: CC-BY-4.0
---

# CASE: Cadence-Aware Set Encoding

The **CASE (Cadence-Aware Set Encoding)** framework addresses a critical gap in modern [[the-unreasonable-effectiveness-of-data-for-recommender-systems|Recommender Systems]]: the inability of traditional models to account for the time-based rhythm, or "cadence," of consumer replenishment. In many retail sectors, particularly those involving frequent replenishment goods, users repurchase items at predictable, item-specific intervals. 

### The Problem: Temporal Blindness
Most existing next-basket repurchase models represent a user's history as a sequence of discrete basket events indexed by visit order. This approach treats every visit as an identical step in a sequence, failing to explicitly model the elapsed calendar time between purchases. Consequently, these models cannot update item rankings as the number of days passes between a user's last interaction and the current moment.

### The CASE Solution
CASE introduces a dual-track architecture that decouples item-level cadence learning from cross-item interaction. The model's primary innovations include:

*   **Calendar-Time Signal Modeling:** Instead of discrete indices, CASE represents each item's purchase history as a continuous calendar-time signal over a fixed horizon.
*   **Multi-Scale Temporal Convolutions:** The model applies shared convolutions at various scales to capture recurring rhythms and seasonal patterns within the temporal signals.
*   **Induced Set Attention:** To ensure the model is suitable for [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] at scale, CASE utilizes induced set attention. This reduces the computational complexity of modeling dependencies between different items in a basket to sub-quadratic levels, enabling efficient batch inference for massive item catalogs.

### Performance and Impact
The effectiveness of CASE has been validated across three public benchmarks and proprietary datasets. The model consistently outperforms strong baseline models in Precision, Recall, and NDCG. 

In a large-scale production evaluation involving tens of millions of users, CASE demonstrated significant measurable gains, achieving up to an **8.6% relative Precision lift** and a **9.9% Recall lift** at the top-5 recommendation cutoff. These results highlight the importance of [[Temporal Modeling]] in driving the accuracy of [[Retail Analytics]] and large-scale industrial recommendation engines.