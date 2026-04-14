---
title: "AV-SQL: Decomposing Complex Text-to-SQL Queries with Agentic Views"
created: 2024-05-22
source: "https://arxiv.org/abs/2604.07041"
tags: [ai, text-to-sql, llm, agents, sql, automation]
category: ai
author: wiki-pipeline
dc.title: "AV-SQL: Decomposing Complex Text-to-SQL Queries with Agentic Views"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/av-sql-decomposing-complex-text-to-sql-queries-with-agentic-views.md
dc.language: en
dc.rights: CC-BY-4.0
---

# AV-SQL: Decomposing Complex Text-to-SQL Queries with Agentic Views

AV-SQL is an innovative framework designed to tackle the challenges of [[av-sql-decomposing-complex-text-to-sql-queries-with-agentic-views|Text-to-SQL]]—the process of translating natural language questions into executable [[av-sql-decomposing-complex-text-to-sql-queries-with-agentic-views|SQL]] code. While [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) have significantly advanced this field, traditional one-shot generation methods struggle with "real-world" scenarios involving massive [[automating-database-native-function-code-synthesis-with-llms|Database]] schemas and queries that require complex, multi-step logical reasoning.

### The Challenge
As database schemas grow in complexity, two primary issues emerge:
1.  **Context Window Limitations**: Large schemas often exceed the input capacity of an LLM, making it impossible to provide the full schema context at once.
2.  **Execution Errors**: One-shot approaches frequently suffer from syntax errors and "schema linking" failures, where the model incorrectly maps natural language terms to the correct table or column.

### The AV-SQL Framework
To address these bottlenecks, AV-SQL introduces the concept of **Agentic Views**. Instead of attempting to generate a full query in one pass, the framework uses agent-generated [[Common Table Expressions]] (CTEs) to encapsulate intermediate logic and filter out irrelevant schema elements.

The process is divided into three specialized stages driven by a pipeline of [[undetectable-conversations-between-ai-agents-via-pseudorandom-noise-resilient-ke|AI Agents]]:
*   **Rewriter Agent**: This agent focuses on the input, compressing and clarifying the user's natural language query to remove ambiguity.
*   **View Generator Agent**: This agent processes specific "chunks" of the schema to produce the aforementioned agentic views, effectively narrowing the scope of the database to only relevant parts.
*   **Planner, Generator, and Revisor Agents**: This final group works collaboratively to compose the individual views into a cohesive, final SQL statement, with the Revisor agent checking for logic and syntax errors.

### Performance Benchmarks
AV-SQL has demonstrated state-of-the-art performance across several critical benchmarks:
*   **Spider 2.0**: Achieved **70.38%** execution accuracy, proving its efficacy in highly complex environments.
*   **Spider**: Achieved **85.59%**.
*   **BIRD**: Achieved **72.16%**.
*   **KaggleDBQA**: Achieved **63.78%**.

By leveraging a multi-agent decomposition strategy, AV-SQL provides a scalable solution for democratizing access to [[toward-a-universal-foundation-model-for-graph-structured-data|Structured Data]] through natural language interfaces.