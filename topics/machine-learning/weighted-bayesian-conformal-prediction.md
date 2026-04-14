---
title: Weighted Bayesian Conformal Prediction
created: 2024-05-22
source: https://arxiv.org/abs/2604.06464
tags: [machine-learning, uncertainty-quantification, conformal-prediction, bayesian-inference]
category: machine-learning
---

# Weighted Bayesian Conformal Prediction (WBCP)

**Weighted Bayesian Conformal Prediction (WBCP)** is a novel framework designed to integrate the advantages of [[bayesian-quadrature|Bayesian Quadrature]]-based [[weighted-bayesian-conformal-prediction|Conformal Prediction]] (BQ-CP) with the robustness of weighted methods used to handle [[learning-stable-predictors-from-weak-supervision-under-distribution-shift|Distribution Shift]]. 

### Context and Problem Statement
Current-generation BQ-CP methods provide powerful, data-conditional guarantees by utilizing Dirichlet posteriors over prediction thresholds. However, a fundamental limitation of BQ-CP is its reliance on the [[iid-assumption|i.i.d. assumption]]. When data undergoes distribution shifts, standard BQ-CP becomes unreliable. While frequentist weighted conformal prediction can handle such shifts via importance weights, it remains limited to providing point-estimate thresholds, lacking the probabilistic depth required for comprehensive [[improving-semantic-uncertainty-quantification-in-language-model-question-answeri|Uncertainty Quantification]].

### The WBCP Framework
WBCP bridges this gap by generalizing BQ-CP to arbitrary importance-weighted settings. The methodology replaces the uniform [[Dir