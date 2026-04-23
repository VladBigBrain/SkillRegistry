---
name: skill-registry-catalog-installer
description: Browse installable skills from temp/skills, myskills/skills, and vendors/skills in the current SkillRegistry workspace, show each entry separately with project-local install state, and delegate installation to skill-installer.
---

# Skill Registry Catalog Installer

Use this skill when the user wants to browse, choose, and install skills from the current local `SkillRegistry` workspace.

This skill is a local catalog and routing layer. It does not copy files directly. It must delegate installation to `skill-installer`.

## Source Of Truth

Use the current workspace checkout as the discovery source.

Search only these workspace roots:

- `temp/skills`
- `myskills/skills`
- `vendors/skills`

Only treat a directory as installable when it contains `SKILL.md`.

Keep each matching directory as its own catalog entry. Do not deduplicate by skill name.

Use the current workspace `.codex/skills` directory as the default install destination and as the source of truth for `already installed` checks. Do not use global `~/.codex/skills` unless the user explicitly asks for it.

## Helper Script

Use the bundled helper script for discovery:

```text
python3 scripts/list-local-skills.py --format json
```

The script:

- resolves the current workspace root
- scans `temp/skills`, `myskills/skills`, and `vendors/skills`
- parses `name` and `description` from each `SKILL.md` when available
- keeps duplicate names as separate entries
- marks installed state relative to the current workspace `.codex/skills`

If the user explicitly wants another install directory, pass it to the script with `--dest <path>` and use that same destination for installation.

## Required Behavior

1. Discover local skills from the current workspace, not from a GitHub listing.
2. Keep every discovered skill directory as a separate entry, even when names repeat.
3. Show the user, for each entry:
   - `name`
   - `description` when available
   - `source_path`
   - `source_root`
   - `already installed` when true
4. Ask the user which entries to install.
5. If the user names a skill that appears multiple times, ask for the item number or exact path. Do not guess.
6. Delegate confirmed installs to `skill-installer`.

## User Interaction

Use a short conversational flow.

### When the user asks what is available

Run the helper script, show separate entries, and then ask:

`Which skills would you like installed?`

### When the user names skills directly

Match the request against the listed entries.

If a name is missing, say so explicitly and ask for correction. Do not guess.

### When a selected name is ambiguous

Ask the user to choose by item number or repository path.

## Installation

After the user confirms the selected entries, delegate installation to `skill-installer`.

Use the GitHub repository `VladBigBrain/SkillRegistry` as the install source and the current workspace `.codex/skills` directory as the default destination.

Pass equivalent install inputs:

```text
--repo VladBigBrain/SkillRegistry
--path <relative-path-to-skill-directory>
--ref <ref>
--dest <workspace-root>/.codex/skills
```

Use `main` as the default ref unless the user explicitly requests another branch, tag, or commit.

The path must point to the skill directory, not to `SKILL.md`.

Examples:

```text
--repo VladBigBrain/SkillRegistry --path temp/skills/brainstorming --ref main --dest /path/to/workspace/.codex/skills
--repo VladBigBrain/SkillRegistry --path myskills/skills/business-discovery --ref main --dest /path/to/workspace/.codex/skills
--repo VladBigBrain/SkillRegistry --path vendors/skills/system/skill-installer --ref main --dest /path/to/workspace/.codex/skills
```

## Error Handling

Separate errors clearly.

### Catalog errors

Examples:

- workspace root could not be resolved
- listing failed
- `SKILL.md` could not be read

Explain what failed and stop only if the catalog cannot be built at all.

### Selection errors

Examples:

- requested skill name not found
- selected skill name matches multiple entries

In these cases, ask the next focused question. Do not guess.

### Installation errors

Preserve `skill-installer` errors as-is when possible, including cases like:

- destination already exists
- selected path is invalid
- GitHub fetch failed

If several installs were requested, report results per skill.

## Boundaries

Do:

- catalog skills
- scan `temp/skills`, `myskills/skills`, and `vendors/skills`
- show each matching skill directory as its own entry
- keep already installed entries visible
- explain available sources
- ask the user what to install
- resolve ambiguity by item number or path
- delegate installation

Do not:

- install by direct filesystem copy
- deduplicate entries by skill name
- edit repository structure
- merge duplicate skills
- write to global `~/.codex/skills` by default
- treat directories without `SKILL.md` as installable skills

## Completion

After successful installation, tell the user:

`Restart Codex to pick up new skills.`
