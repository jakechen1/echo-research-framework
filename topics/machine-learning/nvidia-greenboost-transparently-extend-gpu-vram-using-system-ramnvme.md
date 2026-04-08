---
title: "Nvidia greenboost: Transparently Extending GPU VRAM via System RAM/NVMe"
created: 2024-05-22
source: https://gitlab.com/IsolatedOctopi/nvidia_greenboost
tags: [GPU, VRAM, Virtual Memory, Nvidia, NVMe, Machine Learning, Hardware]
category: [technology, machine-learning]
---

# Nvidia greenboost: Transparently Extending GPU VRAM via System RAM/NVMe

Nvidia greenboost is an experimental utility designed to address the critical hardware limitation of physical [[Video RAM]] (VRAM) capacity on [[Nvidia]] Graphics Processing Units. The project focuses on providing a transparent mechanism to extend the accessible memory pool by leveraging available [[System RAM]] and [[NVMe]] storage.

## Overview and Mechanism

In modern computing workloads, particularly within [[Artificial Intelligence]] and [[Deep Learning]], the primary bottleneck for model scaling is often the VRAM limit. When performing inference or training on [[Large Language Models]] (LLMs) or complex [[Neural Networks]], exceeding the physical memory of the GPU results in fatal "Out of Memory" (OOM) errors.

Nvidia greenboost attempts to mitigate this by implementing a layer of [[Virtual Memory]] that utilizes the system's broader memory architecture. By treating portions of high-speed [[NVMe]] storage and [[System RAM]] as an extension of the GPU's onboard memory, the tool allows for the execution of much larger models than would traditionally be possible on consumer-grade hardware. The "transparent"