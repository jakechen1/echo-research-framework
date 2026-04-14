---
title: "Blink: CPU-Free LLM Inference by Delegating the Serving Stack to GPU and SmartNIC"
created: 2024-05-24
source: https://arxiv.org/abs/2604.07609
tags: [LLM, Inference, GPU, SmartNIC, Systems, Optimization]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "Blink: CPU-Free LLM Inference by Delegating the Serving Stack to GPU and SmartNIC"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/blink-cpu-free-llm-inference-by-delegating-the-serving-stack-to-gpu-and-smartnic.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Blink: CPU-Free LLM Inference

## Overview
The research paper **"Blink: CPU-Free LLM Inference by Delegating the Serving Stack to GPU and SmartNIC"** addresses a critical bottleneck in modern [[Datacenter]] operations: the reliance on host CPUs for [[Large Language Model (LLM)]] orchestration. In traditional serving stacks, the CPU remains on the critical path for token-level control, making [[epistemic-blinding-an-inference-time-protocol-for-auditing-prior-contamination-i|Inference]] performance highly sensitive to [[cpu-z-and-hwmonitor-compromised|CPU]] interference. This dependency forces operators to reserve excessive CPU headroom, leading to inefficient resource utilization.

## The Blink Architecture
Blink introduces an end-to-end serving architecture designed to remove the host CPU from the steady-state inference path. The system redistributes the serving responsibilities between two specialized hardware components:

*   **[[blink-cpu-free-llm-inference-by-delegating-the-serving-stack-to-gpu-and-smartnic|SmartNIC]]**: Acts as the primary interface for request handling, delivering inputs directly into [[when-gpus-fail-quietly-observability-aware-early-warning-beyond-numeric-telemetr|GPU]] memory via [[RDMA]] (Remote Direct Memory Access), bypassing the host CPU entirely.
*   **[[when-gpus-fail-quietly-observability-aware-early-warning-beyond-numeric-telemetr|GPU]]**: Employs a persistent kernel to handle complex logic, including batching, scheduling, and [[comparative-characterization-of-kv-cache-management-strategies-for-llm-inference|KV-cache]] management.

By delegating the serving stack to the network and accelerator hardware, Blink minimizes the overhead traditionally associated with host-driven orchestration.

## Experimental Results
Evaluated against state-of-the-art frameworks including [[TensorRT-LLM]], [[vLLM]], and [[SGLang]], Blink demonstrates superior performance across several key metrics:

*   **Latency**: Achieves a reduction in P99 [[Time To First Token (TTFT)]] by up to 8.47× and P99 [[Time Per Output Token (TPOT)]] by up to 3.40×.
*   **Throughput**: Increases decode throughput by up to 2.1×.
*   **Energy Efficiency**: Reduces the energy consumed per token by up to 48.6%.

## Resilience to Interference
A standout feature of the Blink architecture is its robustness. While existing systems can experience performance degradation of up to two orders of magnitude under heavy CPU workloads, Blink maintains stable and predictable performance. This makes it an ideal candidate for [[Application Colocation]], where multiple services share the same physical hardware.