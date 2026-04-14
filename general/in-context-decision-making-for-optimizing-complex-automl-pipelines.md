---
title: "In-Context Decision Making for Optimizing Complex AutoML Pipelines"
created: 2024-05-22
source: "https://arxiv.org/abs/2508.13657"
tags: [AutoML, PFN, Reinforcement Learning, Hyperparameter Optimization]
category: machine-learning
author: wiki-pipeline
dc.title: "In-Context Decision Making for Optimizing Complex AutoML Pipelines"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/in-context-decision-making-for-optimizing-complex-automl-pipelines.md
dc.language: en
dc.rights: CC-BY-4.0
---

# In-Context Decision Making for Optimizing Complex AutoML Pipelines

The paper "In-Context Decision Making for Optimizing Complex AutoML Pipelines" addresses the evolving complexity of [[machine-learning|Automated Machine Learning]] (AutoML) workflows. Traditionally, the industry has relied on the [[Combined Algorithm Selection and Hyperparameter Optimization]] (CASH) framework to automate model selection. However, as [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] moves toward more sophisticated architectures, the scope of automation has expanded beyond simple hyperparameter tuning to include [[convolearn-a-dataset-for-fine-tuning-dialogic-ai-tutors|Fine-tuning]], [[Ensembling]], and complex pipeline adaptation.

### The Challenge of Heterogeneous Pipelines
Modern ML pipelines are increasingly heterogeneous. The difficulty lies in identifying the optimal model for a specific downstream task when the search space includes various adaptation techniques that vary significantly in complexity and computational requirements. Standard [[Algorithm Selection]] methods often struggle to navigate these highly variable search spaces efficiently.

### Proposed Solution: PS-PFN
To bridge this gap, the authors propose **PS-PFN**, a novel approach designed to explore and exploit modern, adapting ML pipelines. The core methodology extends [[Posterior Sampling]] (PS) to a [[k-armed bandit]] problem setup. 

The breakthrough element of PS-PFN is its use of [[multimodalpfn-extending-prior-data-fitted-networks-for-multimodal-tabular-learni|Prior-Data Fitted Networks]] (PFNs). By leveraging [[graphwalker-graph-guided-in-context-learning-for-clinical-reasoning-on-electroni|In-Context Learning]], these networks can efficiently estimate the posterior distribution of the maximal value without requiring extensive trial-and-error for every new task. Key features of the framework include:

* **Cost-Aware Optimization:** The method can be adapted to consider the varying computational costs of pulling different "arms" (pipeline configurations).
* **Tailored Modeling:** The framework allows for the use of different PFNs to model individual reward distributions for each arm, allowing for more granular precision.

### Experimental Results
Evaluations conducted on one novel benchmark and two existing standard tasks demonstrate that PS-PFN provides superior performance compared to traditional [[Bandit Strategies]] and existing AutoML methodologies. To support the research community, the authors have made their code and data available via the [[CASHPlus]] repository.