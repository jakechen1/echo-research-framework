---
title: "Nvidia greenboost: Transparently Extending GPU VRAM via System RAM/NVMe"
created: 2024-05-22
source: https://gitlab.com/IsolatedOctopi/nvidia_greenboost
tags: [GPU, VRAM, Virtual Memory, Nvidia, NVMe, Machine Learning, Hardware]
category: [technology, machine-learning]
---

# Nvidia greenboost: Transparently Extending GPU VRAM via System RAM/NVMe

Nvidia greenboost is an experimental utility designed to address the critical hardware limitation of physical [[video-ram|Video RAM]] (VRAM) capacity on [[nvidia-greenboost-transparently-extend-gpu-vram-using-system-ramnvme|Nvidia]] Graphics Processing Units. The project focuses on providing a transparent mechanism to extend the accessible memory pool by leveraging available [[nvidia-greenboost-transparently-extend-gpu-vram-using-system-ramnvme|System RAM]] and [[nvidia-greenboost-transparently-extend-gpu-vram-using-system-ramnvme|NVMe]] storage.

## Overview and Mechanism

In modern computing workloads, particularly within [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] and [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]], the primary bottleneck for model scaling is often the VRAM limit. When performing inference or training on [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) or complex [[curvature-aware-optimization-for-high-accuracy-physics-informed-neural-networks|Neural Networks]], exceeding the physical memory of the GPU results in fatal "Out of Memory" (OOM) errors.

Nvidia greenboost attempts to mitigate this by implementing a layer of [[virtual-memory|Virtual Memory]] that utilizes the system's broader memory architecture. By treating portions of high-speed [[nvidia-greenboost-transparently-extend-gpu-vram-using-system-ramnvme|NVMe]] storage and [[nvidia-greenboost-transparently-extend-gpu-vram-using-system-ramnvme|System RAM]] as an extension of the GPU's onboard memory, the tool allows for the execution of much larger models than would traditionally be possible on consumer-grade hardware. The "transparent"