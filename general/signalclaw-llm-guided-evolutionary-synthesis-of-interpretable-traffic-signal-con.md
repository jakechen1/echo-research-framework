---
title: "SignalClaw: LLM-Guided Evolutionary Synthesis of Interpretable Traffic Signal Control Skills"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.05535"
tags: [traffic-control, LLM, evolutionary-computation, program-synthesis]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "SignalClaw: LLM-Guided Evolutionary Synthesis of Interpretable Traffic Signal Control Skills"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/signalclaw-llm-guided-evolutionary-synthesis-of-interpretable-traffic-signal-con.md
dc.language: en
dc.rights: CC-BY-4.0
---

# SignalClaw

**SignalClaw** is a novel framework designed for [[Traffic Signal Control (TSC)]], aimed at bridging the gap between the high performance of [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] and the necessity for human-interpretable control logic. The framework utilizes [[Large Language Models (LLMs)]] as evolutionary skill generators to synthesize, refine, and deploy executable, self-documenting control programs.

## Overview

Traditional approaches to traffic management often face a trade-off between efficiency and transparency. While neural-based policies like [[Deep Q-Network (DQN)]] can optimize flow, they operate as "black boxes" that are difficult for engineers to audit. Conversely, traditional [[scientific-graphics-program-synthesis-via-dual-self-consistency-reinforcement-le|Program Synthesis]] often relies on overly restrictive domain-specific languages. 

SignalClaw addresses this by using LLMs to evolve "skills"—sets of executable code accompanied by natural language rationales and selection guidance. The evolutionary loop is driven by converting [[Simulation Metrics]] (such as queue percentiles, delay trends, and stagnation) into natural language feedback. This feedback instructs the LLM on how to improve the control logic in subsequent generations.

## Key Features

*   **Event-Driven Composition:** Utilizing [[attention-flows-tracing-llm-conceptual-engagement-via-story-summaries|TraCI]], the framework employs an event detector to identify specific scenarios, such as emergency vehicle approach, transit priority needs, or unexpected congestion.
*   **Priority Dispatching:** A specialized dispatcher selects and composes pre-evolved skills at runtime. This allows the system to handle complex, multi-event scenarios without the need for costly retraining.
*   **Interpretability:** Because the output consists of evolved code and text-based rationales, the policies are fully inspectable and modifiable by traffic engineers.

## Performance

In evaluations conducted via the [[SUMO]] simulator, SignalClaw demonstrated superior performance in high-priority scenarios:

| Scenario | SignalClaw Delay (sec) | MaxPressure Delay (sec) | DQN Delay (sec) |
| :--- | :--- | :--- | :--- |
| **Emergency Vehicles** | 11.2 – 18.5 | 42.3 – 72.3 | 78.5 – 95.3 |
| **Transit Priority** | 9.8 – 11.5 | 38.7 – 45.2 | N/A |

The framework shows that evolving skills from simple linear rules to complex [[Automated Program Synthesis]] strategies can maintain stable overall delays even in mixed-event environments.