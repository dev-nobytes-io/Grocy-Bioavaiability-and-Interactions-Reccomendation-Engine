#!/usr/bin/env python3
"""Check that relative links and anchors in Markdown files resolve.

External links (http, https, mailto) are not fetched. Relative links must
point to a file or directory that exists. Anchors must match a heading in
the target file, using GitHub's heading-slug rules.

Usage:
    python3 scripts/check_links.py [paths...]
"""

from __future__ import annotations

import re
import sys
import unicodedata
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "data"}
LINK = re.compile(r"(?<!!)\[(?:[^\[\]]|\[[^\]]*\])*\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")


def markdown_files(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p).resolve() for p in paths]
    return sorted(
        p for p in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts)
    )


def strip_code(lines: list[str]) -> list[tuple[int, str]]:
    """Return (line number, text) for lines outside fenced code blocks, with inline code removed."""
    out = []
    in_fence = False
    for number, line in enumerate(lines, start=1):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            out.append((number, re.sub(r"`[^`]*`", "", line)))
    return out


def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "").replace("*", "").replace("_", "_")
    text = unicodedata.normalize("NFKC", text).lower()
    text = "".join(ch for ch in text if ch.isalnum() or ch in " -_")
    return text.replace(" ", "-")


@lru_cache(maxsize=None)
def anchors(path: Path) -> frozenset[str]:
    seen: dict[str, int] = {}
    result = set()
    for _, line in strip_code(path.read_text(encoding="utf-8").splitlines()):
        match = HEADING.match(line)
        if not match:
            continue
        slug = slugify(match.group(2))
        count = seen.get(slug, 0)
        result.add(slug if count == 0 else f"{slug}-{count}")
        seen[slug] = count + 1
    return frozenset(result)


def check(path: Path) -> list[str]:
    errors = []
    rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
    for number, line in strip_code(path.read_text(encoding="utf-8").splitlines()):
        for target in LINK.findall(line):
            if re.match(r"^[a-z][a-z0-9+.-]*:", target, re.I):
                continue
            file_part, _, anchor = target.partition("#")
            file_part = unquote(file_part.split("?", 1)[0])
            resolved = path if not file_part else (path.parent / file_part).resolve()
            if not resolved.exists():
                errors.append(f"{rel}:{number}: missing target {target}")
                continue
            if anchor and resolved.is_file() and resolved.suffix == ".md":
                if anchor.lower() not in anchors(resolved):
                    errors.append(f"{rel}:{number}: missing anchor #{anchor} in {file_part or rel}")
    return errors


def main() -> int:
    files = markdown_files(sys.argv[1:])
    errors = [error for path in files for error in check(path)]
    for error in errors:
        print(error, file=sys.stderr)
    print(f"Checked {len(files)} Markdown files: {len(errors)} broken relative links.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
