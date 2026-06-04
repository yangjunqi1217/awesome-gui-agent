# Awesome GUI Agent [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of GUI agents, computer-use agents, UI grounding, action models, training methods, safety work, and infrastructure.

This repository is organized around GUI-agent mechanisms rather than benchmark names. Benchmarks are included as experimental substrates for reading papers and comparing systems.

<p align="center">
  <img src="assets/gui-agent-taxonomy.svg" alt="GUI agent taxonomy" width="860" />
</p>

<h3>News</h3>

**2026-06-04** - Reframed the list around GUI-agent paper families: representation, grounding, action models, planning, recovery, memory, RL, safety, and infrastructure.

**2026-06-04** - Added internal reading maps and note templates for mechanism-first paper reading.

<h3>How To Read</h3>

Most GUI-agent papers contribute a mechanism: a screen representation, grounding method, action model, planning/recovery strategy, memory system, training signal, reward model, safety policy, or execution substrate. Read each paper by first identifying the mechanism, then record which benchmarks were used as evidence.

The root README keeps a compact curated list. Broader intake, reading notes, and research questions live in [`docs/`](docs/) and [`notes/`](notes/).

## Contents

- [Surveys](#surveys)
- [GUI Representation and Grounding](#gui-representation-and-grounding)
- [Action Models and Agents](#action-models-and-agents)
- [Planning, Recovery, and Memory](#planning-recovery-and-memory)
- [Training, RL, and Reward Models](#training-rl-and-reward-models)
- [Safety and Trust](#safety-and-trust)
- [Products, APIs, and Infrastructure](#products-apis-and-infrastructure)
- [Evaluation Substrates](#evaluation-substrates)

## Surveys

- [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890) - Broad survey of GUI-agent data resources, architectures, evaluation, and applications.
- [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501) - Survey focused on GUI-agent architectures, training, and evaluation.
- [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/) - ACL survey framing GUI work across computer, phone, and browser-use agents.
- [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434) - Survey of safety, robustness, trustworthiness, and evaluation gaps for GUI agents.

## GUI Representation and Grounding

- [ScreenAI](https://www.ijcai.org/proceedings/2024/339) - Vision-language model for UI and infographic understanding.
- [Ferret-UI](https://eccv.ecva.net/virtual/2024/poster/749) - Grounded mobile UI understanding with region-level multimodal reasoning.
- [OmniParser](https://github.com/microsoft/OmniParser) - Screen parser for interactable element detection and icon captioning in pure-vision GUI agents.
- [SeeClick](https://github.com/njucckevin/SeeClick) - Screenshot-only GUI grounding model and dataset for visual GUI agents.
- [OS-ATLAS](https://github.com/OS-Copilot/OS-Atlas) - Foundation action model and cross-platform grounding corpus for GUI agents.
- [ShowUI](https://github.com/showlab/ShowUI) - Vision-language-action model with UI-guided token selection for GUI tasks.
- [ScreenSpot-Pro](https://github.com/likaixin2000/ScreenSpot-Pro-GUI-Grounding) - High-resolution professional GUI grounding benchmark.
- [GUI-G1](https://arxiv.org/abs/2505.15810) - RL recipe and failure analysis for R1-style GUI grounding.
- [ReGUIDE](https://arxiv.org/abs/2505.15259) - Data-efficient GUI grounding with spatial reasoning and test-time search.
- [A11y-Compressor](https://arxiv.org/abs/2605.00551) - Accessibility-tree compression method for efficient GUI observations.

## Action Models and Agents

- [Agent S](https://proceedings.iclr.cc/paper_files/paper/2025/hash/394c7c30ea87b5c3521b4d9e9d419071-Abstract-Conference.html) - Open agentic framework for using computers through an agent-computer interface.
- [Aguvis](https://proceedings.mlr.press/v267/xu25ae.html) - Unified pure-vision agent for autonomous GUI interaction.
- [OpenCUA](https://github.com/xlang-ai/OpenCUA) - Open foundations for computer-use agents, including data, tooling, and training recipes.
- [UI-TARS](https://github.com/bytedance/UI-TARS) - Native GUI agent model family and open desktop stack from ByteDance.
- [UI-TARS-2](https://arxiv.org/abs/2509.02544) - Technical report on GUI-agent data flywheels, multi-turn RL, and unified sandboxes.
- [ScaleCUA](https://github.com/OpenGVLab/ScaleCUA) - Cross-platform open-source computer-use agent and data scaling effort.
- [Mobile-Agent-v3](https://arxiv.org/abs/2508.15144) - GUI-Owl foundation model and multi-agent framework for GUI automation.
- [UI-Venus](https://arxiv.org/abs/2508.10833) - Screenshot-only UI agent trained with reinforcement fine-tuning and data cleaning.
- [AutoGLM](https://arxiv.org/abs/2411.00820) - Foundation GUI agent for phone and browser control with self-evolving RL.

## Planning, Recovery, and Memory

- [GPT-4V is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html) - Shows that grounding is a central bottleneck for generalist web agents.
- [ExACT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3b893ba1de12f76020b03f7ae8e1afd-Abstract-Conference.html) - Reflective MCTS and exploratory learning for web agents.
- [BacktrackAgent](https://arxiv.org/abs/2505.20660) - Error detection, judgment, reflection, and backtracking for mobile GUI agents.
- [WebDreamer](https://openreview.net/forum?id=c6l7yA0HSq) - World-model planning approach for web agents.
- [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html) - Reusable workflow memory for web agents.
- [Synapse](https://arxiv.org/abs/2306.07863) - Trajectory-as-exemplar prompting and memory for computer control.
- [GUI-explorer](https://aclanthology.org/2025.acl-long.282/) - Transition-aware GUI knowledge mining without model training.
- [VLAA-GUI](https://arxiv.org/abs/2604.21375) - Modular framework for stopping, recovering, and searching in GUI automation.

## Training, RL, and Reward Models

- [DigiRL](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html) - Offline-to-online RL for in-the-wild mobile device-control agents.
- [WebRL](https://openreview.net/forum?id=oVKEAFjEqv) - Self-evolving online curriculum RL for web agents.
- [WebAgent-R1](https://arxiv.org/abs/2505.16421) - End-to-end multi-turn RL for web agents.
- [Web-Shepherd](https://arxiv.org/abs/2505.15277) - Process reward model and trajectory preference data for web agents.
- [ProgRM](https://arxiv.org/abs/2505.18121) - Dense progress rewards for GUI-agent reinforcement learning.
- [ComputerRL](https://arxiv.org/abs/2508.14040) - Online RL framework over parallel virtual desktops and API-GUI actions.
- [MobileRL](https://arxiv.org/abs/2509.18119) - Difficulty-adaptive online RL for mobile GUI agents.
- [OS-Genesis](https://aclanthology.org/2025.acl-long.277/) - Task generation and trajectory data for OS agents.
- [ANCHOR](https://arxiv.org/abs/2602.07153) - Branch-point trajectory expansion for GUI-agent data generation.

## Safety and Trust

- [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/) - Demonstrates adversarial pop-up attacks against VLM computer-use agents.
- [EIA](https://openreview.net/forum?id=xMOLUzo2Lk) - Environmental injection attack for privacy leakage in web agents.
- [AgentDAM](https://arxiv.org/abs/2503.09780) - Data-minimization and privacy leakage evaluation for autonomous web agents.
- [ST-WebAgentBench](https://openreview.net/forum?id=MuCDzH0ctf) - Safety and trustworthiness benchmark for web agents.
- [OS-HARM](https://github.com/tml-epfl/os-harm) - Safety benchmark for misuse, prompt injection, and harmful computer-use behavior.
- [RedTeamCUA](https://github.com/OSU-NLP-Group/RedTeamCUA) - Hybrid web-OS adversarial testing for computer-use agents.
- [Progent](https://arxiv.org/abs/2504.11703) - Programmable privilege control for agent actions.
- [VeriOS](https://arxiv.org/pdf/2509.07553) - Query-driven human-agent-GUI interaction for trustworthy OS agents.
- [Magentic-UI](https://arxiv.org/abs/2507.22358) - Human-in-the-loop agentic system with co-planning, action guards, and answer verification.

## Products, APIs, and Infrastructure

- [OpenAI Computer-Using Agent](https://openai.com/index/computer-using-agent/) - CUA product direction and safety model for computer-use actions.
- [OpenAI CUA sample app](https://github.com/openai/openai-cua-sample-app) - Sample app for experimenting with OpenAI CUA loops.
- [Anthropic computer use](https://www.anthropic.com/news/3-5-models-and-computer-use) - Computer-use tool protocol and model release from Anthropic.
- [Project Mariner](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-ai-update-december-2024/) - Google DeepMind browser-control product direction.
- [trycua/cua](https://github.com/trycua/cua) - Sandboxes, SDKs, and virtualization infrastructure for computer-use agents.
- [BrowserGym](https://openreview.net/forum?id=5298fKGmv3) - Unified web-agent experimentation ecosystem from the ServiceNow research stack.
- [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop) - Open multimodal desktop agent stack.
- [browser-use/vibetest-use](https://github.com/browser-use/vibetest-use) - Browser-use based QA and browser automation workflow.
- [langchain-ai/langgraph-cua-py](https://github.com/langchain-ai/langgraph-cua-py) - LangGraph implementation patterns for CUA loops.
- [vercel-labs/ai-sdk-computer-use](https://github.com/vercel-labs/ai-sdk-computer-use) - Computer-use agent built with Next.js and the Vercel AI SDK.

## Evaluation Substrates

Benchmarks are listed here as experimental substrates. They are useful for reading method papers and designing evaluations, but they are not the default source of new research questions.

- [OSWorld](https://github.com/xlang-ai/OSWorld) - Open-ended desktop tasks in real computer environments.
- [WebArena](https://github.com/web-arena-x/webarena) - Realistic self-hosted web environment for autonomous agents.
- [VisualWebArena](https://aclanthology.org/2024.acl-long.50/) - Visually grounded web-agent task suite.
- [AndroidWorld](https://github.com/google-research/android_world) - Programmatic Android environment and benchmark for autonomous agents.
- [WorkArena](https://proceedings.mlr.press/v235/drouin24a.html) - Enterprise knowledge-work benchmark built around ServiceNow tasks.
- [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena) - Windows-specific OS-agent evaluation environment.
- [OSWorld-G](https://github.com/xlang-ai/OSWorld-G) - Grounding-focused extension of OSWorld.
- [VideoGUI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html) - GUI automation benchmark from instructional videos.
- [ScienceBoard](https://arxiv.org/abs/2505.19897) - Scientific-workflow benchmark with professional desktop software.

## Related Lists

- [showlab/Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) - Broad public list of GUI-agent papers, datasets, projects, and surveys.
- [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) - Paper-first GUI-agent list with environment and keyword browsing.
- [ZJU-REAL/Awesome-GUI-Agents](https://github.com/ZJU-REAL/Awesome-GUI-Agents) - Weekly GUI-agent paper list and taxonomy.
- [Autonomous-Agent-Team/Awesome-GUI-Agent-Safety](https://github.com/Autonomous-Agent-Team/Awesome-GUI-Agent-Safety) - Safety-focused GUI-agent list covering attacks, defenses, and evaluations.
- [cdxeve/awesome-computer-use-agents](https://github.com/cdxeve/awesome-computer-use-agents) - Computer-use agent list covering GUI, browser, and terminal directions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Add only resources we can recommend, keep descriptions factual, and put broad intake or speculative candidates in the docs instead of the root list.
