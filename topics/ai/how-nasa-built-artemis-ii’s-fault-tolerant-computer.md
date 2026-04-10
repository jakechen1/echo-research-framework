---
title: How NASA built Artemis II’s fault-tolerant computer
created: 2024-05-22
source: https://cacm.acm.org/news/how-nasa-built-artemis-iis-fault-tolerant-computer/
tags: [NASA, Artemis II, Fault Tolerance, Space Technology, Computer Architecture]
category: technology
---

# How NASA built Artemis II’s fault-tolerant computer

The development of the computing systems for NASA's [[Artemis II]] mission represents a critical advancement in the field of [[Space Exploration]]. As the mission prepares to send humans near the Moon, the reliability of onboard avionics is paramount, necessitating a specialized approach to [[Computer Architecture]] centered around extreme [[Fault Tolerance]].

The primary engineering hurdle in deep space is the presence of intense cosmic radiation. Unlike the shielded environment of Earth, spacecraft are susceptible to [[Single Event Upsets (SEU)]], a phenomenon where high-energy particles strike semiconductors, causing bit-flips in memory or logic gates. In a mission-critical flight system, an uncorrected error could lead to the loss of navigation data or a total system crash.

To combat these environmental hazards, NASA engineers implemented a multi-layered strategy involving both hardware and software redundancy. The computing system utilizes redundant processing cores that operate in tandem, employing a "voting" mechanism. In this configuration, multiple processors execute the same instructions, and the system compares the outputs; if one processor provides a divergent result due to a radiation-induced error, the system can identify and disregard the faulty data, allowing the mission to proceed safely.

Furthermore, the integration of advanced Error-Correcting Code (ECC) memory provides an additional layer of protection, detecting and repairing memory corruption in real-time. This synergy between hardened [[Embedded Systems]] and resilient software logic ensures that the [[Artemis II]] mission can withstand the harsh lunar environment, providing a robust blueprint for future long-duration missions to Mars and beyond.