---
title: "$k$-server-bench: Automating Potential Discovery for the $k$-Server Conjecture"
created: 2024-05-23
source: https://arxiv.org/abs/2604.07240
tags: [machine-learning, mathematics, benchmarking, artificial-intelligence]
category: machine-learning
---

$k$-server-bench is a specialized benchmark designed for automated, open-ended mathematical discovery, specifically targeting the [[$k$-server conjecture]]. This problem is a central pillar in the field of [[competitive analysis]], focusing on the identification of potential functions that satisfy a complex system of linear inequalities structured over graphs.

The core mechanism of the benchmark involves a search for potential functions. The evaluation process is fundamentally sound but incomplete: while any single violated inequality can definitively refute a candidate function, the successful satisfaction of all inequalities does not, on its own, constitute a formal mathematical proof for the specific case of the conjecture. However, discovering a candidate that satisfies these constraints would represent significant progress and a major contribution to the mathematical community, particularly in the currently unresolved $k=4$ case.

Preliminary experiments using [[agentic methods]] have yielded promising results. In the $k=3$ regime, current [[machine-learning]] approaches have been able to resolve the task entirely. In the more difficult $k=4$ regime, these agents have demonstrated the ability to reduce the frequency of inequality violations relative to existing known potentials. This suggests that while the task is highly complex, it remains a plausible target for current [[artificial intelligence]]-driven discovery tools.

As a research tool, $k$-server-bench offers several advantages over traditional [[code-based discovery agents]] benchmarks. It addresses common issues such as early saturation and the insufficient separation between naive random baselines and more advanced algorithmic models. Consequently, it serves as an essential testbed for developing new hypotheses and refining