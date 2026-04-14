---
title: "Hubble: An LLM-Driven Agentic Framework for Safe and Automated Alpha Factor Discovery"
created: 2024-05-22
source: https://arxiv.org/abs/2604.09601
tags: [alpha-factor-discovery, quantitative-finance, llm, automated-machine-learning, evolutionary-computation]
category: machine-learning
dc.title: "Hubble: An LLM-Driven Agentic Framework for Safe and Automated Alpha Factor Discovery"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/hubble-an-llm-driven-agentic-framework-for-safe-and-automated-alpha-factor-disco.md
dc.language: en
dc.rights: CC-BY-4.0
author: wiki-pipeline
---

# Hubble

**Hubble** is an advanced, closed-loop agentic framework designed to automate the discovery of predictive alpha factors within the complex domain of [[Quantitative Finance]]. The fundamental challenge in financial factor mining lies in the vast combinatorial search space and the notoriously low signal-to-noise ratio found in market data.

### The Challenge of Automated Discovery
Traditional automated methods, most notably [[Genetic Programming]], have been used to navigate this search space. However, these methods often suffer from significant drawbacks, such as producing overly complex, uninterpretable formulas that are highly susceptible to overfitting. These "black-box" models lack the transparency required for institutional-grade financial deployment.

### The Hubble Approach
Hubble introduces a paradigm shift by leveraging [[Large Language Models]] (LLMs) as intelligent search heuristics. Rather than relying on purely stochastic mutations, Hubble uses the reasoning capabilities of LLMs to propose candidate factors. To maintain rigor, the framework is constrained by:

*   **Domain-Specific Language:** A specialized operator language that limits the search to financially meaningful operations.
*   **AST-based Sandbox:** An [[Abstract Syntax Tree]] (AST) execution environment that ensures all generated factors are syntactically valid and computationally stable.

### Evolutionary Feedback Mechanism
The framework operates via a continuous feedback loop. Candidate factors are pushed through a rigorous statistical pipeline that evaluates them based on:
1.  **Rank Information Coefficient (RankIC)**
2.  **Annualized Information Ratio**
3.  **Portfolio Turnover**

The performance metrics and detailed error diagnostics are then returned to the LLM. This enables an evolutionary process where the agent iteratively refines its generation strategy across multiple rounds.

### Experimental Results
In empirical studies involving 30 U.S. equities over 752 trading days, Hubble evaluated 181 syntactically valid factors. The system demonstrated exceptional reliability, achieving a peak composite score of 0.827 and maintaining 100% computational stability. The results suggest that integrating [[Artificial Intelligence]] with deterministic safety constraints provides a scalable, interpretable, and reproducible approach to [[Machine Learning]] in financial engineering.