# Contributing

This is a curated Awesome list, not a raw paper dump. Additions should be resources we would actually recommend reading, reproducing, or citing.

## What Belongs In The Root README

Root README entries should be:

- directly relevant to GUI agents, computer-use agents, browser/mobile agents, UI grounding, GUI-agent safety, or CUA infrastructure;
- high-signal enough that we can explain why the resource is useful;
- described in one factual sentence ending with a period;
- linked to a canonical source such as the paper, project page, or repository.

Use this entry format:

```md
- [Name](https://example.com) - Short factual description explaining why it is useful.
```

Avoid adding:

- papers we have not sanity-checked;
- benchmark-only entries unless they are widely used as experimental substrates;
- duplicate links already covered by a better canonical source;
- vague descriptions like "important paper" or "great repo".

## Where To Put Broader Intake

- Use [`docs/academic-papers.md`](docs/academic-papers.md) for broader academic tracking.
- Use [`docs/industry-reports.md`](docs/industry-reports.md) for technical reports, product APIs, open-source systems, and guardrails.
- Use [`docs/method-paper-shortlist.md`](docs/method-paper-shortlist.md) for mechanism-first reading priority.
- Use [`docs/gui-paper-landscape.md`](docs/gui-paper-landscape.md) for paper families and research mechanisms.
- Use [`docs/research-questions.md`](docs/research-questions.md) for non-benchmark research directions.

Benchmarks should be recorded as evaluation substrates for method papers. Do not use benchmark names as the primary source of new research questions.

## Reading Notes

When we seriously read a resource:

1. Copy the relevant template from [`notes/templates/`](notes/templates/).
2. Save the note under `notes/papers/`, `notes/repos/`, or `notes/products/`.
3. Record the paper family, GUI representation, action representation, mechanism, evidence, limitations, and relevance to us.
4. Link the note from the relevant docs when it becomes central.

The value of the notes is judgment, not abstract rewriting.

## Metadata Hygiene

- Prefer official paper pages, conference pages, arXiv pages, project pages, or GitHub repositories.
- Mark uncertain venue/status claims as `verify` in docs.
- Keep root README descriptions short and stable.
- Do not commit ignored scrape caches under `sources/`.
