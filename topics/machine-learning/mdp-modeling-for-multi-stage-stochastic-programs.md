---
title: "MDP modeling for multi-stage stochastic programs"
created: 2024-05-22
source: "https://arxiv.org/abs/2509.22981"
tags: [stochastic-programming, MDP, optimization, SDDP]
category: machine-learning
---

# MDP modeling for multi-stage stochastic programs

The research paper "MDP modeling for multi-stage stochastic programs" explores a sophisticated mathematical framework designed to bridge the gap between [[multi-stage-stochastic-programming|Multi-stage Stochastic Programming]] and [[markov-decision-processes-mdps|Markov Decision Processes (MDPs)]]. The authors propose a specific class of models that leverage the structural advantages of MDPs to handle complex, sequential decision-making processes under significant uncertainty.

### Key Modeling Features
The paper introduces several advanced modeling capabilities that extend beyond traditional stochastic programming. A significant focus is placed on accommodating [[continuous-action-spaces|Continuous Action Spaces]] and [[continuous-state-spaces|Continuous State Spaces]], which allows the model to represent much more complex and high-dimensional environments than standard discrete-only models. Key innovations include:

*   **Policy Graphs:** The expansion of policy graphs to include advanced features that represent intricate decision logic.
*   **Decision-dependent Uncertainty:** The implementation of one-step transition probabilities that are directly influenced by the decisions made by the controller. This introduces a higher level of realism to [[stochastic-modeling|Stochastic Modeling]] by accounting for how actions change the system's future risk profile.
*   **Statistical Learning Integration:** The framework incorporates elements of [[statistical-learning|Statistical Learning]], enabling the model to refine its understanding of transition probabilities through data-driven updates.

### Algorithmic Solutions
Solving programs with such high degrees of complexity and non-linearity presents significant computational hurdles. To address this, the authors develop new variants of [[stochastic-dual-dynamic-programming-sddp|Stochastic Dual Dynamic Programming (SDDP)]]. These