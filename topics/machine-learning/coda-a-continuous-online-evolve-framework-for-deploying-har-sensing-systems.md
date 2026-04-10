---
title: "CODA: A Continuous Online Evolve Framework for Deploying HAR Sensing Systems"
created: 2024-05-22
source: https://arxiv.org/abs/2403.14922
tags: [HAR, Online Learning, Domain Adaptation, Mobile Sensing, Edge AI]
category: [ai, machine-learning, technology]
---

# CODA: A Continuous Online Evolve Framework for

The **CODA** framework introduces a specialized approach to [[Human Activity Recognition (HAR)]] tailored for long-term, always-on [[Mobile Sensing]] deployments. The core problem addressed by the researchers is the "silent erosion" of model accuracy, a phenomenon where prediction performance degrades as accumulated [[Domain Shift]] renders static models obsolete.

## The Challenge: Non-Stationary Drift
In pervasive computing environments, sensors—such as those found in smartphones and smartwatches—operate in highly dynamic settings. Over time, [[Non-stationary Drift]] occurs due to changes in user behavior, sensor positioning, or environmental conditions. Traditional [[Machine Learning]] approaches typically rely on periodic, one-off updates that are computationally expensive and struggle to keep pace with continuous environmental shifts.

## The CODA Framework
CODA proposes a continuous online adaptation framework that treats model updating as a principled "cache evolution" rather than a resource-heavy parameter reconfiguration. The framework relies on two synergistic components:

1.  **Cache-based Selective Assimilation**: This component identifies and prioritizes informative instances from streaming data. By focusing on high-utility samples, the system can enhance performance even under conditions of sparse supervision.
2.  **Adaptive Temporal Retention Strategy**: To resolve the tension between learning new patterns and retaining historical knowledge, this strategy enables the system to gradually "forget" obsolete instances. This ensures the model remains optimized for current sensing conditions without being cluttered by outdated data.

## Experimental Results
The efficiency of CODA was evaluated across four heterogeneous datasets involving various phone, watch, and multi-sensor configurations. The findings demonstrate that:

*   **Superior Adaptation**: CODA consistently outperforms traditional one-off adaptation methods under conditions of heavy drift.
*   **Edge Compatibility**: The framework incurs negligible on-device latency, making it suitable for real-time [[Artificial Intelligence]] at the edge.
*   **Robustness**: The system remains resilient even when faced with imperfect or noisy feedback during the accumulation process.

By moving away from massive retraining