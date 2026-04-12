---
title: CODESTRUCT: Code Agents over Structured Action Spaces
created: 2024-05-22
source: https://arxiv.org/abs/2604.05407
tags: [code-agents, LLM, software-engineering, AST, automation]
category: ai
---

# CODESTRUCT: Code Agents over Structured Action Spaces

**CODESTRUCT** represents a fundamental shift in the methodology used by [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] to interact with complex software repositories. Historically, [[codestruct-code-agents-over-structured-action-spaces|code agents]] have treated codebases as unstructured sequences of text. This approach relies heavily on brittle string-matching techniques for applying edits, a process that is highly susceptible to failure caused by [[formatting-drift|formatting drift]], ambiguous code patterns, and syntactic errors.

## The Problem: Unstructured Text Manipulation
In traditional text-based interfaces, agents attempt to locate and replace specific spans of text. This methodology often fails when the agent's predicted patch does not perfectly align with the existing indentation or surrounding context, leading to "empty-patch" failures where the agent's instructions are syntactically invalid or contextually lost.

## The Solution: Structured Action Spaces
The CODESTRUCT framework proposes reframing the codebase as a structured action space. Rather than manipulating raw text, the framework allows agents to operate on named entities derived from [[abstract-syntax-trees|Abstract Syntax Trees]] (AST). By leveraging the underlying syntax of the program, the framework introduces two key operational primitives:

*   **readCode**: A mechanism for retrieving complete, syntactically coherent units of code, ensuring the agent has full context of the semantic element.
*   **editCode**: A tool for applying transformations to semantic program elements that are validated against the program's actual syntax, preventing the introduction of structural errors.

## Performance and Efficiency
Evaluations conducted on [[swe-bench-verified|SWE-bench Verified]] across multiple LLMs demonstrate significant advantages. The framework improved Pass@1 accuracy by 1.2% to 5.0% while simultaneously reducing token consumption by 12% to 38%. 

The benefit is most pronounced in models that struggle with text-based precision. For example, **GPT-5-nano** saw a dramatic performance increase of 20.8%, primarily driven by a reduction in empty-patch failures from 46.6% to just 7.2%. Furthermore, testing on [[codeassistbench|CodeAssistBench]] showed consistent accuracy gains and cost reductions of up to 33%.

## Conclusion
By moving from text-based manipulation to a structure-aware interface, CODESTRUCT provides a more reliable and resource-efficient foundation for the next generation of [[claw-eval-toward-trustworthy-evaluation-of-autonomous-agents|Autonomous Agents]] in [[triage-routing-software-engineering-tasks-to-cost-effective-llm-tiers-via-code-q|software engineering]].