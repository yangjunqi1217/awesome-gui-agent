# Method Paper Shortlist

This is the mechanism-first shortlist for the next reading sprint. It deliberately starts from GUI-agent problems rather than benchmark names.

Use this file to decide what to read next. Use benchmark papers only when recording how a method was evaluated.

Status labels:

- `read-now`: should become a full note soon.
- `read-next`: useful after the first pass.
- `watch`: monitor, verify, or read when the project direction matches.

## Representation And Screen Understanding

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [ScreenAI](https://www.ijcai.org/proceedings/2024/339) | IJCAI 2024 | UI/infographic representation and screen-language pretraining | Baseline for UI-specific vision-language representation. |
| read-now | [Ferret-UI](https://eccv.ecva.net/virtual/2024/poster/749) | ECCV 2024 | Mobile UI grounding and region-level reasoning | Good reference for grounded UI understanding before full action agents. |
| read-now | [OmniParser](https://arxiv.org/abs/2408.00203) | arXiv 2024 / Microsoft | Screenshot parsing into interactable regions and captions | Practical perception layer used by many pure-vision agents. |
| read-next | [DeskVision](https://arxiv.org/abs/2503.11170) | arXiv 2025 | Desktop screen understanding | Relevant for dense desktop/professional software screens. |
| read-next | [A11y-Compressor](https://arxiv.org/abs/2605.00551) | arXiv 2026 | Accessibility-tree compression | Directly tests representation cost/noise tradeoffs. |

## Grounding And Pointing

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [SeeClick](../notes/papers/2024-seeclick.md) | ACL 2024 | Screenshot-only GUI grounding | Canonical grounding paper before GUI-VLA models. |
| read-now | [OS-ATLAS](../notes/papers/2024-os-atlas.md) | ICLR 2025 Spotlight | Cross-platform grounding corpus and action model | Bridges grounding, action prediction, and data scaling. |
| read-now | [ShowUI](../notes/papers/2025-showui.md) | CVPR 2025 | UI-guided token selection and VLA action prediction | Important for efficient GUI action models. |
| read-next | [ReGUIDE](https://arxiv.org/abs/2505.15259) | arXiv 2025 | Spatial self-critique and test-time search | Useful for data-efficient grounding. |
| read-next | [GUI-G1](https://arxiv.org/abs/2505.15810) | NeurIPS 2025 | RL recipe for GUI grounding | Good failure analysis for naive R1-style grounding RL. |
| watch | [UI-Zoomer](https://arxiv.org/abs/2604.14113) | arXiv 2026 | Uncertainty-triggered adaptive zoom | Candidate mechanism for efficient perception. |

## Action Models And Native GUI Agents

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [Agent S](../notes/papers/2025-agent-s.md) | ICLR 2025 | Agent-computer interface, memory, and OS control loop | Core open framework for computer-use agents. |
| read-now | [Aguvis](https://proceedings.mlr.press/v267/xu25ae.html) | ICML 2025 | Pure-vision autonomous GUI agent | Tests whether structured interface state is necessary. |
| read-now | [UI-TARS](../notes/papers/2025-ui-tars.md) | arXiv 2025 / ByteDance | Native GUI action model and action schema | Strong industry technical report and open stack. |
| read-now | [OpenCUA](../notes/papers/2025-opencua.md) | arXiv 2025 / XLang | Open CUA data, tool, model, and training pipeline | Reproduction anchor for open computer-use foundations. |
| read-next | [ScaleCUA](https://arxiv.org/abs/2509.15221) | ICLR 2026 listed upstream, verify | Cross-platform data scaling and multi-mode inference | Important for open-source scaling recipes. |
| watch | [Mobile-Agent-v3](https://arxiv.org/abs/2508.15144) | arXiv 2025 / Alibaba | GUI-Owl and multi-agent mobile automation | Useful for mobile-specific action modeling. |

## Planning, State Tracking, And Recovery

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [ExACT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3b893ba1de12f76020b03f7ae8e1afd-Abstract-Conference.html) | ICLR 2025 | Reflective MCTS and exploratory learning | Search-based alternative to direct action prediction. |
| read-now | [BacktrackAgent](https://arxiv.org/abs/2505.20660) | EMNLP 2025 Oral | Error detection, judgment, reflection, backtracking | Directly matches the recovery research direction. |
| read-now | [WebDreamer](https://openreview.net/forum?id=c6l7yA0HSq) | ICML 2025 | World-model planning for web agents | Tests imagined outcomes for long GUI workflows. |
| read-next | [VLAA-GUI](https://arxiv.org/abs/2604.21375) | arXiv 2026 | Early stopping and recovery for GUI agents | Useful for off-track detection and stopping policy. |
| read-next | [Agent-SAMA](https://arxiv.org/abs/2505.23596) | arXiv 2025 | Finite-state-machine planning and recovery | Good mobile recovery/control baseline. |
| watch | [R-WoM](https://arxiv.org/abs/2510.11892) | arXiv 2025 | Retrieval-grounded world model | Candidate direction for tutorial-backed recovery. |

## Memory, Skills, And Personalization

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [Synapse](https://arxiv.org/abs/2306.07863) | ICLR 2024 | Trajectory-as-exemplar memory | Early memory baseline for computer control. |
| read-now | [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html) | ICML 2025 | Reusable workflow memory | Strong fit for memory retrieval and invalidation. |
| read-now | [GUI-explorer](https://aclanthology.org/2025.acl-long.282/) | ACL 2025 | Transition-aware GUI knowledge mining | Useful for app map construction without training. |
| read-next | [MAGNET](https://arxiv.org/abs/2601.19199) | arXiv 2026 | Memory-augmented web navigation | Read if we pursue workflow reuse. |
| watch | [Persona2Web](https://arxiv.org/abs/2602.17003) | arXiv 2026 | Personalized web-agent behavior | Relevant if we pursue user-specific GUI agents. |

## Training Data, Synthetic Trajectories, And Data Valuation

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [OS-Genesis](https://aclanthology.org/2025.acl-long.277/) | ACL 2025 | Task generation and OS-agent trajectory data | Good example of turning GUI environments into data. |
| read-now | [ANCHOR](https://arxiv.org/abs/2602.07153) | arXiv 2026 | Branch-point trajectory expansion | Useful for data generation beyond one successful path. |
| read-now | [CUA-Suite](https://arxiv.org/abs/2603.24440) | arXiv 2026 | Data capture, generation, and evaluation suite | Industry-style data infrastructure reference. |
| read-next | [OpenCUA AgentNet](https://arxiv.org/abs/2508.09123) | arXiv 2025 | Cross-platform trajectory capture and reflective CoT | Reproduction anchor for large-scale CUA data. |
| read-next | [VideoGUI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | Video-derived GUI supervision | Use when considering instructional-video supervision. |
| read-next | [ShowUI-Aloha](https://arxiv.org/abs/2601.07181) | arXiv 2026 / Show Lab | Screen-recording-to-teaching pipeline | Strong match for learning GUI agents from human demonstration videos. |
| read-next | [VideoAgentTrek](https://arxiv.org/abs/2510.19488) | arXiv 2025 | Video mining and inverse dynamics | Direct fit for pretraining from unlabeled tutorial videos. |
| read-next | [Watch and Learn](https://arxiv.org/abs/2510.04673) | CVPR 2026 | Online-video-to-executable-trajectory conversion | Turns public computer-use videos into action supervision. |

## RL, Reward Models, And Self-Improvement

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [DigiRL](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html) | NeurIPS 2024 | Offline-to-online RL for device control | Early strong RL paper for GUI/mobile control. |
| read-now | [WebRL](https://openreview.net/forum?id=oVKEAFjEqv) | ICLR 2025 | Self-evolving online curriculum RL | Core RL recipe for web agents. |
| read-now | [Web-Shepherd](https://arxiv.org/abs/2505.15277) | NeurIPS 2025 Spotlight | Process reward model for web trajectories | Direct input for progress/reward research. |
| read-now | [ProgRM](https://arxiv.org/abs/2505.18121) | arXiv 2025 | Dense GUI progress rewards | Closest prior for state-delta progress reward ideas. |
| read-now | [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178) | arXiv 2026 | Execution-video reward model | Best match for video/VLM-based progress verification. |
| read-next | [ComputerRL](https://arxiv.org/abs/2508.14040) | ICLR 2026 listed upstream, verify | Online RL over parallel virtual desktops and API-GUI actions | Strong industry-style desktop RL system. |
| read-next | [MobileRL](https://arxiv.org/abs/2509.18119) | ICLR 2026 listed upstream, verify | Difficulty-adaptive GRPO for mobile agents | Useful for mobile RL and failure curriculum. |
| watch | [Android Coach](https://arxiv.org/abs/2604.07277) | arXiv 2026 | Critic/process reward for multiple actions per state | Candidate method for efficient online RL. |

## Hybrid GUI + Structured Tool Use

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [Beyond Browsing: API-Based Web Agents](https://aclanthology.org/2025.findings-acl.577/) | Findings ACL 2025 | API-vs-GUI action interfaces | Central for interface routing. |
| read-now | [AXIS](https://aclanthology.org/2025.acl-long.381/) | ACL 2025 | GUI/API hybrid execution | Helps frame when clicking is the wrong abstraction. |
| read-now | [ToolCUA](https://arxiv.org/abs/2605.12481) | arXiv 2026 | GUI-tool path orchestration | Good fit for permission-aware interface routing. |
| read-next | [LiteCUA](https://arxiv.org/abs/2505.18829) | arXiv 2025 | Computer-as-MCP server and environmental contextualization | Useful for cost/reliability tradeoffs. |
| watch | [Terminal Agents Suffice for Enterprise Automation](https://arxiv.org/abs/2604.00073) | arXiv 2026 | Terminal/API alternative to GUI actions | Read if we pursue enterprise automation. |

## Safety, Security, And Trust Boundaries

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/) | ACL 2025 | Adversarial visual UI injection | Canonical example of environment-originated malicious instructions. |
| read-now | [EIA](https://openreview.net/forum?id=xMOLUzo2Lk) | ICLR 2025 | Environmental injection for privacy leakage | Strong trust-boundary prior for web agents. |
| read-now | [AgentDAM](https://arxiv.org/abs/2503.09780) | NeurIPS 2025 | Data minimization and privacy leakage evaluation | Connects safety with action justification and information exposure. |
| read-now | [Progent](https://arxiv.org/abs/2504.11703) | arXiv 2025 | Programmable privilege control | Useful for deterministic policy around risky actions. |
| read-next | [AgentSentinel](https://arxiv.org/abs/2509.07764) | arXiv 2025 | Real-time defense layer for CUA | Candidate runtime guard for GUI agents. |
| read-next | [VeriOS](https://arxiv.org/pdf/2509.07553) | arXiv 2025 | Query-driven human-agent-GUI interaction | Direct fit for confirmation and trust-boundary policies. |
| watch | [RedTeamCUA](https://openreview.net/forum?id=yWwrgcBoK3) | ICLR 2026 listed upstream, verify | Hybrid web-OS adversarial testing | Use as evaluation evidence for safety methods. |

## Human-Agent Interaction

| Status | Paper / report | Venue / year | Mechanism To Extract | Why Read |
| --- | --- | --- | --- | --- |
| read-now | [Magentic-UI](https://arxiv.org/abs/2507.22358) | arXiv 2025 / Microsoft Research | Co-planning, co-tasking, action guards, answer verification | Strong product/research reference for human oversight. |
| read-next | [Toward a Human-Centered Evaluation Framework for Trustworthy LLM-Powered GUI Agents](https://arxiv.org/abs/2504.17934) | arXiv 2025 | Human-centered trust evaluation | Useful for user burden and oversight metrics. |
| read-next | [When Users Change Their Mind](https://arxiv.org/abs/2604.00892) | arXiv 2026 | Interruptions and revised user intent | Relevant for real interactive GUI agents. |
| watch | [OpeFlo](https://arxiv.org/abs/2604.09581) | arXiv 2026 | LLM-as-user evaluation for UI agents | Read if we need scalable user-study proxies. |

## What To Do After Reading

Each full paper note should answer:

1. What GUI mechanism is proposed?
2. What representation and action space does it assume?
3. What failure mode does it target?
4. What training or inference signal is new?
5. Which benchmarks appear only as experimental evidence?
6. Which research question in [research-questions.md](research-questions.md) does it support or weaken?
