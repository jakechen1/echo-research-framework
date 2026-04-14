---
title: "Not All Turns Are Equally Hard Adaptive Thinking Budgets For Efficient Multi Tur"
category: machine-learning
created: 2026-04-12
author: wiki-pipeline
dc.title: "Not All Turns Are Equally Hard Adaptive Thinking Budgets For Efficient Multi Tur"
dc.creator: wiki-pipeline
dc.date: 2026-04-12
dc.type: Text
dc.format: text/markdown
dc.identifier: general/not-all-turns-are-equally-hard-adaptive-thinking-budgets-for-efficient-multi-tur.md
dc.language: en
dc.rights: CC-BY-4.0
---

title: Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning
created: 2024-05-22
source: https://arxiv.org/abs/2604.05164
tags: [LLM, Reasoning, Inference Efficiency, Reinforcement Learning, Compute Allocation]
categories: [ai, machine-learning]

The paper "Not All Turns Are Equally Hard: Adaptive Thinking Budgets For Efficient Multi-Turn Reasoning" addresses a critical bottleneck in the deployment of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs): the inefficiency of [[Inference-time Compute]] during complex, multi-turn interactions. As reasoning capabilities expand, models often suffer from "overthinking" simple queries, resulting in excessively long thinking traces and wasted computational resources.

While previous optimization strategies—such as length regularization or adaptive routing—have attempted to manage compute budgets, they are largely limited to single-turn settings. These approaches fail to address the sequential dependencies inherent in multi-