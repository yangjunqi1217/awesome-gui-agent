# Industry Technical Reports And Systems

This file tracks industry-facing technical reports, model releases, products, and open-source systems relevant to GUI agents and computer-use agents.

The boundary is intentionally practical: include a report or system when it changes what we might use, reproduce, compare against, or build on. Benchmark claims are recorded as evidence, but the reading priority is the underlying mechanism.

Status labels:

- `priority`: read or test soon.
- `watch`: monitor for releases/results.
- `verify`: link, version, or claims need confirmation.

## Model And Agent Technical Reports

| Status | Report / system | Team | Link | Focus |
| --- | --- | --- | --- | --- |
| priority | OpenCUA: Open Foundations for Computer-Use Agents | XLang / Salesforce-style ecosystem | [GitHub](https://github.com/xlang-ai/OpenCUA) | Open CUA foundations, data, model, benchmarks; listed as NeurIPS 2025 Spotlight by repo metadata. |
| priority | UI-TARS: Pioneering Automated GUI Interaction with Native Agents | ByteDance | [Paper](https://arxiv.org/abs/2501.12326), [GitHub](https://github.com/bytedance/UI-TARS) | Native GUI agent model and action interface. |
| priority | UI-TARS-2 Technical Report: Advancing GUI Agent with Multi-Turn Reinforcement Learning | ByteDance Seed | [Paper](https://arxiv.org/abs/2509.02544) | Data flywheel, multi-turn RL, unified sandbox, hybrid GUI-terminal training. |
| priority | UI-TARS Desktop | ByteDance | [GitHub](https://github.com/bytedance/UI-TARS-desktop) | Open multimodal agent stack for desktop use. |
| priority | AutoGLM: Autonomous Foundation Agents for GUIs | Zhipu / Tsinghua | [Paper](https://arxiv.org/abs/2411.00820) | Foundation agent for phone and browser control with self-evolving RL. |
| priority | WebRL / ComputerRL / MobileRL line | Tsinghua / Zhipu | [WebRL](https://openreview.net/forum?id=oVKEAFjEqv), [ComputerRL](https://arxiv.org/abs/2508.14040), [MobileRL](https://arxiv.org/abs/2509.18119) | Online RL recipes across web, desktop, and mobile GUI agents. |
| priority | Mobile-Agent-v3: Fundamental Agents for GUI Automation | Alibaba Tongyi | [Paper](https://arxiv.org/abs/2508.15144), [GitHub](https://github.com/X-PLUG/MobileAgent) | GUI-Owl foundation model plus multi-agent GUI automation framework. |
| priority | UI-Venus Technical Report | Ant Group | [Paper](https://arxiv.org/abs/2508.10833) | Screenshot-only UI agent trained with reinforcement fine-tuning. |
| priority | ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data | Shanghai AI Lab / OpenGVLab | [GitHub](https://github.com/OpenGVLab/ScaleCUA), [Paper](https://arxiv.org/abs/2509.15221) | Cross-platform data and open computer-use models. |
| priority | OS-ATLAS: A Foundation Action Model for Generalist GUI Agents | Shanghai AI Lab / OS-Copilot | [Paper](https://arxiv.org/abs/2410.23218), [GitHub](https://github.com/OS-Copilot/OS-Atlas) | Multi-platform grounding and action model. |
| priority | ShowUI: One Vision-Language-Action Model for GUI Visual Agent | Show Lab / Microsoft / NUS | [Paper](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html), [GitHub](https://github.com/showlab/ShowUI) | Efficient VLA model for GUI tasks. |
| watch | ShowUI-Aloha | Show Lab | [GitHub](https://github.com/showlab/ShowUI-Aloha) | Human-taught CUA for Windows and macOS desktops. |
| watch | EvoCUA | Meituan | [GitHub](https://github.com/meituan/EvoCUA) | Learning from synthetic experience for CUA. |
| watch | SEAgent | Academic/industry mix | [GitHub](https://github.com/SunzeY/SEAgent) | Self-evolving CUA with autonomous learning from experience. |
| watch | AgentS3 | verify | listed by upstream | Scaling agents for computer use. |
| watch | UltraCUA | verify | listed by upstream | Foundation model for CUA with hybrid action. |
| watch | Holo1.5 | H Company | verify blog/repo | Open foundation models for computer-use agents. |
| watch | Fara-7B | Fara / verify | listed by upstream | Efficient agentic model for computer use. |
| watch | Step-GUI Technical Report | StepFun | [PDF](https://github.com/stepfun-ai/gelab-zero/blob/main/report/Step-GUI_Technical_Report.pdf) | GUI-agent technical report. |
| watch | MAI-UI Technical Report | Microsoft AI? verify | listed by upstream | Real-world centric foundation GUI agents. |
| watch | Phi-Ground Tech Report | Microsoft? verify | listed by upstream | GUI grounding and perception. |
| watch | Magentic-UI | Microsoft Research | [Paper](https://arxiv.org/abs/2507.22358) | Human-in-the-loop agentic systems. |
| watch | MiMo-VL Technical Report | Xiaomi? verify | [Paper](https://arxiv.org/abs/2506.03569) | Multimodal model relevant to UI agents. |
| watch | AgentCPM-GUI | OpenBMB? verify | [Paper](https://arxiv.org/pdf/2506.01391) | Mobile-use agents with reinforcement fine-tuning. |
| watch | MAGICGUI | verify | listed by upstream | Foundational mobile GUI agent with scalable data and RFT. |

## Product APIs And Commercial Computer Use

| Status | Product / API | Provider | Link | What To Track |
| --- | --- | --- | --- | --- |
| priority | Computer-Using Agent / CUA | OpenAI | [Announcement](https://openai.com/index/computer-using-agent/), [Sample app](https://github.com/openai/openai-cua-sample-app) | API surface, action schema, safety confirmation policy, supported environments. |
| priority | Computer use | Anthropic | [Announcement](https://www.anthropic.com/news/3-5-models-and-computer-use) | Tool protocol, safety constraints, screen/action loop, benchmark behavior. |
| priority | Project Mariner | Google DeepMind / Google | [Gemini update](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-ai-update-december-2024/) | Browser-control product direction and human supervision policy. |
| priority | Browser-use ecosystem | browser-use | [vibetest-use](https://github.com/browser-use/vibetest-use) | Browser automation stack, QA workflows, agent logs. |
| watch | Vercel AI SDK computer use | Vercel Labs | [GitHub](https://github.com/vercel-labs/ai-sdk-computer-use) | Frontend UX and hosted app integration patterns. |
| watch | LangGraph CUA | LangChain | [GitHub](https://github.com/langchain-ai/langgraph-cua-py) | Agent loop design and framework integration. |
| watch | Surfer 2 | H Company / verify | listed by upstream | Cross-platform computer-use agent product. |
| watch | coasty-ai open-computer-use | Coasty AI | [GitHub](https://github.com/coasty-ai/open-computer-use) | Claims high OSWorld score; verify reproducibility. |

## Infrastructure, Sandboxes, And Parsers

| Status | System | Team | Link | What To Track |
| --- | --- | --- | --- | --- |
| priority | trycua/cua | CUA | [GitHub](https://github.com/trycua/cua) | Sandboxes, SDKs, benchmark harnesses, desktop isolation. |
| priority | OmniParser | Microsoft | [GitHub](https://github.com/microsoft/OmniParser), [Paper](https://arxiv.org/abs/2408.00203) | UI screen parsing, interactable element detection, icon captioning. |
| priority | BrowserGym / AgentLab | ServiceNow Research ecosystem | [Paper](https://openreview.net/forum?id=5298fKGmv3) | Unified web-agent research environment. |
| priority | OSWorld | XLang | [GitHub](https://github.com/xlang-ai/OSWorld) | Desktop environment and evaluation harness. |
| priority | AndroidWorld | Google Research | [GitHub](https://github.com/google-research/android_world) | Android environment and task execution. |
| priority | WindowsAgentArena | Microsoft | [GitHub](https://github.com/microsoft/WindowsAgentArena) | Windows-specific OS-agent evaluation. |
| watch | X-PLUG MobileAgent | Alibaba / Tongyi | [GitHub](https://github.com/X-PLUG/MobileAgent) | Mobile-Agent family implementation. |
| watch | Aria-UI | AriaUI | [GitHub](https://github.com/AriaUI/Aria-UI) | Fast context-aware GUI instruction grounding. |
| watch | OSWorld-MCP | X-PLUG | [GitHub](https://github.com/X-PLUG/OSWorld-MCP) | MCP layer for OSWorld. |
| watch | CUA-Gym | XLang | [GitHub](https://github.com/xlang-ai/CUA-Gym) | Verifiable RLVR training data for CUA. |
| watch | WebArena-Infinity | WebArena team | [GitHub](https://github.com/web-arena-x/webarena-infinity) | Generated browser environments with verifiable tasks. |

## Safety, Guardrails, And Security Systems

| Status | System / report | Team | Link | What To Track |
| --- | --- | --- | --- | --- |
| priority | RedTeamCUA | OSU NLP | [GitHub](https://github.com/OSU-NLP-Group/RedTeamCUA) | Hybrid web-OS adversarial testing. |
| priority | OS-Harm | EPFL / CMU | [GitHub](https://github.com/tml-epfl/os-harm) | Misuse, prompt injection, and model misbehavior benchmark. |
| priority | RiOSWorld | verify | [GitHub](https://github.com/yjyddq/RiOSWorld) | Risk benchmark for multimodal CUA. |
| watch | AgentSentinel | ShanghaiTech / independent | [Paper](https://arxiv.org/abs/2509.07764) | Real-time security defense layer for CUA. |
| watch | Qwen3Guard Technical Report | Qwen Team | [Paper](https://arxiv.org/pdf/2510.14276) | Guard model, relevant to CUA policy enforcement. |
| watch | GUIGuard | verify | [Paper](https://arxiv.org/pdf/2601.18842) | Privacy-preserving GUI agents. |
| watch | WebGuard | verify | [Paper](https://arxiv.org/abs/2507.14293) | Generalizable guardrails for web agents. |
| watch | VeriOS | SJTU / OPPO | [Paper](https://arxiv.org/pdf/2509.07553) | Query-driven human-agent-GUI interaction for trustworthy OS agents. |

## Reading / Testing Priorities

Immediate reading:

1. UI-TARS, OpenCUA, ScaleCUA, OS-ATLAS, ShowUI, Aguvis.
2. UI-TARS-2, ComputerRL, MobileRL, AutoGLM, Mobile-Agent-v3.
3. OpenAI CUA, Anthropic computer use, Google Project Mariner, Magentic-UI.
4. OmniParser, trycua/cua, BrowserGym, LiteCUA, ToolCUA.
5. RedTeamCUA, OS-Harm, AgentDAM, popup attacks, VeriOS, AgentSentinel.

Immediate testing:

1. Run a minimal CUA loop with `openai/openai-cua-sample-app`.
2. Test `trycua/cua` sandbox setup locally.
3. Run OmniParser on desktop/web/mobile screenshots to inspect representation quality.
4. Compare GUI-only, parser-assisted, and structured-tool action loops on one small workflow.
5. Use OSWorld, AndroidWorld, BrowserGym, or WebArena only after choosing the mechanism to test.
