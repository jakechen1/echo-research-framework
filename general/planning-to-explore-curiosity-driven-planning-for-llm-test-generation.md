---
title: "Planning to Explore: Curiosity-Driven Planning for LLM Test Generation"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.05159"
tags: [AI, Software Engineering, Test Generation, Reinforcement Learning]
category: [ai, technology]
author: wiki-pipeline
dc.title: "Planning to Explore: Curiosity-Driven Planning for LLM Test Generation"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/planning-to-explore-curiosity-driven-planning-for-llm-test-generation.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Planning to Explore: Curiosity-Driven Planning for LLM Test Generation

The paper "Planning to Explore: Curiosity-Driven Planning for LLM Test Generation" addresses a critical bottleneck in [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|Software Engineering]]: the difficulty of automating [[Unit Testing]] for complex, deeply nested code structures using [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs).

### The Problem: The Greedy Plateau
Current state-of-the-art approaches for [[LLM-based Code Generation]] rely primarily on greedy strategies. These methods prioritize actions that produce the highest immediate increase in [[Code Coverage]]. However, this approach suffers from a "plateau" effect. In complex programs, reaching "deep" branches often requires a sequence of setup steps—actions that, in isolation, yield zero new coverage. Because greedy algorithms do not value these preparatory steps, they fail to navigate the program's logic effectively.

### The Solution: CovQValue
To overcome this, the authors propose **CovQValue**, a method grounded in the principles of [[Bayesian Exploration]]. Instead of viewing test generation as a single-step optimization, the researchers treat the program’s branch structure as an unknown environment.

The methodology involves several key components:
* **Coverage Map as Posterior:** The system treats the evolving map of discovered code paths as a proxy for a probabilistic posterior, representing the LLM's current knowledge of the environment.
* **Parallel Planning:** The LL