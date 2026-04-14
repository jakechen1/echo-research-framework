---
title: Preference Redirection via Attention Concentration: An Attack on Computer Use Agents
created: 2024-05-22
source: https://arxiv.org/abs/2604.08005
tags: [Computer Use Agents, Adversarial Attacks, Vision-Language Models, AI Security]
category: ai, machine-learning, technology
author: wiki-pipeline
dc.title: "Preference Redirection via Attention Concentration: An Attack on Computer Use Agents"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/preference-redirection-via-attention-concentration-an-attack-on-computer-use-age.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Preference Redirection via Attention Concentration: An Attack on Computer Use Agents

The research paper "Preference Redirection via Attention Concentration: An Attack on Computer Use Agents" explores a critical security vulnerability within the emerging field of [[intentscore-intent-conditioned-action-evaluation-for-computer-use-agents|Computer Use Agents]] (CUAs). As [[Multimodal Foundation Models]] advance, they are increasingly being deployed to interact autonomously with complex [[GUI Environments]], capable of executing tasks ranging from data entry to online commerce. However, this increased autonomy introduces significant risks to [[machine-learning|Machine Learning Security]].

### The PRAC Attack Mechanism

The authors introduce **PRAC**, a novel [[explainability-guided-adversarial-attacks-on-transformer-based-malware-detectors|Adversarial Attack]] that targets the vision modality of [[aligned-vector-quantization-for-edge-cloud-collabrative-vision-language-models|Vision-Language Models]] (VLMs). While much of the existing security research has focused on manipulating the linguistic outputs or text prompts of models, PRAC operates by manipulating the model's internal decision-making processes. 

The attack functions by redirecting the model's internal attention toward a stealthy [[caap-capture-aware-adversarial-patch-attacks-on-palmprint-recognition-models|Adversarial Patch]]. Rather than attempting to force a specific text response, PRAC alters the model's underlying "preferences" by concentrating its attention on specific visual elements. This manipulation is subtle and occurs within the model's internal attention layers, making it difficult to detect through standard output monitoring.

### Experimental Findings and Implications

The researchers demonstrated the practical impact of PRAC by applying it to an online shopping platform. The attack successfully manipulated the CUA's selection process, steering the agent toward a pre-selected target product by altering its visual perception of the shopping interface. 

A major concern highlighted in the paper is the attack's ability to generalize. Although the researchers utilized white-box access to design the initial attack, they demonstrated that PRAC remains effective against fine-tuned versions of the same model. This poses a systemic threat to the ecosystem of [[Open Weights Models]], where many companies build specialized, task-specific agents. If the base model is susceptible to attention redirection, the downstream specialized agents will inherit this fundamental vulnerability, potentially leading to unauthorized or manipulated autonomous actions in sensitive environments.