---
title: "Realistic Market Impact Modeling For Reinforcement Learning Trading Environments"
category: machine-learning
created: 2026-04-12
---

title: Realistic Market Impact Modeling for Reinforcement Learning Trading Environments
created: 2024-05-22
source: https://arxiv.org/abs/2603.29086
tags: [reinforcement-learning, quantitative-finance, algorithmic-trading, market-impact]
category: machine-learning

# Realistic Market Impact Modeling for Reinforcement Learning Trading Environments

In the field of [[algorithmic-trading|Algorithmic Trading]], a significant gap exists between simulated backtesting and real-world execution. Most open-source [[deepsearch-overcome-the-bottleneck-of-reinforcement-learning-with-verifiable-rew|Reinforcement Learning]] (RL) environments utilize fixed or negligible transaction costs, which prevents agents from learning how to handle the price slippage and liquidity constraints inherent in live markets. This paper introduces a framework to bridge this gap by implementing realistic, non-linear market impact models.

## The MACE Suite

The researchers developed the **MACE** (Market-Adjusted Cost Execution) suite, a set of three [[gymnasium|Gymnasium]]-compatible environments designed for high-fidelity trading simulations. The suite includes:
*   **Stock Trading**
*   **Margin Trading**
*   **Portfolio Optimization**

Unlike traditional models, MACE integrates the [[almgren-chriss-framework|Almgren-Chriss framework]] and the empirically validated **square-root impact law**. These models allow for the tracking of permanent market impact with exponential decay, providing a much more rigorous test for [[deep-reinforcement-learning|Deep Reinforcement Learning]] (DRL) agents.

## Key Research Findings

The study evaluated several prominent DRL algorithms, including [[neppo-near-potential-policy-optimization-for-general-sum-multi-agent-reinforceme|PPO]], [[ddpg|DDPG]], [[flashsac-fast-and-stable-off-policy-reinforcement-learning-for-high-dimensional-|SAC]], [[a2c|A2C]], and [[td3|TD3]], using NASDAQ-100 datasets. The findings demonstrate that:

1.  **Algorithm Re-ranking:** The implementation of realistic cost models significantly alters both the absolute performance and the relative performance ranking of various algorithms.
2.  **Behavioral Shifts:** The inclusion of the