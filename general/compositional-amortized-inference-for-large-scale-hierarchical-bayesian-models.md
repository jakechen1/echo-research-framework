---
title: Compositional amortized inference for large-scale hierarchical Bayesian models
created: 2024-05-24
source: https://arxiv.org/abs/2505.14429
tags: [machine-learning, bayesian-inference, diffusion-models, computational-imaging]
category: machine-learning
author: wiki-pipeline
dc.title: "Compositional amortized inference for large-scale hierarchical Bayesian models"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/compositional-amortized-inference-for-large-scale-hierarchical-bayesian-models.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Compositional amortized inference for large-scale hierarchical Bayesian models

## Overview
[[Amortized Bayesian Inference]] (ABI) using [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]] has become a foundational approach for estimating complex mechanistic models through simulation-based methods. However, a significant challenge remains in scaling ABI to [[compositional-amortized-inference-for-large-scale-hierarchical-bayesian-models|Hierarchical Bayesian Models]]. Historically, the hierarchical structure necessitates the simulation and processing of massive datasets, which creates a computational bottleneck in complex scientific workflows.

## Methodology
This research proposes an extension of [[Compositional Score Matching]] (CSM), a divide-and-conquer strategy for Bayesian updating that leverages [[diffhdr-re-exposing-ldr-videos-with-video-diffusion-models|Diffusion Models]]. One of the primary hurdles in previous CSM implementations was the instability encountered when aggregating large numbers of data points. 

To resolve this, the authors developed a new **error-damping estimator**. This mathematical refinement addresses the stability issues inherent in CSM, allowing for more reliable Bayesian updates across large datasets. The researchers verified the numerical stability of this estimator using controlled benchmarks featuring up to 100,000 data points.

## Experimental Results
The efficacy of the proposed method was tested across several domains:

* **Hierarchical AR Models**: In testing on hierarchical Autoregressive (AR) models, the method achieved performance competitive with direct ABI baselines on smaller problem sizes. Notably, for larger problem sizes, the method demonstrated superior efficiency, requiring less than one full model simulation to achieve results.
* **Advanced Microscopy**: The study applied the method to a large-scale [[machine-learning|Inverse Problem]] within the field of microscopy. The framework successfully handled a high-dimensional space containing over 750,000 parameters.

## Significance
By reducing the simulation overhead required for hierarchical structures, this method facilitates the use of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] in large-scale scientific applications. The ability to process high-parameter models efficiently makes this approach highly relevant to fields such as [[Computational Biology]] and high-resolution [[Imaging Science]].