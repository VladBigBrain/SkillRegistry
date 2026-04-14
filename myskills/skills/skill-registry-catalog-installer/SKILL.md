---
name: skill-registry-catalog-installer
description: Build a deduplicated catalog of installable skills from VladBigBrain/SkillRegistry, show all available sources from myskills and vendors, ask which skills to install, resolve source ambiguity with the user, and delegate installation to skill-installer.
---

# Skill Registry Catalog Installer

Use this skill when the user wants to browse, choose, and install skills from the GitHub repository `VladBigBrain/SkillRegistry`.

This skill is a catalog and routing layer. It does not copy files directly. It must delegate installation to `skill-installer`.

## Source Of Truth

Use the GitHub repository:

- repo: `VladBigBrain/SkillRegistry`
- default ref: `main`

Search only these repository roots:

- `myskills/skills`
- `vendors/skills`

Only treat a directory as installable when it contains `SKILL.md`.

## Required Behavior

1. Discover skills from the GitHub repository, not from ad hoc local guesses.
2. Parse each `SKILL.md` and extract:
   - `name`
   - `description`
3. Build a deduplicated catalog keyed by skill name.
4. For each deduplicated skill, keep every available source.
5. Show the user:
   - the unique skill name
   - every matching source
   - where the source comes from
   - the relative repository path
   - the description when available
6. Ask the user which skills to install.
7. If a selected skill has multiple sources, ask the user which source to use.
8. Delegate each confirmed install to `skill-installer`.

Do not silently prefer `myskills` over `vendors`, or one vendor subtree over another, when multiple sources exist.

## Catalog Shape

For each source, include:

- `source_group`: `myskills` or `vendors`
- `source_label`: a concise origin label derived from the path
- `source_path`: relative path to the skill directory
- `description`

For vendor skills, use a short origin label that helps the user distinguish source families, for example:

- `vendors/system`
- `vendors/plugins-cache/openai-curated/github`
- `vendors/tmp-plugins/plugins/gmail`

## User Interaction

Use a short conversational flow.

### When the user asks what is available

Show a deduplicated catalog and then ask:

`Which skills would you like installed?`

### When the user names skills directly

Normalize the requested names against the catalog.

If a name is missing, say so explicitly and ask for correction. Do not guess.

### When a selected skill has one source

Use it without a follow-up question.

### When a selected skill has multiple sources

Ask the user to choose the source before installation.

## Installation

After the user confirms the skill name and source, delegate installation to `skill-installer`.

Pass equivalent install inputs:

```text
--repo VladBigBrain/SkillRegistry
--path <relative-path-to-skill-directory>
--ref <ref>
```

Use `main` as the default ref unless the user explicitly requests another branch, tag, or commit.

The path must point to the skill directory, not to `SKILL.md`.

Examples:

```text
--repo VladBigBrain/SkillRegistry --path myskills/skills/brainstorming --ref main
--repo VladBigBrain/SkillRegistry --path vendors/skills/system/skill-installer --ref main
```

## Error Handling

Separate errors clearly.

### Catalog errors

Examples:

- repository unavailable
- listing failed
- `SKILL.md` could not be read

In these cases, explain the failure and stop before installation.

### Selection errors

Examples:

- requested skill name not found
- selected skill still ambiguous because source is not chosen

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
- explain available sources
- ask the user what to install
- resolve ambiguity
- delegate installation

Do not:

- install by direct filesystem copy
- edit repository structure
- merge duplicate skills
- treat subagents as installable skills without a real skill directory

## Completion

After successful installation, tell the user:

`Restart Codex to pick up new skills.`
