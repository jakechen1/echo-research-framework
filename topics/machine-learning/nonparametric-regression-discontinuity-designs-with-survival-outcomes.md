---
title: Nonparametric Regression Discontinuity Designs with Survival Outcomes
created: 2024-05-23
source: https://arxiv.org/abs/2604.03502
tags: [causal inference, survival analysis, nonparametric statistics, regression discontinuity, R package, healthcare]
category: machine-learning
---

# Nonparametric Regression Discontinuity Designs with Survival Outcomes

The paper "Nonparametric Regression Discontinuity Designs with Survival Outcomes" introduces a novel methodological framework for performing [[Causal Inference]] when dealing with time-to-event data. Within the context of [[Regression Discontinuity Design]] (RDD), researchers aim to estimate the causal effects of treatments that are assigned based on a running variable crossing a specific threshold. This quasi-experimental approach is ubiquitous in [[Healthcare]], where clinical decisions and treatment protocols are frequently guided by threshold-based [[Biomarkers]] and prognostic scores.

### The Challenge of Censoring

A fundamental limitation in standard RDD estimators is their reliance on complete outcome data. In many longitudinal studies, particularly those involving [[Survival Analysis]], researchers encounter the problem of censoring. This occurs when subjects are lost to follow-up or the study period concludes before the event of interest is observed. Such censoring can introduce significant bias if not properly addressed, especially when the probability of censoring is dependent on patient covariates.

### Proposed Methodology

To overcome these obstacles, the authors propose a nonparametric approach that leverages [[Doubly Robust Estimators]] to provide censoring corrections. This method is designed to be compatible with existing RDD estimators while offering several key advantages:
* **Multiple Endpoints:** The ability to handle various survival endpoints simultaneously.
* **Long-term Follow-up:** Robustness during extended periods of observation.
* **Covariate-dependent Variation:** The capacity to account for variations in both survival and censoring rates that depend on individual patient characteristics.

### Empirical Validation and Software

The efficacy of this approach was demonstrated through rigorous simulations and empirical applications to the prostate component of the [[PLCO Cancer Screening Trial]]. The results indicate that the new method offers superior efficiency and greater robustness to model misspecification compared to traditional techniques.

To facilitate widespread adoption in [[Data Science]] and biostatistics, the researchers have developed `rdsurvival`, an open-source software package for the [[R programming language]]. This tool allows researchers to implement complex nonparametric designs to derive more accurate evidence from clinical and biological datasets.