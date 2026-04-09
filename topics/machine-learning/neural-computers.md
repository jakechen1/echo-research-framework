---
title: Neural Computers
created: 2024-05-23
source: https://arxiv.org/abs/2604.06425
tags: [neural-computers, computing-paradigm, machine-learning, automation]
category: ai, machine-learning, technology
---

# Neural Computers

**Neural Computers (NCs)** represent an emerging frontier in computational architecture, proposing a fundamental shift in how machines process information. Unlike [[Conventional Computers]], which execute explicit, predefined programs, or [[AI Agents]], which operate by acting upon external environments, Neural Computers aim to collapse the distinction between the processor and the program. The core objective is to unify computation, memory, and I/O (Input/Output) into a single, learned runtime state.

## Core Concept

The defining characteristic of an NC is that the model itself serves as the running computer. While current [[World Models]] focus on learning the dynamics of an environment, NCs seek to internalize the execution of tasks within their own architecture. This leads to the long-term research goal: the **[[Completely Neural Computer (CNC)]]**. 

The CNC is envisioned as a mature, general-purpose realization of this machine form. Its key features would include:
*   **Stable Execution:** Reliable processing of complex instruction sets.
*   **Explicit Reprogramming:** The ability to alter the model's computational logic without retraining the entire architecture.
*   **Durable Capability Reuse:** The capacity to store and deploy learned primitives across various tasks.

## Current Research and Implementation

Initial studies focus on whether early NC primitives can be learned purely from collected I/O traces, bypassing the need for instrumented program states. Researchers have instantiated these early NCs as **video models** capable of generating frame sequences (rollouts) based on instructions, pixels, and user actions. 

By applying these models to [[Command Line Interface (CLI)]] and [[Graphical User Interface (GUI)]] settings, researchers have observed that learned runtimes can acquire basic interface primitives. Specifically, these models demonstrate success in **I/O alignment** and **short-horizon control**.

## Challenges and Future Roadmap

Despite early successes, the transition to a full CNC faces several critical bottlenecks:
1.  **Symbolic Stability:** Maintaining consistent logic over long-duration tasks.
*   **Routine Reuse:** Effectively leveraging previously learned computational patterns in new contexts.
*   **Controlled Updates:** Implementing updates to the model's capabilities without degrading existing performance.

Overcoming these challenges is essential to establishing a new computing paradigm that transcends the limitations of contemporary [[Machine Learning]] and traditional software engineering.