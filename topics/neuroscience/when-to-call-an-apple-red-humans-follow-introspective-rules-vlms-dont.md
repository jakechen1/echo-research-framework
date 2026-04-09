---
title: When to Call an Apple Red: Humans Follow Introspective Rules, VLMs Don't
created: 2024-05-22
source: https://arxiv.org/abs/2604.06422
tags: [Vision-Language Models, Introspection, Cognitive Science, AI Reliability, Graded Color Attribution]
category: ai, machine-learning, neuroscience
---

# When to Call an Apple Red: Humans Follow Introspective Rules, VLMs Don't

The research paper "When to Call an Apple Red" investigates a critical challenge in the [[trustworthy deployment]] of [[Vision-Language Models (VLMs)]]: the gap between a model's stated [[introspective reasoning]] and its actual decision-making behavior. The study explores whether models can reliably predict their own logic or if they are prone to [[reasoning failures]].

### The GCA Benchmark
To evaluate this, the authors introduced the [[Graded Color Attribution (GCA)]] dataset. This controlled benchmark utilizes line drawings where pixel-level color coverage varies across three specific conditions:
*   **World-knowledge recolorings:** Relying on standard color associations.
*   **Counterfactual recolorings:** Challenging existing color priors.
*   **Shapes with no color priors:** Neutral color environments.

The goal was to determine if participants (both humans and machines) establish a threshold—a minimum percentage of color coverage—and consistently adhere to that threshold when making final color attributions.

### Human vs. Machine Performance
The findings reveal a stark divergence between [[human cognition]] and [[machine learning]] capabilities. 

*   **Human Participants:** Humans demonstrated high levels of **faithfulness**. While humans occasionally appeared to violate rules, these errors were attributed to a documented cognitive tendency to overestimate color coverage rather than a failure of logic.
*   **Vision-Language Models:** VLMs exhibit significant [[miscalibration]]. Despite being excellent estimators of color coverage, models like GPT-5-mini were found to violate their own stated introspective rules in nearly 60% of cases involving strong color priors.

### Implications for AI
The study suggests that VLM errors are not merely the result of task difficulty. Instead, the models suffer from a fundamental lack of self-knowledge, where their internal reasoning does not align with their outputs. As [[world-knowledge priors]] systematically degrade the faithfulness of these models, this discrepancy poses significant risks for [[high-stakes deployment]] in environments where [[AI reliability]] is paramount.