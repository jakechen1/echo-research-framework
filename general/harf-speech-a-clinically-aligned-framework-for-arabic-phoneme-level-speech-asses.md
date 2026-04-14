---
title: "Harf-Speech: A Clinically Aligned Framework for Arabic Phoneme-Level Speech Assessment"
created: 2024-05-23
source: "https://arxiv.org/abs/2604.06191"
tags: [Arabic, Speech-Processing, Clinical-Validation, Machine-Learning]
category: [ai, technology]
author: wiki-pipeline
dc.title: "Harf-Speech: A Clinically Aligned Framework for Arabic Phoneme-Level Speech Assessment"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/harf-speech-a-clinically-aligned-framework-for-arabic-phoneme-level-speech-asses.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Harf-Speech: A Clinically Aligned Framework for Arabic Phoneme-Level Speech Assessment

Harf-Speech is an innovative, modular framework designed for automated, phoneme-level pronunciation assessment specifically for [[Modern Standard Arabic]]. While [[Automatic Speech Recognition]] (ASR) has advanced significantly in recent years, there remains a notable scarcity of validated tools for Arabic-specific clinical applications, such as [[Speech Therapy]] and specialized [[Language Learning]] programs.

### System Architecture

The Harf-Speech architecture is comprised of several integrated modules designed to provide interpretable and clinically relevant feedback. The system utilizes an MSA phonetizer paired with a fine-tuned speech-to-phoneme model. To achieve precise comparison between the target phonemes and the produced speech signals, the framework employs [[Levenshtein Alignment]]. 

The final scoring mechanism utilizes a blended approach, combining the Longest Common Subsequence (LCS) and Edit-Distance metrics. This hybrid scoring system allows the framework to capture both the structural accuracy and the specific phonetic deviations present in the speaker's utterance.

### Model Performance and Benchmarking

The researchers evaluated several [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] architectures, fine-tuning three distinct ASR models on Arabic phoneme data. Through rigorous benchmarking—which included comparisons against zero-shot [[draw-in-mind-rebalancing-designer-painter-roles-in-unified-multimodal-models-ben|Multimodal Models]]—the system identified **OmniASR-CTC-1B-v2** as the top-performing architecture. This model achieved a remarkably low Phoneme Error Rate (PER) of 8.92%, demonstrating high precision in phonetic identification and transcription.

### Clinical Validation

A key differentiator of Harf-Speech is its commitment to clinical alignment. To ensure the system's utility in professional medical and educational settings, three certified [[Speech-Language Pathologists]] independently scored a dataset of 40 utterances. 

The framework demonstrated high-level agreement with human experts, achieving a Pearson correlation of 0.791 and an Intraclass Correlation Coefficient (ICC) of 0.659. These metrics suggest that Harf-Speech produces scores that are comparable to inter-rater expert agreement, making it a highly viable tool for scalable, automated [[Clinical Validation]] of Arabic speech production.