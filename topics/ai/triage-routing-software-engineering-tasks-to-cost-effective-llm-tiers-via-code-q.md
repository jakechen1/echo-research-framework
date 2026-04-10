---
title: Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers via Code Quality Signals
created: 2024-05-22
source: https://arxiv.org/abs/2604.07-494
tags: [LLM, Software Engineering, Cost Optimization, Routing, Code Quality]
category: ai, technology
---

# Triage: Routing Software Engineering Tasks to Cost-Effective LLM Tiers

The **Triage** framework addresses a critical economic bottleneck in the deployment of [[Artificial Intelligence]] agents: the high [[Inference Cost]] associated with using frontier [[Large Language Models]] (LLMs) for all programming tasks. Currently, most [[AI Agent]] workflows route every instruction to the most expensive available models, even when the task involves routine or low-complexity code changes.

## Overview

Triage proposes a dynamic routing mechanism that uses [[Code Quality]] and software health metrics as signals to assign tasks to the most cost-effective model tier. The framework categorizes tasks into three capability tiers—**light**, **standard**, and **heavy**—which mirror the performance-to-cost spectrum of models such as Anthropic's Haiku, Sonnet, and Opus.

By analyzing pre-computed "code health" sub-factors (indicators of [[Software Maintainability]]), the system determines if a cheaper, smaller model can achieve the same verification success rate as a larger, more expensive one. This transforms diagnostic metrics into actionable signals for [[Model Selection]].

## Methodology and Evaluation

The researchers evaluated the Triage framework using [[SWE-bench Lite]], a benchmark consisting of 300 software engineering tasks. The study compared three distinct routing