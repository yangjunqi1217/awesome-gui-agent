# WebArena

- **Year**: 2023
- **Paper**: WebArena: A Realistic Web Environment for Building Autonomous Agents
- **Repo**: https://github.com/web-arena-x/webarena
- **Tags**: `#benchmark` `#browser` `#planning` `#safety`
- **Status**: `candidate`

## One-line Takeaway

WebArena is the baseline realistic web-agent benchmark: useful for browser task planning, but not enough by itself for full computer-use agents.

## Problem

Browser agents need realistic websites with accounts, state, forms, search, navigation, and task verification. Static web QA and simple DOM tasks do not capture the workflow complexity.

## Method

WebArena provides self-hosted websites and tasks that require multi-step web interaction. Agents operate through browser actions and are judged by task success.

## Evidence To Verify

- Website set and task distribution.
- How task verification works.
- How much agents can rely on DOM/accessibility vs screenshot.
- Common failure modes: search, state tracking, form filling, instruction following, hidden dependencies.

## Why It Matters To Us

WebArena is the web-control counterpart to OSWorld. It is useful for browser-only baselines, but we should separate WebArena progress from OS-level GUI progress.

## Follow-ups

- [ ] Read paper and repo setup.
- [ ] Compare WebArena, WebArena Verified, and WebArena Infinity.
- [ ] Track safety/prompt-injection extensions for browser agents.
