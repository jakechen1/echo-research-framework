---
title: Multi-Agent Pathfinding with Non-Unit Integer Edge Costs
created: 2024-05-24
source: https://arxiv.org/abs/2604.05416
tags: [multi-agent pathfinding, CBS, graph discretization, algorithms, robotics]
category: [ai, technology]
---

# Multi-Agent Pathfinding with Non-Unit Integer Edge Costs

The research presented in arXiv:2604.05416 addresses a fundamental limitation in [[Multi-Agent Pathfinding]] (MAPF). Traditionally, MAPF models operate under the assumption of unit edge costs and single-timestep actions. While these constraints allow for efficient computation, they lack the realism required for complex, real-world applications where movement durations and traversal costs vary significantly.

## The Challenge of Realism vs. Complexity

Previous attempts to extend MAPF to handle real-valued edge costs (often referred to as MAPFR) introduced a geometric collision model. However, this approach leads to an unbounded state space, which drastically reduces the efficiency of solvers. To bridge this gap, the authors introduce **MAPFZ**, a novel MAPF variant designed for graphs with non-unit integer costs. This model provides a much higher degree of realism than classical MAPF while ensuring the state space remains finite and computationally tractable.

## Proposed Innovations

The paper introduces two primary technological advancements to solve the MAPFZ problem:

1.  **CBS-NIC**: An enhanced [[Conflict-Based Search]] (CBS) framework. This method integrates time-interval-based conflict detection with an improved version of [[Safe Interval Path Planning]] (SIPP). By focusing on intervals rather than discrete timesteps, the algorithm can more effectively navigate agents through complex, non-uniform temporal constraints.
2.  **Bayesian Optimization for Graph Design (BOGD)**: A sophisticated discretization method used to handle non-unit edge costs. By employing [[Bayesian Optimization]], BOGD designs graph structures that balance computational efficiency with modeling accuracy, successfully achieving a sub-linear regret bound.

## Conclusion

Extensive experimental evaluations demonstrate that the proposed approach significantly outperforms existing state-of-the-art methods. The combination of CBS-NIC and BOGD shows superior performance in both runtime and success rates across various benchmark scenarios, marking a significant advancement in [[Algorithms]] for autonomous [[Robotics]] and coordinated system navigation.