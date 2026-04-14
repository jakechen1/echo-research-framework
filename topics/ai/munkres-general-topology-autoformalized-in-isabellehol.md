---
title: Munkres' General Topology Autoformalized in Isabelle/HOL
created: 2024-05-22
source: https://arxiv.org/abs/2604.07455
tags: [autoformalization, isabelle, topology, llm, mathematics, formal_verification]
category: ai
---

# Munkers' General Topology Autoformalized in Isabelle/HOL

The paper "Munkres' General Topology Autoformalized in Isabelle/HOL" (arXiv:2604.07455) documents a landmark experiment in the field of [[autoformalization|Autoformalization]]. The project demonstrates the successful use of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) to translate the entirety of James Munkres' classic textbook, *Topology*, into the formal, machine-verifiable language of [[munkres-general-topology-autoformalized-in-isabellehol|Isabelle/HOL]].

### Project Scope and Scale
The scale of this formalization effort is unprecedented for a single-textbook project. Using LLM-based coding agents—specifically iterating from [[chatgpt|ChatGPT]] 5.2 to [[issue-claude-code-is-unusable-for-complex-engineering-tasks-with-feb-updates|Claude]] Opus 4.6—the researchers produced over 85,000 lines of formal code. The project covers all 39 sections of the textbook, ranging from fundamental topological spaces to complex [[dimension-theory|Dimension Theory]]. 

Most significantly, the project achieved total formal completeness. All 806 results presented in the book were fully proven within the [[munkres-general-topology-autoformalized-in-isabellehol|Isabelle/HOL]] environment, with zero "sorry" statements (unproven placeholders) remaining in the final output. This includes the formalization of high-level mathematical results such as:
* [[tychonoff-theorem|Tychonoff Theorem]]
* [[baire-category-theorem|Baire Category Theorem]]
* [[stoneech-compactification|Stone–Čech Compactification]]
* [[ascolis-theorem|Ascoli's Theorem]]
* [[nagatasmirnov-metrization-theorem|Nagata–Smirnov Metrization Theorem]]

### Methodology
The efficiency of the project was driven by a "sorry-first" declarative proof workflow. This method leverages the inherent strengths of the [[munkres-general-topology-autoformalized-in-isabellehol|Isabelle/HOL]] ecosystem, particularly the [[sledgehammer|Sledgehammer]] automation tool, to automate the heavy lifting of proof construction. By utilizing LLMs to generate initial structures and then employing