---
title: How to Evaluate Speech Translation with Source-Aware Neural MT Metrics
created: 2024-05-22
source: https://arxiv.org/abs/2511.03295
tags: [speech-translation, evaluation-metrics, asr, neural-mt, nlp]
category: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "How to Evaluate Speech Translation with Source-Aware Neural MT Metrics"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/how-to-evaluate-speech-translation-with-source-aware-neural-mt-metrics.md
dc.language: en
dc.rights: CC-BY-4.0
---

# How to Evaluate Speech Translation with Source-Aware Neural MT Metrics

The paper "How to Evaluate Speech Translation with Source-Aware Neural MT Metrics" addresses a critical bottleneck in [[how-to-evaluate-speech-translation-with-source-aware-neural-mt-metrics|Speech Translation]] (ST) evaluation. Traditional evaluation methods primarily rely on comparing translation hypotheses against one or more reference translations. While this approach is standard, it is inherently limited because it ignores the valuable semantic information present in the original source input.

In the field of [[Machine Translation]] (MT), recent advancements have demonstrated that neural metrics incorporating the source text achieve significantly stronger correlations with human judgment. However, extending this "source-aware" concept to ST is non-trivial. Unlike MT, the source in ST is audio-based, meaning reliable transcripts or precise alignments between the source audio and reference translations are often unavailable in real-world operating conditions.

To address this, the authors conduct a systematic study of source-aware metrics for ST. They explore two complementary strategies for generating textual proxies of the input audio:
1. **ASR Transcripts:** Utilizing [[Automatic Speech Recognition]] to create a textual version of the audio.
2. **Back-translations:** Generating synthetic source text by translating the reference translations back into the source language.

A significant contribution of this work is the introduction of a novel two-step cross-lingual re-segmentation algorithm. This algorithm is designed to mitigate the alignment mismatch that typically occurs between synthetic sources and reference translations.

The research involves extensive experiments across 79 language pairs and six different ST systems with diverse architectures. The findings reveal that ASR transcripts constitute a more reliable synthetic source than back-translations, provided the [[Word Error Rate]] (WER) remains below 20%. However, back-translations were found to be a computationally cheaper and still effective alternative. The robustness of these results was confirmed through testing on low-resource language pairs, such as Bemba-English, and direct validation against human quality judgments. This work paves the way for more accurate and principled evaluation methodologies in [[Natural Language Processing]].