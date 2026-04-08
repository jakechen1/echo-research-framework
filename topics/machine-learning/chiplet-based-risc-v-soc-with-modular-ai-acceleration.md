---
title: Chiplet-Based RISC-V SoC with Modular AI Acceleration
created: 2024-05-23
source: https://arxiv.org/abs/2509.18355
tags: [chiplet, RISC-V, SoC, AI acceleration, edge computing, UCIe, semiconductor]
category: technology
---

# Chiplet-Based RISC-V SoC with Modular AI Acceleration

The paper "Chiplet-Based RISC-V SoC with Modular AI Acceleration" introduces a novel architectural approach to [[System-on-a-Chip (SoC)]] design, specifically targeting the challenges of hardware deployment for [[Edge AI]]. As semiconductor manufacturing advances to smaller process nodes, traditional monolithic [[Chiplet Architecture]] designs face significant hurdles, primarily due to low manufacturing yields (often dropping below 16% at advanced nodes).

### Architecture Overview

The proposed design utilizes a 30mm x 30mm silicon interposer to integrate heterogeneous components into a single, modular package. The core of the architecture consists of a 7nm [[RISC-V]] CPU chiplet paired with dual 5nm [[Artificial Intelligence]] accelerators, each delivering 15 TOPS (INT8). To support high-throughput workloads, the system integrates 16GB of [[High Bandwidth Memory (HBM3)]] and dedicated power management controllers.

The researchers highlight four key technological innovations that optimize the chiplet-to-chiplet communication and energy usage:
1. **Adaptive Cross-Chiplet DVFS:** An implementation of [[Dynamic Voltage and Frequency Scaling (DVFS)]] that works across the interconnect.
2. **AI-Aware UCIe Extensions:** Enhancements to the [[UCIe (Universal Chiplet Interconnect Express)]] protocol, featuring compression-aware transfers and streaming flow control units.
3. **Distributed Security:** A framework for distributed cryptographic security across the various heterogeneous chiplets.
4. **Intelligent Load Migration:** Sensor-driven mechanisms to manage workloads dynamically.

### Performance Results

In evaluations using industry-standard [[Machine Learning]] benchmarks, such as MobileNetV2 and ResNet-50, the architecture demonstrated superior efficiency compared to previous basic chiplet implementations. Key metrics include:
* **Latency Reduction:** ~14.7%
* **Throughput Improvement:** ~17.3%
* **Power Reduction:** ~16.2%

Collectively, these optimizations result in a total efficiency gain of 40.1%, achieving approximately 3.5 mJ per MobileNetV2 inference. This approach proves that modular chiplet designs can approach the computational density of monolithic chips while offering the scalability and cost-effectiveness required for future high-performance edge computing applications.