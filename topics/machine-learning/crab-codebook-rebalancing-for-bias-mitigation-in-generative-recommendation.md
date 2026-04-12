---
title: "Crab Codebook Rebalancing For Bias Mitigation In Generative Recommendation"
category: machine-learning
created: 2026-04-12
---

title: CRAB: Codebook Rebalancing for Bias Mitigation in Generative Recommendation
created: 2024-05-23
source: https://arxiv.org/abs/2604.05113
tags: [[crab-codebook-rebalancing-for-bias-mitigation-in-generative-recommendation|Generative Recommendation]], [[popularity-bias|Popularity Bias]], [[debiasing|Debiasing]], [[the-geometric-alignment-tax-tokenization-vs.-continuous-geometry-in-scientific-f|Tokenization]], [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]
category: ai, machine-learning

# CRAB: Codebook Rebalancing for Bias Mitigation in Generative Recommendation

[[crab-codebook-rebalancing-for-bias-mitigation-in-generative-recommendation|Generative Recommendation]] (GeneRec) has emerged as a transformative paradigm in [[the-unreasonable-effectiveness-of-data-for-recommender-systems|Recommender Systems]]. By representing items as discrete semantic tokens and predicting them through a generative process, GeneRec models can achieve high performance across various recommendation tasks. However, a critical challenge remains: these models are prone to severe [[popularity-bias|Popularity Bias]], often amplifying the dominance of frequently interacted items while neglecting the "long tail" of less popular items.

## The Root Causes of Bias

The researchers behind the CRAB framework conducted an empirical analysis to identify why GeneRec models exacerbate bias. They uncovered two fundamental drivers:

1.  **Imbalanced Tokenization:** The process of converting items into tokens inherits the underlying frequency imbalance of historical interactions. This creates a cycle where the [[the-geometric-alignment-tax-tokenization-vs.-continuous-geometry-in-scientific-f|Tokenization]] process itself amplifies existing popularity trends.
2.  **Training Disparity:** Current training procedures disproportionately favor high-frequency (popular) tokens. This focus comes at a cost, as the model fails to adequately learn the nuanced [[semantic-relationships|Semantic Relationships]] between tokens, leading to a lack of informativeness for unpopular items.

## The CRAB Strategy

To mitigate these issues, the paper proposes **CRAB**, a post-hoc [[debiasing|Debiasing]] strategy designed to rebalance the codebook after a model has been trained. The approach consists of two primary components:

*   **Codebook Rebalancing:** CRAB addresses frequency imbalance by splitting over-represented, popular tokens into multiple sub-tokens. Crucially, this is performed in a way that preserves the existing hierarchical semantic structure of the items.
*   **Tree-structured Regularizer:** To ensure the model maintains high-quality representations, a new regularizer is introduced. This regularizer promotes [[semantic-consistency|Semantic Consistency]] across the adjusted codebook, specifically encouraging the development of more informative and discriminative representations for rare, unpopular tokens.

## Conclusion

Experimental evaluations on real-world datasets demonstrate that CRAB significantly improves the overall performance of [[crab-codebook-rebalancing-for-bias-mitigation-in-generative-recommendation|Generative Recommendation]] models. By effectively alleviating popularity bias, CRAB ensures a more equitable and accurate recommendation experience, reducing the systemic neglect of niche items in the digital ecosystem.