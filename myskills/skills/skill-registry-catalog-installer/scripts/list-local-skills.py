#!/usr/bin/env python3
"""List installable skills from the local SkillRegistry workspace."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path

ALLOWED_ROOTS = ("temp/skills", "myskills/skills", "vendors/skills")


@dataclass
class Entry:
    name: str
    description: str
    install_name: str
    source_root: str
    source_path: str
    installed: bool


def _strip_quotes(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def _parse_frontmatter(skill_md: Path) -> tuple[str | None, str | None]:
    try:
        lines = skill_md.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None, None

    if not lines or lines[0].strip() != "---":
        return None, None

    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = _strip_quotes(value.strip())

    return data.get("name"), data.get("description")


def _resolve_workspace_root(raw_root: str | None) -> Path:
    if raw_root:
        return Path(raw_root).expanduser().resolve()

    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            check=True,
            capture_output=True,
            text=True,
        )
        return Path(result.stdout.strip()).resolve()
    except (OSError, subprocess.CalledProcessError):
        return Path.cwd().resolve()


def _resolve_dest_root(raw_dest: str | None, workspace_root: Path) -> Path:
    if not raw_dest:
        return workspace_root / ".codex/skills"

    dest = Path(raw_dest).expanduser()
    if dest.is_absolute():
        return dest.resolve()
    return (workspace_root / dest).resolve()


def _discover_entries(workspace_root: Path, dest_root: Path) -> list[Entry]:
    entries: list[Entry] = []

    for source_root in ALLOWED_ROOTS:
        root = workspace_root / source_root
        if not root.is_dir():
            continue

        for skill_md in root.rglob("SKILL.md"):
            skill_dir = skill_md.parent
            install_name = skill_dir.name
            name, description = _parse_frontmatter(skill_md)

            entries.append(
                Entry(
                    name=name or install_name,
                    description=description or "",
                    install_name=install_name,
                    source_root=source_root,
                    source_path=skill_dir.relative_to(workspace_root).as_posix(),
                    installed=(dest_root / install_name).is_dir(),
                )
            )

    return sorted(entries, key=lambda entry: (entry.name.lower(), entry.source_path.lower()))


def _build_payload(workspace_root: Path, dest_root: Path, entries: list[Entry]) -> dict[str, object]:
    return {
        "workspace_root": str(workspace_root),
        "dest_root": str(dest_root),
        "entries": [asdict(entry) for entry in entries],
    }


def _print_text(payload: dict[str, object]) -> None:
    print(f"Workspace: {payload['workspace_root']}")
    print(f"Destination: {payload['dest_root']}")

    entries = payload["entries"]
    if not isinstance(entries, list) or not entries:
        print("No installable skills found.")
        return

    for idx, raw_entry in enumerate(entries, start=1):
        if not isinstance(raw_entry, dict):
            continue

        suffix = " (already installed)" if raw_entry.get("installed") else ""
        print(f"{idx}. {raw_entry.get('name', '')}{suffix}")
        print(f"   path: {raw_entry.get('source_path', '')}")
        print(f"   source: {raw_entry.get('source_root', '')}")
        description = str(raw_entry.get("description", "")).strip()
        if description:
            print(f"   description: {description}")


def _parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List local installable skills.")
    parser.add_argument("--workspace-root", help="Workspace root to scan")
    parser.add_argument(
        "--dest",
        help="Destination skills directory used for installed-state checks",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format",
    )
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = _parse_args(argv)
    workspace_root = _resolve_workspace_root(args.workspace_root)
    dest_root = _resolve_dest_root(args.dest, workspace_root)
    payload = _build_payload(
        workspace_root,
        dest_root,
        _discover_entries(workspace_root, dest_root),
    )

    if args.format == "json":
        print(json.dumps(payload, indent=2))
    else:
        _print_text(payload)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
