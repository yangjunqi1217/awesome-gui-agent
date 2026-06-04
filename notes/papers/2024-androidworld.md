# AndroidWorld

- **Year**: 2024
- **Paper**: AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents
- **Repo**: https://github.com/google-research/android_world
- **Tags**: `#benchmark` `#mobile` `#planning` `#grounding`
- **Status**: `candidate`

## One-line Takeaway

AndroidWorld is the main Android/mobile benchmark to track because mobile agents face different constraints from desktop and web agents.

## Problem

Mobile GUI agents must deal with small screens, gestures, app-specific flows, OS permissions, device state, and less visible information. Desktop/web agent assumptions do not transfer cleanly.

## Method

AndroidWorld provides an environment and benchmark tasks for autonomous agents interacting with Android apps and device state.

## Evidence To Verify

- Task set and supported apps.
- Interaction API: tap, type, swipe, back/home, app switching.
- Evaluation reliability.
- Device/emulator setup.
- Generalization across app versions and layouts.

## Evaluation Lens

Use AndroidWorld to answer mobile-agent questions:

- Can an agent complete tasks in real Android apps with stateful setup/teardown?
- Does it handle gestures, permissions, navigation stacks, app switching, and small screens?
- Are tasks programmatically parameterized and reproducible?
- Does a method generalize beyond one device/app configuration?

Do not use AndroidWorld alone to answer:

- Desktop or browser workflow capability.
- Fine-grained high-resolution desktop grounding.
- Safety under malicious UI or notification injection without dedicated adversarial tasks.

## Reproduction Notes

Likely costs and risks:

- Android emulator/device setup can be fragile.
- App versions and permissions can drift.
- Success checks depend on robust task initialization and teardown.
- Mobile action abstractions differ across papers, making leaderboard comparisons tricky.

Minimal reproduction target:

1. Set up one emulator and run one task manually.
2. Run a simple agent on 5 tasks and record screen/action traces.
3. Create a mobile-specific failure taxonomy: navigation, gesture, text input, permission, grounding, task-state.

## Why It Matters To Us

Mobile is a distinct axis of GUI agency. We should avoid treating browser/desktop success as evidence of mobile capability without AndroidWorld-style evaluation.

## Decision

Keep as the default mobile benchmark. Compare with AndroidLab and SPA-Bench before committing to a mobile reproduction project.

## Follow-ups

- [ ] Read paper and install notes.
- [ ] Compare with AndroidControl and MobileAgent-style work.
- [ ] Create a mobile-specific failure taxonomy.
