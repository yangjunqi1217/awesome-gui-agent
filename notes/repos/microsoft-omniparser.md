# microsoft/OmniParser

- **Repo**: https://github.com/microsoft/OmniParser
- **Owner**: Microsoft
- **Tags**: `#grounding` `#tooling` `#desktop` `#browser`
- **Status**: `candidate`

## What It Is

Screen parsing tool for vision-based GUI agents. It aims to turn screenshots into structured UI elements that an agent can reason over.

## Why It Matters

Pure screenshot agents often waste context and miss small controls. A parser layer can expose bounding boxes, text, and candidate clickable elements, improving grounding and action selection.

## What To Inspect

- Element detection quality on desktop, browser, and mobile screenshots.
- Latency and hardware requirements.
- Output schema and how easy it is to plug into an agent loop.
- Failure cases on dense professional GUIs.

## Decision

Watch and test. It is a likely baseline for perception/grounding experiments.

## Follow-ups

- [ ] Run on screenshots from OSWorld or our own desktop tasks.
- [ ] Compare with model-native grounding.
- [ ] Check license and deployment constraints.
