# GUI Paper Landscape

This repository should be organized around GUI-agent research questions and paper families, not around benchmarks. Benchmarks are experiment metadata: when reading a paper, record which benchmarks it uses, but do not let benchmark names define the research agenda.

## How To Read A GUI-Agent Paper

For each paper, first identify the paper family:

- What GUI problem is it solving?
- What representation of the GUI does it assume?
- What action space does it use?
- What training or inference signal is new?
- What is the actual mechanism, not just the benchmark score?
- Which benchmarks are used only as evidence?

Recommended note fields:

- **Paper family**
- **GUI representation**
- **Action representation**
- **Core mechanism**
- **Training signal**
- **Evaluation benchmarks**
- **Failure mode addressed**
- **What question it opens**

## Paper Family 1: GUI Representation And Screen Understanding

Core question: how should an agent represent a GUI screen?

Subproblems:

- Screenshot-only vs accessibility tree vs DOM/XML vs hybrid state.
- OCR and text-rich screen understanding.
- Icon detection, captioning, and UI element parsing.
- Region selection, cropping, zooming, and token efficiency.
- High-resolution professional software screens.

Representative papers/systems:

- ScreenAI
- Ferret-UI
- OmniParser
- DeskVision
- EDGE
- Falcon-UI
- A11y-Compressor
- ShowUI token selection

What to look for:

- Does the representation preserve action-relevant state?
- Does it compress away important context?
- Does it generalize across web, desktop, and mobile?
- Does it improve downstream task success or only perception metrics?

Benchmarks used as evidence:

- ScreenSpot / ScreenSpot-Pro
- VisualWebBench
- OSWorld-G
- AITW / AndroidControl-style mobile tasks

## Paper Family 2: GUI Grounding And Pointing

Core question: how does the agent map an instruction to the correct UI target?

Subproblems:

- Point prediction vs bounding boxes vs element IDs.
- Referring expression grounding in dense UIs.
- Grounding without DOM/XML.
- Test-time zoom/search/refinement.
- Grounding under distribution shift or adversarial perturbation.

Representative papers/systems:

- SeeClick
- OS-ATLAS
- ScreenSpot-Pro
- ReGUIDE
- GUI-G1
- SE-GUI
- UI-Zoomer / iterative narrowing
- Aria-UI

What to look for:

- Is grounding the true bottleneck in the downstream task?
- How does the method handle small or repeated controls?
- Is the model trained for coordinates, elements, or actions?
- Does reasoning help or hurt precise pointing?

Benchmarks used as evidence:

- ScreenSpot variants
- OSWorld-G
- Mind2Web grounding splits
- AITW / mobile grounding tests

## Paper Family 3: Action Models And GUI-VLA Agents

Core question: what model directly predicts GUI actions?

Subproblems:

- Vision-language-action modeling.
- Unified action spaces across desktop, mobile, and web.
- Reasoned-action vs direct-action modes.
- Cross-platform training.
- Small on-device GUI action models.

Representative papers/systems:

- ShowUI
- OS-ATLAS
- Aguvis
- UI-TARS
- OpenCUA
- ScaleCUA
- Mobile-Agent-v3 / GUI-Owl
- AutoGLM
- AppVLM
- TinyClick

What to look for:

- What is the action vocabulary?
- Does the model predict atomic actions or high-level commands?
- Does it require separate planner and executor?
- Is the model trained on demonstrations, synthetic trajectories, RL, or mixed data?

Benchmarks used as evidence:

- OSWorld
- AndroidWorld / AndroidLab
- WebArena / VisualWebArena
- ScreenSpot-style grounding benchmarks

## Paper Family 4: Planning, Recovery, And State Tracking

Core question: how does the agent maintain progress through long GUI workflows?

Subproblems:

- Hierarchical planning.
- State tracking from screenshots and history.
- Backtracking after errors.
- Detecting loops and premature stopping.
- World models and imagined outcomes.

Representative papers/systems:

- Agent S
- ExACT
- WebDreamer
- BacktrackAgent
- Dynamic Planning for GUI Automation
- VLAA-GUI
- SPlanner
- Agent S2

What to look for:

- What is represented as state?
- How are failures detected?
- Is recovery learned, prompted, searched, or rule-based?
- Does the agent have an explicit notion of task progress?

Benchmarks used as evidence:

- WebArena / VisualWebArena
- OSWorld / WindowsAgentArena
- AndroidWorld / AndroidLab
- WorkArena

## Paper Family 5: Memory, Skills, And Personalization

Core question: what should a GUI agent remember and reuse?

Subproblems:

- Episodic memory of trajectories.
- Procedural memory or reusable skills.
- UI-state memory and app maps.
- Personal preference memory.
- Memory invalidation and poisoning.

Representative papers/systems:

- Agent Workflow Memory
- Synapse
- Agent S
- GUI-explorer
- UI-Mem
- AndroTMem
- MAGNET
- ContractSkill
- Persona2Web

What to look for:

- Is memory retrieved by task text, UI state, app identity, or trajectory similarity?
- Does memory improve unseen tasks or only repeated tasks?
- What happens when UI layouts change?
- What privacy risks does memory introduce?

Benchmarks used as evidence:

- Mind2Web / WebArena
- AndroidWorld
- WorkArena
- Personalized web/mobile tasks

## Paper Family 6: Training Data And Trajectory Generation

Core question: where do GUI-agent training trajectories come from, and which ones matter?

Subproblems:

- Human demonstrations.
- Synthetic tasks and reverse task synthesis.
- Video-to-trajectory conversion.
- Branch-point and counterfactual data.
- Data filtering, reward labeling, and quality scoring.

Representative papers/systems:

- OS-Genesis
- ANCHOR
- CUA-Suite
- UI-TARS-2
- OpenCUA
- OS-ATLAS data pipeline
- Web-Shepherd data
- VideoGUI / video-derived supervision

What to look for:

- Are trajectories valid, efficient, recoverable, and safe?
- How is correctness checked?
- Is data generated by agents, humans, scripts, or models?
- Does adding more data solve the problem or amplify bad habits?

Benchmarks used as evidence:

- Usually downstream task suites like OSWorld, WebArena, AndroidWorld.
- Grounding benchmarks for action-target data.

## Paper Family 7: RL, Reward Models, And Self-Improvement

Core question: how do GUI agents improve from interaction?

Subproblems:

- Sparse final rewards.
- Process reward models.
- Progress rewards and milestone rewards.
- Online RL in expensive GUI environments.
- Self-evolving curricula and failed-trajectory learning.

Representative papers/systems:

- DigiRL
- WebRL
- WebAgent-R1
- ComputerRL
- MobileRL
- Web-Shepherd
- GUI-G1
- ProgRM
- OS-Themis
- UI-Voyager

What to look for:

- What is the reward source?
- Does reward correspond to actual UI progress?
- How are failed trajectories used?
- What prevents reward hacking, overlong reasoning, or unsafe exploration?

Benchmarks used as evidence:

- WebArena-Lite / WebArena
- AndroidWorld / AndroidLab
- OSWorld
- ScreenSpot-style grounding tasks

## Paper Family 8: Hybrid GUI + Structured Tool Use

Core question: when should a GUI agent stop clicking and use a structured tool?

Subproblems:

- GUI vs API vs DOM vs shell routing.
- Shortcut discovery.
- Tool-level permission control.
- Mixed action traces.
- Enterprise automation where GUI is only one interface.

Representative papers/systems:

- AXIS
- Beyond Browsing: API-Based Web Agents
- ToolCUA
- LiteCUA
- MAS-Bench
- Terminal Agents Suffice for Enterprise Automation
- ComputerRL API-GUI paradigm

What to look for:

- Is tool use a capability or a benchmark shortcut?
- How does the agent choose the interface?
- How are permissions and trust boundaries enforced?
- Does tool use improve reliability or create hidden failure modes?

Benchmarks used as evidence:

- WorkArena / enterprise web tasks
- OSWorld with shell/file operations
- WebArena with browser tools

## Paper Family 9: Safety, Security, And Trust Boundaries

Core question: how can a GUI agent act safely when the environment itself contains instructions?

Subproblems:

- Prompt injection through web pages, popups, emails, files, and notifications.
- Confused-deputy attacks.
- Privacy leakage and data minimization.
- Runtime action verification.
- Risk-aware confirmation.

Representative papers/systems:

- Attacking Vision-Language Computer Agents via Pop-ups
- EIA
- AEIA-MN
- AgentDAM
- OS-HARM
- RedTeamCUA
- ST-WebAgentBench
- Progent
- AgentSentinel
- VeriOS

What to look for:

- What is the attacker allowed to control?
- Does the agent distinguish user instructions from environmental text?
- Are risky actions blocked before execution?
- Is safety evaluated separately from task success?

Benchmarks used as evidence:

- RedTeamCUA
- OS-HARM
- VisualWebArena adversarial variants
- Mobile notification attack settings

## Paper Family 10: Human-Agent Interaction For GUI Agents

Core question: how should users supervise, interrupt, correct, and understand GUI agents?

Subproblems:

- Confirmation policies.
- Interruptible agents.
- Human-in-the-loop execution.
- Explaining intended next actions.
- User preference and personalization.

Representative papers/systems:

- Magentic-UI
- VeriOS
- When Users Change Their Mind
- Human-agent GUI behavior comparison papers
- OpeFlo / UX evaluation agents

What to look for:

- Does the UI reduce or increase user burden?
- When does the agent ask for help?
- Can the user redirect the agent mid-task?
- Are explanations tied to concrete GUI evidence?

Benchmarks used as evidence:

- Often custom user studies or interaction tasks.
- OS-HARM / RedTeamCUA for risky-action confirmation.

## Immediate Non-Benchmark Research Questions

1. **State-aware recovery:** Can an agent learn when it is off-track and choose undo/retry/search/ask?
2. **Progress reward:** Can UI state deltas produce reliable step-level rewards?
3. **Interface routing:** Can an agent decide between GUI, DOM, API, shell, and shortcuts based on risk and cost?
4. **Trust-boundary labeling:** Can an agent label which observations are user-authoritative vs environment-originated?
5. **Memory invalidation:** Can a GUI agent know when a remembered workflow no longer applies?
6. **Efficient perception:** Can screen parsing/model routing reduce cost without losing task reliability?

For each proposed project, the benchmark choice comes later, after the mechanism and claim are clear.
