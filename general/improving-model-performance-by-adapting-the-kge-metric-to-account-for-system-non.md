---
title: Improving Model Performance by Adapting the KGE Metric to Account for System Non-Stationarity
created: 2024-05-22
source: https://arxiv.org/abs/2604.03906
tags: [non-stationarity, hydrological modeling, KGE, model evaluation, geosciences]
category: machine-learning
author: wiki-pipeline
dc.title: "Improving Model Performance by Adapting the KGE Metric to Account for System Non-Stationarity"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/improving-model-performance-by-adapting-the-kge-metric-to-account-for-system-non.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Improving Model Performance by Adapulating the KGE Metric to Account for System Non-Stationarity

## Overview
In the field of [[geosciences]], particularly within [[logic|hydrological modeling]], a significant challenge is the presence of pronounced [[non-stationarity]]. This phenomenon arises from seasonal fluctuations, climatic variability in hydrometeorological drivers, and anthropogenic changes to land use. 

Traditional evaluation metrics used in model development often rely on the "unjustifiable assumption" that the underlying data-generating process is time-stationary. This paper argues that ignoring these non-stationary trends can render traditional model assessments obsolete for effective water management.

## The JKGE_ss Metric
To rectify the flaws inherent in stationary evaluation, the authors introduce the **JKGE_ss** metric (an adaptation of the [[Kling-Gupta Efficiency (KGE)]]). 

Unlike the [[Nash-Sutcliffe Efficiency (NSE)]] and standard $KGE_{ss}$, which use the long-term mean as a benchmark for model efficiency, the $JKGE_{ss}$ metric is designed to:
* Detect and account for **dynamical non-stationarity** in the statistical properties of data.
* Emphasize the reproduction of **temporal variations** in system storage.
* Improve information extraction during the model training phase.

## Experimental Validation
The robustness of the $JKGE_{ss}$ metric was tested using a variety of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|machine learning]] and physical-conceptual catchment-scale models. The testing environment spanned diverse hydroclimatic conditions, including:
* **Snow-dominated** regimes.
* **Arid** and precipitation-dominated regions.
* Varying levels of flow, specifically focusing on **recession periods**.

Across all tested environments, the $JKGE_{ss}$ metric facilitated improved reproduction of system temporal dynamics at all time scales, performing reliably across both wet and dry years.

## Conclusion
The study concludes that traditional metrics fail to account for temporal shifts in system dynamics, which can lead to misleading assessments of model performance under changing environmental conditions. The authors recommend the formal adoption of $JKGE_{ss}$ for researchers developing models intended for use in non-stationary, real-world environments.