---
title: "AEROS: A Single-Agent Operating Architecture with Embodied Capability Modules"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.07039"
tags: [ai, robotics, operating-systems, embodied-intelligence]
category: technology
author: wiki-pipeline
dc.title: "AEROS: A Single-Agent Operating Architecture with Embodied Capability Modules"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/aeros-a-single-agent-operating-architecture-with-embodied-capability-modules.md
dc.language: en
dc.rights: CC-BY-4.0
---

# AEROS

**AEROS** (Agent Execution Runtime Operating System) represents a paradigm shift in how [[ai-driven-marine-robotics-emerging-trends-in-underwater-perception-and-ecosystem|Robotics]] systems are structured. Traditional robotic architectures often struggle with a lack of principled abstraction, frequently oscillating between monolithic structures that are difficult to update and loosely coordinated multi-agent systems that lack a unified sense of identity and control authority.

## Core Concept: The Single Persistent Agent

The fundamental thesis of AEROS is that a robot should be modeled as a single, persistent intelligent subject. Rather than being a collection of fragmented scripts, the robot acts as a stable agent whose functional reach is extended through **Embodied Capability Modules (ECMs)**. 

These ECMs function similarly to installable software packages. Each module encapsulates:
* Executable skills and primitives.
* Specialized neural models.
* Integrated computational tools.

This architecture enables **modular extensibility**, allowing developers to "hot-swap" capabilities at runtime—a process the researchers demonstrated leads to 100% success in post-swap tasks.

## Safety and Runtime Enforcement

A defining feature of AEROS is the separation of capability execution from a **policy-separated runtime**. While ECMs provide the "intelligence" and "skills," the runtime environment enforces execution constraints and safety guarantees. This separation is vital for [[Safety-Critical Systems]], as it creates a formal boundary that prevents high-level logic errors from translating into physical harm. In testing, this layer successfully blocked all invalid actions with zero false acceptances.

## Performance and Evaluation

The efficacy of AEROS was validated using a Franka Panda 7-DOF manipulator within a [[PyBullet]] simulation environment. The architecture was compared against standard industry benchmarks, including [[BehaviorTree.CPP]] and [[ProgPrompt]]. 

The results showed a significant leap in reliability:
* **AEROS:** Achieved 100% task success across primary test scenarios.
* **BehaviorTree/ProgPrompt Baselines:** Achieved 92–93% success.
* **Flat Pipelines:** Achieved only 67–73% success.

AEROS demonstrated particular strength in [[Failure Recovery]] and cross-task generality, proving that the architecture provides intrinsic benefits to [[dynamic-agentic-ai-expert-profiler-system-architecture-for-multidomain-intellige|Agentic AI]] that do not require task-specific tuning.