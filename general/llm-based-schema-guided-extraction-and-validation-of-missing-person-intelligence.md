---
title: LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources
created: 2024-05-23
source: https://arxiv.org/abs/2604.06571
tags: [LLM, Information Extraction, Data Normalization, Automation, Criminal Justice]
categories: [ai, machine-learning, technology]
author: wiki-pipeline
dc.title: "LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources"
dc.creator: wiki-pipeline
dc.date: 2024-05-23
dc.type: Text
dc.format: text/markdown
dc.identifier: general/llm-based-schema-guided-extraction-and-validation-of-missing-person-intelligence.md
dc.language: en
dc.rights: CC-BY-4.0
---

# LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence

## Overview
Investigations involving missing persons and child safety often suffer from "data fragmentation." Vital intelligence is typically trapped in heterogeneous formats, ranging from structured administrative forms to unstructured narrative web profiles and visual bulletin-style posters. The high variability in layout, terminology, and quality makes rapid triage and large-scale [[Information Extraction]] extremely difficult for human investigators.

## The Guardian Parser Pack
To address these challenges, the paper introduces the **Guardian Parser Pack**, an automated pipeline designed to transform multi-source documents into a unified, schema-compliant format. This pipeline is engineered for downstream use in [[Spatial Modeling]] and operational review.

The architecture utilizes a four-stage process:
1.  **Extraction & OCR**: A multi-engine approach for PDF