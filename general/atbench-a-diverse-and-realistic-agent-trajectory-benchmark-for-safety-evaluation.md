---
title: ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis
created: 2024-05-22
source: https://arxiv.org/abs/2604.02022
tags: [AI Safety, Benchmarking, LLM Agents, Cybersecurity]
category: ai
author: wiki-pipeline
dc.title: "ATBench: A Diverse and Realistic Agent Trajectory Benchmark for Safety Evaluation and Diagnosis"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/atbench-a-diverse-and-realistic-agent-trajectory-benchmark-for-safety-evaluation.md
dc.language: en
dc.rights: CC-BY-4.0
---

# ATBench

**ATBench** is a trajectory-level benchmark engineered for the structured, diverse, and realistic evaluation of safety within [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) acting as autonomous agents. As [[undetectable-conversations-between-ai-agents-via-pseudorandom-noise-resilient-ke|AI Agents]] transition from isolated prompt-response models to multi-step interactive systems, the need for evaluating risks that emerge during long-horizon interactions becomes critical.

### The Challenge of Agentic Safety
Traditional safety evaluations often focus on single-turn prompts or final outputs. However, in realistic deployments, safety risks frequently emerge through complex, multi-step sequences of tool usage and environmental interactions. Existing benchmarks are limited by:
*   **Low Interaction Diversity:** A lack of varied scenarios and tool usage.
*   **Coarse Observability:** Difficulty in pinpointing precisely when and why a safety failure occurred.
*   **Weak Realism:** A failure to simulate long-horizon risks that trigger only after several seemingly benign steps.

### Benchmark Methodology
ATBench addresses these limitations by organizing agentic risk across a three-dimensional taxonomy:
1.  **Risk Source:** Identifying the origin of the potential threat.
2.  **Failure Mode:** Categorizing the specific type of safety breach.
3.  **Real-world Harm:** Assessing the ultimate impact of the failure.

To simulate realistic, complex environments, ATBench utilizes a **long-context delayed-trigger protocol**. This protocol captures risk emergence across multiple stages, making it significantly more difficult for [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] guard systems to detect. The benchmark incorporates a heterogeneous tool pool, featuring 1,954 invoked tools drawn from a wider pool of 2,084 available tools.

### Dataset Composition and Quality
The benchmark comprises **1,000 trajectories**, balanced between safe (503) and unsafe (497) interactions. The data is characterized by:
*   **Complexity:** An average of 9.01 turns per trajectory.
*   **Scale:** An average of 3.95k tokens per trajectory.
*   **Rigorous Validation:** Data quality is maintained through a combination of rule-based filtering, [[analyzing-multimodal-interaction-strategies-for-llm-assisted-manipulation-of-3d-|LLM]]-based filtering, and a comprehensive human audit.

### Significance
Experiments conducted on frontier [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] models and specialized safety systems demonstrate that ATBench provides a significant challenge even for state-of-the-art evaluators. It enables researchers to perform taxonomy-stratified analysis and diagnose complex, long-horizon failure patterns, paving the way for more robust [[dynamic-agentic-ai-expert-profiler-system-architecture-for-multidomain-intellige|Agentic AI]] development.