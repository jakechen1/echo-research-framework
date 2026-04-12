---
title: "Invisible to Humans, Triggered by Agents: Stealthy Jailbreak Attacks on Mobile Vision-Language Agents"
created: 2024-05-22
source: https://arxiv.org/abs/2510.07809
tags: [jailbreak, mobile-agents, lvlm, cybersecurity, prompt-injection]
category: ai, technology
---

# Invisible to Humans, Triggered by Agents: Stealthy Jailbreak Attacks on Mobile Vision-Language Agents

The research paper "Invisible to Humans, Triggered by Agents" explores a critical security frontier in the deployment of [[large-vision-language-models-lvlms|Large Vision-Language Models (LVLMs)]] as autonomous [[mobile-agents|Mobile Agents]]. As these agents are increasingly granted the ability to navigate and operate smartphone user interfaces, they introduce unprecedented attack surfaces that are often overlooked by traditional [[cybersecurity|Cybersecurity]] frameworks.

### The Stealthy Attack Framework

The authors introduce a practical jailbreak framework designed to bypass the safety alignment of advanced models while remaining undetected by human users. The framework is built upon three sophisticated pillars:

1.  **Non-privileged Perception Compromise**: The attack injects malicious visual payloads directly into the application interface. Unlike previous research that relies on intrusive overlays or elevated system permissions, this method functions within standard user-level permissions, making it highly realistic for real-world [[android-coach-improve-online-agentic-training-efficiency-with-single-state-multi|Android]] environments.
2.  **Agent-Attributable Activation**: To maintain stealth, the framework uses input attribution signals to distinguish between human and agent interactions. By limiting the exposure of malicious prompts to transient intervals, the attack avoids alerting the end user.
3.  **Efficient One-Shot Jailbreak (HG-IDA*)**: The researchers developed a heuristic iterative deepening search algorithm, HG-IDA*. This algorithm performs keyword-level detoxification, allowing the attack to bypass the built-in safety guardrails of the LVLM.

### Experimental Results and Impact

To assess the vulnerability, the researchers curated a dedicated [[piarena-a-platform-for-prompt-injection-evaluation|Prompt Injection]] dataset and tested it across various backends, including both open-source models and high-profile closed-source services like [[gpt-4o|GPT-4o]]. The results demonstrated alarming success rates, specifically achieving an 82.5% planning hijack rate and a 75.0% execution hijack rate on [[gpt-4o|GPT-4o]].

These findings present a significant warning for the development of autonomous operating systems. The ability to hijack an agent's planning and execution without human detection underscores a fundamental flaw in current [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] safety protocols, necessitating a shift toward more robust, agent-aware security architectures.