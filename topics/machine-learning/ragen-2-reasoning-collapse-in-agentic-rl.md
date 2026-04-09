---
title: RAGEN-2: Reasoning Collapse in Agentic RL
created: 2024-05-22
source: https://arxiv.org/abs/2604.06268
tags: [ai, machine-learning, LLM, reinforcement-learning]
category: ai, machine-learning
---

# RAGEN-2: Reasoning Collapse in Agentic RL

The paper **RAGEN-2** identifies a critical and previously unrecognized failure mode in the [[Reinforcement Learning]] (RL) training of [[Large Language Models]] (LLMs) acting as autonomous agents. The researchers introduce the concept of **template collapse**, a phenomenon where agents develop reasoning patterns that become "input-agnostic."

### The Problem: Beyond Entropy
In the development of [[LLM Agents]], [[Entropy]] is the standard metric used to track the stability of reasoning. However, the authors demonstrate that entropy is an insufficient metric for evaluating agentic intelligence. While entropy measures how much a model varies its output for a *single* input, it fails to capture whether the model's reasoning actually changes in response to *different* inputs. 

In a state of "template collapse," a model may maintain high entropy (showing linguistic diversity) while actually relying on fixed, repetitive templates that ignore the specific nuances of the task. This makes the collapse invisible to all existing training metrics.

### Diagnosis via Mutual Information
To solve this diagnostic gap, RAGEN-2 proposes decomposing reasoning quality into two distinct dimensions:
1. **Within-input diversity**: Measured by [[Entropy]].
2. **Cross-input distinguishability**: Measured by [[Mutual Information]] (MI).

By utilizing MI proxies, the researchers proved that Mutual Information correlates much more strongly with successful task performance than entropy does, providing a reliable way to detect when an agent is losing its ability to reason contextually.

### The Mechanism and Solution
The authors attribute this collapse to a drop in the [[Signal-to-Noise Ratio]] (SNR). During training, low reward variance weakens the task-specific gradients. This allows regularization terms to dominate the loss function, essentially "erasing" the model's ability to differentiate between different inputs.

To combat this, the paper introduces **SNR-Aware Filtering**. This method uses reward variance as a lightweight proxy to select high-signal prompts during each training iteration. This approach has demonstrated consistent improvements in complex domains, including:
* [[Mathematical Reasoning]]
* Web navigation
* Code execution
* Strategic planning