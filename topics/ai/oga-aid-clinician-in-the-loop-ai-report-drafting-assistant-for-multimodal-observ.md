---
title: OGA-AID: Clinician-in-the-loop AI Report Drafting Assistant
created: 2024-05-22
source: https://arxiv.org/abs/2604.05360
tags: [ai, technology]
category: ai
---

# OGA-AID: Clinician-in-the-loop AI Report Drafting Assistant

OGA-AID is a specialized [[emomas-emotion-aware-multi-agent-system-for-high-stakes-edge-deployable-negotiat|Multi-Agent System]] designed to assist clinicians in the complex process of [[gait-analysis|Gait Analysis]] during [[post-stroke-rehabilitation|Post-Stroke Rehabilitation]]. The system functions as a drafting assistant, alleviating the cognitive load on healthcare professionals by automating the synthesis of complex, multi-source data into structured clinical reports.

## The Challenge in Rehabilitation
Accurate gait assessment is vital for monitoring recovery, yet it remains a highly demanding task. Clinicians are often required to integrate disparate data types—including patient movement videos, [[motion-capture|Motion-Capture]] kinematic trajectories, and longitudinal clinical profiles—into a single, cohesive assessment. This manual integration is time-intensive and prone to the complexities of interpreting high-dimensional [[analyzing-multimodal-interaction-strategies-for-llm-assisted-manipulation-of-3d-|Multimodal]] data.

## System Overview
OGA-AID utilizes a multi-agent [[from-large-language-model-predicates-to-logic-tensor-networks-neurosymbolic-offe|Large Language Model]] (LLM) architecture. Rather than relying on a single processing pass, the system coordinates three specialized agents:
* **Visual Agent:** Processes and interprets patient movement recordings.
* **Kinematic Agent:** Analyzes trajectory data and motion mechanics.
* **Clinical Agent:** Synthesizes patient medical histories and clinical profiles into the final report.

By delegating specific analytical tasks to these specialized agents, OGA-AID can provide a more nuanced and structured output than traditional [[improving-multimodal-learning-with-dispersive-and-anchoring-regularization|Multimodal Learning]] baselines.

## Human-AI Synergy
A core component of the OGA-AID framework is the "clinician-in-the-loop" methodology. Research indicates that the system performs most effectively when paired with human expertise. Evaluation with professional physiotherapists demonstrated that providing the system with brief, expert-led preliminary notes significantly reduces error rates compared to standard reference