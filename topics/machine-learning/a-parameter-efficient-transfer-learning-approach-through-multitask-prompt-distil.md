---
title: A Parameter-Efficient Transfer Learning Approach through Multitask Prompt Distillation and Decomposition for Clinical NLP
created: 2024-05-22
source: https://arxiv.org/abs/260AS
tags: [NLP, Prompt-Tuning, Transfer-Learning, Clinical-AI, PEFT]
category: [ai, machine-learning, technology]
---

# A Parameter-Efficient Transfer Learning Approach through Multitask Prompt Distillation and Decomposition for Clinical NLP

In the rapidly evolving field of [[clinical-natural-language-processing-nlp|Clinical Natural Language Processing (NLP)]], a major challenge is the computational and storage burden caused by deploying multiple task-specific models. Traditional methods often require independent fine-tuning for every clinical task, which becomes unsustainable as the number of specialized medical AI applications grows.

This paper introduces a novel framework designed to address this scalability bottleneck through **multitask prompt distillation and decomposition**. Unlike standard [[parameter-efficient-fine-tuning-peft|Parameter-Efficient Fine-Tuning (PEFT)]] techniques that learn task-specific prompts in isolation, this approach learns a single, shared **metaprompt** derived from 21 diverse clinical source tasks. This shared representation can then be adapted to unseen target tasks with extreme efficiency, utilizing fewer than 0.05% of the total model's trainable parameters.

### Experimental Evaluation

The research evaluated the effectiveness of this framework across several state-of-the-art [[large-language-models-llms|Large Language Models (LLMs)]], including [[llama-31-8b|LLaMA 3.1 8B]], [[meditron3-8b|Meditron3 8B]], and [[gpt-oss-20b|gpt-oss 20B]]. The performance was measured across five core clinical NLP task types:
* [[named-entity-recognition-ner|Named Entity Recognition (NER)]]
* [[relation-extraction|Relation Extraction]]
* [[evaluating-repository-level-software-documentation-via-question-answering-and-fe|Question Answering]]
* [[natural-language-inference-nli|Natural Language Inference (NLI)]]
* [[text-summarization|Text Summarization]]

### Key Findings

The results demonstrate that the distillation framework significantly outperforms existing benchmarks:
1. **Superiority over LoRA:**