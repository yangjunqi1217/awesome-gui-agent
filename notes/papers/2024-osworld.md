# OSWorld

- **Year**: 2024
- **Paper**: OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments
- **Repo**: https://github.com/xlang-ai/OSWorld
- **Tags**: `#benchmark` `#desktop` `#grounding` `#planning` `#reproduce`
- **Status**: `candidate`

## One-line Takeaway

OSWorld is the key desktop-computer benchmark for testing whether a multimodal agent can complete open-ended tasks in a real OS environment, not just in a web page or toy UI.

## Problem

Most early agent benchmarks over-measured browser tasks or structured tool APIs. Desktop computer use needs window management, files, apps, settings, local state, visual grounding, and long-horizon recovery.

## Method

The benchmark runs agents in real computer environments and evaluates task success across operating-system style workflows. It stresses screenshot understanding, action execution, and multi-step planning.

## Evidence To Verify

- Task categories and apps covered.
- Environment setup and reproducibility cost.
- Human baseline vs current model baseline.
- Whether evaluation requires manual judgment or automated state checks.
- Failure breakdown: grounding vs planning vs environment issues.

## Evaluation Lens

Use OSWorld to answer desktop-level questions:

- Can an agent coordinate multiple applications and local files?
- Does the agent recover when an app state is not what it expected?
- Are results comparable across screenshot-only, accessibility-tree, and hybrid API agents?
- Does a reported score use the official environment and task split?

Do not use OSWorld alone to answer:

- Fine-grained grounding quality. Use ScreenSpot-Pro or OSWorld-G.
- Browser-only skill. Use WebArena/VisualWebArena/BrowserGym.
- Mobile skill. Use AndroidWorld/AndroidLab/SPA-Bench.

## Reproduction Notes

Likely costs and risks:

- Environment setup may dominate the first reproduction sprint.
- VM/app version drift can change task behavior.
- Closed-model baselines may depend on model versions that are no longer available.
- Action-space differences can make leaderboards misleading.

Minimal reproduction target:

1. Install the environment and run one task with a trivial baseline.
2. Run a small agent on 5-10 tasks, logging screenshots and actions.
3. Categorize failures manually into grounding, planning, state, and evaluator categories.

## Why It Matters To Us

OSWorld should be our default reference when discussing desktop GUI agent capability. We should also inspect whether reported scores are comparable across agent stacks, action spaces, and environment versions.

## Decision

Keep as a core benchmark. Before building an OS-level agent, inspect OSWorld setup and decide whether to reproduce the official benchmark or use a smaller OSWorld-style internal suite.

## Follow-ups

- [ ] Read the paper carefully.
- [ ] Run one minimal local benchmark episode.
- [ ] Compare with OSWorld-G and OSWorld-Human.
- [ ] Add a table of models and reported scores once sources are verified.
