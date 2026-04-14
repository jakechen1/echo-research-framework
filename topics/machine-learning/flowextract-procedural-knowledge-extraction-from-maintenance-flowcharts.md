---
title: FlowExtract: Procedural Knowledge Extraction from Maintenance Flowcharts
created: 2024-05-22
source: https://arxiv.org/abs/2604.06770
tags: [computer-vision, automation, manufacturing, flowchart-analysis]
category: ai, technology
---

# FlowExtract: Procedural Knowledge Extraction from Maintenance Flowcharts

FlowExtract is a specialized [[computer-vision|Computer Vision]] pipeline engineered to transform static, unstructured maintenance flowcharts into structured, machine-readable directed graphs. In industrial manufacturing environments, critical procedural knowledge is frequently trapped within PDFs or scanned images following [[iso-5807|ISO 5807]] standards. While these documents are vital for [[asset-lifecycle-management|Asset Lifecycle Management]], they remain largely inaccessible to modern [[operator-support-systems|Operator Support Systems]] and automated query engines.

### The Challenge of Topology
Current state-of-the-art [[aligned-vector-quantization-for-edge-cloud-collabrative-vision-language-models|Vision-Language Models]] (VLMs), while dominant in general image understanding, often struggle with the topological reconstruction required for complex technical diagrams. Specifically, these models frequently fail to accurately reconstruct the connection topology (the relationship between nodes) in complex flowchart layouts.

### Methodology
To overcome these limitations, FlowExtract utilizes a decoupled architecture that separates element detection from connectivity reconstruction:

1.  **Element Detection**: The system employs [[yolov8|YOLOv8]] for high-accuracy node detection and [[easyocr|EasyOCR]] for extracting text labels from within the flowchart elements. This ensures that all domain-aligned components are identified with high precision.
2.  **Connectivity Reconstruction**: Rather than relying on holistic image understanding, FlowExtract utilizes a novel edge detection method. This method analyzes the orientation of arrowheads and traces connecting lines backward to their source nodes to reconstruct the graph topology.

### Results and Impact
Experimental evaluations conducted on industrial troubleshooting guides demonstrate that FlowExtract achieves superior node detection accuracy and significantly outperforms [[a-comparative-analysis-of-machine-learning-models-in-shap-analysis|Machine Learning]]-based VLM baselines regarding edge extraction. 

By converting visual diagrams into structured [[graph-theory|Graph Theory]] representations, FlowExtract provides a practical path for organizations to transition from static documentation to intelligent, queryable procedural knowledge bases. This technology is fundamental for the advancement of [[industrial-automation|Industrial Automation]] and autonomous maintenance workflows.

The implementation is available via [[github|GitHub]].