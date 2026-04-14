---
title: Team Fusion@ SU@ BC8 SympTEMIST track: transformer-based approach for symptom recognition and linking
created: 2024-05-22
source: https://arxiv.org/abs/2604.06424
tags: [NLP, NER, Entity-Linking, Transformers, Clinical-Informatics]
category: [ai, machine-learning, biology]
author: wiki-pipeline
dc.title: "Team Fusion@ SU@ BC8 SympTEMIST track: transformer-based approach for symptom recognition and linking"
dc.creator: wiki-pipeline
dc.date: 2024-05-22
dc.type: Text
dc.format: text/markdown
dc.identifier: general/team-fusion-su-bc8-symptemist-track-transformer-based-approach-for-symptom-recog.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Team Fusion@ SU@ BC8 SympTEMIST track: transformer-based approach for symptom recognition and linking

This paper presents a specialized [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|Transformer]]-based architecture designed to address two fundamental challenges in [[Clinical Natural Language Processing]]: [[Named Entity Recognition]] (NER) and [[Entity Linking]] (EL). The research was specifically developed for the SympTEMIST track, focusing on the automated identification and normalization of symptoms within medical texts.

### Technical Approach

#### Named Entity Recognition (NER)
To perform effective symptom recognition, the authors utilize a fine-tuned [[RoBER $﻿$ a]] model. The architecture incorporates [[se-enhanced-vit-and-bilstm-based-intrusion-detection-for-secure-iiot-and-iomt-en|BiLSTM]] (Bidirectional Long Short-Term Memory) and [[crft-consistent-recurrent-feature-flow-transformer-for-cross-modal-image-registr|CRF]] (Conditional Random Fields) layers to improve the accuracy of token-level classification. To enhance the model's ability to handle diverse linguistic variations, the researchers fine-tuned the classifier on an augmented training dataset.

#### Entity Linking (EL)
The process of entity linking involves mapping identified symptoms to a standardized [[llm-augmented-knowledge-base-construction-for-root-cause-analysis|Knowledge Base]]. The researchers employed the cross-lingual **SapBERT XLMR-Large** model to generate a list of potential entity candidates. Once candidates are generated, the system calculates the [[Cosine Similarity]] between the text embeddings and the entries in the knowledge base to determine the most accurate match.

### Research Conclusions

A primary takeaway from this study is the identification of the most critical variable in the extraction pipeline. The researchers demonstrated that the choice of the [[llm-augmented-knowledge-base-construction-for-root-cause-analysis|Knowledge Base]] has the highest impact on overall model accuracy. 

This finding suggests that while improvements in [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]] architectures and [[benchmarking-deep-learning-for-future-liver-remnant-segmentation-in-colorectal-l|Deep Learning]] layers are necessary, the curation and selection of high-quality, structured medical ontologies are equally vital for the success of [[Bioinformatics]] applications and automated clinical decision support systems.