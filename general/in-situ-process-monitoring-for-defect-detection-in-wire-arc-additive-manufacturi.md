---
title: In-situ process monitoring for defect detection in wire-arc additive manufacturing: an agentic AI approach
created: 2024-05-22
source: https://arxiv.org/abs/2604.09889
tags: [AI_Agents, WAAM, Additive_Manufacturing, Defect_Detection, LLM, In_Situ_Monitoring]
category: [ai, technology]
---

# In-situ process monitoring for defect detection in WAAM: An Agentic AI Approach

The research introduces a novel [[Agentic AI]] framework designed for real-time [[In-situ Monitoring]] and [[Defect Detection]] in [[Wire-Arc Additive Manufacturing]] (WAAM). As additive manufacturing moves toward industrial-scale production, the ability to autonomously identify internal flaws, such as porosity, is essential for ensuring structural integrity.

### Framework Architecture

The proposed system utilizes a multi-agent architecture driven by [[Large Language Models]] (LLMs) to perform high-level decision-making and sensor data interpretation. The framework is composed of two specialized, parallel agents:

*   **Processing Agent:** This agent focuses on the electrical characteristics of the welding process, analyzing signals such as current and voltage to identify anomalies.
*   **Monitoring Agent:** This agent processes [[Acoustic Sensing]] data, identifying acoustic signatures that correlate with manufacturing defects.

To establish high-precision classification, the agents were trained using specialized tools validated against ground truth data obtained through [[X-ray Computed Tomography]] (XCT). This ensures that the AI's identification of porosity defects is grounded in highly accurate physical mapping.

### Performance and Results

The study evaluates three distinct configurations: individual agents, a combined single-agent system, and a coordinated multi-agent system. The results demonstrate that the multi-agent orchestration—where the processing and monitoring agents work in parallel—yields the highest efficacy. 

Key performance metrics include:
*   **Decision Accuracy:** 91.6%
*   **F1 Score:** 0.821
*   **Reasoning Quality Score:** 3.74 / 5.0

### Implications for Manufacturing

This [[Machine Learning]]-driven approach represents a significant advancement toward autonomous, closed-loop manufacturing. By integrating [[Artificial Intelligence]] with real-time sensor feedback, the framework provides a roadmap for creating self-correcting manufacturing processes, reducing the need for post-process inspections and increasing the reliability of parts produced via [[Additive Manufacturing]].