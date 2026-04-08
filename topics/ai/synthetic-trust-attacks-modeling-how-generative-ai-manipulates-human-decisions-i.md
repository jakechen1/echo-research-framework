---
title: Synthetic Trust Attacks: Modeling How Generative AI Manipulates Human Decisions in Social Engineering Fraud
created: 2024-05-22
source: https://arxiv.org/abs/2604.04951
tags: [AI, Cybersecurity, Social Engineering, Generative AI, Deepfakes]
category: ai
---

# Synthetic Trust Attacks: Modeling How Generative AI Manipulates Human Decisions in Social Engineering Fraud

## Overview
[[Synthetic Trust Attacks]] (STAs) represent a burgeoning class of [[Cybersecurity]] threats where [[Generative AI]] is utilized not merely to create deceptive media, but to systematically automate the manufacture of social credibility. Unlike traditional [[Social Engineering]], which relies on human-to-human manipulation, STAs leverage the scalability of [[Large Language Models]] and [[Deepfakes]] to industrialize the exploitation of human trust.

The paper highlights the real-world implications of this technology, citing a 2024 incident in Hong Kong where deepfake technology was used to impersonate corporate executives during a video conference, resulting in a $25 million loss. The core thesis is that the true attack surface is not the synthetic media itself, but the victim's cognitive decision-making process.

## The STAM Framework
To formalize this threat, the paper introduces the **Synthetic Trust Attack Model (STAM)**. STAM is an eight-stage operational framework that maps the entire attack lifecycle, ranging from initial adversary reconnaissance to post-compliance leverage (extracting value after the victim has complied with the fraudulent request).

The research highlights a critical failure in current defensive paradigms:
* **Detection Limitations:** Human accuracy in detecting deepfakes sits at approximately 55.5%, which is only marginally better than chance.
* **Agent Efficiency:** [[LLM]]-powered scam agents achieve a 46% compliance rate, vastly outperforming the 18% compliance rate seen with human-operated fraud.

## Shifting Defense to the Decision Layer
The authors argue that because the "perception layer" (the ability to identify fake media) is already failing, defensive strategies must migrate to the "decision layer." The paper introduces a **Trust-Cue Taxonomy** to categorize how attackers generate credibility and proposes a formal, research-grade defense protocol: **Calm, Check, Confirm**. This protocol is designed to provide a structured framework for humans to interrupt the manipulation cycle during high-pressure social engineering attempts.

## See Also
* [[Deepfakes]]
* [[Social Engineering]]
* [[Large Language Models]]
* [[AI Safety]]
* [[Human-Computer Interaction]]