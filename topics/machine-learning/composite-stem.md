---
title: COMPOSITE-STEM
created: 2024-05-22
source: https://arxiv.org/abs/2604.09836
tags: [benchmarking, scientific-discovery, LLM-evaluation, AI-agents]
category: ai, machine-learning, technology
---

# COMPOSITE-STEM

**COMPOSITE-STEM** is a sophisticated new benchmark designed to evaluate the reasoning capabilities of [[AI agents]] within the context of complex scientific discovery. As [[Artificial Intelligence]] begins to integrate into professional research workflows, the need for robust, frontier-level evaluations has become critical. Current benchmarks often suffer from "saturation," where models perform too well on simple tasks, or they rely on highly constrained outputs that do not reflect the nuance of real-world scientific inquiry.

## Benchmark Design

To address these limitations, COMPOSITE-STEM introduces 70 expert-written tasks curated by doctoral-level researchers. The benchmark covers four foundational scientific pillars:
*   [[Physics]]
*   [[Biology]]
*   [[Chemistry]]
*   [[Mathematics]]

A key innovation of COMPOSITE-STEM is its grading methodology. Recognizing that scientific answers often require more than simple "correct/incorrect" verification, the framework utilizes a hybrid approach. It combines traditional exact-match grading with criterion-based rubrics. To facilitate this qualitative assessment, the researchers implemented an [[LLM-as-a-jury]] protocol, allowing for a more flexible and meaningful evaluation of complex, generative scientific outputs.

## Evaluation and Results

The researchers utilized an adapted multimodal **Terminus-2** agent harness within the **Harbor** agentic evaluation framework to test several [[Frontier Models]]. The results reveal a significant performance gap in current [[Machine Learning]] capabilities; the highest-performing model achieved an accuracy of only 21%. This low percentage demonstrates that COMPOSITE-STEM successfully captures high-level reasoning tasks that remain beyond the current reach of autonomous agents.

## Impact on Scientific Discovery

The goal of COMPOSITE-STEM is to provide the scientific community with a standardized tool to measure progress in [[Automated Scientific Discovery]]. By open-sourcing all tasks, the authors aim to support reproducibility and encourage the development of more capable agents capable of driving the next era of technological and biological advancement.