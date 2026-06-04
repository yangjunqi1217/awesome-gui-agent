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

## Evaluation Lens

Use ScreenSpot-Pro to answer grounding questions:

- Can a model localize UI targets in dense professional software?
- Does it handle tiny icons, repeated controls, toolbars, panels, and high-resolution screenshots?
- Are failures caused by visual perception, text recognition, instruction ambiguity, or coordinate precision?
- Does a screen parser like OmniParser help or hurt?

Do not use ScreenSpot-Pro alone to answer:

- Long-horizon planning or recovery.
- Whether grounding improvements transfer to OSWorld task success.
- Safety or irreversible-action control.

## Reproduction Notes

Likely costs and risks:

- Need to inspect metric definitions before comparing scores.
- Pointing/box conventions can change apparent accuracy.
- Professional software screenshots may expose different domain biases than web/mobile screenshots.
- Model resize/cropping policy can dominate results.

Minimal reproduction target:

1. Inspect 30 dataset examples by domain.
2. Run one general VLM and one GUI-specialized model if available.
3. Run OmniParser or another parser on the same examples and compare element proposals.

## Why It Matters To Us

Grounding errors cascade into planning failures. We should use this benchmark when evaluating whether a model is ready for real desktop applications, especially IDEs, design tools, office software, or scientific tools.

## Decision

Keep as the core grounding benchmark for professional desktop UIs. Pair with OSWorld-G for synthetic decomposition and with OSWorld for downstream task transfer.

## Follow-ups

- [ ] Read paper and inspect dataset examples.
- [ ] Add grounding metrics definitions.
- [ ] Compare with OmniParser and OSWorld-G.
