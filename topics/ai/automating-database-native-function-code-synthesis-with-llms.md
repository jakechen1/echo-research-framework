---
title: Automating Database-Native Function Code Synthesis with LLMs
created: 2024-05-22
source: https://arxiv.org/abs/2604.06231
tags: [LLM, Database, Code-Generation, Automation]
categories: [ai, technology]
---

# Automating Database-Native Function Code Synthesis with LLMs

The continuous evolution of [[Database Systems]] necessitates the integration of an increasing number of database-native functions within their kernels to support modern applications and business migrations. However, the manual synthesis of these functions is both complex and error-prone, as it involves registering multiple function units, linking internal references, and ensuring precise implementation logic.

## The Challenge of Generic LLMs
While recent breakthroughs in [[Large Language Models]] (LLMs) have significantly advanced [[Code Generation]], generic models (such as Claude Code) often struggle with database-specific development. These models frequently suffer from hallucinations or overlook the critical context required for database kernels, specifically regarding the intricate dependencies between function units and the registration of internal references.

## Introducing DBCooker
To mitigate these issues, the researchers proposed **DBCooker**, a specialized LLM-based system designed for the automated synthesis of database-native functions. DBCooker operates through three primary architectural components:

1.  **Function Characterization Module**: This module aggregates multi-source declarations, identifies specific function units that require specialized coding, and traces essential cross-unit dependencies.
2.  **Synthesis Operations**: This stage utilizes a pseudo-code-based coding plan generator to construct structured implementation skeletons. It then employs a hybrid fill-in-the-blank model, guided by probabilistic priors and component awareness, to integrate core logic with reusable routines.
3.  **Three-Level Progressive Validation**: To ensure high-quality output, the system implements a rigorous validation pipeline consisting of syntax checking, standards compliance, and LLM-guided semantic verification.

The system is unified by an **Adaptive Orchestration Strategy**, which dynamically sequences operations by leveraging the orchestration history of similar functions and existing development tools.

## Performance and Results
Empirical evaluations demonstrate that DBCooker significantly outperforms existing methods when applied to widely used database engines, including [[SQLite]], [[PostgreSQL]], and [[DuckDB]], yielding an average accuracy improvement of **34.55%**. Furthermore, the system has demonstrated the capability to synthesize entirely new functions that are not present in the latest versions of [[SQLite]] (v3.50), marking a significant step forward in autonomous database development.