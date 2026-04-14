---
title: ReDAct: Uncertainty-Aware Deferral for LLM Agents
created: 2024-05-22
source: https://arxiv.org/abs/2604.07036
tags: [LLM, Agentic-Workflows, Uncertainty-Estimation, Cost-Optimization]
category: ai
---

# ReDAct: Uncertainty-Aware Deferral for LLM Agents

**ReDAct** (Reason-Defer-Act) is a specialized framework designed to address the critical tension between computational efficiency and decision accuracy in [[from-large-language-model-predicates-to-logic-tensor-networks-neurosymbolic-offe|Large Language Model]] (LLM) agents. As agents are increasingly deployed for [[sequential-decision-making|Sequential Decision-Making]] tasks, the risk of [[blending-human-and-llm-expertise-to-detect-hallucinations-and-omissions-in-menta|Hallucinations]] becomes a significant bottleneck; in multi-step environments, a single incorrect action can lead to irreversible failures in a task's trajectory.

### The Core Challenge
In the current landscape of [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]], there is a direct correlation between model scale and reliability. While larger, more sophisticated models exhibit lower error rates, they incur significantly higher [[inference-cost|Inference Cost]] and latency. Conversely, smaller models are highly efficient but prone to errors that can degrade the performance of autonomous agents.

### The ReDAct Mechanism
The ReDAct framework proposes a dual-model architecture to optimize this trade-off. The system employs two distinct LLMs:
1.  **A Small, Efficient Model:** This model acts as the primary worker, handling the majority of the decision-making steps by default.
2.  **A Large, Reliable Model:** This model serves as a high-fidelity fallback.

The innovation lies in the **uncertainty-aware deferral** process. The agent monitors the predictive uncertainty of the small model. When the uncertainty exceeds a specifically calibrated threshold, the decision-making responsibility is **deferred** to the larger model. This ensures that complex or ambiguous steps are handled with high precision, while straightforward steps remain inexpensive.

### Experimental Results
The efficacy of ReDAct was evaluated within text-based embodied environments, including [[alfworld|ALFWorld]] and [[minigrid|MiniGrid]]. The findings indicate that the framework is highly optimized for resource management: by deferring only approximately **15% of decisions** to the larger model, the agent can match the decision quality of a system using the large model exclusively. This reduction in calls to the larger LLM leads to a massive decrease in total token consumption and computational overhead without compromising the success rate of the agent.

### Related Topics
* [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]
* [[decocted-experience-improves-test-time-inference-in-llm-agents|LLM Agents]]
* [[uncertainty-estimation-for-deep-reconstruction-in-actuatic-disaster-scenarios-wi|Uncertainty Estimation]]
* [[claw-eval-toward-trustworthy-evaluation-of-autonomous-agents|Autonomous Agents]]
* [[cost-efficient-ai|Cost-Efficient AI]]