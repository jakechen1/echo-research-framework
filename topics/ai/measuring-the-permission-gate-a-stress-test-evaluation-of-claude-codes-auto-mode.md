---
title: Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code's Auto Mode
created: 2025-05-20
source: https://arxiv.org/abs/2604.04978
tags: [AI Safety, Claude Code, Autonomous Agents, Cybersecurity, Software Engineering]
category: ai
---

# Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code's Auto Mode

This article examines the efficacy of the permission gating system implemented in [[Claude Code]]'s "auto mode." As one of the first deployed permission systems for [[AI Agents]] in a professional coding context, "auto mode" utilizes a two-stage transcript classifier to intercept and gate potentially dangerous tool calls.

## Overview
The study provides the first independent evaluation of the system's ability to handle "ambiguous authorization" scenarios. These are tasks where a user's primary intent is clear, but the "blast radius," target scope, or specific risk level of the operation is underspecified. To