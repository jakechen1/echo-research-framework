title: "OmniDiagram: Advancing Unified Diagram Code Generation via Visual Interrogation Reward"
created: 2024-05-24
source: https://arxiv.org/abs/2604.05514
tags: [AI, Reinforcement Learning, Computer Vision, Data Visualization]
category: ai

# OmniDiagram

## Overview
**OmniDiagram** represents a significant leap in the field of [[Automated Programming]] and [[Data Visualization]]. As the paradigm of programmable diagram generation evolves, the industry faces challenges regarding fragmented language support and limited task applicability. OmniDiagram addresses these limitations through a unified framework designed to handle diverse diagram types and a wide array of diagram code languages.

## The VIVA Innovation
A primary challenge in training models for diagram generation is the alignment of programmatic code logic with the resulting visual fidelity. Traditional [[Reinforcement Learning]] (RL) approaches often rely on two-dimensional feedback: brittle syntax-based rules or pixel-level matching, both of which fail to capture high-level structural semantics.

To overcome this, the researchers introduced **Visual Interrogation Verifies All (VIVA)**. Unlike standard reward functions, VIVA utilizes a generative approach to provide feedback. The system actively generates targeted visual inquiries to scrutinize the rendered output. By asking specific questions about the visual structure, VIVA provides fine-grained feedback that allows the model to optimize its code for structural accuracy. This mechanism enables a self-evolving training process, effectively eliminating the need for massive amounts of manually annotated [[Ground Truth]] code.

## Dataset and Benchmarks
To support the development of this framework, the authors constructed **M3$^2$Diagram**, the first large-scale dataset specifically designed for diagram code generation. The dataset contains over 196,000 high-quality instances, providing the scale necessary for robust [[Machine Learning]] training.

Experimental evaluations confirm that the synergy between Supervised Fine-Tuning (SFT) and the VIVA-based RL strategy allows OmniDiagram to establish a new **State-of-the-art (SOTA)** across various diagram code generation benchmarks.

## See Also
* [[Generative AI]]
* [[Computer Vision]]
* [[Large Language Models]]
* [[Neural Architecture Search]]