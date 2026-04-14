# Skill Registry Catalog Installer Design

## Summary

Create a personal skill that catalogs installable skills from the GitHub repository `VladBigBrain/SkillRegistry`, shows the user a deduplicated list of skill names with all available sources, asks which skills to install, resolves any source ambiguity with the user, and then delegates installation to the existing `skill-installer`.

The new skill is a router and catalog layer. It does not copy files itself and does not replace `skill-installer`.

## Context

The repository no longer uses the old top-level `skills/` namespace for active local skills. The relevant installable sources are:

- `myskills/skills/**`
- `vendors/skills/**`

The existing `skill-installer` already knows how to install a skill from a GitHub repository path into `$CODEX_HOME/skills`, but it does not know how to present a custom catalog of this repository or resolve duplicate skill names across multiple sources.

## Goals

- Build a single catalog from `myskills` and `vendors`.
- Deduplicate entries by skill name.
- Show every available source for each deduplicated skill.
- Show where each source comes from.
- Ask the user which skills to install.
- Ask the user which source to use when a selected skill has multiple sources.
- Delegate actual installation to `skill-installer` using the GitHub repository as the canonical source.

## Non-Goals

- Do not install by copying directly from the local filesystem.
- Do not modify `skill-installer` core install behavior.
- Do not clean or rewrite duplicate entries inside the repository.
- Do not sync, rename, or reorganize `myskills` or `vendors`.
- Do not expose `vendors/subagents` as installable skills unless they are backed by a real skill directory containing `SKILL.md`.

## Canonical Source

The canonical source of truth is the GitHub repository:

- Repository: `VladBigBrain/SkillRegistry`
- Default ref: `main`

The catalog skill should treat GitHub as both:

- the source for discovering installable skills
- the source passed to `skill-installer` for installation

This keeps listing and installation aligned and avoids local-only drift.

## High-Level Flow

1. Query the repository for all skill directories under `myskills/skills` and `vendors/skills`.
2. Keep only directories that contain `SKILL.md`.
3. Parse each `SKILL.md` frontmatter to extract at least:
   - `name`
   - `description`
4. Group all discovered sources by skill `name`.
5. Present a deduplicated catalog to the user.
6. Ask which skills to install.
7. For each selected skill:
   - if it has one source, select it automatically
   - if it has multiple sources, ask the user to choose the source
8. Delegate installation to `skill-installer` with:
   - `--repo VladBigBrain/SkillRegistry`
   - `--path <selected-relative-path>`
   - `--ref main` unless the user explicitly requests another ref
9. Report installation results per selected skill.

## Catalog Model

The skill should build a deduplicated catalog keyed by the frontmatter `name`.

Each catalog entry should contain:

- `skill_name`
- `sources[]`

Each source entry should contain:

- `source_group`: `myskills` or `vendors`
- `source_path`: relative path inside the repository, for example `myskills/skills/brainstorming`
- `description`: frontmatter `description` when available
- `source_label`: short human-readable origin label derived from the path

Recommended `source_label` rules:

- `myskills` sources display as `myskills`
- `vendors` sources display as `vendors/<subtree>` where `<subtree>` is the shortest useful prefix that explains origin, such as:
  - `vendors/system`
  - `vendors/plugins-cache/openai-curated/github`
  - `vendors/tmp-plugins/plugins/gmail`

## Listing Behavior

The catalog shown to the user should be concise and selection-oriented.

Recommended shape:

- one deduplicated entry per skill name
- under each entry, list all sources
- for each source, show:
  - origin label
  - repository path
  - description when available

Example shape:

```text
1. brainstorming
   - myskills
     path: myskills/skills/brainstorming
     description: You MUST use this before any creative work...

2. gmail
   - vendors/plugins-cache/openai-curated/gmail
     path: vendors/skills/plugins-cache/openai-curated/gmail/<hash>/skills/gmail
     description: Manage Gmail inbox triage...
   - vendors/tmp-plugins/plugins/gmail
     path: vendors/skills/tmp-plugins/plugins/gmail/skills/gmail
     description: Manage Gmail inbox triage...
```

## User Interaction

The skill should drive a short conversational selection flow.

### Step 1: Show catalog

If the user asks what is available, or invokes the skill without naming exact skills, the skill shows the deduplicated catalog and asks:

`Which skills would you like installed?`

### Step 2: Normalize requested skills

The skill maps the user request onto catalog entries by skill name.

If a requested name is not found, the skill reports it explicitly and asks for correction instead of guessing.

### Step 3: Resolve source ambiguity

If a requested skill has a single source, the skill proceeds without another question.

If a requested skill has multiple sources, the skill must ask the user which source to use. It must not silently prefer `myskills` or `vendors`.

### Step 4: Install

After source choices are complete, the skill delegates installation to `skill-installer`.

## Delegation To Skill Installer

The new skill is responsible for producing exact install inputs, not for implementing installation mechanics.

For each selected source, it should delegate equivalent arguments to:

```text
--repo VladBigBrain/SkillRegistry
--path <relative-path>
--ref main
```

The relative path must point to the skill directory that contains `SKILL.md`, not to the markdown file itself.

Examples:

```text
--repo VladBigBrain/SkillRegistry --path myskills/skills/brainstorming --ref main
--repo VladBigBrain/SkillRegistry --path vendors/skills/system/skill-installer --ref main
```

If the user explicitly asks to install from another branch or tag, the skill may override `main` with the requested `ref`.

## Error Handling

The skill should separate errors into three categories and report them clearly.

### Catalog errors

Examples:

- GitHub repository unavailable
- source tree fetch failed
- repository path missing
- `SKILL.md` unreadable

Behavior:

- explain that catalog construction failed
- do not continue to installation

### Selection errors

Examples:

- user requested a skill name not present in the catalog
- user selected a skill with multiple sources but did not specify one

Behavior:

- identify the ambiguous or missing item
- ask the next focused question
- do not guess

### Installation errors

These come from `skill-installer`, for example:

- destination already exists in `$CODEX_HOME/skills`
- selected path is not a valid skill directory
- GitHub fetch or sparse checkout failed

Behavior:

- preserve the installer error
- report result per skill
- if multiple skills were selected, continue reporting completed installs and failed installs separately

## Boundaries

The skill is intentionally narrow:

- it catalogs
- it asks
- it resolves ambiguity
- it delegates installation

It does not:

- perform direct filesystem installation
- repair repository structure
- edit or merge duplicate skill directories
- install subagents independently of a skill package

## Testing Strategy

The first implementation should be validated against the following scenarios:

1. Catalog contains only `myskills` and `vendors` sources.
2. A skill with one source installs without a source follow-up question.
3. A skill with multiple sources triggers a source-selection question.
4. A missing skill name is rejected with a correction prompt.
5. A skill already present in `$CODEX_HOME/skills` surfaces the `skill-installer` error unchanged.
6. Mixed batch install reports partial success cleanly when one install succeeds and another fails.
7. GitHub listing and GitHub installation use the same repository and relative paths.

## Recommended Implementation Shape

The skill prompt should describe a two-phase workflow:

- discovery phase:
  - gather skills from `myskills/skills` and `vendors/skills`
  - build the deduplicated catalog
  - present the catalog and gather the user selection
- install phase:
  - resolve source ambiguity
  - hand the chosen repository paths to `skill-installer`
  - report results and remind the user to restart Codex if installation succeeds

## Final Recommendation

Implement the new personal skill as a thin GitHub-backed catalog router in front of `skill-installer`.

This approach keeps one installation mechanism, makes duplicate sources visible instead of hiding them, and matches the requested user experience:

- show available skills from `myskills` and `vendors`
- show where each skill comes from
- ask what to install
- ask which source to use when necessary
- install into the local Codex skills directory through the existing installer
