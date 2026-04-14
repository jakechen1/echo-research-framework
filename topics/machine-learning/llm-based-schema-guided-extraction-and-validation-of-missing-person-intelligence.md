---
title: LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence from Heterogeneous Data Sources
created: 2024-05-23
source: https://arxiv.org/abs/2604.06571
tags: [LLM, Information Extraction, Data Normalization, Automation, Criminal Justice]
categories: [ai, machine-learning, technology]
---

# LLM-based Schema-Guided Extraction and Validation of Missing-Person Intelligence

## Overview
Investigations involving missing persons and child safety often suffer from "data fragmentation." Vital intelligence is typically trapped in heterogeneous formats, ranging from structured administrative forms to unstructured narrative web profiles and visual bulletin-style posters. The high variability in layout, terminology, and quality makes rapid triage and large-scale [[information-extraction|Information Extraction]] extremely difficult for human investigators.

## The Guardian Parser Pack
To address these challenges, the paper introduces the **Guardian Parser Pack**, an automated pipeline designed to transform multi-source documents into a unified, schema-compliant format. This pipeline is engineered for downstream use in [[spatial-modeling|Spatial Modeling]] and operational review.

The architecture utilizes a four-stage process:
1.  **Extraction & OCR**: A multi-engine approach for PDF