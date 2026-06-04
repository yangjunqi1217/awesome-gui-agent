#!/usr/bin/env python3
"""Build docs/paper-summaries.md from the repository paper inventory.

The script intentionally stores short summary notes, not full abstracts. It uses
official or canonical source pages when possible and marks unresolved items.
"""

from __future__ import annotations

import html
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import OrderedDict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from extract_paper_inventory import ROOT, extract  # noqa: E402


OUT = ROOT / "docs" / "paper-summaries.md"
CACHE = ROOT / ".cache" / "paper_summaries_cache.json"

UA = "awesome-gui-agent-summary-builder/0.1 (metadata extraction; contact via repo)"
TIMEOUT = 8

STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "how",
    "in",
    "is",
    "it",
    "its",
    "large",
    "llm",
    "llms",
    "model",
    "models",
    "multimodal",
    "of",
    "on",
    "or",
    "paper",
    "the",
    "their",
    "this",
    "to",
    "towards",
    "using",
    "via",
    "with",
}

SECTION_ORDER = [
    "GUI Agent Surveys",
    "Surveys And Field Framing",
    "Foundations Before The Current GUI-Agent Wave",
    "GUI Representation & Grounding",
    "Models & Agents",
    "Models, Grounding, And Agent Architectures",
    "Planning, Recovery & Memory",
    "Training, RL & Reward Models",
    "Video Demonstrations & Trajectories",
    "Evaluation Papers And Experimental Substrates",
    "Safety & Trust",
    "Safety, Security, And Trustworthiness",
    "Active Preprint / Watchlist Cluster",
]


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, str] = {}
        self.title = ""
        self._in_title = False
        self._title_parts: list[str] = []
        self.text_parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k.lower(): v or "" for k, v in attrs}
        if tag in {"script", "style", "nav", "footer"}:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True
        if tag == "meta":
            key = (
                attrs_dict.get("name")
                or attrs_dict.get("property")
                or attrs_dict.get("itemprop")
                or ""
            ).lower()
            content = attrs_dict.get("content", "")
            if key and content:
                self.meta[key] = html.unescape(content).strip()

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav", "footer"} and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title":
            self._in_title = False
            self.title = clean_text(" ".join(self._title_parts))

    def handle_data(self, data: str) -> None:
        if self._in_title:
            self._title_parts.append(data)
        if not self._skip_depth:
            text = clean_text(data)
            if text:
                self.text_parts.append(text)


def clean_text(text: str) -> str:
    text = html.unescape(text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"^Abstract\s+", "", text)
    return text.strip()


def load_cache() -> dict[str, dict[str, str]]:
    if CACHE.exists():
        return json.loads(CACHE.read_text(encoding="utf-8"))
    return {}


def save_cache(cache: dict[str, dict[str, str]]) -> None:
    CACHE.parent.mkdir(exist_ok=True)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")


def fetch_url(url: str) -> str:
    response = requests.get(url, headers={"User-Agent": UA}, timeout=TIMEOUT)
    response.raise_for_status()
    return response.text


def arxiv_abs_url(url: str) -> str | None:
    parsed = urlparse(url)
    if "arxiv.org" not in parsed.netloc:
        return None
    match = re.search(r"/(?:abs|pdf)/([0-9]{4}\.[0-9]{4,5})(?:v\d+)?", parsed.path)
    if not match:
        return None
    return f"https://arxiv.org/abs/{match.group(1)}"


def fetch_arxiv(url: str) -> dict[str, str]:
    abs_url = arxiv_abs_url(url)
    if not abs_url:
        return {}
    text = fetch_url(abs_url)
    parser = MetaParser()
    parser.feed(text)
    abstract = parser.meta.get("citation_abstract", "")
    title = parser.meta.get("citation_title", "")
    if not abstract:
        m = re.search(
            r'<blockquote class="abstract[^"]*">\s*<span[^>]*>Abstract:</span>\s*(.*?)\s*</blockquote>',
            text,
            re.S,
        )
        if m:
            abstract = re.sub(r"<[^>]+>", " ", m.group(1))
    return {
        "title": clean_text(title),
        "abstract": clean_text(abstract),
        "source_url": abs_url,
        "source_type": "arXiv",
    }


def fetch_openreview(url: str) -> dict[str, str]:
    parsed = urlparse(url)
    if "openreview.net" not in parsed.netloc:
        return {}
    forum = parse_qs(parsed.query).get("id", [""])[0]
    if not forum:
        return {}
    api_url = f"https://api2.openreview.net/notes?forum={forum}"
    data = requests.get(api_url, headers={"User-Agent": UA}, timeout=TIMEOUT).json()
    for note in data.get("notes", []):
        content = note.get("content", {})
        title = unwrap_openreview_value(content.get("title"))
        abstract = unwrap_openreview_value(content.get("abstract"))
        if title and abstract:
            return {
                "title": clean_text(title),
                "abstract": clean_text(abstract),
                "source_url": url,
                "source_type": "OpenReview",
            }
    return {}


def unwrap_openreview_value(value: object) -> str:
    if isinstance(value, dict):
        inner = value.get("value")
        if isinstance(inner, str):
            return inner
    if isinstance(value, str):
        return value
    return ""


def extract_generic(url: str) -> dict[str, str]:
    text = fetch_url(url)
    parser = MetaParser()
    parser.feed(text)
    meta = parser.meta
    title = (
        meta.get("citation_title")
        or meta.get("dc.title")
        or meta.get("og:title")
        or parser.title
    )
    abstract = (
        meta.get("citation_abstract")
        or extract_structured_abstract(text)
        or meta.get("twitter:description")
        or meta.get("description")
        or meta.get("og:description")
        or ""
    )
    if not abstract:
        abstract = find_abstract_in_text(parser.text_parts)
    if not is_valid_abstract(abstract):
        abstract = ""
    return {
        "title": clean_text(title),
        "abstract": clean_text(abstract),
        "source_url": url,
        "source_type": source_type(url),
    }


def find_abstract_in_text(parts: list[str]) -> str:
    for idx, part in enumerate(parts):
        if part.lower() == "abstract":
            return clean_text(" ".join(parts[idx + 1 : idx + 8]))
        if part.lower().startswith("abstract "):
            return clean_text(part[9:])
    return ""


def extract_structured_abstract(text: str) -> str:
    patterns = [
        r'<div[^>]+id=["\']abstract["\'][^>]*>(.*?)</div>',
        r'<div[^>]+class=["\'][^"\']*abstract[^"\']*["\'][^>]*>(.*?)</div>',
        r'<p[^>]+class=["\'][^"\']*abstract[^"\']*["\'][^>]*>(.*?)</p>',
        r'abstract\s*=\s*(?:&#34;|")(.+?)(?:&#34;|")',
        r'abstract\s*=\s*\{(.+?)\}',
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.I | re.S)
        if match:
            candidate = clean_text(match.group(1))
            if is_valid_abstract(candidate):
                return candidate
    return ""


def is_valid_abstract(text: str) -> bool:
    text = clean_text(text)
    if len(text) < 120:
        return False
    bad_fragments = [
        "proceedings of the",
        "electronic proceedings",
        "association for computational linguistics",
        "international conference on machine learning",
    ]
    if any(fragment in text.lower() for fragment in bad_fragments) and len(text) < 350:
        return False
    comma_count = text[:220].count(",")
    if comma_count >= 6 and "." in text[:220]:
        return False
    if re.search(r"^[A-Z][a-z]+ [A-Z][a-z]+,\s+[A-Z][a-z]+", text):
        return False
    return True


def source_type(url: str) -> str:
    host = urlparse(url).netloc
    if "aclanthology" in host:
        return "ACL Anthology"
    if "proceedings.mlr.press" in host:
        return "PMLR"
    if "proceedings.iclr.cc" in host:
        return "ICLR Proceedings"
    if "proceedings.neurips.cc" in host:
        return "NeurIPS Proceedings"
    if "openaccess.thecvf.com" in host:
        return "CVF Open Access"
    if "ijcai.org" in host:
        return "IJCAI Proceedings"
    if "eccv.ecva.net" in host:
        return "ECCV Proceedings"
    if "dl.acm.org" in host:
        return "ACM Digital Library"
    if "doi.org" in host:
        return "DOI"
    if "ojs.aaai.org" in host:
        return "AAAI Proceedings"
    return host


def fetch_metadata(url: str) -> dict[str, str]:
    parsed = urlparse(url)
    if "doi.org" in parsed.netloc or "dl.acm.org" in parsed.netloc:
        return {
            "title": "",
            "abstract": "",
            "source_url": url,
            "source_type": source_type(url),
            "error": "Skipped during automated extraction; use DOI/ACM page manually.",
        }
    if "arxiv.org" in url:
        return fetch_arxiv(url)
    if "openreview.net" in url:
        return fetch_openreview(url)
    return extract_generic(url)


def is_good_meta(meta: dict[str, str]) -> bool:
    return bool(is_valid_abstract(meta.get("abstract", "")))


def canonical_key(item: dict[str, str]) -> str:
    url = item["url"]
    arxiv_url = arxiv_abs_url(url)
    if arxiv_url:
        return arxiv_url
    parsed = urlparse(url)
    if "openreview.net" in parsed.netloc:
        forum = parse_qs(parsed.query).get("id", [""])[0]
        return f"openreview:{forum}" if forum else url
    if "doi.org" in parsed.netloc:
        return parsed.path.lower().strip("/")
    return url.rstrip("/")


def prefer_title(a: str, b: str) -> str:
    if len(b) > len(a) and not re.match(r"^[A-Z0-9-]+$", b):
        return b
    return a


def dedupe_inventory() -> list[dict[str, str]]:
    items: OrderedDict[str, dict[str, str]] = OrderedDict()
    for item in extract():
        key = canonical_key(item)
        if key not in items:
            items[key] = dict(item)
            items[key]["url"] = key if key.startswith("https://arxiv.org/abs/") else item["url"]
            continue
        current = items[key]
        current["title"] = prefer_title(current["title"], item["title"])
        current["sources"] = ";".join(
            sorted(set(current["sources"].split(";")) | set(item["sources"].split(";")))
        )
        current["sections"] = ";".join(
            sorted(set(current["sections"].split(";")) | set(item["sections"].split(";")))
        )
    return list(items.values())


def read_existing_descriptions() -> dict[str, str]:
    descriptions: dict[str, str] = {}
    academic = ROOT / "docs" / "academic-papers.md"
    if academic.exists():
        for line in academic.read_text(encoding="utf-8").splitlines():
            if not (line.startswith("| ") and "](" in line and not line.startswith("| ---")):
                continue
            match = re.search(r"\[([^\]]+)\]\((https?://[^)]+)\)", line)
            if not match:
                continue
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) >= 5:
                url = match.group(2).rstrip("/")
                descriptions[url] = cells[-1].strip()
                arxiv = arxiv_abs_url(url)
                if arxiv:
                    descriptions[arxiv] = cells[-1].strip()
    return descriptions


def words(text: str) -> list[str]:
    return [w for w in re.findall(r"[A-Za-z][A-Za-z0-9-]+", text.lower()) if w not in STOPWORDS]


def classify_focus(title: str, abstract: str, sections: str) -> str:
    section_lower = sections.lower()
    if "survey" in section_lower:
        return "Survey / field framing"
    if "safety" in section_lower:
        return "Safety / trust"
    if "video" in section_lower:
        return "Video demonstrations"
    if "training, rl" in section_lower or "reward" in section_lower:
        return "RL / reward learning"
    if "planning" in section_lower or "recovery" in section_lower or "memory" in section_lower:
        return "Planning / recovery / memory"
    if "evaluation" in section_lower or "substrates" in section_lower:
        return "Benchmark / evaluation"
    if "representation" in section_lower or "grounding" in section_lower:
        return "Grounding / perception"
    if "models" in section_lower or "architectures" in section_lower:
        return "Model / agent architecture"

    combined = f"{title} {abstract} {sections}".lower()
    checks = [
        ("Survey / field framing", ["survey", "taxonomy", "review"]),
        ("Safety / trust", ["safety", "attack", "adversarial", "privacy", "jailbreak", "privilege", "guardrail", "harm"]),
        ("Video demonstrations", ["video", "screen recording", "tutorial", "demonstration"]),
        ("RL / reward learning", ["reinforcement", "reward", "rl", "self-evolving", "online curriculum"]),
        ("Grounding / perception", ["grounding", "grounded", "screen", "ui understanding", "perception", "localize", "vision-language"]),
        ("Planning / recovery / memory", ["planning", "memory", "backtracking", "explore", "world model", "trajectory", "workflow"]),
        ("Benchmark / evaluation", ["benchmark", "dataset", "evaluating", "testbed", "arena"]),
        ("Model / agent architecture", ["agent", "model", "framework", "computer-use", "gui automation"]),
    ]
    for label, needles in checks:
        if any(n in combined for n in needles):
            return label
    return "General GUI-agent resource"


def first_sentence(text: str) -> str:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", text)
    for part in parts:
        part = clean_text(part)
        if len(part) >= 45:
            return part
    return clean_text(text[:240])


def synthesize_summary(title: str, abstract: str, sections: str, fallback: str = "") -> str:
    if not abstract:
        if fallback:
            focus = classify_focus(title, fallback, sections)
            return f"{fallback} Needs abstract verification against the canonical source. Focus: {focus}."
        return "Summary pending: the canonical page did not expose an abstract during metadata extraction."

    focus = classify_focus(title, abstract, sections)
    sentences = [clean_text(s) for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", abstract)]
    sentences = [s for s in sentences if len(s) >= 45]
    sentence = sentences[0] if sentences else first_sentence(abstract)
    second = ""
    for candidate in sentences[1:]:
        lower = candidate.lower()
        if any(k in lower for k in ["introduce", "propose", "present", "construct", "build", "evaluate", "benchmark", "dataset", "framework", "agent"]):
            second = candidate
            break
    combined_sentence = sentence if not second else f"{sentence} {second}"
    if len(combined_sentence) > 420:
        combined_sentence = combined_sentence[:417].rstrip() + "..."

    lower = abstract.lower()
    contribution = ""
    if any(k in lower for k in ["introduce", "propose", "present", "build", "construct"]):
        contribution = "It is useful for tracking the paper's proposed method, dataset, or system design."
    elif any(k in lower for k in ["evaluate", "benchmark", "measure"]):
        contribution = "It is useful as evaluation evidence and for understanding task setup, metrics, and failure modes."
    elif "survey" in lower:
        contribution = "It is useful for field framing and for locating related papers."
    else:
        contribution = "It is useful for understanding this part of the GUI-agent stack."

    return f"{combined_sentence} {contribution}"


def section_rank(item: dict[str, str]) -> tuple[int, str]:
    sections = item.get("sections", "")
    for idx, section in enumerate(SECTION_ORDER):
        if section in sections:
            return idx, item["title"].lower()
    return len(SECTION_ORDER), item["title"].lower()


def metadata_for_inventory(
    inventory: list[dict[str, str]], cache: dict[str, dict[str, str]], offline: bool
) -> dict[str, dict[str, str]]:
    metadata: dict[str, dict[str, str]] = {}
    missing: list[dict[str, str]] = []

    for item in inventory:
        key = canonical_key(item)
        cached = cache.get(key)
        if cached and is_good_meta(cached):
            metadata[key] = cached
        elif offline:
            metadata[key] = {
                "title": item["title"],
                "abstract": "",
                "source_url": item["url"],
                "source_type": source_type(item["url"]),
                "error": "Offline build; abstract not fetched yet.",
            }
        else:
            missing.append(item)

    if offline or not missing:
        return metadata

    def fetch_item(item: dict[str, str]) -> tuple[str, dict[str, str]]:
        key = canonical_key(item)
        try:
            meta = fetch_metadata(item["url"])
            if not is_good_meta(meta):
                meta["abstract"] = ""
            return key, meta
        except Exception as exc:  # noqa: BLE001 - keep building.
            return key, {
                "title": item["title"],
                "abstract": "",
                "source_url": item["url"],
                "source_type": source_type(item["url"]),
                "error": str(exc),
            }

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(fetch_item, item) for item in missing]
        for future in as_completed(futures):
            key, meta = future.result()
            metadata[key] = meta
            if is_good_meta(meta):
                cache[key] = meta
                save_cache(cache)

    return metadata


def build(offline: bool = False) -> tuple[str, int, int]:
    inventory = dedupe_inventory()
    cache = load_cache()
    descriptions = read_existing_descriptions()
    metadata = metadata_for_inventory(inventory, cache, offline)
    rows = []
    failures = 0

    for idx, item in enumerate(inventory, 1):
        key = canonical_key(item)
        meta = metadata.get(key, {})
        if not meta.get("abstract"):
            failures += 1

        title = meta.get("title") or item["title"]
        abstract = clean_text(meta.get("abstract", ""))
        fallback = descriptions.get(item["url"].rstrip("/")) or descriptions.get(canonical_key(item), "")
        rows.append(
            {
                **item,
                "title": title,
                "abstract": abstract,
                "summary": synthesize_summary(title, abstract, item.get("sections", ""), fallback),
                "focus": classify_focus(title, abstract, item.get("sections", "")),
                "source_url": meta.get("source_url") or item["url"],
                "source_type": meta.get("source_type") or source_type(item["url"]),
                "error": meta.get("error", ""),
            }
        )

    rows.sort(key=section_rank)

    lines = [
        "# Paper Summaries",
        "",
        "This file gives an abstract-level summary for each paper-like resource tracked by the repository. It is a reading map, not a replacement for full paper notes.",
        "",
        "Method: entries are extracted from `README.md`, `docs/academic-papers.md`, `docs/venue-index.md`, and `roadmaps/`; summaries are generated from canonical abstracts or page metadata when available. Items whose official page did not expose an abstract are marked as pending.",
        "",
        "| Paper | Focus | Abstract-level summary | Source | Repo locations |",
        "| --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        locations = ", ".join(f"`{src}`" for src in sorted(set(row["sources"].split(";"))))
        source = f"[{row['source_type']}]({row['source_url']})"
        title = row["title"].replace("|", "\\|")
        focus = row["focus"].replace("|", "\\|")
        summary = row["summary"].replace("|", "\\|")
        lines.append(f"| [{title}]({row['source_url']}) | {focus} | {summary} | {source} | {locations} |")

    pending = [row for row in rows if not row["abstract"]]
    if pending:
        lines.extend(
            [
                "",
                "## Pending Abstract Verification",
                "",
                "These entries stayed in the map, but the script could not extract an abstract from the official page. They need manual reading or a better source URL.",
                "",
            ]
        )
        for row in pending:
            err = f" Error: `{row['error']}`." if row.get("error") else ""
            lines.append(f"- [{row['title']}]({row['source_url']}) - {row['source_type']}.{err}")

    content = "\n".join(lines) + "\n"
    return content, len(rows), failures


def main() -> None:
    offline = "--offline" in sys.argv
    content, total, failures = build(offline=offline)
    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT.relative_to(ROOT)} with {total} entries; {failures} extraction gaps.")


if __name__ == "__main__":
    main()
