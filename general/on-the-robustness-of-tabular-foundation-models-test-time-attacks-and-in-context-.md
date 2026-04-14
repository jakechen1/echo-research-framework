---
title: On the Robustness of Tabular Foundation Models: Test-Time Attacks and In-Context Defenses
created: 2024-05-22
source: https://arxiv.org/abs/2506.02978
tags: [adversarial-learning, tabular-data, foundation-models, cybersecurity, machine-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "On the Robustness of Tabular Foundation Models: Test-Time Attacks and In-Context Defenses"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/on-the-robustness-of-tabular-foundation-models-test-time-attacks-and-in-context-.md
dc.language: en
dc.rights: CC-BY-4.0
---

# On the Robustness of Tabular Foundation Models: Test-Time Attacks and In-Context Defenses

The research paper "On the Robustness of Tabular Foundation Models: Test-Time Attacks and In-Context Defenses" investigates the security implications of the emerging class of [[on-the-robustness-of-tabular-foundation-models-test-time-attacks-and-in-context-|Tabular Foundation Models]] (FMs), such as [[TabPFN]] and [[TabICL]]. Unlike traditional models that require gradient updates or fine-tuning, these models leverage [[graphwalker-graph-guided-in-context-learning-for-clinical-reasoning-on-electroni|In-Context Learning]] (ICL) to achieve high performance, positioning them as highly efficient but potentially unstable tools in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] workflows.

### Vulnerabilities and Attack Mechanisms
The study identifies two primary adversarial risks associated with tabular FMs:

1.  **Test-Time Susceptibility:** The authors demonstrate that small, structured perturbations applied to test inputs can cause significant degradation in prediction accuracy. This vulnerability persists even when the training context remains fixed.
2.  **Adversarial Tooling:** Beyond being targets, FMs can be repurposed as engines to generate "transferable evasion" attacks. These attacks are capable of compromising conventional-model architectures, including [[Random Forest]] and [[XGBoost]], and to a more limited extent, deep tabular models.

### Experimental Scope
The research evaluated these vulnerabilities across three critical, high-stakes sectors