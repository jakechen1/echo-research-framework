---
title: "From Governance Norms to Enforceable Controls: A Layered Translation Method for Runtime Guardrails in Agentic AI"
created: 2024-05-22
source: https://arxiv.org/abs/2604.05229
tags: [ai-governance, agentic-ai, runtime-guardrails, ai-safety, machine-learning]
category: ai
author: wiki-pipeline
dc.title: "From Governance Norms to Enforceable Controls: A Layered Translation Method for Runtime Guardrails in Agentic AI"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/from-governance-norms-to-enforceable-controls-a-layered-translation-method-for-r.md
dc.language: en
dc.rights: CC-BY-4.0
---

# From Governance Normances to Enforceable Controls

## Overview
This paper addresses the fundamental gap between high-level [[AI Governance]] standards and the technical implementation of [[Runtime Guardrails]] for [[dynamic-agentic-ai-expert-profiler-system-architecture-for-multidomain-intellige|Agentic AI]]. As AI systems evolve from single-turn generative models to agents capable of planning, tool use, and executing multi-step trajectories, the risk profile shifts. Unlike traditional [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] deployment, where risks are often mitigated during training, agentic systems introduce emergent risks that manifest during execution through external environmental interactions.

## The Problem: The Governance-Implementation Gap
Current regulatory and organizational frameworks—such as the [[NIST AI Risk Management Framework]], [[ISO/IEC 42001]], and [[ISO/IEC 23894]]—provide essential high-level objectives for safety and ethics. However, these standards do not inherently provide the technical specifications required to create actionable, automated controls for autonomous agents. There is a lack of a clear translation layer between "what" must be governed and "how" that governance is enforced at the software level.

## The Proposed Solution: Layered Translation Method
The authors propose a "layered translation method" designed to map governance objectives into four distinct operational layers:

1.  **Governance Objectives:** The high-level requirements derived from legal and organizational standards.
2.  **Design-time Constraints:** Architectural decisions and [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|Software Engineering]] constraints established during development.
3.  **Runtime Mediation:** Active intervention mechanisms that monitor and interact with the agent during execution.
4.  **Assurance Feedback:** The mechanisms used to collect evidence that controls are functioning as intended.

To facilitate this, the paper introduces a **control tuple** and a **runtime-enforceability rubric**. This allows developers to assign controls to the appropriate layer based on whether a requirement is observable, determinate, and time-sensitive.

## Practical Application
The researchers demonstrate the efficacy of this method through a case study involving a **procurement agent**. By applying the translation method, they show that while some governance objectives are best handled via auditing (assurance), others must be strictly enforced via runtime interventions to prevent unauthorized or harmful resource allocation.

## Key Distinction
A central thesis of the paper is the limitation of runtime intervention: **Runtime guardrails should be reserved exclusively for controls that are observable, determinate, and time-sensitive enough to justify execution-time intervention.** Other governance needs should be addressed through architecture and audit trails rather than interrupting the agent's execution flow.