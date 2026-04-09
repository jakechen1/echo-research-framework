---
title: LeLaR: The First In-Orbit Demonstration of an AI-Based Satellite Attitude Controller
created: 2024-05-22
source: https://arxiv.org/abs/2512.19576
tags: [space-technology, deep-reinforcement-learning, nanosatellites, autonomous-systems]
category: technology
---

# LeLaR: The First In-Orbit Demonstration of an AI-Based Satellite Attitude Controller

LeLaR represents a landmark achievement in [[Space Technology]], marking the first successful in-orbit demonstration of an attitude controller powered by [[Deep Reinforcement Learning]] (DRL). Traditionally, the control of satellite orientation—known as attitude control—has relied on [[Classical Control]] methods. While effective, these traditional controllers are often difficult to design for complex scenarios and remain sensitive to model uncertainties and shifting operational boundaries.

## Overcoming the Sim2Real Gap

A major hurdle in the application of [[Machine Learning]] to orbital mechanics is the "Sim2Real gap." This refers to the discrepancy between an agent's performance in a highly controlled [[Simulation]] and its behavior when deployed on physical hardware. The LeLaR project addresses this by developing an AI agent capable of learning adaptive control strategies through autonomous interaction within a simulation environment, specifically optimized to handle the transition to real-world physics.

## Mission Implementation

The controller was successfully deployed on the **InnoCube 3U nanosatellite**, a project developed through the collaboration of the [[Julius-Maximilians-Universität Würzburg]] and the [[Technische Universität Berlin]]. Launched in January 2025, the mission provided a live environment to test the AI agent's ability to execute inertial pointing maneuvers.

## Experimental Results

The research provides a detailed comparative analysis between the new AI-based controller and the conventional [[Proportional-Derivative (PD) Controller]] utilized by the InnoCube. Key areas of investigation included:

*   **Training Methodology:** The design of the AI agent and the procedural learning steps taken in simulation.
*   **Discrepancy Analysis:** Identifying the gaps between simulated predictions and observed satellite behavior in orbit.
*   **Performance Metrics:** Evaluating steady-state accuracy during repeated maneuvers.

The findings confirm that despite the complexities of the orbital environment, the AI-based controller demonstrates robust performance and maintains high stability, proving that [[Autonomous Systems]] are a viable and powerful alternative for future [[Satellite Technology]] missions.