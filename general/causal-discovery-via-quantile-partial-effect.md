---
title: Causal Discovery via Quantile Partial Effect
created: 2024-05-22
source: https://arxiv.org/abs/2509.12981
tags: [causal-inference, quantile-regression, statistical-learning, machine-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Causal Discovery via Quantile Partial Effect"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/causal-discovery-via-quantile-partial-effect.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Causal Discovery via Quantile Partial Effect

The paper "Causal Discovery via Quantile Partial Effect" introduces a novel statistical framework for identifying causal directions in both bivariate and multivariate settings. The methodology is centered on the concept of **Quantile Partial Effect (QPE)**, a statistic derived from [[Conditional Quantile Regression]] that measures the influence of covariates across different quantiles of a distribution.

### Core Methodology

The primary contribution of this research is the demonstration that causal identifiability can be achieved directly from the observational distribution. The authors prove that if the QPE of a cause on an effect is assumed to lie within a finite linear span, the causal direction becomes identifiable. 

This approach represents a significant advancement over traditional [[Functional Causal Models]] (FCMs). While previous FCM-based methods often rely heavily on strict assumptions regarding noise—such as additive or heteroscedastic noise—the QPE method bypasses these requirements. Instead, it utilizes the inherent asymmetry in the shape characteristics of the observed data. Notably, this framework does not require the [[Markov Assumption]] or an explicit model of the underlying generative mechanisms or noise types.

### Discovery Approaches

The paper distinguishes between two primary scenarios:

1.  **Bivariate Causal Discovery**: For simple two-variable systems, the researchers implement basis function tests on the estimated QPE. This method allows for the distinction of causal directions and has been empirically validated against a large number of bivariate causal discovery datasets.
2.  **Multivariate Causal Discovery**: For more complex systems, the authors establish a mathematical link between QPE and [[Score Functions]]. By leveraging [[Fisher Information]] as a statistical measure, the researchers demonstrate that causal order can be determined when specific assumptions are made regarding the second moment of the QPE.

### Validation

The feasibility and robustness of the QPE-based framework were validated using multiple synthetic and real-world multivariate causal discovery datasets, proving highly effective in complex structural environments.