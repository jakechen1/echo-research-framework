---
title: "Foundry: Template-Based CUDA Graph Context Materialization for Fast LLM Serving Cold Start"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.06664"
tags: [ai, machine-learning, technology, cuda, llm-serving]
category: [ai, technology]
author: wiki-pipeline
dc.title: "Foundry: Template-Based CUDA Graph Context Materialization for Fast LLM Serving Cold Start"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/foundry-template-based-cuda-graph-context-materialization-for-fast-llm-serving-c.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Foundry

**Foundry** is a template-based [[foundry-template-based-cuda-graph-context-materialization-for-fast-llm-serving-c|CUDA graph]] context materialization system designed to mitigate the significant cold-start latency encountered during the deployment of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). 

## The Problem: The CUDA Graph Bottleneck

As [[a-mathematical-theory-of-evolution-for-self-designing-ais|AI]] service providers increasingly adopt [[Autoscaling]] to manage fluctuating workloads, the speed of "cold starts"—the time taken to bring a new model instance online—has become a critical metric. While modern engineering has reduced the time required to load model weights to mere seconds, the process of capturing [[CUDA graphs]] remains a major bottleneck, often lasting tens of seconds or even several minutes.

The core difficulty arises because [[CUDA graphs]] are not easily serializable. They are tightly coupled to their specific execution context, which includes:
* **Device Addresses:** Embedded memory addresses in kernel arguments.
* **Kernel Binaries:** Kernel code that is lazily loaded only during an initial warmup phase.

Existing solutions have attempted to use process-level checkpoint/restore or brittle, kernel-specific patching, but these methods lack the flexibility required for dynamic [[almab-dc-active-learning-multi-armed-bandits-and-distributed-computing-for-seque|Distributed Computing]] environments.

## The Solution: Context Materialization

Foundry introduces a system that separates the graph capture into two distinct phases: an **offline processing stage** and an **online reconstruction stage**. 

By utilizing a template-based approach, Foundry persists both the graph topology and the necessary execution context during the offline phase. During the online phase, the system reconstructs executable graphs with negligible overhead by:
1. **Enforcing Deterministic Memory Layouts:** Ensuring predictable addressability.
2. **Kernel Extraction:** Automatically extracting and reloading the specific kernel binaries required by the captured graphs.
3. **Topology-Based Templating:** Reducing the computational cost of reconstruction through efficient graph templates.

Furthermore, Foundry supports scalable [[almab-dc-active-learning-multi-armed-bandits-and-distributed-computing-for-seque|Distributed Computing]] by allowing a single-GPU offline capture to generate templates for multi-GPU deployments. This is achieved by patching only the rank-dependent communication states required for parallel execution.

## Performance Impact

Foundry has demonstrated transformative performance across dense and [[efficient-quantization-of-mixture-of-experts-with-theoretical-generalization-gua|Mixture-of-Experts]] (MoE) models with up to 235B parameters. The system has achieved:
* **Latency Reduction:** Up to a 99% reduction in cold-start latency.
* **Case Study:** Reduced the initialization time of the **Qwen3-235B-A22B** model from 10 minutes to just **3.9 seconds**.
* **Efficiency:** Maintained the high throughput advantages typically provided by [[CUDA graphs]] without the associated startup penalties.