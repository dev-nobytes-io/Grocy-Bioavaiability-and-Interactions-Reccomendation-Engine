#!/usr/bin/env python3
"""Validate every Mermaid diagram in the repository's Markdown files.

Each ```mermaid fenced block is rendered with the Mermaid CLI (mmdc). A block
that fails to render fails the check, with its file and line number.

Usage:
    python3 scripts/check_mermaid.py [paths...]

Requirements:
    npm install -g @mermaid-js/mermaid-cli
    A Chromium or Chrome browser. Set PUPPETEER_EXECUTABLE_PATH if puppeteer
    did not download one.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / ".github" / "mermaid" / "puppeteer-config.json"
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "data"}
FENCE_OPEN = re.compile(r"^(\s*)(```|~~~)\s*mermaid\s*$")


def markdown_files(paths: list[str]) -> list[Path]:
    if paths:
        return [Path(p).resolve() for p in paths]
    files = []
    for path in ROOT.rglob("*.md"):
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            files.append(path)
    return sorted(files)


def extract_blocks(path: Path) -> list[tuple[int, str]]:
    blocks = []
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        match = FENCE_OPEN.match(lines[i])
        if match:
            fence = match.group(2)
            start = i + 1
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(fence):
                body.append(lines[i])
                i += 1
            blocks.append((start, "\n".join(body) + "\n"))
        i += 1
    return blocks


def render(block: str, workdir: Path, index: int) -> tuple[bool, str]:
    source = workdir / f"diagram-{index}.mmd"
    target = workdir / f"diagram-{index}.svg"
    source.write_text(block, encoding="utf-8")
    command = ["mmdc", "-q", "-i", str(source), "-o", str(target), "-p", str(CONFIG)]
    result = subprocess.run(command, capture_output=True, text=True, timeout=120)
    ok = result.returncode == 0 and target.exists() and target.stat().st_size > 0
    message = (result.stderr or result.stdout).strip()
    return ok, message


def main() -> int:
    if shutil.which("mmdc") is None:
        print("mmdc not found. Install with: npm install -g @mermaid-js/mermaid-cli", file=sys.stderr)
        return 2
    files = markdown_files(sys.argv[1:])
    total = 0
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        for path in files:
            for line, block in extract_blocks(path):
                total += 1
                ok, message = render(block, workdir, total)
                rel = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
                if ok:
                    print(f"ok    {rel}:{line}")
                else:
                    first = next((l for l in message.splitlines() if l.strip()), "render failed")
                    failures.append(f"{rel}:{line}: {first}")
                    print(f"FAIL  {rel}:{line}\n{message}\n", file=sys.stderr)
    print(f"\n{total - len(failures)} of {total} Mermaid diagrams rendered.")
    if failures:
        print("Failures:", *failures, sep="\n  ", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    os.environ.setdefault("PUPPETEER_EXECUTABLE_PATH", os.environ.get("CHROME_PATH", ""))
    if not os.environ["PUPPETEER_EXECUTABLE_PATH"]:
        del os.environ["PUPPETEER_EXECUTABLE_PATH"]
    sys.exit(main())
