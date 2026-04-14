---
title: Joint Knowledge Base Completion and Question Answering by Combining Large Language Models and Small Language Models
created: 2024-05-24
source: https://arxiv.org/abs/2604.05875
tags: [AI, LLM, SLM, Knowledge_Base, Machine_Learning]
category: ai, machine-learning
author: wiki-pipeline
dc.title: "Joint Knowledge Base Completion and Question Answering by Combining Large Language Models and Small Language Models"
dc.creator: wiki-pipeline
dc.date: 2024-05-24
dc.type: Text
dc.format: text/markdown
dc.identifier: general/joint-knowledge-base-completion-and-question-answering-by-combining-large-langua.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Joint Knowledge Base Completion and Question Answering by Combining Large Language Models and Small Language Models

## Overview
The research paper introduces **JCQL**, an innovative framework designed to bridge the gap between [[joint-knowledge-base-completion-and-question-answering-by-combining-large-langua|Knowledge Base Completion]] (KBC) and [[Knowledge Base Question Answering]] (KBQA). The authors argue that because these two tasks are inherently complementary and closely related, they should be solved jointly to allow for mutual reinforcement and improved accuracy.

## The Problem
In the current landscape of [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]], existing studies often rely heavily on [[Small Language Models]] (SLMs) to perform joint enhancement of KBC and KBQA. However, these methods frequently overlook the significant reasoning capabilities inherent in [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs). By ignoring the LLM's utility, existing models struggle to handle complex queries and are prone to errors in logic.

## The JCQL Framework
The JCQL framework proposes a bidirectional enhancement loop that utilizes the specific strengths of both model types:

1.  **KBC-to-KBQA Enhancement**: To improve the KBQA process, the framework utilizes an LLM-based agent. This agent is augmented with an SLM-trained KBC model, which acts as a specific "action" or tool within the agent's reasoning repertoire. This integration helps alleviate common [[blending-human-and-llm-expertise-to-detect-hallucinations-and-omissions-in-menta|Hallucination]] issues in LLMs and significantly reduces [[Computational Cost]] by offloading structural retrieval tasks to the more efficient SLM.

2.  **KBQA-to-KBC Enhancement**: To improve the KBC process, the framework leverages the complex reasoning paths generated