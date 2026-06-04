# Agent S

- **Year**: 2025
- **Paper**: Agent S: An Open Agentic Framework that Uses Computers Like a Human
- **Venue**: ICLR 2025
- **Links**: https://proceedings.iclr.cc/paper_files/paper/2025/hash/394c7c30ea87b5c3521b4d9e9d419071-Abstract-Conference.html
- **Tags**: `#desktop` `#framework` `#planning` `#memory`
- **Status**: `candidate`

## One-line Takeaway

Agent S is a reference framework for desktop computer-use agents, combining an agent-computer interface with hierarchical planning and experience-augmented memory.

## Problem

Desktop CUA needs more than screenshots and clicks. Agents need an interface abstraction, planning hierarchy, online knowledge, and reusable experience.

## Method

The paper uses an Agent-Computer Interface, experience-augmented hierarchical planning, and memory mechanisms to support computer-use tasks.

## Evidence To Verify

- Exact observation/action interface.
- Memory format: narrative, episodic, procedural, or trajectory retrieval.
- OSWorld results and whether they use official splits.
- Transfer to WindowsAgentArena or other OS benchmarks.

## Why It Matters To Us

Agent S is important for architecture, not just scores. It should be a baseline mental model for how desktop agents are structured before adding RL or specialized grounding models.

## Follow-ups

- [ ] Read paper.
- [ ] Look for code/reproduction artifacts.
- [ ] Compare with UI-TARS Desktop and trycua/cua.
