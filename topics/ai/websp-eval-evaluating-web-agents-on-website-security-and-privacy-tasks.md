---
title: WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks
created: 2024-05-23
source: https://arxiv.org/abs/2604.06367
tags: [web-agents, cybersecurity, multimodal-llm, automation, evaluation]
category: [ai, technology]
---

# WebSP-Eval: Evaluating Web Agents on Website Security and Privacy Tasks

WebSP-Eval is a specialized evaluation framework designed to assess the ability of [[Web Agents]] to perform user-facing website security and privacy tasks. While current industry benchmarks, such as [[WebArena]], focus on general-purpose web automation, and others, like [[SafeArena]], focus on protecting agents from malicious actions, there has been a lack of standardized testing for an agent's ability to manage personal privacy settings.

## The Research Gap

Current autonomous agents are increasingly used to automate browser-based workflows, ranging from simple forms to complex shopping tasks. However, there is no existing framework to measure if these agents can successfully navigate privacy-sensitive configurations, such as:
* Managing cookie preferences.
* Configuring account privacy settings.
* Revoking inactive user sessions.

## Framework Components

To address this gap, the WebSP-Eval framework introduces three fundamental pillars:
1. **Task Dataset**: A manually crafted collection of 200 task instances spanning 28 diverse websites.
2. **Agentic System**: A robust environment utilizing a custom Google Chrome extension to manage account states and ensure repeatable initial conditions across different runs.
3. **Automated Evaluator**: A system designed to provide objective, automated feedback on task completion.

## Key