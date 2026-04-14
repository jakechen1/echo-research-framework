---
title: "Draw-In-Mind: Rebalancing Designer-Painter Roles in Unified Multimodal Models"
created: 2024-05-22
source: "https://arxiv.org/abs/2509.01986"
tags: [ai, machine-learning, computer-vision, image-editing]
category: ai
---

# Draw-In-Mind (DIM)

**Draw-In-Mind (DIM)** is a novel framework designed to resolve inefficiency in unified [[draw-in-mind-rebalancing-designer-painter-roles-in-unified-multimodal-models-ben|Multimodal Models]] during complex [[image-editing|Image Editing]] tasks. The research addresses a fundamental "imbalance" found in current [[text-to-image-generation|Text-to-Image Generation]] architectures, where the roles of understanding and rendering are poorly distributed.

## The Designer-Painter Problem

In standard unified models, the architecture is split into an understanding module and a generation module. The researchers identified that while the understanding module effectively acts as a "translator" (converting text to semantic conditions), the generation module is overburdened. It is forced to perform two distinct, difficult roles simultaneously:
1.  **The Designer**: Identifying the target editing regions and inferring the necessary spatial layout.
2.  **The Painter**: Rendering the new content and textures into the image.

This imbalance is compounded by the fact that understanding modules are typically trained on significantly more data regarding complex reasoning than their generative counterparts.

## The DIM Solution

The DIM approach rebalances these responsibilities by explicitly assigning the "design" responsibility to the understanding module. This is facilitated through the creation of two complementary datasets:

*   **DIM-T2I**: A massive dataset containing 14 million long-context image-text pairs, specifically designed to enhance the model's ability to comprehend complex, multi-step instructions.
*   **DIM-Edit**: A dataset consisting of 233,000 "chain-of-thought" imaginations. Generated via GPT-4o, these entries serve as explicit "design blueprints" that guide the model through the spatial reasoning required for an edit.

## Architecture and Performance

The DIM architecture, specifically the **DIM-4.6B** model, utilizes a frozen [[qwen25-vl-3b|Qwen2.5-VL-3B]] model integrated with a trainable [[sana15-16b|SANA1.5-1.6B]] module via a lightweight two-layer MLP. 

Despite its relatively modest parameter scale, the DIM-4.6B-Edit model achieves state-of-the-art (SOTA) or highly competitive performance on the **ImgEdit** and **GEdit-Bench** benchmarks. Remarkably, it outperforms much larger models, such as [[uniworld-v1|UniWorld-V1]] and [[step1x-edit|Step1X-Edit]], proving that explicit architectural delegation of design tasks is more effective than raw model scaling.