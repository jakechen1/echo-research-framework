---
title: LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals
created: 2024-05-23
source: https://arxiv.org/abs/2604.05655
tags: [LLM, Chain-of-Thought, Representation Learning, Mechanistic Interpretability, AI Safety]
category: [ai, machine-learning]
author: wiki-pipeline
dc.title: "LLM Reasoning as Trajectories: Step-Specific Representation Geometry and Correctness Signals"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/llm-reasoning-as-trajectories-step-specific-representation-geometry-and-correctn.md
dc.language: en
dc.rights: CC-BY-4.0
---

# LLM Reasoning as Trajectories

The research paper **"LLM Reasoning as Trajectories"** introduces a novel geometric framework for understanding how [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] process complex logic. Rather than viewing [[tool-mcot-tool-augmented-multimodal-chain-of-thought-for-content-safety-moderati|Chain-of-Thought]] (CoT) generation as a simple sequence of tokens, the authors characterize it as a structured movement—or trajectory—through [[Representation Space]].

## Core Findings

### Representation Geometry
The study demonstrates that mathematical reasoning is not stochastic in its internal processing; instead, it traverses functionally ordered, step-specific subspaces. These subspaces exhibit increased separability as the computation progresses through deeper layers of the transformer architecture. 

A vital discovery is that this geometric structure is inherent to [[Base Models]]. The process of [[Reasoning Training]] (such as RLHF or fine-tuning for logic) does not fundamentally reorganize the model's representational architecture. Instead, training primarily serves to accelerate the model's convergence toward "termination-related subspaces," effectively refining the path toward a conclusion.

### Predictability and Divergence
The researchers identified a "late-stage divergence" phenomenon. While the initial steps of a reasoning chain may look nearly identical for both valid and invalid logic, the trajectories for correct and incorrect solutions begin to deviate systematically during the final stages of the process. This allows for high-accuracy mid-reasoning monitoring, with the authors achieving a [[ROC-AUC]] of up to 0.87 when predicting the final answer's correctness before the sequence has even ended.

## Clinical and Engineering Implications: Trajectory-Based Steering
The paper introduces **Trajectory-based Steering**, an [[Inference-time Intervention]] framework. By utilizing the derived ideal trajectories, this method enables:
* **Reasoning Correction:** Real-time adjustment of the model's path when divergence toward an incorrect subspace is detected.
* **Length Control:** Manipulating the trajectory to ensure concise or sufficiently detailed reasoning.

This work provides a transformative lens for [[a-multi-level-causal-intervention-framework-for-mechanistic-interpretability-in-|Mechanistic Interpretability]], offering a mathematical foundation for predicting and controlling the behavior of increasingly complex [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] systems.