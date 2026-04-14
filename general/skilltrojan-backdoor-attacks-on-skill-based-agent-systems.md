---
title: SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems
created: 2024-05-24
source: https://arxiv.org/abs/2604.06811
tags: [AI Security, Backdoor Attacks, Agentic Workflows, Cybersecurity, Machine Learning]
category: ai
author: wiki-pipeline
dc.title: "SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/skilltrojan-backdoor-attacks-on-skill-based-agent-systems.md
dc.language: en
dc.rights: CC-BY-4.0
---

# SkillTrojan: Backdoor Attacks on Skill-Based Agent Systems

**SkillTrojan** is a novel class of [[skilltrojan-backdoor-attacks-on-skill-based-agent-systems|Backdoor Attacks]] specifically designed to target [[skilltrojan-backdoor-attacks-on-skill-based-agent-systems|Skill-Based Agent Systems]]. Unlike traditional [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] vulnerabilities that focus on poisoning training data or corrupting model parameters, SkillTrojan shifts the attack surface to the modular components—the "skills"—that these agents use to execute complex, multi-step tasks.

## Attack Mechanism

The core innovation of SkillTrojan lies in its ability to embed malicious logic within otherwise benign and functional skill implementations. Rather than relying on a single catastrophic instruction, the attack leverages [[skill|Skill Composition]] to reconstruct an attacker-specified payload. Key features include:

*   **Payload Partitioning:** An encrypted malicious payload is fragmented and distributed across multiple, seemingly harmless skill invocations.
*   **Trigger-Based Activation:** The reconstructed payload only executes when a predefined, specific trigger is encountered during the agent's operational workflow.
*   **Automated Synthesis:** The framework supports the automated creation of backdoored skills from arbitrary templates, enabling the scalable propagation of the attack across [[from-large-language-model-predicates-to-logic-tensor-networks-neurosymbolic-offe|Large Language Model]] (LLM) ecosystems.

## Experimental Results and Impact

To facilitate systematic evaluation, the researchers released a dataset of over 3,000 curated backdoored skills spanning various patterns and configurations. Evaluations conducted in representative code-based agent environments demonstrate the high efficacy of the attack with minimal impact on utility. 

Specifically, on the EHR SQL benchmark, SkillTrojan achieved an **Attack Success Rate (ASR) of up to 97.2%**, while maintaining a **Clean Accuracy (ACC) of 89.3%** on the GPT-5.2-1211-Global model.

## Implications for [[robust-ai-security-and-alignment-a-sisyphean-endeavor|AI Security]]

The findings reveal a critical security blind spot in modern [[Agentic Workflows]]. Because the malicious behavior is distributed across the composition of skills rather than a single module, standard detection methods that inspect individual skills in isolation may fail to detect the threat. This research emphasizes the urgent need for new [[security|Cybersecurity]] defenses that can reason about the security of complex, composite execution paths within [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] architectures.