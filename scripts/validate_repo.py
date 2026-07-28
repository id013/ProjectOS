#!/usr/bin/env python3
"""Validate the public ProjectOS repository without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".cff", ".txt"}
IGNORED_PARTS = {".git", ".venv", "node_modules"}
CYRILLIC = re.compile(r"[\u0400-\u04FF]")
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")


def public_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.suffix.lower() in PUBLIC_TEXT_SUFFIXES
        and not IGNORED_PARTS.intersection(path.parts)
    )


def validate_english_only(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for line_number, line in enumerate(text.splitlines(), start=1):
            if CYRILLIC.search(line):
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number}: "
                    "Cyrillic text is not allowed in the public repository"
                )
    return errors


def validate_markdown_links(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in (item for item in paths if item.suffix.lower() == ".md"):
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = match.group(1).strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("#", "http://", "https://", "mailto:")):
                continue
            file_target = unquote(target.split("#", 1)[0])
            resolved = (path.parent / file_target).resolve()
            if not resolved.exists():
                line_number = text.count("\n", 0, match.start()) + 1
                errors.append(
                    f"{path.relative_to(ROOT)}:{line_number}: "
                    f"broken local link: {target}"
                )
    return errors


def parse_frontmatter(path: Path) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    if len(lines) < 3 or lines[0] != "---":
        return {}, [f"{path.relative_to(ROOT)}: missing YAML frontmatter"]
    try:
        end = lines.index("---", 1)
    except ValueError:
        return {}, [f"{path.relative_to(ROOT)}: unclosed YAML frontmatter"]

    fields: dict[str, str] = {}
    for line_number, line in enumerate(lines[1:end], start=2):
        if not line.strip():
            continue
        if ":" not in line:
            errors.append(
                f"{path.relative_to(ROOT)}:{line_number}: invalid frontmatter field"
            )
            continue
        key, value = line.split(":", 1)
        fields[key.strip()] = value.strip().strip("\"'")
    return fields, errors


def validate_skill() -> list[str]:
    skill_file = ROOT / "skills" / "projectos" / "SKILL.md"
    if not skill_file.exists():
        return ["skills/projectos/SKILL.md: required skill is missing"]

    fields, errors = parse_frontmatter(skill_file)
    unexpected = sorted(set(fields) - {"name", "description"})
    if unexpected:
        errors.append(
            "skills/projectos/SKILL.md: unsupported frontmatter fields: "
            + ", ".join(unexpected)
        )
    if fields.get("name") != "projectos":
        errors.append("skills/projectos/SKILL.md: name must be 'projectos'")
    if not fields.get("description"):
        errors.append("skills/projectos/SKILL.md: description is required")
    return errors


def main() -> int:
    paths = public_files()
    errors = [
        *validate_english_only(paths),
        *validate_markdown_links(paths),
        *validate_skill(),
    ]
    if errors:
        print("ProjectOS validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    markdown_count = sum(path.suffix.lower() == ".md" for path in paths)
    print(
        f"ProjectOS validation passed: {len(paths)} public text files, "
        f"{markdown_count} Markdown files, English-only policy, links, and skill."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

