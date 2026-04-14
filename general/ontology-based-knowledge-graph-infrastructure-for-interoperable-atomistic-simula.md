---
title: Ontology-based knowledge graph infrastructure for interoperable atomistic simulation data
created: 2024-05-23
source: https://arxiv.org/abs/2604.06230
tags: [knowledge-graph, atomistic-simulation, ontology, data-science, materials-science]
category: technology
author: wiki-pipeline
dc.title: "Ontology-based knowledge graph infrastructure for interoperable atomistic simulation data"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/ontology-based-knowledge-graph-infrastructure-for-interoperable-atomistic-simula.md
dc.language: en
dc.rights: CC-BY-4.0
---

# Ontology-based knowledge graph infrastructure for interoperable atomistic simulation data

The reuse of [[quasar-a-universal-autonomous-system-for-atomistic-simulation-and-a-benchmark-of|Atomistic Simulation]] data is a significant challenge in modern [[Computational Materials Science]]. Currently, researchers struggle with heterogeneous file formats, incomplete metadata, and a lack of standardized representations for computational workflows and [[provenance-research-methodologies|Provenance]]. This fragmentation prevents the seamless integration of datasets, limiting the scientific community's ability to perform large-scale meta-analyses and predictive modeling.

To address these bottlenecks, this research introduces an infrastructure built upon [[ontology-based-knowledge-graph-infrastructure-for-interoperable-atomistic-simula|Knowledge Graph]] technology and [[ontology-based-knowledge-graph-infrastructure-for-interoperable-atomistic-simula|Ontology]]-based modeling. The system utilizes a specialized software framework designed to capture data both from legacy datasets and directly from active simulation workflows at the moment of generation. By employing domain-specific ontologies, the framework normalizes disparate data sources into a unified, ontology-aligned representation. This enables consistent [[Semantic Web]] querying and complex analysis across previously disconnected datasets.

A core strength of this infrastructure is its ability to represent computational workflows in a machine-readable format. This provides both forward [[provenance-research-methodologies|Provenance]] tracking and the ability to perform the partial reconstruction of computational procedures, ensuring that the experimental context is preserved alongside the results. 

Through practical demonstrations, the authors showcase the system's ability to:
* Integrate complex grain boundary data.
* Execute cross-dataset analyses of material properties.
* Extract derived [[Thermodynamics]] quantities from existing simulations.

The scale of the implemented solution is substantial, featuring a knowledge graph containing over 750,000 triples describing nearly 8,000 computational samples. Ultimately, this framework serves as a practical implementation of [[FAIR Data Principles]] (Findability, Interoperability, Accessibility, and Reusability), significantly improving the efficiency of data-driven discovery in the physical sciences.