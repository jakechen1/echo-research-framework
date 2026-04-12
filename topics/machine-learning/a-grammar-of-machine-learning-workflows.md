---
title: A Grammar of Machine Learning Workflows
created: 2024-05-22
source: https://arxiv.org/abs/2603.10742
tags: [data leakage, reproducibility, ml workflows, software engineering]
category: machine-learning
---

The research paper "A Grammar of Machine Learning Workflows" addresses one of the most pervasive and damaging issues in modern [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]: [[data-leakage-in-automotive-perception-practitioners-insights|Data Leakage]]. Through a rigorous audit of scientific literature, the authors identified that leakage-related errors are present in 648 published machine learning papers across 30 different scientific fields. This systemic issue suggests that while the theoretical knowledge to prevent such errors is widely understood, existing [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|Software Engineering]] tools and [[ml-framework|ML Framework]]s lack the structural enforcement required to prevent developers from inadvertently compromising their models.

To combat this, the paper introduces a formal "grammar" for workflows. This grammar is built upon eight typed primitives structured within a [[directed-acyclic-graph-dag|Directed Acyclic Graph (DAG)]]. By applying four specific hard constraints, the authors have created a system where the most damaging types of leakage are "structurally unrepresentable"—meaning the workflow cannot be mathematically or computationally represented if the leakage error is present in the logic.

The core innovation of this grammar is the **terminal assessment gate**. This acts as a call-time-enforced boundary between the evaluation and assessment stages. This mechanism is supported by a specification so precise that it allows for independent reimplementation, fostering