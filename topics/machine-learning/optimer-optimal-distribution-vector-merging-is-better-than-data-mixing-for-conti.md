---
title: OptiMer: Optimal Distribution Vector Merging Is Better than Data Mixing for Continual Pre-Training
created: 2024-05-22
source: https://arxiv.org/abs/2603.28858
tags: [OptiMer, Continual Pre-training, LLM, Bayesian Optimization, Parameter Merging, Machine Learning]
category: ai
---

# OptiMer: Optimal Distribution Vector Merging Is Better than Data Mixing for Continual Pre-Training

In the field of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]], [[continual-pre-training|Continual Pre-training]] (CPT) is a fundamental technique used to adapt [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) to new languages and specialized domains. However, a significant challenge in CPT is that the mixture ratio of training data is a sensitive hyperparameter that is notoriously difficult to tune. Traditionally, these ratios must be decided before training begins, and a suboptimal choice can result in the waste of weeks of expensive compute resources.

## The OptiMer Framework

The researchers propose **OptiMer**, a novel approach that decouples the selection of data ratios from the actual training process. Instead of attempting to