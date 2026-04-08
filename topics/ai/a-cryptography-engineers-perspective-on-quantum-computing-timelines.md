---
title: A cryptography engineer's perspective on quantum computing timelines
created: 2024-05-22
source: https://words.filippo.io/crqc-timeline/
tags: [quantum-computing, cryptography, cybersecurity, CRQC, technological-forecasting]
category: technology
---

This article provides a technical and grounded assessment of the timeline for the emergence of a Cryptographically Relevant Quantum Computer (CRQC). Rather than focusing on speculative hype, the author applies a cryptography engineer's lens to evaluate when quantum hardware might become capable of executing [[Shor's Algorithm]] at a scale sufficient to compromise widely used asymmetric cryptographic protocols, such as RSA and Elliptic Curve Cryptography.

A primary theme of the discussion is the distinction between the development of noisy, intermediate-scale quantum (NISQ) devices and the realization of large-scale, fault-tolerant quantum computing. The author explores the significant engineering hurdles remaining, particularly in the realm of [[Quantum Error Correction]] and the massive scaling requirements for logical qubits.

One of the most critical takeaways is the concept of the "Harvest Now, Decrypt Later" (HNDL) threat. This strategy involves malicious actors capturing encrypted traffic today with the intent to decrypt it once a CRQC becomes available. This reality necessitates an immediate and proactive shift toward [[Post-Quantum Cryptography]] (PQC). The complexity of updating global digital infrastructure—ranging from web browsers to industrial control systems—means that the "quantum threat" is not merely a future event but a present-day architectural challenge for [[Cybersecurity]] professionals.

The article serves as a sobering look at the intersection of [[Quantum Computing]] and global [[Information Security]]. It underscores that the window for a safe transition is determined not by the arrival of the quantum computer itself, but by the speed at which we can implement resilient, quantum-resistant standards across all layers of the modern technology stack.