---
title: Local Markov-Equivalence for PC-style Local Causal Discovery and Identification of Controlled Direct Effects
created: 2024-05-24
source: https://arxiv.org/abs/250able
tags: [causal-inference, graph-theory, algorithms, structural-equation-modeling]
category: machine-learning
author: wiki-pipeline
dc.title: "Local Markov-Equivalence for PC-style Local Causal Discovery and Identification of Controlled Direct Effects"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/local-markov-equivalence-for-pc-style-local-causal-discovery-and-identification-.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Local Markov Equivalence for PC-style Local Causal Discovery

The identification of [[Controlled Direct Effects (CDEs)]] is a cornerstone of causal analysis in many scientific domains, including [[targeting-phgdh-for-alzheimers-disease-drug-discovery-strategies|drug-discovery]] and [[neuroscience]]. While CDEs can be identified when the underlying [[Directed Acyclic Graphs (DAGs)]] are known, practical applications rarely provide a complete causal map. Instead, researchers must work with the [[Essential Graph]], which represents the [[Markov equivalence class]] of DAGs sharing the same conditional independencies.

## The Problem with Global Discovery
The traditional [[PC algorithm]] is the most widely used method for learning these essential graphs. However, global discovery approaches face significant hurdles:
* **Computational Complexity**: Learning the full graph structure is computationally expensive, especially as the number of variables increases.
* **Strong Assumptions**: Global methods often rely on untestable and stringent assumptions regarding the entire system.
* **Over-computation**: In many scientific contexts, researchers only care about the causal relationship between a specific target variable and its neighbors, making the discovery of the entire graph unnecessarily intensive.

## Proposed Solution: LocPC and LocPC-CDE
This paper introduces a localized approach to causal discovery, shifting the focus from the entire network to a target-specific structure.