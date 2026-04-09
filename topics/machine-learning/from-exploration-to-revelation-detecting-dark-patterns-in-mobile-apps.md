---
title: From Exploration to Revelation: Detecting Dark Patterns in Mobile Apps
created: 2024-05-22
source: https://arxiv.org/abs/2411.18084
tags: [dark patterns, mobile apps, automated detection, LLM, machine learning]
category: technology
---

# From Exploration to Revelation: Detecting Dark Patterns in Mobile Apps

## Overview
In the modern digital ecosystem, [[Mobile Applications]] are indispensable tools for daily life. However, many apps increasingly employ [[Dark Patterns]]—deceptive design elements such as visual emphasis or linguistic nudging—to manipulate user behavior, often leading to unintended purchases or privacy compromises. Traditionally, identifying these patterns has required manual inspection, a process that is labor-intensive and unable to keep pace with the rapid evolution of mobile software.

## The Problem
While recent efforts have moved toward [[Automated Detection]], significant hurdles remain. Current methods are largely limited to "intra-page" patterns (deceptions contained within a single screen) and heavily depend on manual app exploration. Because these tools lack the flexibility to navigate complex app flows, they fail to detect "inter-page" patterns—deceptions that manifest through the relationship between different screens or sequential user actions.

## The AppRay Solution
To address these gaps, the researchers present **AppRay**, a system designed to integrate task-oriented exploration with automated detection to expand coverage and reduce manual effort. The system operates via a two-stage architecture:

1.  **Intelligent Exploration**: AppRay utilizes [[Large Language Models]] (LLMs) to guide task-oriented exploration. By combining LLM-driven navigation with random exploration, the system can capture a vast and diverse range of [[User Interface]] (UI) states.
2.  **Contrastive Detection**: The system employs a multi-label classifier based on [[Contrastive Learning]]. To ensure high accuracy, this is augmented with a rule-based refiner that provides context-aware detection, allowing the system to identify both intra-page and inter-page deceptive patterns.

## Contributions and Performance
The research introduces two significant datasets: **AppRay-Tainted-UIs** and **AppRay-Benign-UIs**. These datasets contain 2,185 deceptive pattern instances across 16 different types, preserving the critical relationships between UI elements. 

