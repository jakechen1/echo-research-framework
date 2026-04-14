---
title: "The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models"
created: 2024-05-22
source: https://arxiv.org/abs/260rag.05995
tags: [knowledge-editing, LLM-reliability, AI-safety, neural-networks]
category: ai
---

# The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Language Models

This article examines the phenomenon of "Surface Compliance" within [[large-language-models-llms|Large Language Models (LLMs)]], specifically regarding the effectiveness of [[knowledge-editing|Knowledge Editing]] techniques. As [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] models rely on [[parametric-memory|Parametric Memory]] to store world knowledge, they inevitably inherit errors and temporal staleness from their training corpora. While editing allows for surgical updates without the massive computational cost of retraining, this paper suggests that current successes may be illusory.

## The Problem of Surface Compliance

Current evaluation frameworks for [[knowledge-editing|Knowledge Editing]] primarily focus on whether the model produces the correct output under specific prompts. However, the authors demonstrate that many editors achieve high benchmark scores through "Surface Compliance"—a state where the model mimics the target output without fundamentally altering its underlying internal beliefs. In this scenario, the model's [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]] are not truly updated; rather, they are essentially "