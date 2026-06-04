# SeeClick

- **Year**: 2024
- **Paper**: SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents
- **Venue**: ACL 2024
- **Links**: https://aclanthology.org/2024.acl-long.505/, https://github.com/njucckevin/SeeClick
- **Tags**: `#grounding` `#benchmark` `#desktop` `#mobile` `#web`
- **Status**: `candidate`

## One-line Takeaway

SeeClick reframes visual GUI control around grounding: if an agent can reliably point to the right UI target from screenshots, many downstream GUI actions become easier.

## Problem

GUI agents often rely on HTML, XML, accessibility trees, or structured UI metadata. Those signals are not always available and do not generalize across desktop, web, and mobile. Screenshot-only control needs a model that can localize intended UI elements.

## Method

SeeClick introduces GUI grounding data curation and trains a visual GUI agent to map instructions and screenshots to UI targets. It also introduces ScreenSpot as a cross-platform grounding benchmark.

## Evidence To Verify

- How GUI grounding data is collected and filtered.
- ScreenSpot domains and metric definitions.
- Whether improvements transfer to downstream agent tasks.
- How SeeClick compares with general VLMs and later models such as OS-ATLAS, ShowUI, and Aguvis.

## Why It Matters To Us

This is a foundational grounding paper. It should be read before newer grounding-heavy papers, because many later works either improve its data recipe, benchmark against ScreenSpot, or argue that grounding is not the only bottleneck.

## Follow-ups

- [ ] Read paper and inspect ScreenSpot.
- [ ] Compare ScreenSpot, ScreenSpot-v2, ScreenSpot-Pro, and OSWorld-G.
- [ ] Add a model comparison table.
