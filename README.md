# Awesome GUI Agent [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome) <!-- omit in toc -->

## [A Mechanism-First Reading Hub For GUI Agents](docs/gui-paper-landscape.md)

GUI agents, computer-use agents (CUA), browser agents, mobile agents, and UI-grounding models are moving from isolated demos toward full digital-work automation. This repository tracks the papers, reports, projects, datasets, benchmarks, and infrastructure needed to understand that shift.

The goal is not to mirror every new list. The goal is to make each paper readable from the README: what problem it studies, what mechanism it proposes, and where it fits in the GUI-agent stack.

Key observations:

- **Grounding is still a central bottleneck.** Strong VLMs fail if they cannot localize actionable UI elements precisely.
- **Native GUI action models are scaling quickly.** Recent systems combine screenshot perception, action schemas, cross-platform data, and online RL.
- **Video demonstrations are becoming a major data source.** Screen recordings, tutorial videos, and execution videos connect GUI agents with temporal understanding and inverse dynamics.
- **Recovery and verification matter as much as first-step prediction.** Long-horizon GUI tasks need progress rewards, state tracking, backtracking, and guardrails.
- **Benchmarks are experimental substrates, not the research agenda.** Read them to understand evidence, action spaces, and failure modes, but start from GUI-agent mechanisms.

<p align="center">
  <img src="assets/gui-agent-taxonomy.svg" alt="GUI agent taxonomy" style="display: block; margin: 0 auto;" />
</p>

----

### How To Read A GUI-Agent Paper

For each paper, identify six things first:

- **Representation**: screenshot, OCR, accessibility tree, DOM, UI hierarchy, video, or mixed state.
- **Grounding**: coordinates, boxes, element IDs, UI regions, zooming, or parsing.
- **Action modeling**: low-level mouse and keyboard actions, structured GUI commands, tool calls, or hybrid actions.
- **Planning and recovery**: state tracking, progress estimation, backtracking, verification, and failure repair.
- **Learning signal**: demonstrations, synthetic trajectories, videos, reward models, RL, or self-improvement.
- **Safety model**: trust boundaries, confirmations, containment, audit logs, and adversarial UI behavior.

Benchmark and dataset papers are included because they reveal action spaces, failure labels, evaluation protocols, and reproducibility constraints. They should be read as evidence for mechanisms, not as the research agenda itself.

### Start Here

| Goal | Entry Point |
| --- | --- |
| Understand the field structure | [GUI paper landscape](docs/gui-paper-landscape.md) |
| Read one-summary-per-paper notes | [Paper summaries](docs/paper-summaries.md) |
| Choose a reading order | [Reading roadmap](docs/reading-roadmap.md) |
| Find high-priority method papers | [Method paper shortlist](docs/method-paper-shortlist.md) |
| Focus on execution-video reward and compression | [Execution-video reward and compression survey](docs/execution-video-reward-and-compression.md) |
| Compare models, products, and infrastructure | [Model zoo and system map](docs/model-zoo.md) |
| Track academic papers and venues | [Academic paper map](docs/academic-papers.md), [venue index](docs/venue-index.md) |
| Track industry systems and APIs | [Industry technical reports](docs/industry-reports.md) |
| Develop research directions | [Research questions](docs/research-questions.md) |
| Understand source intake | [Source map](docs/source-map.md) |
| Add or review resources | [Contributing guide](CONTRIBUTING.md), [notes workflow](notes/) |

### Recent Additions To Check First

These are recent GUI-agent / computer-use papers added or promoted in this README. Dates are based on the canonical paper pages available on 2026-06-04.

| Paper | Date | Why It Matters | Link |
| --- | --- | --- | --- |
| CLI-Anything | Jun. 2026 | Challenges GUI-only automation by turning apps into agent-native command interfaces. | [arXiv](https://arxiv.org/abs/2606.03854) |
| MedCUA-Bench | Jun. 2026 | Tests screenshot-only agents in clinical software with safety dimensions, not only task success. | [arXiv](https://arxiv.org/abs/2606.03203) |
| Multi-Agent Computer Use | Jun. 2026 | Moves CUA scaling from one serial agent to manager-orchestrated parallel subagents. | [arXiv](https://arxiv.org/abs/2606.01533) |
| AgentHijack | May 2026 | Tests robustness under popups, resolution changes, competing apps, and other common corruptions. | [arXiv](https://arxiv.org/abs/2605.25707) |
| OpenComputer | May 2026 | Builds verifiable desktop software worlds with app-specific state checkers and partial-credit rewards. | [arXiv](https://arxiv.org/abs/2605.19769) |
| CutVerse | May 2026 | Evaluates GUI agents on professional media editing tasks in dense creative software. | [arXiv](https://arxiv.org/abs/2605.19484) |
| SaaS-Bench | May 2026 | Evaluates long-horizon professional workflows across deployable SaaS systems. | [arXiv](https://arxiv.org/abs/2605.15777) |
| A11y-Compressor | May 2026 | Compresses accessibility-tree observations while preserving structural context. | [arXiv](https://arxiv.org/abs/2605.00551) |
| Step-level Optimization | Apr. 2026 | Uses risk monitors to cascade between cheap and strong policies during long GUI tasks. | [arXiv](https://arxiv.org/abs/2604.27151) |
| Training CUAs To Assess Usability | Apr. 2026 | Trains a CUA-like evaluator to explore UIs and predict usability scores. | [arXiv](https://arxiv.org/abs/2604.26020) |
| VLAA-GUI | Apr. 2026 | Adds explicit stop verification, loop breaking, search, coding, and grounding modules. | [arXiv](https://arxiv.org/abs/2604.21375) |
| On The Reliability Of CUAs | Apr. 2026 | Analyzes stochastic execution, task ambiguity, and behavior variability as reliability factors. | [arXiv](https://arxiv.org/abs/2604.17849) |
| ClawGUI | Apr. 2026 | Packages GUI-agent RL, standardized evaluation, and deployment into one open framework. | [arXiv](https://arxiv.org/abs/2604.11784) |
| AgentHazard | Apr. 2026 | Evaluates harmful multi-step behavior that emerges from locally plausible agent actions. | [arXiv](https://arxiv.org/abs/2604.02947) |
| SecAgent | Mar. 2026 | Builds an efficient mobile GUI agent with semantic history compression and Chinese GUI data. | [arXiv](https://arxiv.org/abs/2603.08533) |

#### This Project Is Ongoing

If you find missing papers, reports, projects, datasets, or metadata errors, please open an issue or pull request. A title plus URL is already useful; deeper evaluation can go into `notes/`.

If you find this repo useful, please star it.

## Table of Contents <!-- omit in toc -->

- [GUI Agent Surveys](#gui-agent-surveys)
- [GUI Representation & Grounding](#gui-representation--grounding)
- [Models & Agents](#models--agents)
- [Video Demonstrations & Trajectories](#video-demonstrations--trajectories)
- [Planning, Recovery & Memory](#planning-recovery--memory)
- [Training, RL & Reward Models](#training-rl--reward-models)
- [Safety & Trust](#safety--trust)
- [Evaluation Substrates](#evaluation-substrates)
- [Products, APIs & Infrastructure](#products-apis--infrastructure)
- [Related Awesome Lists](#related-awesome-lists)

### GUI Agent Surveys

| Paper | Date / venue | What problem it frames | How it helps |
| --- | --- | --- | --- |
| [GUI Agents with Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2411.04890) | Nov. 2024 | The field lacks a common taxonomy for GUI-agent data, construction, evaluation, and applications. | Organizes GUI-agent work around foundation-model capabilities, resources, agent pipelines, evaluation, and industrial use cases. |
| [GUI Agents: A Survey](https://arxiv.org/abs/2412.13501) | Dec. 2024 | GUI agents span many environments and training recipes, making papers hard to compare. | Summarizes architectures, planning loops, training data, action spaces, and benchmark families for general GUI automation. |
| [OS Agents: A Survey on MLLM-based Agents for Computer, Phone and Browser Use](https://aclanthology.org/2025.acl-long.369/) | ACL 2025 | Computer, phone, and browser-use agents are often studied separately despite sharing MLLM mechanisms. | Places GUI agents under the broader OS-agent stack: perception, planning, action execution, memory, and evaluation across platforms. |
| [Towards Trustworthy GUI Agents: A Survey](https://arxiv.org/abs/2503.23434) | Mar. 2025 | GUI agents perform irreversible actions, so capability-only evaluation misses safety and trust requirements. | Surveys risks such as privacy leakage, prompt injection, robustness failure, permission control, and trustworthy evaluation. |

### GUI Representation & Grounding

| Paper / system | Date / venue | Problem it studies | Core mechanism |
| --- | --- | --- | --- |
| [ScreenAI](https://www.ijcai.org/proceedings/2024/339) | IJCAI 2024 | General VLMs are weak on UI screens and infographics because layout, OCR, and visual semantics interact. | Builds a UI/infographic VLM and task mixture for screen understanding, layout reasoning, and element-level comprehension. |
| [Ferret-UI](https://eccv.ecva.net/virtual/2024/poster/749) | ECCV 2024 | Mobile UI reasoning needs referring, grounding, and widget understanding beyond generic image captioning. | Adapts a multimodal LLM to mobile screens with region-level grounding, referring expressions, OCR-aware reasoning, and UI-specific data. |
| [OmniParser](https://github.com/microsoft/OmniParser) | Aug. 2024 | Pure-vision agents need structured UI elements when accessibility trees or DOM are unavailable. | Parses screenshots into detected icons, text, and labeled UI regions that downstream agents can reference for grounding and action selection. |
| [SeeClick](https://aclanthology.org/2024.acl-long.505/) | ACL 2024 | Screenshot-only GUI control fails if the model cannot point to the intended UI element across desktop, web, and mobile. | Curates GUI grounding data, trains screenshot-to-target models, and introduces ScreenSpot-style cross-platform grounding evaluation. |
| [OS-ATLAS](https://arxiv.org/abs/2410.23218) | ICLR 2025 Spotlight | A generalist action model needs cross-platform GUI grounding and action data instead of environment-specific selectors. | Builds a large GUI grounding/action corpus and trains a foundation action model for desktop, mobile, and web interfaces. |
| [ShowUI](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html) | CVPR 2025 | GUI screenshots are dense and expensive to process at every step. | Uses UI-guided visual token selection plus interleaved vision-language-action modeling to reduce visual tokens while preserving action context. |
| [ScreenSpot-Pro](https://arxiv.org/abs/2504.07981) | Apr. 2025 | Existing grounding benchmarks under-test dense, high-resolution professional software. | Builds a professional desktop grounding benchmark focused on tiny controls, repeated icons, toolbars, panels, and high-resolution UI layouts. |
| [GUI-G1](https://arxiv.org/abs/2505.15810) | May 2025 | R1-Zero-like RL for GUI grounding can improve scores but may be unstable or overfit to reasoning traces. | Analyzes RL-style grounding training and proposes targeted fixes for data, reward, and reasoning behavior in GUI visual grounding. |
| [ReGUIDE](https://arxiv.org/abs/2505.15259) | May 2025 | GUI grounding often needs huge training data and still misses small or ambiguous targets. | Improves data efficiency with spatial reasoning and test-time search/scaling so the model can refine coordinates more deliberately. |
| [A11y-Compressor](https://arxiv.org/abs/2605.00551) | May 2026 | Linearized accessibility trees are token-heavy, redundant, and weak at preserving spatial structure. | Reconstructs visual context from accessibility trees, reduces redundant nodes, and preserves spatial relationships for compact observations. |

### Models & Agents

| Paper / system | Date / venue | Problem it studies | Core mechanism |
| --- | --- | --- | --- |
| [Agent S](https://proceedings.iclr.cc/paper_files/paper/2025/hash/394c7c30ea87b5c3521b4d9e9d419071-Abstract-Conference.html) | ICLR 2025 | Desktop computer use needs long-horizon planning, domain knowledge, and reusable experience, not only screenshots and clicks. | Combines an Agent-Computer Interface with experience-augmented hierarchical planning and memory for OS-level workflows. |
| [Aguvis](https://proceedings.mlr.press/v267/xu25ae.html) | ICML 2025 | GUI agents often depend on DOM, accessibility trees, or platform-specific wrappers. | Proposes a unified pure-vision agent that standardizes cross-platform actions and uses structured internal reasoning over screenshots. |
| [OpenCUA](https://github.com/xlang-ai/OpenCUA) | Aug. 2025 | CUA research needs open data, models, benchmarks, and reproducible training recipes. | Releases an open computer-use foundation stack spanning data construction, model training, tools, and evaluation artifacts. |
| [UI-TARS](https://arxiv.org/abs/2501.12326) | Jan. 2025 | Prompt-wrapped general VLMs are brittle for GUI tasks because GUI interaction is not a native model capability. | Trains native GUI agents to perceive screenshots and directly emit human-like mouse/keyboard actions across desktop, mobile, and web. |
| [UI-TARS-2](https://arxiv.org/abs/2509.02544) | Sep. 2025 | Native GUI agents still need scalable multi-turn data, RL, memory, and environment stability. | Extends UI-TARS with a data flywheel and multi-turn RL recipe for GUI action, reasoning, and memory improvement. |
| [ScaleCUA](https://arxiv.org/abs/2509.15221) | Sep. 2025 | Open CUA models need cross-platform scale rather than narrow benchmark tuning. | Scales open-source computer-use agents with cross-platform trajectory/data mixtures and unified evaluation across desktop, mobile, and web. |
| [Mobile-Agent-v3](https://arxiv.org/abs/2508.15144) | Aug. 2025 | Mobile GUI automation needs a strong foundation model plus an agent framework for practical device tasks. | Introduces GUI-Owl as a foundation GUI agent model and wraps it in Mobile-Agent-v3 for multi-benchmark mobile and desktop automation. |
| [Mobile-Agent-v3.5](https://arxiv.org/abs/2602.16855) | Feb. 2026 | GUI agents need stronger cross-platform generalization, model scaling, and real-time execution after the v3 foundation. | Introduces GUI-Owl-1.5 with multiple model sizes and platform coverage across desktop, mobile, browser, and related GUI settings. |
| [AutoGLM](https://arxiv.org/abs/2411.00820) | Nov. 2024 | Foundation agents should learn autonomous GUI control through environment interaction rather than only static instruction following. | Builds a ChatGLM-family GUI agent trained for autonomous device control, action prediction, and environment feedback. |
| [Magentic-UI](https://arxiv.org/abs/2507.22358) | Jul. 2025 | Fully autonomous GUI agents create safety and usability risks when users need oversight or collaboration. | Designs a human-in-the-loop agentic UI framework where users can inspect, steer, approve, and collaborate with the agent. |
| [IntentCUA](https://arxiv.org/abs/2602.17049) | Feb. 2026 | CUAs can execute steps but often lose the user's true intent across long workflows. | Centers the agent loop around intent modeling so action choices and state interpretation stay tied to the original user goal. |
| [UI-Voyager](https://arxiv.org/abs/2603.24533) | Mar. 2026 | Mobile GUI agents learn inefficiently from failed long-horizon trajectories under sparse rewards. | Uses a self-evolving learning process that mines failed experience and assigns credit more clearly for future GUI attempts. |
| [SecAgent](https://arxiv.org/abs/2603.08533) | Mar. 2026 | Small mobile GUI agents need better multilingual data and cheaper history representations. | Builds a 3B mobile GUI agent with human-verified Chinese grounding/navigation data and semantic context summaries of past actions. |

### Video Demonstrations & Trajectories

| Paper / system | Date / venue | Problem it studies | Core mechanism |
| --- | --- | --- | --- |
| [CUA-Suite](https://arxiv.org/abs/2603.24440) | Mar. 2026 | CUA training lacks large human demonstrations with screen videos and actionable trajectories. | Builds a large human-annotated video-demonstration suite for computer-use tasks, including temporal grounding and execution traces. |
| [ExeVRM](https://arxiv.org/abs/2603.10178) | Mar. 2026 | Reward models for CUA need to judge process and outcome from execution evidence, not only final screenshots. | Learns video-based reward modeling for computer-use trajectories, using execution videos to score success and localize failure over time. |
| [ShowUI-Aloha](https://arxiv.org/abs/2601.07181) | Jan. 2026 | Human screen recordings are plentiful but hard to convert into training data for GUI agents. | Converts human-taught desktop demonstrations into structured GUI-agent trajectories and uses them for behavior learning. |
| [VideoAgentTrek](https://arxiv.org/abs/2510.19488) | Oct. 2025 | Unlabeled tutorial videos contain useful computer-use behavior but lack action annotations. | Mines video data for computer-use pretraining by detecting action boundaries and reconstructing task-relevant interaction signals. |
| [Watch and Learn](https://arxiv.org/abs/2510.04673) | Oct. 2025, CVPR 2026 | Agents need to learn software workflows from ordinary online videos without expensive manual trajectories. | Transforms online computer-use videos into executable UI trajectories through temporal understanding and inverse-action modeling. |
| [VideoWebArena](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5b555804d495321df2e3208cc27f4fbc-Abstract-Conference.html) | ICLR 2025 | Long-context web tasks often depend on information shown in videos, not static pages. | Extends web-agent evaluation with video-understanding tasks that require watching, remembering, and acting in a browser. |
| [VideoGUI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | Instructional videos are a natural supervision source for GUI automation but require grounding to concrete UI actions. | Provides a video-conditioned GUI automation benchmark where agents infer actions from tutorial-style demonstrations. |
| [GUI-KV](https://arxiv.org/abs/2510.00536) | Oct. 2025 | Long GUI histories make repeated screenshot/context processing expensive. | Uses spatio-temporal KV-cache strategies so GUI agents can reuse visual context efficiently across action steps. |

### Planning, Recovery & Memory

| Paper / system | Date / venue | Problem it studies | Core mechanism |
| --- | --- | --- | --- |
| [Multi-Agent Computer Use](https://arxiv.org/abs/2606.01533) | Jun. 2026 | Single serial CUA execution is slow and brittle on complex long-horizon tasks. | Uses a manager model to decompose tasks into a DAG, dispatch parallel subagents, pass forward partial observations, and revise the plan online. |
| [WebDreamer](https://openreview.net/forum?id=c6l7yA0HSq) | ICML 2025 | Web agents need to plan over possible future states rather than react step by step. | Treats the LLM as a world model for the internet and uses model-based planning to imagine outcomes before acting. |
| [BacktrackAgent](https://arxiv.org/abs/2505.20660) | May 2025, EMNLP 2025 Oral | GUI agents often continue after wrong actions because they cannot detect or repair errors. | Adds explicit error detection, reflection, and backtracking so the agent can recover from failed GUI transitions. |
| [ExACT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3b893ba1de12f76020b03f7ae8e1afd-Abstract-Conference.html) | ICLR 2025 | Web agents need exploration strategies when the next useful action is uncertain. | Combines reflective MCTS with exploratory learning to search possible web actions and learn from exploration traces. |
| [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html) | ICML 2025 | Agents waste effort rediscovering workflows that recur across websites and tasks. | Stores and retrieves reusable workflow memories from past trajectories to guide future planning and action selection. |
| [A-Mem](https://arxiv.org/abs/2502.12110) | NeurIPS 2025 | General LLM agents need memory systems that organize and update experiences, not only store and retrieve them. | Builds an agentic memory network with Zettelkasten-style notes, dynamic indexing/linking, and memory evolution. |
| [GUI-explorer](https://aclanthology.org/2025.acl-long.282/) | ACL 2025 | Mobile agents lack transition-aware knowledge about how app states connect. | Autonomously explores GUIs and mines state-transition knowledge that can be reused by downstream agents without retraining. |
| [Synapse](https://arxiv.org/abs/2306.07863) | ICLR 2024 | In-context computer-control agents need useful past examples, not only current observations. | Retrieves and prompts with trajectory exemplars plus memory so the agent can imitate prior successful computer-control patterns. |
| [MobileDreamer](https://arxiv.org/abs/2601.04035) | Jan. 2026 | Mobile agents need internal models of UI transitions to plan before acting. | Learns a generative sketch world model for mobile GUI states, enabling imagined transitions and planning support. |
| [Code2World](https://arxiv.org/abs/2602.09856) | Feb. 2026 | GUI world models are hard to learn from pixels alone when exact UI dynamics matter. | Generates renderable code as a structured world model so agents can simulate and reason over GUI states. |
| [DynaWeb](https://arxiv.org/abs/2601.22149) | Jan. 2026 | Web agents need sample-efficient learning in dynamic sites with sparse rewards. | Applies model-based reinforcement learning to web agents by learning environment dynamics and planning with them. |
| [VLAA-GUI](https://arxiv.org/abs/2604.21375) | Apr. 2026 | GUI agents prematurely stop, loop, or fail when unfamiliar workflows need external knowledge. | Adds a completeness verifier, loop breaker, search agent, coding agent, and grounding agent as modular tools around a VLM agent. |
| [Step-level Optimization](https://arxiv.org/abs/2604.27151) | Apr. 2026 | Always calling a frontier multimodal model is slow and expensive, but cheap policies fail at high-risk steps. | Uses stuck and milestone monitors to trigger escalation from a small policy to a stronger model only when risk or verification need increases. |

### Training, RL & Reward Models

| Paper / system | Date / venue | Problem it studies | Core mechanism |
| --- | --- | --- | --- |
| [ComputerRL](https://arxiv.org/abs/2508.14040) | Aug. 2025 | End-to-end CUA training needs scalable online interaction with desktop environments. | Trains computer-use agents with online RL over GUI/API hybrid actions and parallel desktop execution. |
| [MobileRL](https://arxiv.org/abs/2509.18119) | Sep. 2025 | Mobile agents need online RL that handles real app state, gestures, and sparse success signals. | Uses agentic online RL for mobile GUI tasks, connecting interaction rollouts with reward and policy improvement. |
| [Web-Shepherd](https://arxiv.org/abs/2505.15277) | May 2025, NeurIPS 2025 Spotlight | Web agents need process-level feedback, not only final success/failure labels. | Builds process reward models and trajectory annotations for reinforcing web agents step by step. |
| [ProgRM](https://arxiv.org/abs/2505.18121) | May 2025 | GUI-agent rewards are hard to specify when success depends on task-specific state. | Uses multi-agent programmatic reward modeling to generate more reliable GUI-task reward signals. |
| [WebAgent-R1](https://arxiv.org/abs/2505.16421) | May 2025, EMNLP 2025 | Web agents require multi-turn RL rather than single-step imitation or prompting. | Trains web agents end to end with multi-turn reinforcement learning over browser trajectories. |
| [WebRL](https://openreview.net/forum?id=oVKEAFjEqv) | ICLR 2025 | Web-agent RL must discover a curriculum instead of relying on fixed handcrafted tasks. | Uses self-evolving online curriculum RL so agents generate and learn from progressively harder web tasks. |
| [DigiRL](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html) | NeurIPS 2024 | In-the-wild mobile device control needs autonomous RL beyond offline demonstrations. | Starts from offline policies and improves them through online interaction with real Android tasks and reward signals. |
| [OS-Genesis](https://aclanthology.org/2025.acl-long.277/) | ACL 2025 | GUI trajectory data is expensive because humans must specify tasks and record successful actions. | Synthesizes tasks in reverse from reachable GUI states to automate trajectory construction for agent training. |
| [ANCHOR](https://arxiv.org/abs/2602.07153) | Feb. 2026 | GUI-agent datasets miss alternative branches and recovery paths around important decision points. | Expands trajectories from branch points to create richer counterfactual and recovery-oriented GUI-agent training data. |
| [Training CUAs To Assess Usability](https://arxiv.org/abs/2604.26020) | Apr. 2026 | Automated usability assessment requires agents that can explore interfaces like users and judge interaction quality. | Trains uxCUA to prioritize important flows, execute human-like interactions, and predict learned usability scores from UI data and preferences. |

### Safety & Trust

| Paper / system | Date / venue | Problem it studies | Core mechanism |
| --- | --- | --- | --- |
| [RedTeamCUA](https://github.com/OSU-NLP-Group/RedTeamCUA) | 2026 | CUA safety must be tested in hybrid web-OS settings where attacks can cross surfaces. | Provides realistic adversarial tasks for indirect prompt injection and misuse across browser and desktop environments. |
| [OS-HARM](https://arxiv.org/abs/2503.18492) | Mar. 2025, NeurIPS 2025 Datasets and Benchmarks Spotlight | Computer-use agents can execute harmful or policy-violating OS actions. | Builds an OSWorld-style safety benchmark covering misuse, injections, unsafe actions, and model-behavior failures. |
| [AgentDAM](https://arxiv.org/abs/2503.09780) | Mar. 2025, NeurIPS 2025 | Web agents may over-disclose user data while completing legitimate tasks. | Evaluates privacy leakage and data-minimization behavior for autonomous web agents. |
| [Pop-up Attack](https://aclanthology.org/2025.acl-long.411/) | ACL 2025 | Vision-language computer agents are vulnerable to malicious UI popups and visual instructions. | Constructs popup-based attacks and measures whether agents follow adversarial screen content during computer-use tasks. |
| [EIA](https://openreview.net/forum?id=xMOLUzo2Lk) | ICLR 2025 | Generalist web agents may leak private information when compromised environments inject malicious content. | Studies environmental injection attacks that manipulate web pages to induce privacy leakage during otherwise normal tasks. |
| [ST-WebAgentBench](https://openreview.net/forum?id=MuCDzH0ctf) | ICLR 2025 | Web-agent benchmarks often measure task success while ignoring whether the task was completed safely. | Adds safety and trustworthiness scenarios to evaluate web agents on constraint following, policy compliance, and risky behavior. |
| [Progent](https://arxiv.org/abs/2504.11703) | Apr. 2025 | Agent permissions are hard to control when policies change with task state and risk. | Introduces programmable privilege control that gates tool and environment access according to explicit security rules. |
| [SafePred](https://arxiv.org/abs/2602.01725) | Feb. 2026 | Reactive guardrails may intervene too late after an agent has already entered a risky path. | Uses world-model prediction to forecast dangerous future states and block unsafe computer-use actions before execution. |
| [AgentHazard](https://arxiv.org/abs/2604.02947) | Apr. 2026 | Harm can emerge from sequences of individually plausible tool and environment actions. | Provides harmful objectives plus locally legitimate step sequences to test whether agents interrupt unsafe multi-step behavior. |
| [AgentHijack](https://arxiv.org/abs/2605.25707) | May 2026 | Real environments contain non-adversarial corruptions such as popups, resolution shifts, and competing apps. | Defines configurable corruptions and proposes an agent framework with stronger grounding plus an onlooker for environment checking. |
| [On The Reliability Of Computer Use Agents](https://arxiv.org/abs/2604.17849) | Apr. 2026 | Reported CUA success hides instability from randomness, ambiguous task specs, and variable action choices. | Separates reliability factors and evaluates how execution stochasticity, specification ambiguity, and behavior variation affect completion. |

### Evaluation Substrates

| Benchmark / paper | Date / venue | What it tests | How it is built |
| --- | --- | --- | --- |
| [OSWorld](https://github.com/xlang-ai/OSWorld) | NeurIPS 2024 Datasets and Benchmarks | Open-ended desktop tasks in real OS environments. | Runs agents in real computer environments with task-specific success checks across files, apps, settings, and web workflows. |
| [WebArena](https://github.com/web-arena-x/webarena) | ICLR 2024 | Realistic stateful browser tasks on self-hosted websites. | Provides websites, accounts, data, browser actions, and task validators for multi-step web navigation. |
| [VisualWebArena](https://aclanthology.org/2024.acl-long.50/) | ACL 2024 | Multimodal web tasks where visual page content matters. | Extends WebArena-style tasks with screenshot-dependent information and visual grounding requirements. |
| [AndroidWorld](https://github.com/google-research/android_world) | ICLR 2025 | Autonomous agents in Android apps and device state. | Uses Android environments with programmatic task initialization, mobile actions, and success checks. |
| [WorkArena](https://proceedings.mlr.press/v235/drouin24a.html) | ICML 2024 | Enterprise knowledge-work tasks in ServiceNow-like workflows. | Builds realistic browser tasks around common enterprise operations and later supports BrowserGym-style evaluation. |
| [Windows Agent Arena](https://github.com/microsoft/WindowsAgentArena) | ICML 2025 | Multi-modal OS agents on Windows applications. | Provides Windows-specific desktop tasks, automation harnesses, and evaluation for OS-level agent capability. |
| [OSWorld-G](https://github.com/xlang-ai/OSWorld-G) | May 2025 | Fine-grained GUI grounding for computer-use agents. | Decomposes OSWorld-style tasks into grounding data and synthetic UI-element localization examples. |
| [MedCUA-Bench](https://arxiv.org/abs/2606.03203) | Jun. 2026 | Screenshot-only clinical computer-use agents in safety-sensitive medical software. | Reconstructs clinical interfaces from manuals/open-source systems and evaluates strict success plus five clinical safety dimensions. |
| [OpenComputer](https://arxiv.org/abs/2605.19769) | May 2026 | Verifiable desktop software workflows with auditable partial credit. | Combines app-specific state verifiers, task synthesis, self-improving verification, and trajectory-level evaluation across 33 applications. |
| [SaaS-Bench](https://arxiv.org/abs/2605.15777) | May 2026 | Professional SaaS workflows involving long horizons and cross-application coordination. | Uses 23 deployable SaaS systems, 106 realistic tasks, multimodal evidence, and weighted verification checkpoints. |
| [CutVerse](https://arxiv.org/abs/2605.19484) | May 2026 | Professional media post-production in dense creative software. | Curates expert demonstrations across seven creative applications and parses screen recordings/logs into compositional GUI trajectories. |

### Products, APIs & Infrastructure

| System / report | Date | What problem it addresses | How it works |
| --- | --- | --- | --- |
| [OpenAI Computer-Using Agent](https://openai.com/index/computer-using-agent/) | Jan. 2025 | General web/computer tasks need an agent trained to inspect screens and execute UI actions. | Provides a computer-use model/interface used for browser and UI interaction under safety and task-completion constraints. |
| [OpenAI CUA Sample App](https://github.com/openai/openai-cua-sample-app) | 2025 | Developers need a concrete reference loop for CUA-style observation, action, and execution. | Shows how to wire a computer-use model to browser/computer control, screenshots, action execution, and user oversight. |
| [Anthropic Computer Use](https://www.anthropic.com/news/3-5-models-and-computer-use) | Oct. 2024 | Claude models need a standard interface for controlling computers through screenshots and tools. | Exposes computer-use actions such as mouse and keyboard control with a loop that returns updated screenshots after each step. |
| [Project Mariner](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/google-gemini-ai-update-december-2024/) | Dec. 2024 | Browser agents need stronger navigation, visual context, and task execution inside real web pages. | Demonstrates Gemini-based browser operation with planning, page understanding, and user-facing controls. |
| [trycua/cua](https://github.com/trycua/cua) | 2025 | CUA experiments need reproducible virtual computers and local/remote execution infrastructure. | Provides a computer-use agent infrastructure stack for running agents in isolated desktop environments. |
| [BrowserGym](https://openreview.net/forum?id=5298fKGmv3) | TMLR 2025 | Web-agent research needs standardized environments, wrappers, and reproducible evaluation. | Unifies browser tasks, action/observation wrappers, and benchmark interfaces for web-agent experimentation. |
| [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop) | 2025 | Native GUI models need a usable desktop agent shell. | Packages UI-TARS-style models into a desktop automation application with screen perception and action execution. |
| [ClawGUI](https://arxiv.org/abs/2604.11784) | Apr. 2026 | GUI-agent progress is limited by fragmented RL training, drifting evaluation protocols, and weak deployment paths. | Provides an open framework with RL infrastructure, standardized benchmark reproduction, and mobile deployment through chat platforms. |
| [CLI-Anything](https://arxiv.org/abs/2606.03854) | Jun. 2026 | GUI control is brittle for agents when structured programmatic interfaces could expose the same functionality. | Converts existing applications into command-line harnesses with explicit state, structured commands, and deterministic feedback. |

### Related Awesome Lists

| List | Focus |
| --- | --- |
| [showlab/Awesome-GUI-Agent](https://github.com/showlab/Awesome-GUI-Agent) | Broad GUI-agent paper and project tracking. |
| [OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | GUI-agent paper list with active academic updates. |
| [ZJU-REAL/Awesome-GUI-Agents](https://github.com/ZJU-REAL/Awesome-GUI-Agents) | GUI-agent resources and benchmarks. |
| [Autonomous-Agent-Team/Awesome-GUI-Agent-Safety](https://github.com/Autonomous-Agent-Team/Awesome-GUI-Agent-Safety) | GUI-agent safety and trustworthiness resources. |
| [cdxeve/awesome-computer-use-agents](https://github.com/cdxeve/awesome-computer-use-agents) | Computer-use agent products, APIs, and ecosystem links. |
