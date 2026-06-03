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

## Curated Maps

The two highest-signal entry points are:

- [docs/academic-papers.md](docs/academic-papers.md): top-venue and high-impact academic paper map.
- [docs/industry-reports.md](docs/industry-reports.md): industry technical reports, products, open-source systems, sandboxes, and guardrails.

Use [docs/taxonomy.md](docs/taxonomy.md) to classify new entries and [docs/source-map.md](docs/source-map.md) to find upstream discovery sources.

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

- [ ] [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890).
- [ ] [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501).
- [ ] [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/).
- [ ] [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434).

### Benchmarks

- [ ] [OSWorld](https://github.com/xlang-ai/OSWorld): open-ended desktop tasks in real computer environments.
- [ ] [WebArena](https://github.com/web-arena-x/webarena): realistic web environment for autonomous agents.
- [ ] [VisualWebArena](https://aclanthology.org/2024.acl-long.50/): visually grounded web-agent tasks.
- [ ] [AndroidWorld](https://github.com/google-research/android_world): Android environment and benchmark for autonomous agents.
- [ ] [WorkArena](https://proceedings.mlr.press/v235/drouin24a.html): enterprise knowledge-work benchmark.
- [ ] [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena): Windows OS-agent benchmark.
- [ ] [ScreenSpot-Pro](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding): professional high-resolution GUI grounding.
- [ ] [OSWorld-G](https://github.com/xlang-ai/OSWorld-G): grounding-focused OSWorld extension.
- [ ] [VideoGUI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html): GUI automation from instructional videos.
- [ ] [RiOSWorld](https://github.com/yjyddq/RiOSWorld): risk benchmark for multimodal computer-use agents.
- [ ] [OS-Harm](https://github.com/tml-epfl/os-harm): safety benchmark for computer-use agents.

### Models And Agents

- [ ] [OpenCUA](https://github.com/xlang-ai/OpenCUA): open foundations for computer-use agents.
- [ ] [UI-TARS](https://github.com/bytedance/UI-TARS): native GUI agent work from ByteDance.
- [ ] [UI-TARS-2 Technical Report](https://arxiv.org/abs/2509.02544): multi-turn RL and data flywheel.
- [ ] [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop): open multimodal agent stack for desktop use.
- [ ] [SeeClick](https://github.com/njucckevin/SeeClick): visual GUI agent model/data/code.
- [ ] [OS-ATLAS](https://github.com/OS-Copilot/OS-Atlas): foundation action model for generalist GUI agents.
- [ ] [ShowUI](https://github.com/showlab/ShowUI): vision-language-action model for GUI visual agents.
- [ ] [Aguvis](https://github.com/xlang-ai/aguvis): unified pure-vision GUI agent.
- [ ] [Agent S](https://proceedings.iclr.cc/paper_files/paper/2025/hash/394c7c30ea87b5c3521b4d9e9d419071-Abstract-Conference.html): open agentic framework for computer use.
- [ ] [ScaleCUA](https://github.com/OpenGVLab/ScaleCUA): cross-platform computer-use agent.
- [ ] [Mobile-Agent-v3](https://arxiv.org/abs/2508.15144): fundamental agents for GUI automation.
- [ ] [UI-Venus Technical Report](https://arxiv.org/abs/2508.10833): high-performance UI agents with RFT.
- [ ] [ShowUI-Aloha](https://github.com/showlab/ShowUI-Aloha): human-taught computer-use agent for Windows and macOS.
- [ ] [EvoCUA](https://github.com/meituan/EvoCUA): evolving computer-use agent.
- [ ] [SEAgent](https://github.com/SunzeY/SEAgent): self-evolving computer-use agent.

### Learning And Reward Models

- [ ] [WebRL](https://openreview.net/forum?id=oVKEAFjEqv): self-evolving online curriculum RL for web agents.
- [ ] [WebAgent-R1](https://arxiv.org/abs/2505.16421): end-to-end multi-turn RL for web agents.
- [ ] [DigiRL](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html): in-the-wild mobile device-control RL.
- [ ] [Web-Shepherd](https://arxiv.org/abs/2505.15277): process reward model for web agents.
- [ ] [GUI-G1](https://arxiv.org/abs/2505.15810): R1-Zero-like RL for GUI grounding.

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
- [ ] [AgentDAM](https://arxiv.org/abs/2503.09780): privacy leakage evaluation for autonomous web agents.
- [ ] [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/): adversarial UI attacks.
- [ ] [ST-WebAgentBench](https://openreview.net/forum?id=MuCDzH0ctf): safety and trustworthiness in web agents.
- [ ] Prompt-injection, malicious UI, and environmental injection attacks against browser/computer-use agents.

## Notes Index

### Papers

- [OSWorld](notes/papers/2024-osworld.md)
- [WebArena](notes/papers/2023-webarena.md)
- [AndroidWorld](notes/papers/2024-androidworld.md)
- [ScreenSpot-Pro](notes/papers/2025-screenspot-pro.md)

### Repos And Systems

- [Academic paper map](docs/academic-papers.md)
- [Industry technical reports](docs/industry-reports.md)
- [Public source map](docs/source-map.md)
- [Working taxonomy](docs/taxonomy.md)

## Maintenance

- Review public upstream lists weekly or before any literature review sprint.
- Prefer fewer, higher-signal entries over broad dumping.
- Every note should end with a concrete decision: read deeper, reproduce, benchmark, ignore, or watch.
- For copied facts from public repos, link the source and write our own summary.
