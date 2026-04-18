---
title: "EE-MCP: Self-Evolving MCP-GUI Agents via Automated Environment Generation and Experience Learning"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.09815"
tags: [ai, machine-learning, automation, agents]
category: [ai, machine-learning, technology]
---

# EE-MCP

**EE-MCP** is a novel framework designed to enhance the capabilities of [[Computer-use Agents]] by optimizing the interplay between structured [[Model Context Protocol]] (MCP) calls and unstructured [[Graphical User Interface]] (GUI) interactions. The research addresses the fundamental challenge of how an agent should balance these two distinct modalities to achieve autonomous task completion in complex software environments.

## Overview

As [[Artificial Intelligence]] moves toward more sophisticated desktop automation, agents must navigate both "structured" paths (APIs) and "unstructured" paths (visual clicking and typing). Current approaches often struggle to determine when an API call is superior to a GUI interaction, or how to iteratively improve performance without constant human supervision.

EE-MCP proposes a unified hybrid policy learning problem. The framework introduces a fully automated, self-evolving pipeline that requires no manual intervention. This involves:

*   **Automatic Environment Generation:** Creating and validating digital environments for testing.
*   **Trajectory Collection:** Harvesting interaction data from successful and failed tasks.
*   **Gap-driven Task Synthesis:** Automatically generating new training tasks specifically designed to address identified performance gaps.
*   **Quality-filtered Training:** Using high-quality data to refine the agent's decision-making capabilities.

## Key Innovations

### The Experience Bank
A standout feature of EE-MCP is the **experience bank**. Unlike traditional methods that rely solely on [[Fine-tuning]], the experience bank accumulates LLM-learned rules derived from trajectory comparisons. This allows for **inference-time improvement**, enabling the agent to apply learned logic dynamically during live tasks without requiring weight updates to the underlying model.

### Strategy Selection
The research demonstrates that the optimal learning strategy is task-dependent:
*   **Distillation:** Highly effective for **MCP-dominant tasks**, increasing the pass rate by 17.8pp to reach 77.8%.
*   **Experience Augmentation:** Outperforms other methods in **GUI-intensive tasks**, providing a 10.0pp boost.

Through this application-aware mechanism selection, EE-MCP provides a blueprint for the next generation of [[Autonomous Agents]] capable of mastering diverse, complex software ecosystems.