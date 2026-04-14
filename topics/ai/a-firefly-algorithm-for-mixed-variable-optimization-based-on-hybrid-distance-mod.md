---
title: "A Firefly Algorithm For Mixed Variable Optimization Based On Hybrid Distance Mod"
category: artificial-intelligence
created: 2026-04-12
---

title: A Firefly Algorithm for Mixed-Variable Optimization Based on Hybrid Distance Modeling
created: 2024-05-22
source: https://arxiv.org/abs/2603.26792
tags: [firefly-algorithm, optimization, mixed-variable, metaheuristics, artificial-intelligence]
category: ai

# A Firefly Algorithm for Mixed-Variable Optimization Based on Hybrid Distance Modeling

## Introduction
A significant challenge in modern [[optimization-problems|Optimization Problems]] is the management of mixed-variable search spaces. In these environments, decision variables are heterogeneous, consisting of continuous, ordinal, and categorical types. Most existing [[metaheuristic-algorithms|Metaheuristic Algorithms]] are designed for either purely continuous or purely discrete optimization, making them poorly suited for handling the complexities of unified, mixed-type landscapes.

## The FAmv Approach
This paper proposes a specialized adaptation of the [[a-firefly-algorithm-for-mixed-variable-optimization-based-on-hybrid-distance-mod|Firefly Algorithm]], named **FAmv** (Firefly Algorithm for mixed-variable optimization). The fundamental contribution of this research is the implementation of a **hybrid distance modeling** mechanism. This modified distance-based attractiveness model integrates continuous and discrete components within a single, unified mathematical framework.

The primary goal of this mixed-distance approach is to provide a more accurate representation of the heterogeneous search space. By doing so, the algorithm maintains an optimal balance between:
*   **Exploration**: The ability of the algorithm to traverse new and unvisited regions of the search space.
