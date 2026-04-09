---
title: The Geometry of Forgetting
created: 2024-05-23
source: https://arxiv.org/abs/2604.06222
tags: [geometry, memory, embeddings, interference, false-memory]
categories: [ai, machine-learning, neuroscience]
---

# The Geometry of Forgetting

The paper "The Geometry of Forgetting" (arXiv:2604.06222) proposes a paradigm shift in our understanding of [[Memory]]-related phenomena. While traditional views in [[Neuroscience]] often attribute forgetting and false memories to biological decay or hardware limitations, this research suggests these are emergent properties of the [[Geometry]] inherent in [[High-dimensional embedding spaces]].

### Interference and Power-law Forgetting
A central finding of the study is that forgetting is driven by competition rather than temporal decay. In [[Machine learning]] models—specifically production embedding models ranging from 384 to 1,024 dimensions—the researchers observed that the decay follows a power-law pattern ($b = 0.460 \pm 0.183$), closely approximating the human rate ($b \approx 0.5$).

Crucially, the study demonstrates that time alone does not produce this effect. When competitors are removed, the decay rate drops significantly to $b \approx 0.009$, a fifty-fold decrease. This suggests that forgetting is a byproduct of [[Interference]] among competing memories. This vulnerability is heightened because these models concentrate their variance in only approximately 16 effective dimensions, placing them deep within an interference-prone regime.

### The Emergence of False Memories
The research also addresses the [[Deese-Roediger-McDermott (DRM) effect]], a phenomenon where individuals recall items that were never actually presented. The authors found that no specific engineering or parameter tuning was required to reproduce this effect. By applying [[Cosine similarity]]