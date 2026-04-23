# Skill Registry Catalog Installer Design

## Summary

Refactor `skill-registry-catalog-installer` into a thin local UI wrapper over `skill-installer`.

The updated skill should:

- discover installable skills from the current repository checkout
- show every matching skill directory as a separate selectable entry
- mark installed state relative to the current project's `.codex/skills`
- delegate installation to the existing `skill-installer`

The new skill remains a router and catalog layer. It does not copy files itself and does not replace `skill-installer`.

## Context

The desired workflow is project-local, not global. Users want to choose skills from this repository and install them into the current project's `.codex/skills` directory instead of `~/.codex/skills`.

The relevant installable sources are:

- `temp/skills/**`
- `myskills/skills/**`
- `vendors/skills/**`

The existing `skill-installer` already knows how to install a skill from a GitHub repository path into a chosen destination via `--dest`, but it does not know how to present a local catalog for this workspace or compute installed state relative to the project's `.codex/skills`.

## Goals

- Build a local catalog from `temp/skills`, `myskills/skills`, and `vendors/skills`.
- Treat every directory containing `SKILL.md` as a separate entry.
- Keep duplicate skill names as separate entries when they come from different paths.
- Show installed state relative to the project-local `.codex/skills`.
- Delegate actual installation to `skill-installer` with an explicit project-local destination.

## Non-Goals

- Do not install by copying directly from the local filesystem.
- Do not modify `skill-installer` core install behavior.
- Do not deduplicate entries by skill name.
- Do not default to the global Codex skills directory.
- Do not expose directories that lack `SKILL.md` as installable skills.

## Discovery Model

The source of truth for listing is the current local checkout of this repository.

Discovery should scan only:

- `temp/skills`
- `myskills/skills`
- `vendors/skills`

Each directory containing `SKILL.md` becomes one catalog entry.

## Helper Script

The skill should use a bundled helper script for deterministic discovery and installed-state checks:

```text
python3 scripts/list-local-skills.py --format json
```

The script should:

- resolve the current workspace root
- default the install destination to `<workspace-root>/.codex/skills`
- scan the three allowed roots
- parse `name` and `description` from `SKILL.md`
- emit separate entries for duplicate names
- mark `installed` based on the project-local destination

## Catalog Model

Each entry should include:

- `name`
- `description`
- `install_name`
- `source_root`
- `source_path`
- `installed`

## Listing Behavior

The catalog shown to the user should be concise and selection-oriented.

Recommended shape:

- one visible item per discovered skill directory
- show duplicates as separate list items
- show path and source root so the user can choose the exact variant

Example shape:

```text
1. brainstorming
   path: temp/skills/brainstorming
   source: temp/skills

2. brainstorming (already installed)
   path: myskills/skills/brainstorming
   source: myskills/skills

3. skill-installer
   path: vendors/skills/system/skill-installer
   source: vendors/skills
```

## User Interaction

The skill should drive a short conversational selection flow:

1. Show the local catalog.
2. Ask which entries to install.
3. If a name matches multiple entries, ask for the item number or exact path.
4. Delegate the final selection to `skill-installer`.

## Delegation To Skill Installer

The skill is responsible for producing exact install inputs, not for implementing installation mechanics.

For each selected entry, it should delegate equivalent arguments to:

```text
--repo VladBigBrain/SkillRegistry
--path <relative-path>
--ref main
--dest <workspace-root>/.codex/skills
```

The relative path must point to the skill directory that contains `SKILL.md`, not to the markdown file itself. The default destination must stay project-local unless the user explicitly asks for another path.

## Error Handling

Separate errors into discovery, selection, and installation stages. Preserve `skill-installer` errors as-is when possible. If several installs were requested, report results per entry.

## Boundaries

The skill is intentionally narrow:

- it catalogs local skills
- it asks
- it resolves ambiguity by item number or path
- it delegates installation

It does not:

- perform direct filesystem installation
- repair repository structure
- edit or merge duplicate skill directories
- use global `~/.codex/skills` as the default destination

## Testing Strategy

The first implementation should be validated against the following scenarios:

1. Listing includes entries from `temp/skills`, `myskills/skills`, and `vendors/skills`.
2. Duplicate names appear as separate entries.
3. Installed state is computed from the project-local `.codex/skills`.
4. Installation delegates to `skill-installer` with explicit `--dest`.
5. Ambiguous name-only requests trigger a follow-up asking for item number or path.
6. Directories without `SKILL.md` are ignored.

## Final Recommendation

Implement the new skill as a local repository browser and installer wrapper in front of `skill-installer`.

This keeps one installation mechanism, makes duplicate entries visible, and matches the project-local workflow the user asked for.
