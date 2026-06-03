# trycua/cua

- **Repo**: https://github.com/trycua/cua
- **Owner**: trycua
- **Tags**: `#tooling` `#desktop` `#benchmark` `#product`
- **Status**: `candidate`

## What It Is

Open-source infrastructure for computer-use agents, including sandboxes, SDKs, and evaluation support for agents that operate full desktops.

## Why It Matters

Practical GUI-agent work needs reliable environments more than another toy demo. A reusable sandbox/runtime layer could make experiments more reproducible.

## What To Inspect

- Supported operating systems and isolation model.
- Whether it handles VM snapshots, browser profiles, file transfer, and screen/action logging.
- How benchmarks are represented.
- Whether it integrates cleanly with OpenAI, Anthropic, local VLMs, or custom agents.

## Decision

Watch and test. This is likely relevant infrastructure if we run our own GUI-agent experiments.

## Follow-ups

- [ ] Try the quickstart.
- [ ] Document setup cost on macOS.
- [ ] Compare with OSWorld setup and browser-use style stacks.
