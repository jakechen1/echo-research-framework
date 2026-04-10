---
title: Munkres' General Topology Autoformalized in Isabelle/HOL
created: 2024-05-22
source: https://arxiv.org/abs/2604.07455
tags: [autoformalization, isabelle, topology, llm, mathematics, formal_verification]
category: ai
---

# Munkers' General Topology Autoformalized in Isabelle/HOL

The paper "Munkres' General Topology Autoformalized in Isabelle/HOL" (arXiv:2604.07455) documents a landmark experiment in the field of [[Autoformalization]]. The project demonstrates the successful use of [[Large Language Models]] (LLMs) to translate the entirety of James Munkres' classic textbook, *Topology*, into the formal, machine-verifiable language of [[Isabelle/HOL]].

### Project Scope and Scale
The scale of this formalization effort is unprecedented for a single-textbook project. Using LLM-based coding agents—specifically iterating from [[ChatGPT]] 5.2 to [[Claude]] Opus 4.6—the researchers produced over 85,000 lines of formal code. The project covers all 39 sections of the textbook, ranging from fundamental topological spaces to complex [[Dimension Theory]]. 

Most significantly, the project achieved total formal completeness. All 806 results presented in the book were fully proven within the [[Isabelle/HOL]] environment, with zero "sorry" statements (unproven placeholders) remaining in the final output. This includes the formalization of high-level mathematical results such as:
* [[Tychonoff Theorem]]
* [[Baire Category Theorem]]
* [[Stone–Čech Compactification]]
* [[Ascoli's Theorem]]
* [[Nagata–Smirnov Metrization Theorem]]

### Methodology
The efficiency of the project was driven by a "sorry-first" declarative proof workflow. This method leverages the inherent strengths of the [[Isabelle/HOL]] ecosystem, particularly the [[Sledgehammer]] automation tool, to automate the heavy lifting of proof construction. By utilizing LLMs to generate initial structures and then employing