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

## Why It Matters To Us

Mobile is a distinct axis of GUI agency. We should avoid treating browser/desktop success as evidence of mobile capability without AndroidWorld-style evaluation.

## Follow-ups

- [ ] Read paper and install notes.
- [ ] Compare with AndroidControl and MobileAgent-style work.
- [ ] Create a mobile-specific failure taxonomy.
