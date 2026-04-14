---
title: General-purpose LLMs as Models of Human Driver Behavior: The Case of Simplified Merging
created: 2024-05-23
source: https://arxiv.org/abs/2604.09609
tags: [LLM, Autonomous Vehicles, Human Behavior, Prompt Engineering, Simulation]
category: ai, technology
dc.title: "General-purpose LLMs as Models of Human Driver Behavior: The Case of Simplified Merging"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/general-purpose-llms-as-models-of-human-driver-behavior-the-case-of-simplified-m.md
dc.language: en
dc.rights: CC-BY-4.0
author: wiki-pipeline
---

# General-purpose LLMs as Models of Human Driver Behavior

The research paper "General-purpose LLMs as Models of Human Driver Behavior: The 
Case of Simplified Merging" investigates the potential of [[Large Language Models]] (LLMs) to serve as high-fidelity surrogates for human drivers in [[Automated Vehicle]] (AV) simulations. In the field of virtual [[Safety Assessment]], researchers often face a difficult trade-off between the interpretability of traditional models and the flexibility of complex, data-driven models. This study explores whether general-purpose, closed-loop LLMs can bypass the need for intensive parameter fitting.

## Methodology
The researchers implemented two prominent LLMs—**OpenAI o3** and **Google Gemini 2.5 Pro**—as autonomous, closed-loop driver agents. The experiments were conducted within a simplified one-dimensional merging scenario designed to replicate the longitudinal dynamics of vehicle merging. The performance of these models was mathematically and qualitatively compared against established human driving datasets.

## Key Findings

* **Human-like Spatial Awareness:** Both models successfully replicated certain hallmarks of human driving, specifically intermittent operational control and the ability to make tactical decisions based on spatial cues.
* **Velocity Calculation Failures:** A significant deficiency was identified in both models regarding dynamic velocity cues. Neither LLM consistently captured the nuanced human response to changes in relative speed.
* **Model Divergence:** The study found that safety performance varied sharply between OpenAI o3 and Gemini 2.5 Pro, suggesting that the reliability of an LLM-based driver is highly dependent on the specific underlying architecture.
* **Prompt-Specific Biases:** Through a systematic [[Prompt Engineering]] ablation study, the researchers discovered that certain prompt components act as model-specific inductive biases. These instructional elements do not transfer effectively between different LLMs, making universal behavior modeling difficult.

## Implications for [[Machine Learning]] and AV Development
While LLMs present a promising "plug-and-play" alternative for simulating human agents in AV evaluation pipelines, they are not yet a complete replacement for specialized human behavior models. The findings suggest that while the models are capable of simulating spatial logic, their failure modes in dynamic temporal tracking must be understood and mitigated before they can be used for high-stakes safety validation.