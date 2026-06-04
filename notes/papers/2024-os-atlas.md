# OS-ATLAS

- **Year**: 2024
- **Paper**: OS-ATLAS: A Foundation Action Model for Generalist GUI Agents
- **Venue**: ICLR 2025 Spotlight
- **Links**: https://arxiv.org/abs/2410.23218, https://github.com/OS-Copilot/OS-Atlas
- **Tags**: `#grounding` `#model` `#desktop` `#mobile` `#web`
- **Status**: `candidate`

## One-line Takeaway

OS-ATLAS is a foundation action model for cross-platform GUI agents, built around large-scale GUI grounding/action data.

## Problem

Single-environment GUI agents overfit to web DOMs, Android XML, or desktop-specific affordances. A generalist GUI action model needs cross-platform data and a unified grounding/action formulation.

## Method

The work builds a multi-platform grounding-data synthesis toolkit and a large GUI-element corpus, then trains a foundation action model for desktop, mobile, and web settings.

## Evidence To Verify

- Data sources and synthesis pipeline.
- Whether the corpus includes real user trajectories, synthetic labels, or both.
- Cross-platform benchmark coverage.
- How much improvement comes from scale vs architecture vs training objective.

## Why It Matters To Us

OS-ATLAS is one of the main links between GUI grounding and generalist action models. It should be compared with SeeClick, ShowUI, Aguvis, UI-TARS, and ScaleCUA.

## Follow-ups

- [ ] Read paper.
- [ ] Inspect repo/data release.
- [ ] Add comparison with SeeClick and ShowUI.
