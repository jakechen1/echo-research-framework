---
title: LLM Evaluation as Tensor Completion: Low Rank Structure and Semiparametric Efficiency
created: 2024-05-22
source: https://arxiv.org/abs/2604.05460
tags: [LLM, Tensor Completion, Semiparametric Inference, Machine Learning, Uncertainty Quantification]
category: machine-learning
---

# LLM Evaluation as Tensor Completion

The research paper **"LLM Evaluation as Tensor Completion: Low Rank Structure and Semiparametric Efficiency"** (arXiv:2604.05460) addresses a critical stability issue in the evaluation of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). Currently, most LLM leaderboards rely on pairwise human comparisons. However, these datasets are notoriously noisy, sparse, and lack uniform sampling, leading to leaderboards that lack robust [[improving-semantic-uncertainty-quantification-in-language-model-question-answeri|Uncertainty Quantification]].

### Problem Formulation
The authors propose a novel framework that treats LLM evaluation as a problem of [[semiparametric-inference|Semiparametric Inference]] applied to a low-rank latent score tensor. By modeling the underlying data through [[bradley-terry-luce-model|Bradley-Terry-Luce Model]] dynamics, the study views the sparse, noisy pairwise comparisons as observations of a structured, low-rank latent space. The objective is to provide precise estimates for smooth functionals, $\psi(T^\star)$, which include critical metrics such as:
*   **Ability Gaps:** The performance difference between specific models.
*   **Win Probabilities:** The likelihood of one model outperforming another in a head-to-head match.

### Technical Contributions
A major challenge identified in the study is that the information operator in this specific tensor completion setting is anisotropic and does not commute with the tangent-space projection. This characteristic introduces a significant bottleneck that is absent in standard, isotropic models. 

To resolve this, the authors introduce a **score-whitening method**. This method serves to equalize the local [[fisher-information|Fisher Information]], restoring stable inference at the optimal sample-complexity scale. The researchers successfully derive:
1.  The information operator on the low-rank tangent space.
2.  The efficient influence function.
3.  The semiparametric efficiency bound.
4.  A one-step debiased estimator that achieves asymptotic normality.

### Significance
This work provides a mathematically principled framework for interpreting LLM leaderboards. Beyond the scope of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]], the methodology offers a robust way to perform inference on [[llm-evaluation-as-tensor-completion-low-rank-structure-and-semiparametric-effici|Low-Rank Structure]] from sparse, pairwise contrast data, which has broad applications in any field dealing with incomplete comparative datasets.