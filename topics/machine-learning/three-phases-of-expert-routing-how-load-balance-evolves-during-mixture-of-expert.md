---
title: Three Phases of Expert Routing: How Load Balance Evolves During Mixture-of-Experts Training
created: 2024-05-22
source: https://arxiv.org/abs/2604.04230
tags: [Mixture-of-Experts, Machine Learning, Neural Networks, Load Balancing]
category: machine-learning
---

# Three Phases of Expert Routing

The research paper **"Three Phases of Expert Routing: How Load Balance Evolves During Mixture-of-Experts Training"** introduces a novel framework for understanding the dynamic behavior of token routing in [[efficient-quantization-of-mixture-of-experts-with-theoretical-generalization-gua|Mixture-of-Experts]] (MoE) models. By modeling token routing as a [[congestion-game|Congestion Game]], the authors identify a non-monotone evolution of routing logic during the training process.

## The Congestion Game Framework

The authors propose that MoE token routing can be mathematically represented through a single effective parameter, the **congestion coefficient** ($\gamma_{eff}$). This coefficient quantifies the fundamental tradeoff between [[load-balancing|Load Balancing]] (ensuring all experts are used equally) and routing quality (ensuring tokens are sent to the most relevant experts). The study demonstrates that while the framework is a simplified model, it accurately captures the functional reality of how [[attention-sinks-are-provably-necessary-in-softmax-transformers-evidence-from-tri|Softmax]] temperature influences routing behavior.

## The Three-Phase Trajectory

Through the analysis of checkpoints from the OLMoE-1B-7B and OpenMoE-8B models, the researchers identified three distinct evolutionary stages in the router's behavior:

1.  **Surge Phase:** Occurring in the early stages of training (e.g., 30K–40K steps), the router focuses intensely on learning to distribute tokens. During this phase, $\gamma_{eff}$ rises sharply from 14 to nearly 39 as the system prioritizes establishing a baseline of load balance.
2.  **Stabilization Phase:** In the intermediate stage (100K–400K steps), the system enters a period of steady-state balance. Experts begin to specialize, but the router maintains a consistent level of load distribution.
3.  **Relaxation Phase:** In the late stages of training (400K–1.2M steps), the router shifts its priority. As experts become highly differentiated, the router is willing to trade perfect balance for higher routing quality, leading to a drop in $\gamma_{eff}$ from 27 down to approximately 9.

## Scientific Significance

This research is critical for [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] because these dynamics are invisible when analyzing only converged, post-training models. The discovery that MoE training shifts from a "balance-first" to a "quality-first" objective provides new insights for [[can-llms-beat-classical-hyperparameter-optimization-algorithms-a-study-on-autore|Hyperparameter Optimization]] and the development of more efficient [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]] architectures. The study's use of effective congestion decomposition further improves the ability to predict load distribution across complex neural layers.