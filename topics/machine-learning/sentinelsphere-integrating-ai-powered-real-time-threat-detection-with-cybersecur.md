---
title: SentinelSphere: Integrating AI-Powered Real-Time Threat Detection with Cybersecurity Awareness Training
created: 2024-05-22
source: https://arxiv.org/abs/2604.06900
tags: [cybersecurity, machine learning, LLM, threat detection, artificial intelligence]
category: technology
---

# SentinelSphere

**SentinelSphere** is an integrated platform designed to address the dual challenges of the modern [[Cybersecurity]] landscape: the global shortage of qualified professionals and the persistent vulnerability of human factors in security breaches. The system bridges the gap between automated [[Machine Learning]] detection and proactive, human-centric education.

## Technical Architecture

The platform operates through two primary synergistic modules:

### 1. Threat Detection Module
At its core, the detection engine utilizes an **Enhanced Deep Neural Network (DNN)** specifically engineered for high-precision identification of malicious activities. The model was trained using prominent benchmarks, including [[CIC-IDS2017]] and [[CIC-DDoS2019]]. 

A significant innovation in this module is the implementation of advanced HTTP-layer feature engineering, which allows the system to capture complex signatures of application-level attacks. Experimental results demonstrate that this approach maintains high recall for critical threats—such as [[DDoS]], brute-force attacks, and web-based exploits—while significantly reducing false positive rates compared to traditional baseline models.

### 2. Educational Module
To mitigate human error, SentinelSphere incorporates an adaptive training component driven by a **Large Language Model (LLM)**. The platform utilizes a quantized variant of the **Phi-4 model (Q4_K_M)**, which has been fine-tuned specifically for the cybersecurity domain. 

By leveraging quantization techniques, the model is optimized for deployment on standard commodity hardware, requiring only 16 GB of RAM and bypassing the need for expensive, dedicated [[GPU]] resources. This makes the technology accessible to organizations without massive computational budgets.

## User Experience and Impact

SentinelSphere is designed for high accessibility, featuring a "Traffic Light" visualization system and a conversational [[Artificial Intelligence]] assistant. These interfaces are specifically designed to make complex security data intuitive for users without specialized technical backgrounds. 

Through this cohesive framework, SentinelSphere demonstrates that the integration of automated [[Deep Learning]] detection with real-time, LLM-driven education can effectively mitigate both technical and human-centered digital vulnerabilities within a single, unified ecosystem.