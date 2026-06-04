# Video/VLM To GUI Agent Roadmap

Profile: a researcher with experience in video understanding, VLMs, temporal grounding, and multimodal representation learning who wants to move into GUI agents.

This is a profile-specific reading and project roadmap. It intentionally avoids personal identifiers and keeps reusable field notes in `docs/`.

The best match is not "build another GUI benchmark." The natural bridge is to treat GUI interaction as a temporally grounded video-and-action problem: infer intent from screen recordings, recover action boundaries, predict state deltas, judge whether progress happened, and compress long visual histories into the evidence an agent needs before acting.

Related survey: [Execution-video reward and compression](../docs/execution-video-reward-and-compression.md). It collects execution-video reward modeling papers and GUI video/history compression papers.

## Why This Profile Transfers

GUI agents observe a screen sequence, choose a low-level action, and then observe a changed screen. That makes many GUI-agent failures look like video-understanding failures:

- action boundary detection over screen recordings,
- temporal grounding between instruction text and UI changes,
- inverse dynamics from before/after frames to mouse and keyboard actions,
- progress recognition from state deltas,
- long-context memory over repeated visual states,
- future-state prediction for planning and safety.

The key difference is that GUI videos are actionable. A good model must not only describe what happened; it must decide what action would reproduce, continue, repair, or avoid that transition.

## Read First

| Priority | Paper | Mechanism To Extract | Why It Matches Video/VLM |
| --- | --- | --- | --- |
| 1 | [VideoGUI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html) | Instructional-video-conditioned GUI automation | Closest bridge from instructional video understanding to desktop GUI actions. |
| 2 | [VideoWebArena](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5b555804d495321df2e3208cc27f4fbc-Abstract-Conference.html) | Long-context video-conditioned web tasks | Tests whether an agent can retain procedural and factual evidence from tutorial videos. |
| 3 | [CUA-Suite](https://arxiv.org/abs/2603.24440) | Human-annotated video demonstrations for desktop CUA | Data infrastructure reference for continuous expert screen videos, grounding, and desktop workflows. |
| 4 | [ShowUI-Aloha](https://arxiv.org/abs/2601.07181) | Screen-recording-to-teaching-trajectory pipeline | Directly turns ordinary human screen recordings into structured GUI-agent supervision. |
| 5 | [VideoAgentTrek](https://arxiv.org/abs/2510.19488) | Pretraining from unlabeled videos via inverse dynamics | Strong fit for mining tutorial videos and recovering action sequences without dense labels. |
| 6 | [Watch and Learn](https://arxiv.org/abs/2510.04673) | Online-video-to-executable-trajectory conversion | Frames computer-use annotation as inverse dynamics over consecutive screen states. |
| 7 | [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178) | Execution-video reward modeling | Turns an agent's run into a video-understanding and progress-verification problem. |
| 8 | [ShowUI](https://github.com/showlab/ShowUI) | Vision-language-action GUI model | Useful baseline for moving from perception to action prediction. |
| 9 | [BacktrackAgent](https://arxiv.org/abs/2505.20660) | Error detection and backtracking | Recovery can be reframed as temporal divergence detection over GUI state sequences. |
| 10 | [WebDreamer](https://openreview.net/forum?id=c6l7yA0HSq) | World-model planning for web agents | Connects video-style future prediction to GUI action selection. |

## Paper Clusters

### Video To Action Supervision

Core question: can we turn passive screen recordings into executable GUI trajectories?

- [VideoAgentTrek](https://arxiv.org/abs/2510.19488)
- [Watch and Learn](https://arxiv.org/abs/2510.04673)
- [ShowUI-Aloha](https://arxiv.org/abs/2601.07181)
- [CUA-Suite](https://arxiv.org/abs/2603.24440)
- [OpenCUA](https://github.com/xlang-ai/OpenCUA)

Good research angles:

- action boundary detection for cursor, typing, dragging, scrolling, and menu interactions,
- inverse dynamics from two or more GUI frames to structured actions,
- noisy tutorial-video filtering and data valuation,
- aligning narration, cursor movement, UI state, and hidden keyboard actions.

### Execution-Video Reward And Verification

Core question: can a model judge whether an agent made progress by watching the execution video?

- [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178)
- [Web-Shepherd](https://arxiv.org/abs/2505.15277)
- [ProgRM](https://arxiv.org/abs/2505.18121)
- [CUARewardBench](https://arxiv.org/abs/2510.18596)
- [IntentScore](https://arxiv.org/abs/2604.05157)
- [GUIDE](https://arxiv.org/abs/2603.25864)

Good research angles:

- state-delta progress rewards instead of final sparse success,
- temporal attribution for which step caused success or failure,
- verifier models that can distinguish visual plausibility from actual task completion,
- reward-model robustness when actions look similar but have different semantic effects.

### GUI World Models And Future-State Prediction

Core question: can an agent imagine the next GUI state before committing to an action?

- [WebDreamer](https://openreview.net/forum?id=c6l7yA0HSq)
- [MobileDreamer](https://arxiv.org/abs/2601.04035)
- [Code2World](https://arxiv.org/abs/2602.09856)
- [DynaWeb](https://arxiv.org/abs/2601.22149)
- [SafePred](https://arxiv.org/abs/2602.01725)

Good research angles:

- predicting task-relevant future state rather than pixels,
- modeling irreversible actions before clicking,
- using generated future states for search, recovery, and risk scoring,
- learning compact state deltas that preserve action-relevant information.

### Recovery, Divergence Detection, And Temporal State Tracking

Core question: can an agent know that the current screen no longer matches the intended workflow?

- [BacktrackAgent](https://arxiv.org/abs/2505.20660)
- [VLAA-GUI](https://arxiv.org/abs/2604.21375)
- [GUI-explorer](https://aclanthology.org/2025.acl-long.282/)
- [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
- [Synapse](https://arxiv.org/abs/2306.07863)

Good research angles:

- compare expected and observed state transitions,
- detect off-track behavior before final failure,
- choose repair actions from temporal evidence,
- invalidate stale memory when the UI has drifted.

### Long-Horizon Visual Memory And Compression

Core question: how much visual history should the GUI agent keep?

- [ReVision](https://arxiv.org/abs/2605.11212)
- [GUI-KV](https://arxiv.org/abs/2510.00536)
- [STaR-KV](https://arxiv.org/abs/2606.01790)
- [Less is More](https://arxiv.org/abs/2507.03730)
- [ShowUI](https://github.com/showlab/ShowUI)
- [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
- [MAGNET](https://arxiv.org/abs/2601.19199)
- [A11y-Compressor](https://arxiv.org/abs/2605.00551)
- [SecAgent](https://arxiv.org/abs/2603.08533)

Good research angles:

- keyframe selection for repeated GUI states,
- temporal redundancy removal for screenshots and screen elements,
- storing visual memory as state deltas or workflow graphs,
- routing between raw pixels, parsed UI elements, OCR, DOM, and accessibility trees.

## Project Ideas That Match This Profile

1. **Video-to-trajectory parser for GUI agents**

   Convert screen recordings into action trajectories with action boundaries, action types, target coordinates, and state-delta summaries. The contribution is an inverse-dynamics pipeline and data-quality model, not another benchmark.

2. **Execution-video progress verifier**

   Train a VLM reward model that watches an agent run and predicts progress, failure, and the first harmful or useless step. This connects directly to process reward models and long-horizon GUI reliability.

3. **Temporal state-delta representation**

   Learn compact before/after GUI representations that explain what changed, what stayed stable, and whether the change is task-relevant. This can support grounding, recovery, reward modeling, and memory invalidation.

4. **Tutorial-video retrieval for GUI agents**

   Retrieve relevant tutorial segments or prior demonstrations at inference time, then convert them into action hints conditioned on the current screen. This uses video retrieval, temporal localization, and GUI grounding.

5. **Keyframe memory for long-horizon computer use**

   Replace full screenshot histories with selected keyframes, UI deltas, and persistent workflow summaries. The aim is lower token cost without losing recovery-critical evidence.


6. **Predictive safety from execution video**

   Use a future-state model or execution-video verifier to detect irreversible or privacy-sensitive trajectories before the agent continues.

## Practical Reading Order

First week:

1. VideoGUI
2. VideoWebArena
3. ShowUI
4. ShowUI-Aloha
5. Video-Based Reward Modeling for Computer-Use Agents

Second week:

1. VideoAgentTrek
2. Watch and Learn
3. CUA-Suite
4. BacktrackAgent
5. WebDreamer

Third week:

1. ProgRM
2. Web-Shepherd
3. GUI-KV
4. MobileDreamer
5. Code2World

After each paper, write one note that answers:

1. What temporal mechanism does the paper introduce?
2. What is observed: screenshot, video, DOM, accessibility tree, action trace, or execution log?
3. What action supervision or reward signal is used?
4. What failure mode would a video/VLM method help fix?
5. Which benchmarks are only evidence, not the research question?
