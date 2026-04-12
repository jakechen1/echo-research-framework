---
title: LanG -- A Governance-Aware Agentic AI Platform for Unified Security Operations
created: 2024-05-22
source: https://arxiv.org/abs/2604.05440
tags: [[cybersecurity|Cybersecurity]], [[dynamic-agentic-ai-expert-profiler-system-architecture-for-multidomain-intellige|Agentic AI]], [[analyzing-multimodal-interaction-strategies-for-llm-assisted-manipulation-of-3d-|LLM]], [[agentcity-constitutional-governance-for-autonomous-agent-economies-via-separatio|Governance]], [[social-dynamics-as-critical-vulnerabilities-that-undermine-objective-decision-ma|SOC]], [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]
categories: ai, technology
---

# LanG: A Governance-Aware Agentic AI Platform

**LanG** (LLM-assisted network Governance) is an open-source, governance-aware [[dynamic-agentic-ai-expert-profiler-system-architecture-for-multidomain-intellige|Agentic AI]] platform designed to revolutionize modern [[security-operations-center|Security Operations Center]] (SOC) workflows. The platform addresses critical industry challenges, such as alert fatigue, fragmented security tooling, and the inability to correlate events across disparate sources.

## Core Architecture and Governance

The platform is built upon a layered architecture that integrates an **Agentic AI Orchestrator** using [[langgraph|LangGraph]], incorporating essential human-in-the-loop checkpoints for operational safety. A standout feature of LanG is its use of the **Model Context Protocol (MCP)**, which allows all integrated security tools to be exposed through a unified interface.

To ensure enterprise-grade safety, LanG implements an **AI Governance Policy Engine**. This engine utilizes a two-layer guardrail pipeline—combining traditional regex with the `Llama Prompt Guard 2` semantic classifier—achieving a 98.1% F1 score and an experimental zero false positive rate in enforcing security policies.

## Key Technical Contributions

LanG introduces several high-performance modules for automated threat management:

*   **LLM-based Rule Generator**: Finetuned on multiple base models, this module generates deployable [[snort|Snort]], [[suricata|Suricata]], and [[yara|YARA]] rules with an average acceptance rate of 96.2%.
*   **Three-Phase Attack Reconstructor**: This component utilizes [[louvain-community-detection|Louvain community detection]], LLM-driven hypothesis generation, and Bayesian scoring to reconstruct attack kill-chains with 87.5% accuracy.
*   **Unified Incident Context Record**: A powerful correlation engine (F1 = 87%) that unifies fragmented security data into a single, actionable stream.

## Performance and Deployment

Designed specifically for Managed Security Service Providers (MSSPs), LanG supports multi-tenant isolation, role-based access control, and fully local deployment to ensure data privacy. In performance benchmarks, the platform's anomaly and threat detectors achieved weighted F1 scores of 99.0% and 91.0%, respectively. The system is highly efficient, maintaining inference latencies of approximately 21 ms, making it suitable for real-time, high-throughput [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]-driven security operations.