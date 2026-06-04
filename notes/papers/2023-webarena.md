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

## Evaluation Lens

Use WebArena to answer web-agent questions:

- Can an agent complete realistic multi-step web tasks in stateful websites?
- Does it plan over account state, forms, search, shopping, forums, and content management?
- How much does structured browser state help relative to screenshots?
- Are failures caused by exploration, form semantics, hidden state, or final-answer verification?

Do not use WebArena alone to answer:

- Visual grounding under screenshots. Use VisualWebArena or ScreenSpot-style tasks.
- Live-web robustness. Use WebCanvas, WebVoyager, or online evaluations.
- Desktop/multi-app workflow capability. Use OSWorld or WindowsAgentArena.

## Reproduction Notes

Likely costs and risks:

- Self-hosted web environments require setup and seeded data.
- Browser automation details can affect action success.
- Some results may rely on DOM pruning, accessibility trees, or customized action abstractions.
- The benchmark can reward website-specific heuristics if not evaluated carefully.

Minimal reproduction target:

1. Run the environment locally and complete one task manually.
2. Run a baseline agent on 5-10 tasks with full trajectory logs.
3. Compare screenshot-only, DOM-based, and accessibility-tree observations if feasible.

## Why It Matters To Us

WebArena is the web-control counterpart to OSWorld. It is useful for browser-only baselines, but we should separate WebArena progress from OS-level GUI progress.

## Decision

Keep as the default browser-agent benchmark. Pair it with VisualWebArena for visual grounding and with safety benchmarks for prompt-injection risk.

## Follow-ups

- [ ] Read paper and repo setup.
- [ ] Compare WebArena, WebArena Verified, and WebArena Infinity.
- [ ] Track safety/prompt-injection extensions for browser agents.
