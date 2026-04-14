---
title: A Parameter-Efficient Transfer Learning Approach through Multitask Prompt Distillation and Decomposition for Clinical NLP
created: 2024-05-22
source: https://arxiv.org/abs/260AS
tags: [NLP, Prompt-Tuning, Transfer-Learning, Clinical-AI, PEFT]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "A Parameter-Efficient Transfer Learning Approach through Multitask Prompt Distillation and Decomposition for Clinical NLP"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/a-parameter-efficient-transfer-learning-approach-through-multitask-prompt-distil.md
dc.language: en
dc.rights: CC-BY-4.0
---

# A Parameter-Efficient Transfer Learning Approach through Multitask Prompt Distillation and Decomposition for Clinical NLP

In the rapidly evolving field of [[Clinical Natural Language Processing (NLP)]], a major challenge is the computational and storage burden caused by deploying multiple task-specific models. Traditional methods often require independent fine-tuning for every clinical task, which becomes unsustainable as the number of specialized medical AI applications grows.

This paper introduces a novel framework designed to address this scalability bottleneck through **multitask prompt distillation and decomposition**. Unlike standard [[Parameter-Efficient Fine-Tuning (PEFT)]] techniques that learn task-specific prompts in isolation, this approach learns a single, shared **metaprompt** derived from 21 diverse clinical source tasks. This shared representation can then be adapted to unseen target tasks with extreme efficiency, utilizing fewer than 0.05% of the total model's trainable parameters.

### Experimental Evaluation

The research evaluated the effectiveness of this framework across several state-of-the-art [[Large Language Models (LLMs)]], including [[LLaMA 3.1 8B]], [[Meditron3 8B]], and [[gpt-oss 20B]]. The performance was measured across five core clinical NLP task types:
* [[Named Entity Recognition (NER)]]
* [[Relation Extraction]]
* [[evaluating-repository-level-software-documentation-via-question-answering-and-fe|Question Answering]]
* [[Natural Language Inference (NLI)]]
* [[Text Summarization]]

### Key Findings

The results demonstrate that the distillation framework significantly outperforms existing benchmarks:
1. **Superiority over LoRA:**