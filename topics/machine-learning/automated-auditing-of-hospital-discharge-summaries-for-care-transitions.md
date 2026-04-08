---
title: Automated Auditing of Hospital Discharge Summaries for Care Transitions
created: 2024-05-23
source: https://arxiv.org/abs/2604.05435
tags: [healthcare, LLM, clinical-auditing, patient-safety]
category: ai, technology
---

# Automated Auditing of Hospital Discharge Summaries for Care Transitions

Discharge summaries serve as a critical bridge in patient care, yet their incompleteness and inconsistency are primary drivers of care fragmentation and avoidable [[readmissions]]. While auditing these documents is essential for maintaining patient safety, traditional manual review processes are notoriously difficult to scale within large-scale hospital networks.

This paper proposes a novel, automated framework for the large-scale auditing of discharge summaries using locally deployed [[Large Language Models (LLMs)]]. A key innovation of this research is the emphasis on privacy-preserving [[Artificial Intelligence]] in clinical settings. By utilizing locally deployed models, the framework mitigates the significant risks associated with processing sensitive patient data in the cloud, ensuring that clinical data remains within secure boundaries.

The researchers utilize the **DISCHARGED** framework to operationalize core transition-of-care requirements. This involves transforming qualitative clinical needs—such as follow-up instructions, medication history and changes, and patient clinical course—into a structured validation checklist of specific, auditable questions. This structured approach allows the LLM to precisely identify the presence, absence, or ambiguity of critical documentation elements.

To validate the approach, the study utilized adult inpatient summaries from the [[MIMIC-IV]] database. The findings demonstrate the feasibility of using [[Machine Learning]] for automated clinical auditing