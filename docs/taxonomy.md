# GUI Agent Taxonomy

This is a working taxonomy for organizing reading notes. It should evolve as the field shifts.

## 1. Environment

- **Desktop OS**: Windows, macOS, Ubuntu/Linux, virtual machines, remote desktops.
- **Browser/Web**: realistic websites, enterprise web apps, browser automation, web-only actions.
- **Mobile**: Android and iOS-style app interaction, device APIs, small-screen constraints.
- **Professional software**: office suites, IDEs, design tools, scientific tools, high-resolution dense GUIs.
- **Hybrid Web-OS**: tasks that move across browser, files, system settings, local apps, and external services.

## 2. Observation Channel

- **Screenshot-only**: pure vision input, usually closest to human-facing GUI use.
- **Screenshot plus OCR/UI parsing**: detected text, icons, bounding boxes, element descriptions.
- **Accessibility tree / DOM / UI hierarchy**: structured interface state, useful but not always available.
- **Video/history**: temporal context, demonstrations, cursor traces, action histories.
- **Mixed observation**: screenshot plus browser DOM, app metadata, clipboard, file state, or API responses.

## 3. Action Space

- **Coordinate actions**: click, drag, type, scroll, hotkeys.
- **Element actions**: click a named DOM or accessibility node.
- **Programmatic actions**: shell, API, browser devtools, scripts, database actions.
- **Hybrid actions**: GUI control plus code/tool actions. Important for productivity, risky for evaluation comparability.

## 4. Core Capability

- **Grounding**: identify the correct UI target from instruction and screen.
- **Navigation**: move through screens, menus, pages, and app states.
- **Planning**: decompose long tasks into feasible GUI actions.
- **Recovery**: detect failure, backtrack, retry, and repair wrong state.
- **Memory**: remember user preferences, task context, app-specific procedures, credentials boundaries.
- **Generalization**: handle unseen apps, layouts, devices, languages, and task types.

## 5. Learning Signal

- **Prompting / inference-time reasoning**: no fine-tuning, model controls GUI through planning.
- **Supervised demonstrations**: trajectories, screenshots, actions, human traces.
- **Synthetic data**: generated screens, tasks, instructions, UI decompositions.
- **Reward models and RL/RLVR**: verifiable tasks, environment feedback, policy improvement.
- **Self-evolution**: agents collect experience, reflect, and improve behavior.

## 6. Evaluation

- **End-to-end task success**: whether the final state satisfies the user goal.
- **Step-level correctness**: whether each action is legal, relevant, and reversible.
- **Grounding accuracy**: element/coordinate localization.
- **Efficiency**: number of steps, time, cost, human interventions.
- **Robustness**: perturbations, unseen domains, layout changes, noisy observations.
- **Safety**: permission violations, privacy leakage, harmful actions, susceptibility to adversarial UI.

## 7. Safety Model

- **Action risk**: read-only, reversible edit, irreversible edit, purchase/payment, credential/security action.
- **Trust boundary**: user instruction, webpage content, app content, local files, remote services.
- **Confirmation policy**: when the agent must ask before acting.
- **Containment**: sandboxing, browser profile isolation, VM snapshots, file-system permissions.
- **Auditability**: logs, screenshots, trajectories, state diffs, provenance.

## 8. Notes Tags

Use these tags in notes:

- `#survey`
- `#benchmark`
- `#grounding`
- `#desktop`
- `#browser`
- `#mobile`
- `#safety`
- `#rl`
- `#data`
- `#tooling`
- `#product`
- `#reproduce`
- `#watch`
