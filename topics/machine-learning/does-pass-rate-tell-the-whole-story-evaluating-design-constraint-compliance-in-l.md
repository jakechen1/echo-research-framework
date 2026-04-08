---
title: Does Pass Rate Tell the Whole Story? Evaluating Design Constraint Compliance in LLM-based Issue Resolution
created: 2024-05-24
source: https://arxiv.org/abs/2604.05955
tags: [LLM, Software Engineering, Benchmarking, AI Agents]
category: ai
---

# Does Pass Rate Tell the Whole Story?

The current landscape of [[Large Language Models]] (LLMs) evaluation for software engineering focuses heavily on repository-level issue resolution. Success is traditionally measured by "pass rates"—the ability of an agent to produce a patch that passes existing unit tests. However, this paper argues that this metric serves as an insufficient proxy for true patch quality.

## The Problem: Design Constraint Neglect
In professional software development, a "correct" patch must do more than simply pass functional tests. It must adhere to project-specific [[software design constraints]], including:
* Architectural conventions
* Error-handling policies
* Maintainability requirements

These constraints are often documented implicitly within code review discussions and are rarely captured by standard [[automated testing]] suites. Consequently, current [[AI Agents]] may solve functional bugs while simultaneously introducing structural technical debt or violating established patterns.

## Introducing [[bench]]
To address this gap, the authors propose the concept of **design-aware issue resolution** and introduce a new benchmark called [[bench]]. The researchers constructed this benchmark by mining and validating design constraints from real-world pull requests across six different repositories. The resulting dataset includes 495 issues and 1,787 validated constraints, specifically aligned with established benchmarks like [[SWE-bench-Verified]] and [[SWE-bench-Pro]].

## Key Findings
Experiments conducted on state-of-the-art agents yielded several critical insights:
1.  **Overestimation of Quality:** Test-based correctness substantially overestimates the actual quality of patches.
2.  **Low Compliance:** Fewer than 50% of resolved issues were found to be fully "design-satisfying."
3.  **Decoupled Metrics:** There is a negligible statistical association between functional correctness (passing tests) and design satisfaction.

## Conclusion
The study highlights a fundamental gap in the capabilities of current [[machine learning]] models applied to software engineering. It concludes that the industry must move toward [[design-aware evaluation]] to ensure that automated agents produce code that is not only functional but also architecturally sound and maintainable.