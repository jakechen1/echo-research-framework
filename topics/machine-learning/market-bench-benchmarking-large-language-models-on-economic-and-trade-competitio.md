---
title: Market-Bench: Benchmarking Large Language Models on Economic and Trade Competition
created: 2024-05-22
source: https://arxiv.org/abs/2604.05523
tags: [LLM, Benchmarking, Multi-Agent Systems, Economics, Supply Chain]
category: ai
---

# Market-Bench

**Market-Bench** is an innovative benchmarking framework developed to assess the proficiency of [[Large Language Models]] (LLMs) in performing tasks relevant to [[Economics]] and international trade. As [[Artificial Intelligence]] moves toward more autonomous roles, understanding how these models manage resources, navigate auctions, and compete in complex markets becomes a vital area of research within [[Machine Learning]].

## Overview

The core of Market-Bench is a configurable, multi-agent supply chain economic model. Within this ecosystem, LLM agents are assigned the specific role of retailers. The operational cycle is divided into two distinct stages designed to simulate real-world trade competition:

* **The Procurement Stage**: In this phase, agents participate in budget-constrained auctions. They must strategically bid for limited inventory, necessitating effective resource management and decision-making under financial uncertainty.
* **The Retail Stage**: Once inventory is secured, agents are responsible for the sale of goods. This involves setting optimal retail prices and generating persuasive marketing slogans. To facilitate the transaction, the framework utilizes a specialized role-based attention mechanism that allows buyers to interact with the agents' marketing efforts.

## Evaluation Methodology

A key strength of Market-Bench is its comprehensive logging system. The framework tracks complete trajectories of bids, prices, slogans, sales, and balance-sheet states. This granularity allows researchers to conduct multidimensional evaluations across three primary categories:
1. **Economic Metrics**: Tracking capital appreciation and profit margins.
2. **Operational Metrics**: Assessing the efficiency of the supply chain movements.
3. **Semantic Metrics**: Measuring the linguistic quality and persuasiveness of marketing outputs.

## Key Findings

Research conducted on 20 different open- and closed-source LLM agents uncovered significant performance disparities. Notably, the study identified a **"winner-take-most"** phenomenon. While a small, elite subset of LLM retailers was able to achieve consistent capital appreciation, a much larger group of agents remained near the break-even point. Interestingly, many agents remained economically stagnant even when they achieved high semantic matching scores, suggesting that linguistic competence does not inherently translate to economic success within [[Multi-Agent Systems]].