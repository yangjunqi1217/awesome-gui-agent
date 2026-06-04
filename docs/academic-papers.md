# Academic Paper Map

This is a curated academic entry map for GUI agents, computer-use agents, web agents, mobile agents, and UI grounding.

Scope:

- Prefer top venues and high-impact method/model papers.
- Keep benchmark and dataset papers as evaluation evidence for method papers, not as the main research agenda.
- Include strong arXiv/preprint candidates only when they look central to the field.
- Mark uncertain or very recent items as `verify` instead of pretending the venue/status is settled.

Status labels:

- `priority`: should become a full reading note.
- `watch`: useful to track, but not first-pass reading.
- `verify`: venue, claims, or relevance needs confirmation.

## Surveys And Field Framing

| Status | Paper | Venue / year | Environment | Why It Matters |
| --- | --- | --- | --- | --- |
| priority | [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890) | arXiv 2024 | General GUI | Broad survey around data resources, agent construction, taxonomy, and industrial applications. |
| priority | [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501) | arXiv 2024 | General GUI | Useful for architectures, training, evaluation, and benchmark framing. |
| priority | [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/) | ACL 2025 | Desktop, mobile, web | Positions GUI work under OS/computer/phone/browser-use agents. |
| priority | [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434) | arXiv 2025 | General GUI | Safety, robustness, trustworthiness, and evaluation gaps. |
| watch | [A Survey of WebAgents: Towards Next-Generation AI Agents for Web Automation with Large Foundation Models](https://arxiv.org/abs/2503.23350) | arXiv 2025 | Web | Web-specific history and taxonomy. |
| watch | [Generalist Virtual Agents: A Survey on Autonomous Agents Across Digital Platforms](https://arxiv.org/abs/2411.10943) | arXiv 2024 | Desktop, mobile, web | Broader framing for cross-platform digital agents. |

## Foundations Before The Current GUI-Agent Wave

| Status | Paper | Venue / year | Environment | Why It Matters |
| --- | --- | --- | --- | --- |
| priority | [World of Bits: An Open-Domain Platform for Web-Based Agents](https://proceedings.mlr.press/v70/shi17a.html) | ICML 2017 | Web | Early open-domain web-agent benchmark and dataset. |
| priority | [Reinforcement Learning on Web Interfaces using Workflow-Guided Exploration](https://arxiv.org/abs/1802.08802) | ICLR 2018 | Web | Early RL approach for web UI interaction. |
| priority | [Mapping Natural Language Instructions to Mobile UI Action Sequences](https://arxiv.org/abs/2005.03776) | ACL 2020 | Mobile | Pre-LLM mobile UI action-sequence grounding. |
| priority | [WebSRC: A Dataset for Web-Based Structural Reading Comprehension](https://arxiv.org/abs/2101.09465) | EMNLP 2021 | Web | Web structure understanding, adjacent to later web-agent perception. |
| priority | [SheetCopilot: Bringing Software Productivity to the Next Level through Large Language Models](https://arxiv.org/abs/2305.19308) | NeurIPS 2023 | Spreadsheet | Early productivity-software automation with LLMs. |
| priority | [Mind2Web: Towards a Generalist Agent for the Web](https://arxiv.org/abs/2306.06070) | NeurIPS 2023 Datasets and Benchmarks | Web | Core web-agent dataset/benchmark for generalization. |
| priority | [Android in the Wild: A Large-Scale Dataset for Android Device Control](https://arxiv.org/abs/2307.10088) | NeurIPS 2023 Datasets and Benchmarks | Mobile | Major Android device-control dataset. |
| priority | [WebArena: A Realistic Web Environment for Building Autonomous Agents](https://arxiv.org/abs/2307.13854) | ICLR 2024 | Web | Realistic self-hosted web-agent benchmark. |
| watch | [Synapse: Trajectory-as-Exemplar Prompting with Memory for Computer Control](https://arxiv.org/abs/2306.07863) | ICLR 2024 | Desktop / web | Memory and trajectory-as-exemplar prompting for computer control. |

## Evaluation Papers And Experimental Substrates

Read these after the relevant method papers, mainly to understand experimental setup, failure labels, action spaces, and reproducibility constraints.

| Status | Paper | Venue / year | Environment | Why It Matters |
| --- | --- | --- | --- | --- |
| priority | [VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks](https://aclanthology.org/2024.acl-long.50/) | ACL 2024 | Web | Visual extension of WebArena; central for multimodal web agents. |
| priority | [WebVoyager: Building an End-to-End Web Agent with Large Multimodal Models](https://aclanthology.org/2024.acl-long.371/) | ACL 2024 | Web | Live-website web-agent benchmark and GPT-4V judge protocol. |
| priority | [WebLINX: Real-World Website Navigation with Multi-Turn Dialogue](https://proceedings.mlr.press/v235/lu24e.html) | ICML 2024 | Web | 100K interactions from expert demonstrations across real websites. |
| priority | [WorkArena: How Capable are Web Agents at Solving Common Knowledge Work Tasks?](https://proceedings.mlr.press/v235/drouin24a.html) | ICML 2024 | Web / enterprise | Enterprise ServiceNow benchmark and BrowserGym origin. |
| priority | [OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5d413e48f84dc61244b6be550f1cd8f5-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | Desktop / web | Core benchmark for open-ended computer-use tasks in real OS environments. |
| priority | [VideoGUI: A Benchmark for GUI Automation from Instructional Videos](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | Desktop | Video-conditioned GUI automation benchmark. |
| priority | [DigiRL: Training In-The-Wild Device-Control Agents with Autonomous Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html) | NeurIPS 2024 | Mobile | Offline-to-online RL for real Android device-control agents. |
| priority | [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0b82662b6c32e887bb252a74d8cb2d5e-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | Web / enterprise | Compositional knowledge-work tasks and oracle traces. |
| priority | [Spider2-V: How Far Are Multimodal Agents From Automating Data Science and Engineering Workflows?](https://proceedings.neurips.cc/paper_files/paper/2024/hash/c2f71567cd53464161cab3336e8fc865-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | Web / data workflows | Tests multimodal agents on data science and engineering workflows. |
| priority | [LlamaTouch: A Faithful and Scalable Testbed for Mobile UI Task Automation](https://arxiv.org/abs/2404.16054) | UIST 2024 | Mobile | State-based mobile UI task automation evaluation. |
| priority | [OmniACT: A Dataset and Benchmark for Enabling Multimodal Generalist Autonomous Agents for Desktop and Web](https://eccv.ecva.net/virtual/2024/poster/1107) | ECCV 2024 | Desktop / web | Screenshot-to-program benchmark for desktop/web tasks. |
| priority | [AndroidWorld: A Dynamic Benchmarking Environment for Autonomous Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/01a83bc2f2732a58e6aa731e659e7101-Abstract-Conference.html) | ICLR 2025 | Mobile | Programmatic Android benchmark with task initialization and success checks. |
| priority | [SPA-Bench: A Comprehensive Benchmark for SmartPhone Agent Evaluation](https://proceedings.iclr.cc/paper_files/paper/2025/hash/9a75f4dd9679aa4ff80a4e6f0a1dc700-Abstract-Conference.html) | ICLR 2025 | Mobile | Smartphone-agent evaluation with broader task coverage. |
| priority | [VideoWebArena: Evaluating Long Context Multimodal Agents with Video Understanding Web Tasks](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5b555804d495321df2e3208cc27f4fbc-Abstract-Conference.html) | ICLR 2025 | Web / video | Tests long-context video-conditioned web tasks. |
| priority | [BrowserGym: The BrowserGym Ecosystem for Web Agent Research](https://openreview.net/forum?id=5298fKGmv3) | TMLR 2025 | Web | Standardizes observation/action wrappers and agent experimentation. |
| priority | [Windows Agent Arena: Evaluating Multi-Modal OS Agents at Scale](https://proceedings.mlr.press/v267/bonatti25a.html) | ICML 2025 | Desktop / Windows | Windows-specific OS-agent benchmark at scale. |
| verify | [ScreenSpot-Pro: GUI Grounding for Professional High-Resolution Computer Use](https://arxiv.org/abs/2504.07981) | ICLR 2026 (listed by upstream; verify) | Desktop / grounding | High-resolution professional GUI grounding benchmark. |
| priority | [Scaling Computer-Use Grounding via User Interface Decomposition and Synthesis](https://arxiv.org/abs/2505.13227) | NeurIPS 2025 Datasets and Benchmarks Spotlight | General GUI / grounding | OSWorld-G plus large synthetic grounding data. |
| priority | [Mind2Web 2: Evaluating Agentic Search with Agent-as-a-Judge](https://openreview.net/forum?id=AUaW6DS9si) | NeurIPS 2025 Datasets and Benchmarks | Web / search | Long-horizon agentic search with judge agents and source attribution. |
| priority | [OS-HARM: A Benchmark for Measuring Safety of Computer Use Agents](https://arxiv.org/abs/2503.18492) | NeurIPS 2025 Datasets and Benchmarks Spotlight | Desktop / safety | Safety benchmark for computer-use agents built on OSWorld. |
| verify | [ScienceBoard: Evaluating Multimodal Autonomous Agents in Realistic Scientific Workflows](https://arxiv.org/abs/2505.19897) | ICLR 2026 (verify) | Desktop / scientific software | Professional scientific-workflow benchmark with integrated software. |
| verify | [RedTeamCUA: Realistic Adversarial Testing of Computer-Use Agents in Hybrid Web-OS Environments](https://openreview.net/forum?id=yWwrgcBoK3) | ICLR 2026 Oral (verify) | Desktop / web / safety | Hybrid OS-web indirect prompt-injection benchmark. |
| watch | [VisualWebBench: How Far Have Multimodal LLMs Evolved in Web Page Understanding and Grounding?](https://openreview.net/forum?id=egVSgtJJAx) | COLM 2024 | Web | Web-page understanding and grounding. |
| watch | [OfficeBench: Benchmarking Language Agents across Multiple Applications for Office Automation](https://arxiv.org/abs/2407.19056) | arXiv 2024 | Office automation | Multi-app office workflow benchmark. |
| watch | [WebCanvas: Benchmarking Web Agents in Online Environments](https://arxiv.org/abs/2406.12373) | arXiv 2024 | Web | Online/live-web progress-aware evaluation. |
| watch | [MobileAgentBench: An Efficient and User-Friendly Benchmark for Mobile LLM Agents](https://arxiv.org/abs/2406.08184) | arXiv 2024 | Mobile | Real-device mobile benchmark. |
| watch | [TurkingBench: A Challenge Benchmark for Web Agents](https://aclanthology.org/2025.naacl-long.188/) | NAACL 2025 Oral | Web | Web-agent tasks from crowdsourcing pages. |
| watch | [BEARCUBS: A benchmark for computer-using web agents](https://arxiv.org/abs/2503.07919) | arXiv 2025 | Web | Browser/computer-use web-agent benchmark. |
| watch | [UI-Vision: A Desktop-centric GUI Benchmark for Visual Perception and Interaction](https://arxiv.org/abs/2503.15661) | arXiv 2025 | Desktop | Desktop visual perception and interaction evaluation. |
| watch | [WorldGUI: An Interactive Benchmark for Desktop GUI Automation from Any Starting Point](https://arxiv.org/abs/2502.08047) | arXiv 2025 | Desktop | Any-starting-state desktop GUI automation. |

## Models, Grounding, And Agent Architectures

| Status | Paper | Venue / year | Environment | Why It Matters |
| --- | --- | --- | --- | --- |
| priority | [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://aclanthology.org/2024.acl-long.505/) | ACL 2024 | Desktop, mobile, web | Screenshot-only GUI grounding and ScreenSpot. |
| priority | [GPT-4V(ision) is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html) | ICML 2024 | Web | Shows grounding bottleneck for generalist web agents. |
| priority | [Dual-View Visual Contextualization for Web Navigation](https://doi.org/10.1109/CVPR52733.2024.01369) | CVPR 2024 | Web | Fuses DOM/text and screenshot regions for web grounding. |
| priority | [AutoWebGLM: A Large Language Model-based Web Navigating Agent](https://dl.acm.org/doi/10.1145/3637528.3671620) | KDD 2024 | Web | Web-navigation agent with HTML simplification and RL. |
| priority | [ScreenAI: A Vision-Language Model for UI and Infographics Understanding](https://www.ijcai.org/proceedings/2024/339) | IJCAI 2024 | General UI | UI/infographic understanding model and datasets. |
| priority | [Ferret-UI: Grounded Mobile UI Understanding with Multimodal LLMs](https://eccv.ecva.net/virtual/2024/poster/749) | ECCV 2024 | Mobile | Mobile UI grounding and reasoning MLLM from Apple. |
| priority | [ScreenAgent: A Vision Language Model-driven Computer Control Agent](https://www.ijcai.org/proceedings/2024/711) | IJCAI 2024 | Desktop | VLM-driven computer-control environment and agent loop. |
| priority | [OS-ATLAS: A Foundation Action Model for Generalist GUI Agents](https://arxiv.org/abs/2410.23218) | ICLR 2025 Spotlight | Desktop, mobile, web | Cross-platform GUI grounding corpus and foundation action model. |
| priority | [ShowUI: One Vision-Language-Action Model for GUI Visual Agent](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html) | CVPR 2025 | Mobile / web | Lightweight VLA model with UI-guided token selection. |
| priority | [Aguvis: Unified Pure Vision Agents for Autonomous GUI Interaction](https://proceedings.mlr.press/v267/xu25ae.html) | ICML 2025 | General GUI | Pure-vision GUI agent without text interface representations. |
| priority | [Agent S: An Open Agentic Framework that Uses Computers Like a Human](https://proceedings.iclr.cc/paper_files/paper/2025/hash/394c7c30ea87b5c3521b4d9e9d419071-Abstract-Conference.html) | ICLR 2025 | Desktop | Open computer-use framework with agent-computer interface and memory. |
| priority | [ExACT: Teaching AI Agents to Explore with Reflective-MCTS and Exploratory Learning](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3b893ba1de12f76020b03f7ae8e1afd-Abstract-Conference.html) | ICLR 2025 | Web | Test-time search and exploratory learning for web agents. |
| priority | [WebRL: Training LLM Web Agents via Self-Evolving Online Curriculum Reinforcement Learning](https://openreview.net/forum?id=oVKEAFjEqv) | ICLR 2025 | Web | Online RL for open web agents. |
| priority | [Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/4ca0e369689dadb25a5345ba9755ad6f-Abstract-Conference.html) | ICLR 2025 | General GUI | Universal visual grounding for GUI agents. |
| priority | [Lightweight Neural App Control](https://openreview.net/forum?id=BL4WBIfyrz) | ICLR 2025 | Mobile / on-device | Efficient app-control model. |
| priority | [DistRL: An Asynchronous Distributed Reinforcement Learning Framework for On-Device Control Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/b9e472cd579c83e2f6aa3459f46aac28-Abstract-Conference.html) | ICLR 2025 | Mobile | Distributed RL for on-device control agents. |
| priority | [Web-Shepherd: Advancing PRMs for Reinforcing Web Agents](https://arxiv.org/abs/2505.15277) | NeurIPS 2025 Spotlight | Web | Process reward model and benchmark for web trajectories. |
| priority | [GUI-G1: Understanding R1-Zero-Like Training for Visual Grounding in GUI Agents](https://arxiv.org/abs/2505.15810) | NeurIPS 2025 | Grounding | RL training analysis for GUI grounding. |
| priority | [SE-GUI: Enhancing Visual Grounding for GUI Agents via Self-Evolutionary Reinforcement Learning](https://arxiv.org/abs/2505.12370) | NeurIPS 2025 | Grounding | Self-evolutionary RL for high-resolution GUI grounding. |
| priority | [WebAgent-R1: Training Web Agents via End-to-End Multi-Turn Reinforcement Learning](https://arxiv.org/abs/2505.16421) | EMNLP 2025 | Web | End-to-end online RL on browser interactions. |
| priority | [BacktrackAgent: Enhancing GUI Agent with Error Detection and Backtracking Mechanism](https://arxiv.org/abs/2505.20660) | EMNLP 2025 Oral | Mobile | Explicit error detection, reflection, and backtracking. |
| verify | [ScaleCUA: Scaling Open-Source Computer Use Agents with Cross-Platform Data](https://arxiv.org/abs/2509.15221) | ICLR 2026 Oral (verify) | Desktop, mobile, web | Cross-platform open CUA data and model scaling. |
| verify | [ComputerRL: Scaling End-to-End Online Reinforcement Learning for Computer Use Agents](https://arxiv.org/abs/2508.14040) | ICLR 2026 (verify) | Desktop | Online RL over parallel virtual desktops. |
| verify | [MobileRL: Online Agentic Reinforcement Learning for Mobile GUI Agents](https://arxiv.org/abs/2509.18119) | ICLR 2026 (verify) | Mobile | Online RL for AndroidWorld/AndroidLab style agents. |
| watch | [OmniParser for Pure Vision Based GUI Agent](https://arxiv.org/abs/2408.00203) | arXiv 2024 | General GUI | Screen parsing layer for element detection and captions. |
| watch | [OpenWebVoyager: Building Multimodal Web Agents via Iterative Real-World Exploration, Feedback and Optimization](https://aclanthology.org/2025.acl-long.1336/) | ACL 2025 | Web | Real-world exploration and feedback for web agents. |
| watch | [AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://aclanthology.org/2025.acl-long.107/) | ACL 2025 | Mobile | Android training/evaluation environment and data. |
| watch | [GUI-explorer: Autonomous Exploration and Mining of Transition-aware Knowledge for GUI Agent](https://aclanthology.org/2025.acl-long.282/) | ACL 2025 | Mobile | Transition-aware knowledge mining without training. |
| watch | [Aria-UI: Visual Grounding for GUI Instructions](https://aclanthology.org/2025.findings-acl.1152/) | Findings ACL 2025 | Grounding | Lightweight GUI grounding. |
| watch | [UFO: A UI-Focused Agent for Windows OS Interaction](https://aclanthology.org/2025.naacl-long.26/) | NAACL 2025 | Desktop / Windows | Windows app interaction with hierarchical agent design. |
| watch | [LiteWebAgent: The Open-Source Suite for VLM-Based Web-Agent Applications](https://aclanthology.org/2025.naacl-demo.36/) | NAACL 2025 Demo | Web | Open-source web-agent application suite. |

## Safety, Security, And Trustworthiness

| Status | Paper | Venue / year | Environment | Why It Matters |
| --- | --- | --- | --- | --- |
| priority | [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/) | ACL 2025 | Desktop / web | Demonstrates adversarial pop-up attacks against VLM agents. |
| priority | [Dissecting Adversarial Robustness of Multimodal LM Agents](https://proceedings.iclr.cc/paper_files/paper/2025/hash/460a1d8eac34125dad453b28d6d64446-Abstract-Conference.html) | ICLR 2025 | Web / multimodal agents | Adversarial robustness analysis for multimodal agents. |
| priority | [ST-WebAgentBench: A Benchmark for Evaluating Safety and Trustworthiness in Web Agents](https://openreview.net/forum?id=MuCDzH0ctf) | ICLR 2025 | Web | Safety/trustworthiness benchmark for web agents. |
| priority | [EIA: Environmental Injection Attack on Generalist Web Agents for Privacy Leakage](https://openreview.net/forum?id=xMOLUzo2Lk) | ICLR 2025 | Web | Environment injection attacks for privacy leakage. |
| priority | [Refusal-Trained LLMs Are Easily Jailbroken As Browser Agents](https://arxiv.org/abs/2410.13886) | arXiv 2024 | Web / safety | Shows refusal training may fail under browser-agent settings. |
| priority | [AgentDAM: Privacy Leakage Evaluation for Autonomous Web Agents](https://arxiv.org/abs/2503.09780) | NeurIPS 2025 | Web / privacy | Data-minimization benchmark for web agents. |
| priority | [OS-HARM](https://arxiv.org/abs/2503.18492) | NeurIPS 2025 Spotlight | Desktop / safety | Safety benchmark for misuse, injection, and model misbehavior. |
| verify | [RedTeamCUA](https://openreview.net/forum?id=yWwrgcBoK3) | ICLR 2026 Oral (verify) | Desktop / web | Hybrid OS-web adversarial CUA testing. |
| watch | [SAFEARENA: Evaluating the Safety of Autonomous Web Agents](https://arxiv.org/pdf/2503.04957) | arXiv 2025 | Web | Safety evaluation for autonomous web agents. |
| watch | [MobileSafetyBench: Evaluating Safety of Autonomous Agents in Mobile Device Control](https://arxiv.org/abs/2410.17520) | arXiv 2024 | Mobile | Mobile safety benchmark. |
| watch | [AEIA-MN: Evaluating the Robustness of Multimodal LLM-Powered Mobile Agents Against Active Environmental Injection Attacks](https://arxiv.org/abs/2502.13053) | arXiv 2025 | Mobile | Active environmental injection attacks. |
| watch | [Progent: Programmable Privilege Control for LLM Agents](https://arxiv.org/abs/2504.11703) | arXiv 2025 | Tool agents / security | Deterministic privilege control for agents. |
| watch | [VeriSafe Agent: Safeguarding Mobile GUI Agent via Logic-based Action Verification](https://arxiv.org/abs/2503.18492) | MobiCom 2025 (verify link collision) | Mobile | Runtime logic-based action verification. |

## Active Preprint / Watchlist Cluster

These are too relevant to ignore, but should be verified before we treat them as canonical top-venue papers.

| Status | Paper | Environment | Why It Matters |
| --- | --- | --- | --- |
| watch | [OpenCUA: Open Foundations for Computer-Use Agents](https://github.com/xlang-ai/OpenCUA) | Desktop / CUA | Open foundations, data, and training recipe. |
| watch | [UI-TARS: Pioneering Automated GUI Interaction with Native Agents](https://arxiv.org/abs/2501.12326) | General GUI | Native GUI agent from ByteDance; strong industry signal. |
| watch | [UI-TARS-2 Technical Report](https://arxiv.org/abs/2509.02544) | General GUI | Multi-turn RL and data flywheel for GUI agents. |
| watch | [Mobile-Agent-v3: Fundamental Agents for GUI Automation](https://arxiv.org/abs/2508.15144) | Desktop / mobile | GUI-Owl foundation model and multi-agent framework. |
| watch | [UI-Venus Technical Report](https://arxiv.org/abs/2508.10833) | Desktop / mobile / web | Screenshot-only UI agent with reinforcement fine-tuning. |
| watch | [Agent S2: A Compositional Generalist-Specialist Framework for Computer Use Agents](https://openreview.net/forum?id=zg5is4GJ3R) | Desktop | Generalist-specialist composition for CUA. |
| watch | [OSWorld-G / Jedi](https://arxiv.org/abs/2505.13227) | Grounding | Already a priority benchmark; also important for synthetic data methodology. |
| watch | [Agent-E: From Autonomous Web Navigation to Foundational Design Principles in Agentic Systems](https://arxiv.org/abs/2407.13032) | Web | Architecture/design principles from web navigation. |
| watch | [WebPilot: A Versatile and Autonomous Multi-Agent System for Web Task Execution with Strategic Exploration](https://ojs.aaai.org/index.php/AAAI/article/view/34505) | Web | Planning plus MCTS execution for web agents. |
| watch | [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html) | Web | Reusable workflow memory from past trajectories. |
| watch | [Magentic-UI: Towards Human-in-the-loop Agentic Systems](https://arxiv.org/abs/2507.22358) | Human-in-loop | Human oversight and mixed-initiative GUI agent systems. |

## Reading Priorities

First pass:

1. ScreenAI, Ferret-UI, SeeClick, OS-ATLAS, ShowUI, Aguvis, Agent S.
2. ExACT, BacktrackAgent, WebDreamer, Agent Workflow Memory, GUI-explorer.
3. DigiRL, WebRL, Web-Shepherd, GUI-G1, WebAgent-R1.
4. EIA, AgentDAM, Progent, Attacking VLM Computer Agents via Pop-ups, OS-HARM.

Second pass:

1. UI-TARS, OpenCUA, ScaleCUA, UI-Venus, Mobile-Agent-v3.
2. OS-Genesis, ANCHOR, CUA-Suite, UI-TARS-2, ComputerRL, MobileRL.
3. Magentic-UI, VeriOS, AgentSentinel, RedTeamCUA.
4. WebArena, OSWorld, AndroidWorld, WorkArena, Windows Agent Arena, ScreenSpot-Pro only as experiment substrates for the methods above.
