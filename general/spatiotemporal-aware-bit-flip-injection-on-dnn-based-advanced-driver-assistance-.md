---
title: Spatiotemporal-Aware Bit-Flip Injection on DNN-based Advanced Driver Assistance Systems
created: 2024-05-22
source: https://arxiv.org/abs/2604.03753
tags: [ADAS, DNN, Fault Injection, Hardware Security, Reliability, Computer Vision]
category: technology
author: wiki-pipeline
dc.title: "Spatiotemporal-Aware Bit-Flip Injection on DNN-based Advanced Driver Assistance Systems"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/spatiotemporal-aware-bit-flip-injection-on-dnn-based-advanced-driver-assistance-.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Spatiotemporal-Aware Bit-Flip Injection on DNN-based Advanced Driver Assistance Systems

Modern [[Advanced Driver Assistance Systems]] (ADAS) rely heavily on the deployment of [[Deep Neural Networks]] (DNNs) for essential tasks like perception, object detection, and path planning. While these models are highly sophisticated, their physical implementation introduces significant vulnerabilities. During inference, the parameters of these DNNs reside in [[DRAM]], making them susceptible to bit flips. These single-event upsets, often caused by cosmic radiation or low-voltage hardware operations, can corrupt computations and lead to catastrophic driving decisions, such as unintended steering or acceleration.

## The STAFI Framework

To address the challenge of identifying high-impact hardware errors, this paper proposes the **Spatentially-Temporal-Aware Fault Injection (STAFI)** framework. The goal of STAFI is to move beyond random error simulation to efficiently locate critical fault sites that pose the greatest risk to vehicle safety. The framework operates on two primary dimensions:

### 1. Spatial Dimension: PMBS
The authors introduce the **Progressive Metric-guided Bit Search (PMBS)**. Instead of an exhaustive search of all possible bits in the network weights, PMBS utilizes a progressive approach to identify specific weight bits whose corruption causes the largest deviations in driving behavior. By focusing on the metrics of behavior deviation (e.g., steering angle error), the system can pinpoint critical bits much more efficiently than traditional random injection methods.

### 2. Temporal Dimension: CFTI
The **Critical Fault Time Identification (CFTI)** mechanism focuses on the temporal aspect of the error. Recognizing that not all moments in a driving cycle are equally dangerous, CFTI determines the optimal time to trigger a fault. It evaluates the environmental states and the real-time context of the system to identify windows where a bit flip would maximize the safety impact and hazard potential.

## Experimental Results

The efficiency of the STAFI framework was validated using DNNs deployed in production-level ADAS environments. The results demonstrated that STAFI is significantly more effective at identifying high-risk vulnerabilities, uncovering **29.56x more** hazard-inducing critical faults than the strongest baseline methods. This research highlights a critical need for improved [[Fault Tolerance]] and [[security|Hardware Security]] protocols in the development of autonomous driving technologies.