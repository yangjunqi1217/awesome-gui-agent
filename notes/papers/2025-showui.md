# ShowUI

- **Year**: 2025
- **Paper**: ShowUI: One Vision-Language-Action Model for GUI Visual Agent
- **Venue**: CVPR 2025
- **Links**: https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html, https://github.com/showlab/ShowUI
- **Tags**: `#model` `#grounding` `#mobile` `#web`
- **Status**: `candidate`

## One-line Takeaway

ShowUI proposes a vision-language-action model for GUI agents, emphasizing efficient screenshot perception and action-history modeling.

## Problem

GUI screenshots are dense, and naive full-image processing is expensive. Agents also need to condition on prior actions and observations rather than make isolated single-step predictions.

## Method

ShowUI uses UI-guided visual token selection and interleaved vision-language-action streaming to build a more efficient GUI visual agent.

## Evidence To Verify

- What data is used for grounding and action training.
- How action history is represented.
- Which benchmarks show transfer across web and mobile.
- Runtime and token-efficiency gains from UI-guided token selection.

## Why It Matters To Us

ShowUI is a strong reference for efficient VLA-style GUI agents and connects academic grounding work to practical agent inference constraints.

## Follow-ups

- [ ] Read paper.
- [ ] Inspect model/repo availability.
- [ ] Compare with OS-ATLAS, Aguvis, and UI-TARS.
