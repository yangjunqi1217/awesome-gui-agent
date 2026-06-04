#!/usr/bin/env python3
"""Extract paper-like resources from repository markdown files."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILES = [
    ROOT / "docs" / "academic-papers.md",
    ROOT / "README.md",
    ROOT / "docs" / "venue-index.md",
    ROOT / "roadmaps" / "video-vlm-to-gui-agent.md",
]

SKIP_HOSTS = (
    "github.com",
    "openai.com",
    "anthropic.com",
    "blog.google",
    "microsoft.com",
    "img.shields.io",
    "cdn.rawgit.com",
)

MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")


def clean_title(title: str) -> str:
    title = re.sub(r"\s+", " ", title).strip()
    return title.removeprefix("**").removesuffix("**").strip()


def looks_like_paper(title: str, url: str) -> bool:
    if any(host in url for host in SKIP_HOSTS):
        return False
    if title.lower().startswith(("arxiv", "website", "acl", "star")):
        return False
    return True


def section_for_line(text_before: str) -> str:
    headings = re.findall(r"^(#{2,3})\s+(.+)$", text_before, re.MULTILINE)
    if not headings:
        return ""
    return clean_title(headings[-1][1])


def extract() -> list[dict[str, str]]:
    seen: dict[str, dict[str, str]] = {}

    for path in SOURCE_FILES:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            title = clean_title(match.group(1))
            url = match.group(2).rstrip(".,")
            if not looks_like_paper(title, url):
                continue
            before = text[: match.start()]
            section = section_for_line(before)
            key = re.sub(r"\W+", " ", title).strip().lower()
            item = seen.setdefault(
                key,
                {
                    "title": title,
                    "url": url,
                    "sources": "",
                    "sections": "",
                },
            )
            sources = set(filter(None, item["sources"].split(";")))
            sections = set(filter(None, item["sections"].split(";")))
            sources.add(path.relative_to(ROOT).as_posix())
            if section:
                sections.add(section)
            item["sources"] = ";".join(sorted(sources))
            item["sections"] = ";".join(sorted(sections))

    return sorted(seen.values(), key=lambda x: (x["sections"], x["title"].lower()))


def main() -> None:
    print(json.dumps(extract(), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
