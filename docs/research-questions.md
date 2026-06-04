# Research Questions Beyond Benchmark Building

We are not looking for a new benchmark as the main contribution. We are looking for GUI-related research questions. Benchmarks enter later as experimental evidence.

Use [gui-paper-landscape.md](gui-paper-landscape.md) as the main map of paper families.

## Principle

Start from a GUI-agent mechanism:

- representation,
- grounding,
- action modeling,
- planning,
- recovery,
- memory,
- training signal,
- reward,
- safety,
- human interaction,
- systems efficiency.

Then ask which existing benchmark or small controlled test can evaluate it.

Do not start from "OSWorld is popular, what can we do on OSWorld?"

## Research Direction 1: State-Aware Recovery

Claim shape:

GUI agents need explicit recovery policies, not just stronger first-step action prediction.

Research questions:

- Can a model detect that the current GUI state is inconsistent with the intended workflow?
- Can it classify the right repair action: undo, retry, navigate back, search, ask user, or abandon?
- Can failed trajectories be converted into supervision for recovery?

Why this is not a benchmark paper:

The contribution is a recovery mechanism and training/evaluation protocol. Existing tasks only provide environments where failures happen.

Likely paper families:

- Planning, recovery, and state tracking.
- RL/reward models.
- Human confirmation if recovery is risky.

## Research Direction 2: Progress Rewards From GUI State Deltas

Claim shape:

GUI agents can learn better from state-delta progress signals than from sparse final success or generic LLM judges.

Research questions:

- Can we infer task progress from UI state changes?
- Can milestones be discovered automatically from successful trajectories?
- Can progress rewards distinguish "looks plausible" from "actually moved task forward"?

Why this is not a benchmark paper:

The contribution is a reward/verification method. Benchmarks only supply trajectories and final success labels.

Likely paper families:

- RL, reward models, and self-improvement.
- Training data and trajectory generation.

## Research Direction 3: GUI Representation Selection

Claim shape:

No single GUI representation is best; agents need adaptive representation selection.

Research questions:

- When is screenshot-only enough?
- When does accessibility tree, DOM, XML, OCR, or screen parsing help?
- Can an agent request a more expensive representation only when uncertainty is high?

Why this is not a benchmark paper:

The contribution is a representation-routing policy and analysis of representation failure modes.

Likely paper families:

- GUI representation and screen understanding.
- Efficient computer use.
- Hybrid GUI + structured tool use.

## Research Direction 4: Interface Routing Between GUI And Tools

Claim shape:

Reliable computer-use agents should route between GUI actions and structured tools based on risk, cost, and observability.

Research questions:

- When should an agent click versus use DOM, API, shell, or app shortcuts?
- Can a router learn from successful human/agent traces?
- How do we prevent tool use from overreaching user intent?

Why this is not a benchmark paper:

The contribution is an action-interface policy. Existing web/desktop/enterprise tasks are just evaluation substrates.

Likely paper families:

- Hybrid GUI + structured tool use.
- Safety and trust boundaries.
- Planning and recovery.

## Research Direction 5: Trust-Boundary-Aware GUI Agents

Claim shape:

GUI agents need to know which screen contents are instructions, evidence, app state, or adversarial environmental text.

Research questions:

- Can an agent label provenance and authority of observed text/UI elements?
- Can policy block actions whose justification comes from untrusted environmental content?
- Can visual layout attacks be handled without relying only on text filtering?

Why this is not a benchmark paper:

The contribution is a trust-boundary representation and runtime policy. Safety benchmarks are used to test it.

Likely paper families:

- Safety, security, and trust boundaries.
- GUI representation and screen understanding.
- Human confirmation and interruptibility.

## Research Direction 6: Memory Invalidation

Claim shape:

GUI-agent memory is only useful if the agent can tell when a remembered workflow is stale or unsafe.

Research questions:

- Can an agent detect UI drift or state mismatch before replaying a remembered workflow?
- What memory representation is easiest to invalidate: trajectory, state graph, skill, or natural-language recipe?
- Can memory retrieval be conditioned on screen-state similarity instead of only instruction similarity?

Why this is not a benchmark paper:

The contribution is memory validity and retrieval. Repeated-task environments only help evaluate it.

Likely paper families:

- Memory, skills, and personalization.
- Planning and recovery.
- Safety and privacy.

## Research Direction 7: Data Valuation For GUI Trajectories

Claim shape:

The quality of GUI trajectories matters more than raw scale, and trajectory quality can be estimated automatically.

Research questions:

- Which trajectory features predict training usefulness?
- Are branch points more valuable than full action histories?
- Can contrastive wrong-but-plausible actions improve robustness?
- Can trajectory filters reduce unsafe or inefficient behavior?

Why this is not a benchmark paper:

The contribution is a data selection/scoring method. Benchmarks provide downstream validation.

Likely paper families:

- Training data and trajectory generation.
- RL, reward models, and self-improvement.

## Research Direction 8: Efficient Perception And Model Routing

Claim shape:

GUI agents should adapt perception and model cost to task uncertainty.

Research questions:

- Can we route easy steps to small grounding/action models and hard steps to frontier VLMs?
- Can screen parsing or region selection reduce token cost while preserving reliability?
- Can the agent decide when to re-perceive versus reuse cached screen state?

Why this is not a benchmark paper:

The contribution is an efficiency-reliability mechanism. Existing benchmarks measure task success under budget constraints.

Likely paper families:

- GUI representation and screen understanding.
- Action models and GUI-VLA agents.
- Systems efficiency.

## Research Direction 9: Human Confirmation Policy

Claim shape:

GUI agents need confirmation policies that are risk-sensitive, not fixed prompts before every sensitive action.

Research questions:

- Which action/state features predict irreversible or high-risk outcomes?
- Can the agent ask compact, evidence-grounded confirmation questions?
- How does confirmation timing affect task success and user burden?

Why this is not a benchmark paper:

The contribution is a policy and interaction protocol. Safety tasks and user studies evaluate it.

Likely paper families:

- Human-agent interaction.
- Safety and trust boundaries.
- Planning and recovery.

## Most Promising Shortlist

1. **Trust-boundary-aware GUI agents**: strong safety angle, clear gap beyond ordinary prompt injection.
2. **Progress rewards from GUI state deltas**: connects method, training, and reliability.
3. **Interface routing between GUI and tools**: important for real systems and less saturated than benchmark work.
4. **State-aware recovery**: practical and directly addresses long-horizon failure.
5. **Efficient perception/model routing**: testable without training giant models.

Next action:

Pick one direction and write a one-page project memo:

- problem,
- core claim,
- related paper family,
- proposed mechanism,
- minimal experiment,
- likely benchmarks,
- baselines,
- risk,
- target venue.
