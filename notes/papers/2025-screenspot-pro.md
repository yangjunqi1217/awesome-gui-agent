# ScreenSpot-Pro

- **Year**: 2025
- **Paper**: GUI Grounding for Professional High-Resolution Computer Use
- **Repo**: https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding
- **Tags**: `#benchmark` `#grounding` `#desktop`
- **Status**: `candidate`

## One-line Takeaway

ScreenSpot-Pro isolates a key bottleneck: finding the right UI element in dense, high-resolution, professional interfaces.

## Problem

End-to-end GUI agents fail when they cannot accurately ground instructions to UI targets. Professional software makes this worse because screens are dense, icons are small, and many controls look similar.

## Method

The benchmark evaluates GUI grounding on high-resolution professional UI screenshots. It focuses on whether models can localize the correct target element.

## Evidence To Verify

- Dataset domains and screen resolutions.
- Annotation format and localization metric.
- Model leaderboard and error categories.
- How it compares with earlier ScreenSpot/GUI grounding benchmarks.

## Why It Matters To Us

Grounding errors cascade into planning failures. We should use this benchmark when evaluating whether a model is ready for real desktop applications, especially IDEs, design tools, office software, or scientific tools.

## Follow-ups

- [ ] Read paper and inspect dataset examples.
- [ ] Add grounding metrics definitions.
- [ ] Compare with OmniParser and OSWorld-G.
