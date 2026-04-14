---
title: Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems
created: 2024-05-22
source: https://arxiv.org/abs/2604.08366
tags: [MOSAIC, Autonomous Driving, Data Selection, Scaling Laws, Deep Learning, Physical AI]
category: machine-learning
author: wiki-pipeline
dc.title: "Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/scaling-aware-data-selection-for-end-to-end-autonomous-driving-systems.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems

The research paper "Scaling-Aware Data Selection for End-to-End Autonomous Driving Systems" addresses a fundamental bottleneck in the development of [[Physical AI]]: the efficient collection and curation of massive, diverse datasets. As [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] models transition from digital environments to real-world applications like [[dvgt-2-vision-geometry-action-model-for-autonomous-driving-at-scale|Autonomous Driving]], the training data must satisfy a wide array of complex evaluation criteria to ensure safe and reliable deployment.

## The Challenge of Data Ambiguity
Current [[on-the-step-length-confounding-in-llm-reasoning-data-selection|Data Selection]] frameworks often struggle with "metric ambiguity"—the difficulty in predicting how specific subsets of data will impact various performance metrics. In complex environments, simply adding more data does not guarantee improvements in all necessary safety or compliance dimensions.

## The MOSAIC Framework
To resolve this, the authors propose **MOSAIC** (Mixture Optimization via Scaling-Aware Iterative Collection). MOSAIC is a general-purpose framework designed to optimize the composition of a training set through a structured, three-step approach:

1.  **Domain Partitioning**: The total available dataset is segmented into distinct, specialized domains.
2.  **Neural Scaling Law Fitting**: The framework fits [[Neural Scaling Laws]] to each specific domain, mapping how data volume from that domain correlates with target evaluation metrics.
3.  **Iterative Optimization**: The system optimizes the final data mixture by iteratively incorporating data from domains that provide the maximum marginal gain to the targeted metrics.

## Application in Autonomous Driving
The researchers applied MOSAIC to an [[End-to-End Learning]] planner for autonomous vehicles. The model was evaluated using the Extended Predictive Driver Model Score (EPDMS), which aggregates various driving rule compliance metrics. 

The experimental results demonstrate that MOSAIC significantly outperforms existing baselines. Most importantly, the framework achieves superior performance on the EPDMS while requiring up to **80% less data** than traditional collection methods. This efficiency indicates that MOSAIC could drastically reduce the massive computational and logistical costs associated with training large-scale [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models for robotics and automated transit.