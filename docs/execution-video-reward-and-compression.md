# Execution-Video Reward And Video/History Compression

This note is a literature map for two related GUI-agent directions:

1. **Execution-video reward modeling**: judge whether a computer-use trajectory actually completed the user instruction by watching the execution video.
2. **Video/history compression for GUI agents**: compress long screenshot or screen-video histories into compact, action-relevant memory.

The file is intentionally a survey and reading guide, not a project proposal.

## Why This Direction

GUI agents repeatedly observe high-resolution screens. Long tasks create many redundant screenshots, but task success can depend on small localized events: a selected account, a hidden modal, a changed file name, a saved setting, or a transient error. This creates a tension:

- Full video/history is expensive and often redundant.
- Final screenshot is cheap but loses temporal evidence.
- Uniform frame sampling is simple but may miss sparse task-critical changes.
- Text summaries are cheap but may hallucinate or discard visual state.

For this cluster, the important comparison is whether a compression method preserves the evidence needed for reward, progress, or next-action judgment, not whether it reconstructs the original video.

## Reading Map

### A. Execution-Video Reward And Verification

| Paper | Date | Problem | Mechanism to extract |
| --- | --- | --- | --- |
| [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178) | Mar. 2026 | Final-state labels and script verifiers do not scale to open-ended CUA trajectories. | Treats an agent trajectory as execution keyframes and trains reward models to predict success from video evidence. |
| [CUARewardBench](https://arxiv.org/abs/2510.18596) | Oct. 2025 | Reward models for CUA lack systematic evaluation across outcome and process judgment. | Builds a benchmark for outcome reward models and process reward models on computer-use tasks. |
| [Web-Shepherd](https://arxiv.org/abs/2505.15277) | May 2025 | Web agents need fast step-level reward signals instead of expensive general MLLM judges. | Builds process reward models for web navigation trajectories and uses them for training/test-time guidance. |
| [ProgRM](https://arxiv.org/abs/2505.18121) | May 2025 | Outcome reward models cannot provide fine-grained progress supervision for GUI agents. | Uses progress rewards so intermediate GUI states can be scored by how much they advance the task. |
| [IntentScore](https://arxiv.org/abs/2604.05157) | Apr. 2026 | CUAs execute candidate actions without evaluating action quality under the user's plan. | Scores candidate actions with an intent-conditioned reward model trained on offline GUI interaction steps. |
| [GUIDE](https://arxiv.org/abs/2603.25864) | Mar. 2026 | GUI agents should understand and assist users in open-ended workflows, not only execute fixed tasks. | Provides user-intent and task-understanding evidence for judging GUI progress in open-ended screen activity. |

Takeaway: reward papers use temporal evidence, but they differ in whether the evidence is final-state, step-level, action-level, or video-level.

### B. Video Demonstrations And Action Evidence

| Paper | Date | Problem | Mechanism to extract |
| --- | --- | --- | --- |
| [CUA-Suite](https://arxiv.org/abs/2603.24440) | Mar. 2026 | High-quality continuous human screen-video demonstrations are scarce for CUA training. | Large-scale human-annotated desktop videos with grounding and execution traces. |
| [VideoAgentTrek](https://arxiv.org/abs/2510.19488) | Oct. 2025 | Public screen-recorded videos contain implicit demonstrations but no action labels. | Mines unlabeled videos and uses inverse dynamics to recover computer-use action supervision. |
| [Watch and Learn](https://arxiv.org/abs/2510.04673) | Oct. 2025 / CVPR 2026 | Agents need large-scale workflow data from ordinary online computer-use videos. | Converts internet videos into executable UI trajectories through video-to-action reasoning. |
| [ShowUI-Aloha](https://arxiv.org/abs/2601.07181) | Jan. 2026 | Human GUI recordings are long, unstructured, and hard to train from directly. | Turns in-the-wild screen recordings into structured tasks, actions, and agent supervision. |
| [VideoGUI](https://proceedings.neurips.cc/paper_files/paper/2024/hash/804e757b7d7043c26701c3a313032101-Abstract-Datasets_and_Benchmarks_Track.html) | NeurIPS 2024 Datasets and Benchmarks | GUI automation from instructional videos requires temporal grounding between demonstrations and UI actions. | Evaluates whether an agent can use instructional video evidence to perform desktop GUI tasks. |
| [VideoWebArena](https://proceedings.iclr.cc/paper_files/paper/2025/hash/5b555804d495321df2e3208cc27f4fbc-Abstract-Conference.html) | ICLR 2025 | Web-agent tasks may require long-context video understanding before acting. | Adds video-conditioned web tasks where agents must retain procedural/factual evidence from videos. |

Takeaway: these works provide the raw material for temporal evidence, from human demonstrations to mined online videos and video-conditioned tasks.

### C. Video/History Compression And GUI Memory

| Paper | Date | Problem | Mechanism to extract |
| --- | --- | --- | --- |
| [ReVision](https://arxiv.org/abs/2605.11212) | May 2026 | Long CUA histories accumulate many redundant visual tokens, so adding history often fails to improve performance. | Trains MLLMs on trajectories where a learned patch selector removes visual patches that are redundant across consecutive screenshots. |
| [GUI-KV](https://arxiv.org/abs/2510.00536) | Oct. 2025 | Long GUI tasks make VLM inference slow, costly, and KV-cache memory-bound. | Compresses KV cache with spatio-temporal awareness of GUI attention and screenshot history. |
| [STaR-KV](https://arxiv.org/abs/2606.01790) | Jun. 2026 | GUI VLM KV caches grow linearly with interaction steps and can exceed practical GPU memory after only a few screenshots. | Uses spatio-temporal adaptive re-weighting for GUI-specific KV-cache compression. |
| [A11y-Compressor](https://arxiv.org/abs/2605.00551) | May 2026 | Accessibility-tree observations are redundant and lose spatial relationships when linearized. | Reconstructs visual context and removes redundant nodes to create compact accessibility-tree observations. |
| [Less is More](https://arxiv.org/abs/2507.03730) | Jul. 2025 | GUI agents suffer from unrelated elements in the current screen and redundant history context. | Uses context-aware simplification over element context and history context. |
| [SecAgent](https://arxiv.org/abs/2603.08533) | Mar. 2026 | Mobile GUI agents need efficient history representations and stronger non-English GUI data. | Compresses past actions into semantic context summaries for a small mobile GUI agent. |
| [MAGNET](https://arxiv.org/abs/2601.19199) | Jan. 2026 | Mobile GUI agents fail when app UIs update and old workflows become stale. | Uses memory-driven knowledge evolution with stationary and procedural memory. |
| [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html) | ICML 2025 | Agents rediscover recurring workflows instead of reusing past task structure. | Induces reusable workflow memories from prior trajectories and retrieves them during future tasks. |
| [A-Mem](https://arxiv.org/abs/2502.12110) | NeurIPS 2025 | General LLM agents need memory that evolves through organization, linking, and updating. | Builds an agentic memory network with Zettelkasten-style notes, dynamic indexing, link generation, and memory evolution. |
| [Synapse](https://arxiv.org/abs/2306.07863) | ICLR 2024 | Computer-control agents need past trajectories as useful in-context examples. | Retrieves trajectory exemplars and memory for computer-control prompting. |
| [Step-level Optimization for Efficient Computer-use Agents](https://arxiv.org/abs/2604.27151) | Apr. 2026 | Calling a strong multimodal model at every GUI step is too slow and expensive. | Uses monitors to decide when cheap policies are enough and when to escalate to stronger models. |

Takeaway: compression work is moving quickly, with methods targeting patches, KV cache, accessibility trees, element context, action history, and semantic memory.

## Recommended Reading Order

First pass:

1. [Video-Based Reward Modeling for Computer-Use Agents](https://arxiv.org/abs/2603.10178)
2. [ReVision](https://arxiv.org/abs/2605.11212)
3. [GUI-KV](https://arxiv.org/abs/2510.00536)
4. [A11y-Compressor](https://arxiv.org/abs/2605.00551)
5. [ProgRM](https://arxiv.org/abs/2505.18121)
6. [CUARewardBench](https://arxiv.org/abs/2510.18596)

Second pass:

1. [CUA-Suite](https://arxiv.org/abs/2603.24440)
2. [VideoAgentTrek](https://arxiv.org/abs/2510.19488)
3. [Watch and Learn](https://arxiv.org/abs/2510.04673)
4. [ShowUI-Aloha](https://arxiv.org/abs/2601.07181)
5. [Less is More](https://arxiv.org/abs/2507.03730)
6. [STaR-KV](https://arxiv.org/abs/2606.01790)

Third pass:

1. [IntentScore](https://arxiv.org/abs/2604.05157)
2. [SecAgent](https://arxiv.org/abs/2603.08533)
3. [MAGNET](https://arxiv.org/abs/2601.19199)
4. [Agent Workflow Memory](https://proceedings.mlr.press/v267/wang25bx.html)
5. [A-Mem](https://arxiv.org/abs/2502.12110)
6. [Step-level Optimization for Efficient Computer-use Agents](https://arxiv.org/abs/2604.27151)

## What To Record In Paper Notes

For every paper in this cluster, record:

- Input evidence: screenshot, video, action log, OCR, DOM, a11y tree, or hidden state.
- Compression target: frames, patches, UI elements, KV cache, text summary, memory slots, or action candidates.
- Reward/progress signal: final success, process label, verifier score, human label, environment check, or contrastive candidate ranking.
- What must not be compressed away.
- Evaluation budget: frames, visual tokens, KV size, context length, latency, or dollar cost.
- Whether the method is usable with frozen VLMs or requires training a GUI foundation model.
