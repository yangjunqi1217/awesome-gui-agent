# Source Map

This file records where we discover GUI agent material. It is a map of sources, not a mirrored awesome list.

## Existing Awesome Lists

| Source | Focus | Why Monitor |
| --- | --- | --- |
| [showlab/Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) | Broad datasets, benchmarks, models, surveys, projects, safety | High-coverage starting point with frequent updates. |
| [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | Paper-first index with environment and keyword browsing | Useful for literature review and recency tracking. |
| [ZJU-REAL/Awesome-GUI-Agents](https://github.com/ZJU-REAL/Awesome-GUI-Agents) | Weekly paper list, modules, data, RL, memory, privacy | Good taxonomy inspiration and emerging-topic coverage. |
| [Autonomous-Agent-Team/Awesome-GUI-Agent-Safety](https://github.com/Autonomous-Agent-Team/Awesome-GUI-Agent-Safety) | GUI agent safety | Dedicated safety tracker. |
| [cdxeve/awesome-computer-use-agents](https://github.com/cdxeve/awesome-computer-use-agents) | Computer-use agents across GUI and terminal/CLI | Useful for broader CUA framing. |

Local snapshots of selected public READMEs can be kept under `sources/` while researching, but they are ignored by Git. Do not copy long upstream lists into our README.

## Benchmarks And Evaluation Repos

| Repo | Environment | What To Read For |
| --- | --- | --- |
| [xlang-ai/OSWorld](https://github.com/xlang-ai/OSWorld) | Desktop OS | Open-ended task design, virtual desktop evaluation, success metrics. |
| [web-arena-x/webarena](https://github.com/web-arena-x/webarena) | Web | Realistic web tasks, site setup, agent failure patterns. |
| [google-research/android_world](https://github.com/google-research/android_world) | Android | Mobile tasks, device control, app-state evaluation. |
| [likaixin2000/ScreenSpot-Pro-GUI-Grounding](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) | GUI grounding | High-resolution professional GUI grounding. |
| [xlang-ai/OSWorld-G](https://github.com/xlang-ai/OSWorld-G) | Desktop grounding | UI decomposition and grounding data generation. |
| [yjyddq/RiOSWorld](https://github.com/yjyddq/RiOSWorld) | Safety/risk | Risk evaluation for multimodal computer-use agents. |
| [tml-epfl/os-harm](https://github.com/tml-epfl/os-harm) | Safety | Harm-oriented benchmark design. |
| [ServiceNow/webarena-verified](https://github.com/ServiceNow/webarena-verified) | Web | Verification and benchmark reliability. |

See [academic-papers.md](academic-papers.md) for the curated paper-level map and [industry-reports.md](industry-reports.md) for technical reports and systems.

## Models, Agents, And Training

| Repo | Focus | What To Read For |
| --- | --- | --- |
| [xlang-ai/OpenCUA](https://github.com/xlang-ai/OpenCUA) | Open computer-use foundations | Data, model, training recipe, evaluation claims. |
| [bytedance/UI-TARS](https://github.com/bytedance/UI-TARS) | Native GUI agent | Model interface, grounding, action format, agent architecture. |
| [bytedance/UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) | Desktop agent stack | Productized desktop integration and infra. |
| [njucckevin/SeeClick](https://github.com/njucckevin/SeeClick) | Visual GUI agent | Visual grounding and action prediction data. |
| [OpenGVLab/ScaleCUA](https://github.com/OpenGVLab/ScaleCUA) | Cross-platform CUA | Scaling and cross-platform generalization. |
| [showlab/ShowUI-Aloha](https://github.com/showlab/ShowUI-Aloha) | Human-taught CUA | Demonstration learning and desktop behavior. |
| [meituan/EvoCUA](https://github.com/meituan/EvoCUA) | Evolving CUA | Self-improvement setup and evidence quality. |
| [SunzeY/SEAgent](https://github.com/SunzeY/SEAgent) | Self-evolving CUA | Learning from experience and autonomous improvement. |
| [xlang-ai/CUA-Gym](https://github.com/xlang-ai/CUA-Gym) | RLVR training data | Verifiable training tasks and RL pipeline. |

## Infrastructure

| Repo | Focus | What To Read For |
| --- | --- | --- |
| [trycua/cua](https://github.com/trycua/cua) | Sandboxes, SDKs, benchmarks | Practical environment management for CUA. |
| [openai/openai-cua-sample-app](https://github.com/openai/openai-cua-sample-app) | OpenAI CUA sample | API usage and reference app structure. |
| [microsoft/OmniParser](https://github.com/microsoft/OmniParser) | Screen parsing | UI element detection and parser-agent interface. |
| [langchain-ai/langgraph-cua-py](https://github.com/langchain-ai/langgraph-cua-py) | LangGraph CUA | Agent loop and framework integration. |
| [vercel-labs/ai-sdk-computer-use](https://github.com/vercel-labs/ai-sdk-computer-use) | Web app CUA demo | Frontend integration and UX patterns. |

## Products And APIs

Track these when product behavior, API surface, or safety policy changes:

- [OpenAI Computer-Using Agent](https://openai.com/index/computer-using-agent/)
- [Anthropic computer use](https://www.anthropic.com/news/3-5-models-and-computer-use)
- Google Project Mariner / Gemini browser-control work
- Browser-use and hosted browser automation products

## Search Queries

Useful GitHub queries:

- `awesome gui agent`
- `GUI agents paper list`
- `computer use agent`
- `GUI agent benchmark`
- `OSWorld`
- `WebArena`
- `AndroidWorld`
- `ScreenSpot`
- `OmniParser`
- `UI-TARS`

Useful paper queries:

- `GUI agent survey`
- `computer-use agent benchmark`
- `GUI grounding benchmark`
- `multimodal agent desktop benchmark`
- `browser agent prompt injection`
- `computer-use agent safety`
