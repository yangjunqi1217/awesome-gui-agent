# GUI Agent Model Zoo And System Map

This file tracks GUI-agent models, products, frameworks, and infrastructure. It separates venue status from release status because many high-impact GUI-agent systems are technical reports or product releases rather than conference papers.

Access labels:

- `open-weights`: model weights are released.
- `open-code`: code or framework is released, but weights may be partial or absent.
- `closed-api`: model is available only through a hosted API or product.
- `technical-report`: paper/report exists; release status needs verification.
- `infrastructure`: not a model, but important for running or evaluating agents.

## Open Or Partly Open Models

| System | Team | Access | Environment | Venue / report status | What It Provides |
| --- | --- | --- | --- | --- | --- |
| [OpenCUA](https://github.com/xlang-ai/OpenCUA) | XLang | open-weights / open-code | Windows, macOS, Ubuntu desktop | NeurIPS 2025 Spotlight | Models, AgentNet data, annotation tools, and training/evaluation pipeline for computer-use agents. |
| [UI-TARS](https://github.com/bytedance/UI-TARS) | ByteDance Seed | open-weights / open-code | Desktop, mobile, web, games | Technical report; UI-TARS-1.5-7B released | Native GUI model family; screenshot-to-action prompts and OSWorld/AndroidWorld/Web tasks. |
| [UI-TARS-2](https://arxiv.org/abs/2509.02544) | ByteDance Seed | technical-report | Desktop, mobile, web, code/tool use | Technical report | Multi-turn RL, data flywheel, unified sandbox, and hybrid GUI/code/tool training. |
| [ShowUI](https://github.com/showlab/ShowUI) | Show Lab / collaborators | open-weights / open-code | Mobile, web, computer use | CVPR 2025 | Lightweight VLA model with UI-guided token selection and interleaved action history. |
| [OS-ATLAS](https://github.com/OS-Copilot/OS-Atlas) | OS-Copilot / Shanghai AI Lab | open-code / model release | Desktop, mobile, web | ICLR 2025 | Cross-platform grounding corpus and foundation action model for GUI agents. |
| [Aguvis](https://proceedings.mlr.press/v267/xu25ae.html) | Salesforce / OSU / collaborators | paper; release status verify | General GUI | ICML 2025 | Pure-vision GUI agent that avoids DOM/accessibility text reliance. |
| [ScaleCUA](https://github.com/OpenGVLab/ScaleCUA) | OpenGVLab | open-weights / open-code | Windows, macOS, Ubuntu, Android | Venue verify; technical report | Cross-platform CUA data scaling and open-source computer-use models. |
| [Mobile-Agent](https://github.com/X-PLUG/MobileAgent) | Alibaba Tongyi / X-PLUG | open-code / model release | Mobile, desktop, web | Technical report series | Mobile-Agent-v3/v3.5 and GUI-Owl models for multi-platform GUI automation. |
| [MobileRL](https://openreview.net/forum?id=C3F0G9nXhl) | THUDM | open-code announced | Mobile | ICLR 2026 Poster | Online agentic RL recipe for AndroidWorld and AndroidLab-style mobile environments. |
| [OmniParser](https://github.com/microsoft/OmniParser) | Microsoft | open-code / model release | General GUI perception | Technical report | Screen parsing layer for interactable element detection and icon captioning; not a full agent. |
| [Magentic-UI](https://www.microsoft.com/en-us/research/publication/magentic-ui-report/) | Microsoft Research | open-code research prototype | Web / computer-use assistance | Technical report | Human-in-the-loop agentic UI with co-planning, action guards, and verification. |
| [Agent S](https://openreview.net/forum?id=lIVRgt4nLv) | Simular / academic collaborators | open-code framework | Desktop | ICLR 2025 Poster | Agent-computer interface, memory, and control framework for desktop tasks. |

## Closed Or Hosted Computer-Use Systems

| System | Provider | Access | Environment | Public Evidence | What To Track |
| --- | --- | --- | --- | --- | --- |
| [Computer-Using Agent](https://openai.com/index/computer-using-agent/) | OpenAI | closed-api / product | Computer-use and web tasks | OpenAI reports OSWorld, WebArena, and WebVoyager results | Action schema, safety confirmations, API surface, sample app behavior, supported sandboxes. |
| [Claude computer use](https://www.anthropic.com/news/3-5-models-and-computer-use?lang=us) | Anthropic | closed-api beta / hosted providers | General GUI via screenshots, cursor, clicks, typing | Anthropic launch post and model development notes | Tool protocol, sandbox requirements, scrolling/dragging reliability, safety classifiers. |
| [Project Mariner](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-ai-update-december-2024/) | Google DeepMind / Google | closed prototype / product path | Browser / Chrome-first web tasks | Google announcement and Gemini product updates | Whether Mariner-style browser control moves into Gemini app, Search, Vertex AI, or Chrome. |
| Claude / Gemini / GPT frontier VLMs as baselines | Anthropic / Google / OpenAI | closed-api | Web, desktop, mobile depending on wrapper | Benchmarks report them as baselines | Use as comparison models; do not treat as reproducible open baselines. |

## Frameworks And Execution Infrastructure

| System | Team | Access | Environment | Why It Matters |
| --- | --- | --- | --- | --- |
| [trycua/cua](https://github.com/trycua/cua) | CUA | infrastructure | macOS, Linux, virtual desktops | Sandboxes, SDKs, and repeatable computer-use execution. |
| [BrowserGym](https://github.com/ServiceNow/BrowserGym) | ServiceNow Research | infrastructure | Web | Gymnasium-style environment wrapping MiniWoB, WebArena, VisualWebArena, WorkArena, WebLINX, and more. |
| [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop) | ByteDance | infrastructure / app | Desktop | Open desktop application for running UI-TARS-style agents. |
| [OpenAI CUA sample app](https://github.com/openai/openai-cua-sample-app) | OpenAI | infrastructure sample | Web/computer-use loop | Practical reference for CUA loop design with a hosted model. |
| [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena) | Microsoft | infrastructure / benchmark | Windows desktop | Reproducible Windows environment for desktop agents. |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | XLang | infrastructure / benchmark | Desktop OS | Standard desktop environment for real computer-use evaluation. |

## Immediate Reading Priority

1. OpenCUA, UI-TARS, ShowUI, OS-ATLAS, Aguvis.
2. OpenAI CUA, Anthropic computer use, Project Mariner, Magentic-UI.
3. ScaleCUA, Mobile-Agent-v3/v3.5, MobileRL, UI-TARS-2.
4. OmniParser, BrowserGym, trycua/cua, Windows Agent Arena, OSWorld.
