---
title: A Comprehensive Survey of Agents for Computer Use: Foundations, Challenges, and Future Directions
created: 2024-05-22
source: https://arxiv.org/abs/2501.16150
tags: [agents, automation, computer-use, survey, ai]
category: ai

# A Comprehensive Survey of Agents for Computer Use

[[Agents for Computer Use]] (ACUs) represent an emerging class of [[Artificial Intelligence]] systems capable of executing complex digital tasks—ranging from desktop automation to mobile interaction—using only natural language instructions. By mimicking human-like interactions such as mouse clicks and touchscreen gestures, these agents aim to provide high-level [[Automation]] for software control across various platforms.

## Taxonomy of the ACU Landscape

The paper provides a unifying framework to understand the current state of ACU development across three specific dimensions:

1.  **Domain Perspective**: Characterizing the various operating contexts, including web platforms, mobile operating systems, and desktop environments.
2.  **Interaction Perspective**: Analyzing the modalities used for perception and action. This includes observation methods like [[Computer Vision]] (screenshots) and [[HTML]] analysis, as well as action methods such as mouse manipulation, keyboard input, and direct code execution.
3.  **Agent Perspective**: Detailing the underlying architectures regarding how agents perceive their environment, reason through steps, and learn from interaction.

## Current Challenges and Research Gaps

After reviewing 87 distinct ACUs and 33 datasets, the authors identify six significant barriers preventing ACUs from becoming mature tools for everyday use:

*   **Insufficient Generalization**: Difficulty adapting to new or unseen software interfaces.
*   **Inefficient Learning**: The high computational or data cost of developing effective agents.
*   **Limited Planning**: Weaknesses in long-horizon reasoning and complex decision-making.
*   **Benchmark Limitations**: Existing datasets often lack the complexity of real-world user tasks.
*   **Non-standardized Evaluation**: A lack of consistent, reliable metrics for measuring success.
*   **Research-to-Practice Disconnect**: A gap between laboratory performance and the constraints of actual deployment.

## Future Directions

To move toward robust