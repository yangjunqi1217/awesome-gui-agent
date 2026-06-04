# Reading Roadmap

This roadmap is ordered by GUI-agent paper families. It is not a plan to build a new benchmark. Benchmarks are recorded only as experimental evidence used by papers.

Start with [gui-paper-landscape.md](gui-paper-landscape.md), use [method-paper-shortlist.md](method-paper-shortlist.md) to choose papers, then use [research-questions.md](research-questions.md) to choose a non-benchmark research direction.

## Track 1: GUI Representation And Grounding

Goal: understand how papers represent the GUI and map language to UI targets.

Read in order:

1. [ScreenAI](https://www.ijcai.org/proceedings/2024/339)
2. [Ferret-UI](https://eccv.ecva.net/virtual/2024/poster/749)
3. [SeeClick](../notes/papers/2024-seeclick.md)
4. [OmniParser](../notes/repos/microsoft-omniparser.md)
5. [OS-ATLAS](../notes/papers/2024-os-atlas.md)
6. [ShowUI](../notes/papers/2025-showui.md)
7. [ScreenSpot-Pro](../notes/papers/2025-screenspot-pro.md)

Questions to answer:

- What GUI representation does the paper assume?
- Is the output a point, box, element, action, or structured state?
- Does the method solve perception, grounding, or action prediction?
- Which benchmarks are used only as evidence?

## Track 2: Action Models And Planning

Goal: understand how GUI papers model actions, state, planning, and recovery.

Read in order:

1. [GPT-4V is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
2. [Agent S](../notes/papers/2025-agent-s.md)
3. [ExACT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3b893ba1de12f76020b03f7ae8e1afd-Abstract-Conference.html)
4. [BacktrackAgent](https://arxiv.org/abs/2505.20660)
5. [WebDreamer](https://openreview.net/forum?id=c6l7yA0HSq)
6. [UI-TARS](../notes/papers/2025-ui-tars.md)
7. [OpenCUA](../notes/papers/2025-opencua.md)

Questions to answer:

- What is the action representation?
- Is planning explicit or implicit?
- How does the agent detect it is off-track?
- Is recovery part of the method or just an observed failure mode?

## Track 3: Memory, Skills, And Data

Goal: understand how GUI papers reuse experience and construct training data.

Read in order:

1. [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
2. [Synapse](https://arxiv.org/abs/2306.07863)
3. [GUI-explorer](https://aclanthology.org/2025.acl-long.282/)
4. [OS-Genesis](https://aclanthology.org/2025.acl-long.277/)
5. [UI-TARS-2](https://arxiv.org/abs/2509.02544)
6. [CUA-Suite](https://arxiv.org/abs/2603.24440)

Questions to answer:

- What is remembered or generated?
- How is memory retrieved or invalidated?
- How is data quality checked?
- Does more data improve robustness or only benchmark fit?

## Track 4: Learning, RL, And Reward Models

Goal: understand how GUI agents improve beyond prompting.

Read in order:

1. [DigiRL](https://proceedings.neurips.cc/paper_files/paper/2024/hash/1704ddd0bb89f159dfe609b32c889995-Abstract-Conference.html)
2. [WebRL](https://openreview.net/forum?id=oVKEAFjEqv)
3. [WebAgent-R1](https://arxiv.org/abs/2505.16421)
4. [Web-Shepherd](https://arxiv.org/abs/2505.15277)
5. [GUI-G1](https://arxiv.org/abs/2505.15810)
6. [ComputerRL](https://arxiv.org/abs/2508.14040)
7. [UI-TARS-2](https://arxiv.org/abs/2509.02544)

Questions to answer:

- What is the reward source: environment success, judge model, process reward, dense progress, or human feedback?
- Is training online, offline, or offline-to-online?
- How are failed trajectories used?
- What prevents reward hacking or overlong reasoning?

## Track 5: Safety And Trust

Goal: understand why GUI agents are risky beyond ordinary chatbot safety.

Read in order:

1. [Attacking Vision-Language Computer Agents via Pop-ups](https://aclanthology.org/2025.acl-long.411/)
2. [EIA](https://openreview.net/forum?id=xMOLUzo2Lk)
3. [ST-WebAgentBench](https://openreview.net/forum?id=MuCDzH0ctf)
4. [AgentDAM](https://arxiv.org/abs/2503.09780)
5. [OS-HARM](https://arxiv.org/abs/2503.18492)
6. [RedTeamCUA](https://openreview.net/forum?id=yWwrgcBoK3)
7. [Progent](https://arxiv.org/abs/2504.11703)

Questions to answer:

- What is the threat model?
- Can attacks modify the environment without changing the user request?
- What actions require human confirmation?
- Can guardrails inspect planned actions before execution?
- Are safety metrics separate from task success?

## Track 6: Industry Systems And Reproduction

Goal: decide what we can actually run or build on.

Read/test in order:

1. [OpenAI CUA sample app](https://github.com/openai/openai-cua-sample-app)
2. [Anthropic computer use](https://www.anthropic.com/news/3-5-models-and-computer-use)
3. [trycua/cua](../notes/repos/trycua-cua.md)
4. [BrowserGym](https://openreview.net/forum?id=5298fKGmv3)
5. [OmniParser](../notes/repos/microsoft-omniparser.md)
6. [UI-TARS Desktop](https://github.com/bytedance/UI-TARS-desktop)
7. [OpenCUA](https://github.com/xlang-ai/OpenCUA)

Questions to answer:

- What is the minimum environment setup?
- Does it run locally, remotely, or in a hosted sandbox?
- How are screenshots, actions, logs, and confirmations represented?
- Can it run our target workflows?

## Suggested First Two Weeks

Week 1:

1. Read ScreenAI, Ferret-UI, SeeClick, OmniParser, OS-ATLAS.
2. Fill notes for all five.
3. Extract GUI representation and grounding assumptions; do not design a new benchmark.

Week 2:

1. Read ShowUI, Agent S, WebRL, BacktrackAgent.
2. Extract method families and failure assumptions.
3. Decide whether our first project should target recovery, progress rewards, hybrid action routing, trust boundaries, or efficient perception.
