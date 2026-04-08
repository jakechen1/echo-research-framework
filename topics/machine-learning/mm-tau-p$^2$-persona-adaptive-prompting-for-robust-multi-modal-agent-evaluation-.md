---
title: "MM-tau-p$^2$: Persona-Adaptive Prompting for Robust Multi-Modal Agent Evaluation in Dual-Control Settings"
created: 2024-05-22
source: "https://arxiv.org/abs/2603.09643"
tags: [multi-modal, LLM, evaluation, benchmarking, persona-adaptation, AI-agents]
category: [ai, machine-learning, technology]
---

# MM-tau-p$^2$

The research paper, **MM-tau-p$^2$**, addresses a critical gap in the current evaluation landscape for [[Large Language Models]] (LLMs) and [[AI Agents]]. Existing evaluation frameworks and benchmarks primarily focus on text-driven chat agents, operating in "user-agnostic" environments. These frameworks fail to account for the user's persona, a limitation that becomes significant in sectors like customer experience management, where an agent's effectiveness depends on its ability to adapt to user personality and communication styles.

## The Shift to Multi-modality

With the rapid proliferation of [[Multi-modal Language Models]] (MLLMs) and real-time [[Text-to-Speech]] (TTS) technologies, the industry is shifting toward agents capable of handling various input types beyond simple text. The authors argue that as agents become increasingly multi-modal, evaluation metrics must move beyond text-only accuracy to assess how agents manage complex, multi-sensory inputs during the task-planning process.

## The MM-tau-p$^2$ Benchmark

To address these challenges, the authors propose the **MM-tau-p$^2$** benchmark. This framework is designed for evaluating the robustness of multi-modal agents within a "dual-control" setting. The benchmark evaluates performance both with and without the persona adaptation of the user, specifically looking at how user inputs influence the agent's planning process to resolve queries.

Building upon the authors' prior work, [[FOCAL]], MM-tau-p$^2$ introduces **12 novel metrics** to provide a holistic, automated evaluation. Key areas of measurement include:
*   **[[Multi-modal Robustness]]**: The ability of the agent to maintain performance across different modalities.
*   **Turn Overhead**: The efficiency cost (in terms of conversation turns) introduced when multi-modality is integrated into the agent's workflow.

## Experimental Results and Methodology

The study employs an [[LLM-as-judge]] approach, using carefully crafted prompts and well-defined rubrics to automate the evaluation of conversations. The researchers applied this methodology to the [[Telecom]] and [[Retail]] domains to provide real-world estimates of the new metrics. 

Significantly, the research highlights that even state-of-the-art frontier models, such as [[GPT-4.1]] and [[GPT-5]], encounter specific challenges regarding robustness and efficiency when operating in these complex, multi-modal, and persona-adaptive environments.