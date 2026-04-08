---
title: LAG-XAI: A Lie-Inspired Affine Geometric Framework
created: 2024-05-22
source: https://arxiv.org/abs/2604.06086
tags: [Explainable AI, Transformers, Lie Groups, Hallucination Detection, Semantic Manifolds]
category: ai, machine-learning, technology
---

# LAG-XAI

**LAG-XAI** (Lie Affine Geometry for Explainable AI) is a novel geometric framework designed to address the "black box" nature of modern [[Transformer]]-based language models. Rather than viewing semantic changes as discrete word substitutions, LAG-XAI models the latent semantic space as a continuous manifold where paraphrasing is represented as a structured [[Affine Transformation]].

## Theoretical Framework

The core innovation of LAG-XAI lies in its application of [[Lie Group]] theory to model semantic transitions. By treating paraphrasing as a continuous geometric flow, the framework uses a mean-field approximation to decompose complex embedding shifts into three mathematically interpretable components:

*   **Rotation**: Angular shifts within the embedding space.
*   **Deformation**: Changes to the structural shape of the semantic cluster.
*   **Translation**: Linear shifts in the vector positions.

The framework identifies a state of "local isometry," characterized by near-zero deformation and a stabilized reconfiguration angle of approximately $27.84^{\circ}$.

## Experimental Results

The effectiveness of LAG-XAI was tested using [[Sentence-BERT]] on the noisy PIT-2015 Twitter corpus. The researchers observed a phenomenon termed "linear transparency." While the proposed affine operator achieved an AUC of 0.7713—notably lower than the non-linear baseline's AUC of 0.8405—it retained approximately 80% of the baseline's effective classification capacity. This marginal loss in absolute accuracy is compensated for by the gain in [[Mechanistic Interpretability]], as the model provides explicit, parametric explanations for semantic shifts.

## Applications in Hallucination Detection

Beyond purely linguistic analysis, LAG-XAI serves as a high-efficiency tool for [[LLM Hallucination Detection]]. The framework implements a "cheap geometric check" that monitors embeddings for deviations that exit a predefined "semantic corridor." When tested on the [[HaluEval]] dataset, this method successfully detected 95.3% of factual distortions. This demonstrates the framework's utility as a resource-efficient layer for monitoring the reliability of large-scale generative models.