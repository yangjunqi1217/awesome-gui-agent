# Awesome GUI Agent

Private reading hub for GUI agents, computer-use agents, browser agents, mobile-use agents, and GUI safety.

This repository is for our own reading notes and research tracking. It is not meant to replace the public awesome lists. Public lists are good for breadth; this repo should keep the smaller set of papers, repos, benchmarks, and products that we actually read, evaluate, or plan to use.

## Scope

GUI agents are agents that observe and operate graphical interfaces: desktop OSes, browsers, mobile apps, web apps, and professional tools. We track work that improves one or more of these layers:

- **Perception and grounding**: screenshots, UI parsing, element localization, coordinates, OCR, accessibility trees.
- **Planning and control**: long-horizon task decomposition, reflection, memory, recovery, tool use, action spaces.
- **Benchmarks and evaluation**: OS, browser, mobile, grounding, web, safety, and task-efficiency benchmarks.
- **Training data and learning**: demonstrations, synthetic task generation, RL/RLVR, reward models, distillation.
- **Safety and reliability**: prompt injection, adversarial UI, privacy, irreversible actions, permission boundaries.
- **Products and infra**: local/remote desktops, browser-use stacks, sandboxes, CUA APIs, agent SDKs.

See [docs/taxonomy.md](docs/taxonomy.md) for the working taxonomy.

## How We Use This Repo

1. Add candidate papers, repos, and benchmarks to the relevant watchlist below.
2. When someone reads something seriously, create a note from [notes/templates/paper-note.md](notes/templates/paper-note.md) or [notes/templates/repo-note.md](notes/templates/repo-note.md).
3. Link the note from this README under the relevant section.
4. Keep notes opinionated: what problem it solves, why it matters, how convincing it is, and what we should do next.

Naming convention:

- Papers: `notes/papers/YYYY-short-title.md`
- Repos/projects: `notes/repos/repo-owner-name.md`
- Products/APIs: `notes/products/product-name.md`

## Existing Public Lists To Monitor

These are our upstream discovery sources. We should use them for breadth and updates, but keep our own notes independent.

- [showlab/Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent): broad list covering datasets, benchmarks, models, surveys, projects, and safety.
- [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List): paper-first list with environment and keyword browsing.
- [ZJU-REAL/Awesome-GUI-Agents](https://github.com/ZJU-REAL/Awesome-GUI-Agents): weekly paper list and modular taxonomy.
- [Autonomous-Agent-Team/Awesome-GUI-Agent-Safety](https://github.com/Autonomous-Agent-Team/Awesome-GUI-Agent-Safety): safety-focused papers, attacks, defenses, and evaluation.
- [cdxeve/awesome-computer-use-agents](https://github.com/cdxeve/awesome-computer-use-agents): computer-use agents, including GUI and terminal/CLI directions.

More detail is in [docs/source-map.md](docs/source-map.md).

## Core Reading Queue

### Surveys And Framing

- [ ] Survey of GUI agents and foundation-model-based GUI automation.
- [ ] Trustworthy GUI agents: reliability, safety, attacks, and defenses.
- [ ] Computer-use agents: relation between GUI control, browser agents, and OS-level automation.

### Benchmarks

- [ ] [OSWorld](https://github.com/xlang-ai/OSWorld): open-ended desktop tasks in real computer environments.
- [ ] [WebArena](https://github.com/web-arena-x/webarena): realistic web environment for autonomous agents.
- [ ] [AndroidWorld](https://github.com/google-research/android_world): Android environment and benchmark for autonomous agents.
- [ ] [ScreenSpot-Pro](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding): professional high-resolution GUI grounding.
- [ ] [OSWorld-G](https://github.com/xlang-ai/OSWorld-G): grounding-focused OSWorld extension.
- [ ] [RiOSWorld](https://github.com/yjyddq/RiOSWorld): risk benchmark for multimodal computer-use agents.
- [ ] [OS-Harm](https://github.com/tml-epfl/os-harm): safety benchmark for computer-use agents.

### Models And Agents

- [ ] [OpenCUA](https://github.com/xlang-ai/OpenCUA): open foundations for computer-use agents.
- [ ] [UI-TARS](https://github.com/bytedance/UI-TARS): native GUI agent work from ByteDance.
- [ ] [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop): open multimodal agent stack for desktop use.
- [ ] [SeeClick](https://github.com/njucckevin/SeeClick): visual GUI agent model/data/code.
- [ ] [ScaleCUA](https://github.com/OpenGVLab/ScaleCUA): cross-platform computer-use agent.
- [ ] [ShowUI-Aloha](https://github.com/showlab/ShowUI-Aloha): human-taught computer-use agent for Windows and macOS.
- [ ] [EvoCUA](https://github.com/meituan/EvoCUA): evolving computer-use agent.
- [ ] [SEAgent](https://github.com/SunzeY/SEAgent): self-evolving computer-use agent.

### Infrastructure And Tools

- [ ] [trycua/cua](https://github.com/trycua/cua): sandboxes, SDKs, and benchmarks for computer-use agents.
- [ ] [openai/openai-cua-sample-app](https://github.com/openai/openai-cua-sample-app): OpenAI CUA sample app.
- [ ] [microsoft/OmniParser](https://github.com/microsoft/OmniParser): screen parsing for vision-based GUI agents.
- [ ] [browser-use/vibetest-use](https://github.com/browser-use/vibetest-use): browser-use based QA testing.
- [ ] [langchain-ai/langgraph-cua-py](https://github.com/langchain-ai/langgraph-cua-py): CUA implementation with LangGraph.
- [ ] [vercel-labs/ai-sdk-computer-use](https://github.com/vercel-labs/ai-sdk-computer-use): computer-use agent with Next.js and Vercel AI SDK.

### Safety And Red Teaming

- [ ] [RedTeamCUA](https://github.com/OSU-NLP-Group/RedTeamCUA): adversarial testing in hybrid web-OS environments.
- [ ] [RiOSWorld](https://github.com/yjyddq/RiOSWorld): risk benchmark.
- [ ] [OS-Harm](https://github.com/tml-epfl/os-harm): harm-oriented computer-use safety benchmark.
- [ ] Prompt-injection and malicious UI attacks against browser/computer-use agents.

## Notes Index

### Papers

- [OSWorld](notes/papers/2024-osworld.md)
- [WebArena](notes/papers/2023-webarena.md)
- [AndroidWorld](notes/papers/2024-androidworld.md)
- [ScreenSpot-Pro](notes/papers/2025-screenspot-pro.md)

### Repos And Systems

- [Public source map](docs/source-map.md)
- [Working taxonomy](docs/taxonomy.md)

## Maintenance

- Review public upstream lists weekly or before any literature review sprint.
- Prefer fewer, higher-signal entries over broad dumping.
- Every note should end with a concrete decision: read deeper, reproduce, benchmark, ignore, or watch.
- For copied facts from public repos, link the source and write our own summary.
