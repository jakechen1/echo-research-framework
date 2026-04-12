---
title: "One Life to Learn: Inferring Symbolic World Models for Stochastic Environments from Unguided Exploration"
created: 2024-05-22
source: https://arxiv.org/abs/2510.12088
tags: [AI, Machine Learning, World Models, Probabilistic Programming, Reinforcement Learning]
category: machine-learning
---

# One Life to Learn

The research paper **"One Life to Learn"** addresses a critical gap in [[one-life-to-learn-inferring-symbolic-world-models-for-stochastic-environments-fr|Symbolic World Models]]: the ability to model complex, stochastic environments when interaction data is extremely scarce and human guidance is unavailable. While existing models excel in deterministic or heavily supervised settings, they often fail in "hostile" environments where an agent has only "one life" to learn the underlying rules of the world.

### The OneLife Framework

To solve this, the authors introduce **OneLife**, a framework that leverages [[probabilistic-programming|Probabilistic Programming]] to represent environmental dynamics as executable programs. Unlike traditional dense neural models, OneLife utilizes **conditionally-activated programmatic laws**. 

Each law within the system operates via a **precondition-effect structure**. A specific rule is only triggered when the agent's current state meets certain criteria. This mechanism creates a **dynamic computation graph**, which provides two major advantages:
1. **Scalability:** It routes inference and optimization only through the laws relevant to the current state, preventing computational explosions in hierarchical environments.
2. **Efficiency:** It enables the learning of stochastic dynamics even when certain rules are only rarely activated during the agent's short exploration period.

### Evaluation and Performance

The study evaluates the framework using **Crafter-OO**, a specialized version of the Crafter environment that provides an object-oriented symbolic state and a pure transition function. The authors established a new evaluation protocol focusing on two key metrics:
* **State Ranking:** The ability of the model to distinguish between plausible and implausible future trajectories.
* **State Fidelity:** The accuracy with which the model generates future states that mirror reality.

The results were significant, with OneLife outperforming strong baselines in **16 out of 23** tested scenarios. Additionally, the framework demonstrated robust [[automated-planning|Automated Planning]] capabilities, using simulated rollouts to successfully identify superior survival strategies.

### Conclusion

This work establishes a new foundation for [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] agents to autonomously construct programmatic world models. By moving away from human-dependent training, OneLife paves the way for agents capable of navigating and understanding entirely unknown, unpredictable, and complex ecosystems.