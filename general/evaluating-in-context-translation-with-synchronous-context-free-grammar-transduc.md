---
title: Evaluating In-Context Translation with Synchronous Context-Free Grammar Transduction
created: 2023-10-27
source: https://arxiv.org/abs/2604.07320
tags: [machine-translation, LLM, formal-languages, in-context-learning]
category: machine-learning
author: wiki-pipeline
dc.title: "Evaluating In-Context Translation with Synchronous Context-Free Grammar Transduction"
dc.creator: wiki-pipeline
dc.date: 2023-10-27
dc.type: Text
dc.format: text/markdown
dc.identifier: general/evaluating-in-context-translation-with-synchronous-context-free-grammar-transduc.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Evaluating In-Context Translation with Synchronous Context-Free Grammar Transduction

This research explores the capacity of [[large-language-models-for-outpatient-referral-problem-definition-benchmarking-an|Large Language Models]] (LLMs) to perform [[Machine Translation]] for [[languages|Low-resource Languages]] by leveraging in-context instructions—such as dictionaries or textbooks—rather than relying on massive parallel datasets. The core problem addressed is whether LLMs can effectively bridge the gap between high-level grammatical descriptions and the actual execution of translation tasks.

## Methodology

To assess this ability without the noise of natural language complexity, the researchers utilized a formal proxy: **string transduction** based on [[Synchronous Context-Free Grammars]] (SCFG). By using these grammars, the study modeled specific linguistic features including syntax, [[Morphology]], and written scripts. 

The experimental setup involved providing the LLM with a formal grammar in the prompt and asking it to translate a source sentence into a target language derived from that grammar. This allowed the researchers to systematically vary grammar size, sentence length, and the structural divergence between the two languages.

## Key Findings

The study identifies three primary limitations in the current state of [[graphwalker-graph-guided-in-context-learning-for-clinical-reasoning-on-electroni|In-Context Learning]] for linguistic tasks:

1.  **Scale Sensitivity:** Translation accuracy drops markedly as the complexity of the grammar increases or the length of the sentences grows, suggesting a ceiling on the model's working memory for complex rule-following.
2.  **Structural Divergence:** Differences in [[Morphology]] and written representation between the source and target languages act as significant barriers to performance, often diminishing the model's ability to apply rules accurately.
3.  **Error Characterization:** The errors committed by models are predictable and fall into three categories:
    *   **Hallucination:** The generation of entirely new, non-existent words.
    *   **Vocabulary Error:** Recalling the incorrect word from the provided target vocabulary.
    *   **Translation Failure:** Leaving words from the source language untranslated in the final output.

These findings provide critical insights into the boundaries of [[Natural Language Processing]] when models are tasked with