---
title: Entropy, Disagreement, and the Limits of Foundation Models in Genomics
created: 2024-05-23
source: https://arxiv.org/abs/2604.04287
tags: [Genomics, Foundation Models, Entropy, DNA, Machine Learning, Self-supervised Learning]
category: ai, machine-learning, biology
---

# Entropy, Disagreement, and the Limits of Foundation Models in Genomics

The research explores a critical performance gap between [[a-family-of-open-time-series-foundation-models-for-the-radio-access-network|Foundation Models]] used in [[natural-language-processing|Natural Language Processing]] (NLP) and those applied to [[entropy-disagreement-and-the-limits-of-foundation-models-in-genomics|Genomics]]. While large-scale language models have achieved remarkable success in predicting text, their counterparts in genomic science have shown significantly more mixed results. This paper investigates whether the fundamental nature of [[dna-sequences|DNA sequences]] acts as a barrier to the development of effective genomic models.

## The Role of Entropy

The study identifies [[tende-transfer-entropy-neural-diffusion-estimation|Entropy]] as a primary limiting factor. By analyzing ensembles of models trained on both text and DNA, the researchers found that the high entropy inherent in genomic sequences—specifically regarding the prediction of unseen tokens—results in near-uniform output distributions. This high level of uncertainty leads to two significant issues:
1.  **Model Disagreement:** Even when models share identical architectures, training regimes, and datasets, they exhibit significant disagreement in their predictions.
2.  **Unstable Embeddings:** The [[static-embeddings|Static Embeddings]] produced by these models are highly unstable, failing to provide a consistent representational space for genomic features.

## Fisher Information and Structural Failures

A deeper analysis of [[empirical-fisher-information|Empirical Fisher Information]] flow reveals a structural failure in how these models learn. Unlike text-based models that capture complex linguistic structures, genomic models tend to concentrate their learned information within the [[embedding-layers|Embedding Layers]]. This suggests that the models are primarily learning to identify individual tokens rather than effectively exploiting the complex, long-range [[inter-token-relationships|Inter-token Relationships]] that define biological function.

## Implications for Future Research

The findings present a significant challenge to the current paradigm of [[self-supervised-learning|Self-supervised Learning]] in biology. The study suggests that training models on raw sequences alone may be insufficient to capture the complexities of the genome. This calls into question the scalability of current methodologies and suggests that future [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] development in the biological sciences may require new approaches, such as integrating structural biological priors or multi-modal data, to overcome the limitations imposed by genomic entropy.