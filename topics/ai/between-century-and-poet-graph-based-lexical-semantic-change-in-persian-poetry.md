---
title: Between Century and Poet: Graph-Based Lexical Semantic Change in Persian Poetry
created: 2024-05-22
source: https://arxiv.org/abs/2604.06674
tags: [Persian Poetry, NLP, Graph Theory, Semantic Change, Digital Humanities]
category: ai
---

The research paper "Between Century

and Poet: Graph-Based Lexical Semantic Change in Persian Poetry presents a novel computational framework designed to track the evolution of word meanings within the vast and complex landscape of Persian verse. By leveraging [[graph-theory|Graph Theory]] and [[natural-language-processing|Natural Language Processing]] (NLP), the research addresses the dual challenge of identifying how vocabulary shifts across different historical epochs (centuries) and how individual poetic styles (poets) influence semantic usage.

## Overview of the Research Problem

[[lexical-semantic-change|Lexical Semantic Change]] (LSC) refers to the phenomenon where the meaning of a word evolves over time—a process known in [[linguistics|Linguistics]] as semantic drift. Traditionally, detecting these changes has relied heavily on [[word-embeddings|Word Embeddings]] (such as [[word2vec|Word2Vec]] or [[fasttext|FastText]]) by comparing vector spaces from different time periods. However, these methods often struggle with the high levels of metaphor, ambiguity, and stylistic variation inherent in classical [[persian-literature|Persian Literature]].

The paper identifies two primary dimensions of semantic variation that are often conflated in existing literature:
1.  **Diachronic Change (Temporal):** The macro-level evolution of the Persian language across centuries (e.g., from the Khorasani style to the Indian style).
2.  **Idiolectal Change (Authorial):** The micro-level semantic nuances unique to specific poets, where a word may take on a specialized or highly metaphorical meaning within a single author's corpus.

The research proposes that by treating the lexicon as a dynamic graph rather than a static collection of vectors, researchers can better capture the structural shifts in how words relate to their neighbors, providing a more robust metric for semantic change.

## Graph-Based Methodology

The core innovation of the paper lies in its transition from vector-space comparison to [[graph-based-learning|Graph-Based Learning]]. The authors represent the Persian poetic corpus as a series of interconnected graphs, where each node represents a unique word (lemma) and each edge represents a semantic or syntactic relationship derived from [[co-occurrence-networks|Co-occurrence Networks]].

### Graph Construction
To construct these graphs, the researchers implemented a multi-step pipeline:
*   **Preprocessing:** The corpus underwent intensive [[tokenization|Tokenization]] and [[lemmatization|Lemmatization]], specifically tuned for the morphological complexities of the Persian language.
*   **Edge Definition:** Edges were established based on a sliding window of co-occurrence. Unlike standard models, the researchers used a weighted approach, where the strength of an edge is determined by the frequency and strength of association between two words within a specific poetic context.
*   **Node Features:** Each node was enriched with features derived from [[contextualized-embeddings|Contextualized Embeddings]], allowing the graph to retain deep semantic information while benefiting from the structural advantages of [[graph-neural-networks|Graph Neural Networks]] (GNNs).

### Detecting Semantic Drift
The paper introduces a "Graph Topology Comparison" metric. Instead of simply measuring the distance between word vectors, the model analyzes the change in a node's **structural neighborhood**. If a word's neighbors in the graph change significantly between Century A and Century B, or between Poet X and Poet Y, the system flags this as a potential semantic shift. This approach is particularly effective for identifying "polysemy shifts," where a word's primary sense moves from a concrete meaning to an abstract one.

## Dual-Axis Analysis: Century vs. Poet

A significant contribution of this work is the decoupling of temporal evolution from authorial style. The researchers conducted experiments across two distinct axes:

### 1. The Temporal Axis (Diachronic Evolution)
By partitioning the Persian poetic corpus into historical slices (e.g., 10th, 13th, and 16th centuries), the study mapped the "semantic trajectory" of key Persian terms. The graph-based approach successfully identified shifts in words related to socio-political structures, religious terminology, and nature, documenting how the "semantic field" of the Persian language expanded or contracted in response to historical uphevers.

### 2. The Authorial Axis (Stylistic Variation)
The study applied the same graph-based metrics to compare different poets within the same era. This allowed for the detection of "poetic idiolects"—instances where a poet like [[hafez|Hafez]] or [[rumi|Rumi]] uses a word in a way that deviates from the linguistic norm of their century. This distinction is crucial for [[digital-humanities|Digital Humanities]], as it prevents the misclassification of a poet's unique stylistic choice as a widespread linguistic change.

## Experimental Results and Findings

The researchers validated their model against known historical linguistic shifts and manual annotations by experts in [[persian-philology|Persian Philology]]. The results demonstrated that the graph-based approach outperformed traditional [[cosine-similarity|Cosine Similarity]] methods in several key metrics:
*   **Precision in Metaphor Detection:** The model was significantly more accurate at identifying words that underwent "metaphorical extension" (e.g., a word moving from a physical object to a spiritual concept).
*   **Robustness to Sparsity:** Because graph structures rely on local connectivity, the model remained performant even in eras where the available poetic corpus was significantly smaller (addressing the "data sparsity" problem in historical NLP).
*   **Identification of Semantic Clusters:** The researchers were able to visualize how entire "semantic clusters" (groups of related words) migrated together across the centuries, providing a macro-view of linguistic evolution.

## Implications for Digital Humanities and NLP

The findings presented in "Between Century and Poet" have profound implications for several fields:

*   **Computational Philology:** The methodology provides a scalable tool for scholars to study the evolution of classical texts without requiring manual, word-by-word analysis of thousands of poems.
*   **Low-Resource NLP:** While Persian is a well-documented language, many other historical languages suffer from a lack of large-scale corpora. The graph-based approach offers a blueprint for extracting semantic meaning from sparse, fragmented historical datasets.
*   **Automated Literary Analysis:** The ability to distinguish between period-wide linguistic shifts and individual authorial brilliance opens new doors for the automated study of [[literary-theory|Literary Theory]] and [[stylometry|Stylometry]].

## Challenges and Future Directions

Despite the success of the proposed model, the paper acknowledges several ongoing challenges:
*   **Ambiguity in Poetry:** The inherent ambiguity of poetic language (where a single word may serve multiple metaphorical purposes simultaneously) remains a difficult boundary for even the most advanced [[graph-neural-networks|Graph Neural Networks]].
*   **Computational Complexity:** Constructing and comparing large-scale dynamic graphs is computationally expensive, requiring significant memory and processing power as the corpus grows.
*   **Integration of Metadata:** Future research aims to incorporate more metadata, such as geographic origin (e.g., comparing Persian poetry from the Samarkand school vs. the Shiraz school) to see if regional dialects influence semantic change similarly to temporal or authorial factors.

## Related Concepts

*   [[diachronic-linguistics|Diachronic Linguistics]]
*   [[graph-convolutional-networks|Graph Convolutional Networks]]
*   [[semantic-web|Semantic Web]]
*   [[natural-language-understanding|Natural Language Understanding]]
*   [[historical-linguistics|Historical Linguistics]]
*   [[word-embeddings|Word Embeddings]]
