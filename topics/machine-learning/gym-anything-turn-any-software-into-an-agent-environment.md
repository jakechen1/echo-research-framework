---
title: Gym-Anything: Turn any Software into an Agent Environment
created: 2024-05-23
source: https://arxiv.org/abs/2604.06-126
tags: [Computer-use agents, Multi-agent systems, CUA-World, Benchmarking, Automation]
categories: [ai, machine-learning, technology]
---

# Gym-Anything

**Gym-Anything** is an innovative framework designed to overcome the scalability bottleneck in developing [[intentscore-intent-conditioned-action-evaluation-for-computer-use-agents|Computer-use agents]]. Traditionally, creating training environments for agents has been a labor-intensive process, limited to simple, short-horizon tasks such as basic web navigation or OS configuration. This limitation prevents [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] from advancing into complex, economically valuable professional domains.

## The Framework

The core innovation of Gym-Anything is treating the creation of a software environment as a [[strategic-persuasion-with-trait-conditioned-multi-agent-systems-for-iterative-le|Multi-agent systems]] problem. Rather than relying on human engineers to manually configure software, the framework employs a dual-agent pipeline:

1.  **Coding Agent**: This agent is responsible for the heavy lifting of environment construction. It writes necessary setup scripts, retrieves real-world datasets, and configures the target software. Crucially, it produces verifiable evidence to prove the setup was successful.
2.  **Audit Agent**: An independent agent that reviews the evidence produced by the Coding Agent against a predefined quality checklist, ensuring the environment is stable and ready for training.

## CUA-World and Benchmarking

Using a taxonomy derived from U.S. GDP data to identify high-value occupations, the researchers applied this framework to 200 diverse software applications. This resulted in the creation of **CUA-World**, a massive-scale collection of over 10,000 long-horizon tasks. These tasks span highly specialized fields, including [[medical-science|Medical science]], [[astronomy|Astronomy]], [[hyve-hybrid-views-for-llm-context-engineering-over-machine-data|Engineering]], and enterprise systems.

A subset of this collection, **CUA-World-Long**, serves as a rigorous [[evgeoqa-benchmarking-llms-on-dynamic-multi-objective-geo-spatial-exploration|Benchmarking]] tool. It features tasks that often require more than 500 sequential steps, significantly exceeding the complexity of existing benchmarks.

## Key Results

The research demonstrates two significant breakthroughs in agent training and execution:
*   **Model Distillation**: Detailed trajectories from the training split were distilled into a 2B [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (vision-language model), which outperformed models twice its size.
*   **Test-Time Auditing**: By applying the auditing principle during inference—using a separate VLM to review completed trajectories and provide feedback—the researchers improved the performance of Gemini-3-Flash on CUA-World-Long from 11.5% to 14.0%.

By automating the creation of complex digital environments, Gym-Anything provides the necessary infrastructure to train agents capable of performing sophisticated, real-world professional labor.