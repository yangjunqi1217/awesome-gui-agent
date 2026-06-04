# Reading Roadmap

This roadmap is ordered by what will make future reading easier. It is not a ranking of paper quality.

## Track 1: Benchmarks First

Goal: understand what "success" means across web, desktop, and mobile.

Read in order:

1. [WebArena](../notes/papers/2023-webarena.md)
2. [VisualWebArena](https://aclanthology.org/2024.acl-long.50/)
3. [OSWorld](../notes/papers/2024-osworld.md)
4. [AndroidWorld](../notes/papers/2024-androidworld.md)
5. [WorkArena](https://proceedings.mlr.press/v235/drouin24a.html)
6. [Windows Agent Arena](https://proceedings.mlr.press/v267/bonatti25a.html)
7. [OS-HARM](https://arxiv.org/abs/2503.18492)

Questions to answer:

- What is the observation/action space?
- How is task success checked?
- Can results be reproduced without hidden manual judgment?
- What failures dominate: grounding, planning, app state, memory, safety, or evaluation brittleness?

## Track 2: Grounding And UI Perception

Goal: understand the screen-to-action bottleneck.

Read in order:

1. [SeeClick](https://aclanthology.org/2024.acl-long.505/)
2. [ScreenAI](https://www.ijcai.org/proceedings/2024/339)
3. [Ferret-UI](https://eccv.ecva.net/virtual/2024/poster/749)
4. [OmniParser](../notes/repos/microsoft-omniparser.md)
5. [OS-ATLAS](https://arxiv.org/abs/2410.23218)
6. [ShowUI](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html)
7. [ScreenSpot-Pro](../notes/papers/2025-screenspot-pro.md)
8. [OSWorld-G / Jedi](https://arxiv.org/abs/2505.13227)

Questions to answer:

- Does the method rely on screenshot-only, UI tree, OCR, DOM, or hybrid state?
- Is grounding evaluated as points, boxes, element IDs, or action success?
- Does better grounding transfer into end-to-end task success?
- What breaks on dense professional software?

## Track 3: Agent Architecture And Memory

Goal: understand how agents plan, recover, and reuse experience.

Read in order:

1. [GPT-4V is a Generalist Web Agent, if Grounded](https://proceedings.mlr.press/v235/zheng24e.html)
2. [Agent S](https://proceedings.iclr.cc/paper_files/paper/2025/hash/394c7c30ea87b5c3521b4d9e9d419071-Abstract-Conference.html)
3. [ExACT](https://proceedings.iclr.cc/paper_files/paper/2025/hash/a3b893ba1de12f76020b03f7ae8e1afd-Abstract-Conference.html)
4. [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
5. [BacktrackAgent](https://arxiv.org/abs/2505.20660)
6. [UI-Evol](https://arxiv.org/abs/2505.21964)

Questions to answer:

- Is the agent reactive, planner-executor, tree-search, memory-augmented, or specialist-generalist?
- How does it detect failures?
- Does it backtrack safely?
- Does memory store trajectories, reusable skills, state abstractions, or natural-language procedures?

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

1. Read WebArena, VisualWebArena, OSWorld, AndroidWorld.
2. Fill notes for all four.
3. Run no code except benchmark setup inspection.

Week 2:

1. Read SeeClick, OS-ATLAS, ShowUI, Agent S.
2. Test OmniParser on 10 screenshots from desktop/web/mobile.
3. Decide whether our first reproduction should be grounding-only, browser-only, or OSWorld-style.
