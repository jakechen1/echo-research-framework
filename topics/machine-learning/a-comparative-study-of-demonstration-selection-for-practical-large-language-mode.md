---
title: A Comparative Study of Demonstration Selection for Practical Large Language Models-based Next POI Prediction
created: 2024-05-22
source: https://arxiv.org/abs/2604.06207
tags: [ai, machine-learning, technology]
category: ai
---

# A Comparative Study of Demonstration Selection for Practical Large Language Models-based Next POI Prediction

This research investigates the optimization of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) for the specific task of [[next-poi-prediction|Next POI Prediction]]. The study focuses on predicting a user's subsequent location based on historical check-in data, a critical component of modern [[urban-computing|Urban Computing]] and location-based services.

The core challenge addressed is the efficiency of [[graphwalker-graph-guided-in-context-learning-for-clinical-reasoning-on-electroni|In-Context Learning]] (ICL). In ICL, the performance of the model is heavily dependent on the "demonstrations"—the specific historical examples provided in the prompt to guide the output. While previous methodologies have attempted to use complex [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] techniques, such as [[embedding-based-selection|Embedding-based selection]], to choose the most relevant examples, this paper provides a much-needed comparative analysis of various selection strategies.

The researchers evaluated several approaches, ranging from high-complexity methods to simple logic-based strategies:
*   **Complex Strategies:** Including random selection and sophisticated vector-based embedding methods.
*   **Heuristic Approaches:** Utilizing [[geographical-proximity|Geographical Proximity]], [[temporal-ordering|Temporal Ordering]], and the identification of [[sequential-patterns|Sequential Patterns]].

The experimental results, derived from three real-world datasets, reveal that simpler [[the-traveling-thief-problem-with-time-windows-benchmarks-and-heuristics|Heuristic]] methods consistently outperform computationally expensive embedding-based methods. These heuristic strategies are superior in both predictive accuracy and [[computational-cost|Computational Cost]]. 

A significant finding of this study is that LLMs utilizing demonstrations selected through these efficient, simple heuristics can even outperform existing [[fine-tuned-models|Fine-tuned models]] without the need for additional training or parameter updates. This suggests that for practical, large-scale deployments in [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]], prioritizing efficient, rule-based demonstration selection is more effective than implementing high-overhead, computationally taxing architectures. This research offers a streamlined roadmap for implementing highly accurate prediction models in resource-constrained environments.