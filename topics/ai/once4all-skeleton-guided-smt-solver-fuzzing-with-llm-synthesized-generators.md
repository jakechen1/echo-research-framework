---
title: Once4All: Skeleton-Guided SMT Solver Fuzzing with LLM-Synthesized Generators
created: 2024-05-22
source: https://arxiv.org/abs/2508.20340
tags: [SMT Solvers, Large Language Models, Fuzzing, Software Verification, Automated Testing]
category: ai
---

# Once4All: Skeleton-Guided SMT Solver Fuzzing

**Once4All** is an innovative [[artificial-intelligence-and-the-structure-of-mathematics|Artificial Intelligence]]-driven fuzzing framework designed to enhance the testing and reliability of [[satisfiability-modulo-theory-smt-solvers|Satisfiability Modulo Theory (SMT) Solvers]]. Because SMT solvers serve as the backbone for critical tasks such as [[symbolic-execution|Symbolic Execution]] and [[automated-verification|Automated Verification]], maintaining their correctness is essential for the security of modern software and programming languages.

## The Problem: Syntax and Overhead
As SMT solvers evolve, traditional [[once4all-skeleton-guided-smt-solver-fuzzing-with-llm-synthesized-generators|Fuzzing]] techniques struggle to cover new, complex features. While recent research has leveraged [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) to generate test formulas, two significant bottlenecks remain:
1. **Syntactic Invalidity**: Nearly half of the formulas generated directly by LLMs are syntactically incorrect, making them useless for testing.
2. **Computational Cost**: Performing iterative, real-time interactions with LLMs during the fuzzing process introduces substantial latency and high operational costs.

## The Once4All Approach
Once4All solves these issues by shifting the LLM's responsibility from generating raw formulas to synthesizing **generators** for reusable components. The framework follows a structured pipeline:

1. **Grammar Extraction**: The LLM parses solver documentation to automatically extract [[context-free-grammars|Context-Free Grammars]] (CFGs). This allows the framework to understand both standard SMT theories and solver-specific extensions.
2. **Generator Synthesis**: The LLM synthesizes composable Boolean term generators that strictly adhere to the extracted CFGs, ensuring that all generated parts are syntactically sound.
3. **Skeleton-Guided Population**: During the fuzzing runtime, the system uses "structural skeletons" (templates derived from existing valid formulas) and populates them with new, diverse terms produced by the synthesized generators.

## Results and Impact
By utilizing a one-time LLM interaction investment, Once4All dramatically reduces runtime overhead while maintaining high semantic diversity. In evaluations performed on the leading [[z3|Z3]] and [[cvc5]] solvers, the framework successfully discovered **43 confirmed bugs**, 40 of which had already been addressed by the developers, proving its efficacy in identifying high-impact vulnerabilities in critical software infrastructure.