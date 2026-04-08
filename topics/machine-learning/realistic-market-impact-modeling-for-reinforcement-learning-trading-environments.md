title: Realistic Market Impact Modeling for Reinforcement Learning Trading Environments
created: 2024-05-22
source: https://arxiv.org/abs/2603.29086
tags: [reinforcement-learning, quantitative-finance, algorithmic-trading, market-impact]
category: machine-learning

# Realistic Market Impact Modeling for Reinforcement Learning Trading Environments

In the field of [[Algorithmic Trading]], a significant gap exists between simulated backtesting and real-world execution. Most open-source [[Reinforcement Learning]] (RL) environments utilize fixed or negligible transaction costs, which prevents agents from learning how to handle the price slippage and liquidity constraints inherent in live markets. This paper introduces a framework to bridge this gap by implementing realistic, non-linear market impact models.

## The MACE Suite

The researchers developed the **MACE** (Market-Adjusted Cost Execution) suite, a set of three [[Gymnasium]]-compatible environments designed for high-fidelity trading simulations. The suite includes:
*   **Stock Trading**
*   **Margin Trading**
*   **Portfolio Optimization**

Unlike traditional models, MACE integrates the [[Almgren-Chriss framework]] and the empirically validated **square-root impact law**. These models allow for the tracking of permanent market impact with exponential decay, providing a much more rigorous test for [[Deep Reinforcement Learning]] (DRL) agents.

## Key Research Findings

The study evaluated several prominent DRL algorithms, including [[PPO]], [[DDPG]], [[SAC]], [[A2C]], and [[TD3]], using NASDAQ-100 datasets. The findings demonstrate that:

1.  **Algorithm Re-ranking:** The implementation of realistic cost models significantly alters both the absolute performance and the relative performance ranking of various algorithms.
2.  **Behavioral Shifts:** The inclusion of the