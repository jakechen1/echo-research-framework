---
title: VenusBench-Mobile: A Challenging and User-Centric Benchmark for Mobile GUI Agents with Capability Diagnostics
created: 2024-05-22
source: https://arxiv.org/abs/2604.06182
tags: [benchmark, mobile-gui, autonomous-agents, evaluation, computer-vision]
category: ai
---

# VenusBench-Mobile

**VenusBench-Mobile** is a novel [[Benchmark]] designed to evaluate the performance of [[Mobile GUI Agents]] under realistic, user-centric conditions. While existing evaluation methods for mobile automation are often criticized for being app-centric and task-homogeneous, VenusBench-Mobile addresses the lack of diversity and the inherent instability found in real-world mobile usage.

## Core Evaluation Pillars

The framework introduces two foundational pillars to ensure a rigorous assessment of [[Artificial Intelligence]]:

1.  **User-Intent-Driven Task Design**: Instead of focusing on isolated app functions, this pillar defines tasks based on actual user intentions, reflecting the complex and varied ways humans interact with mobile devices.
2.  **Capability-Oriented Annotation**: This scheme provides a fine-grained approach to analyzing agent behavior. Rather than providing a simple pass/fail metric, it allows researchers to perform deep-dive diagnostics on specific agent capabilities.

## Key Findings and Diagnostics

Extensive testing of state-of-the-art [[Machine Learning]] agents via this benchmark revealed significant performance gaps when compared to results achieved on previous, less demanding benchmarks. The research highlights several critical vulnerabilities in current [[Autonomous Agents]]:

*   **Perception and Memory Deficiencies**: Diagnostic analysis shows that most agent failures are rooted in fundamental issues with visual perception and long-term memory retention, flaws that are often hidden by coarser evaluation methods.
*   **Environmental Brittleness**: The study found that even the most powerful agents exhibit near-zero success rates when faced with environmental variations. This level of brittleness indicates that current models are not yet prepared for the unpredictability of real-world deployment.

## Significance

By identifying these specific failure modes, VenusBench-Mobile serves as a vital stepping stone for the development of robust, reliable [[Technology]] in the field of mobile automation. It provides a roadmap for moving beyond simple task completion toward the deployment of truly resilient mobile agents.

**Resources:**
*   **Code and Data**: [GitHub Repository](https://github.com/inclusionAI/UI-Venus/tree/VenusBench-Mobile)