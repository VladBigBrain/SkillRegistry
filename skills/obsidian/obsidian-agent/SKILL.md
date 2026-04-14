---
name: obsidian-agent
description: Use when coordinating Obsidian vault work that may require profiling, research integration, existing-note integration, theory weaving, map generation, note generation, practice generation, or patching
---

# Obsidian Agent

## Goal
Route an Obsidian vault request to the narrowest next skill and return the next structured artifact to produce.

## Input
- User request
- Optional topic
- Optional source material
- Optional vault context
- Optional ready artifact such as a vault profile, integration plan, theory pack, map, or approved patch plan

## Rules
1. Select exactly one next skill.
2. Prefer the narrowest atomic skill that can complete the next step.
3. Route raw topic or raw research requests to read-only planning skills first.
4. Do not generate theory, notes, maps, or HTML directly if a downstream skill should do that work.
5. Use `obsidian-vault-patcher` only when an approved plan or approved artifact already exists and the user explicitly asks to apply it.
6. Use `obsidian-practice-lab-builder` only when a ready theory pack, map, or other learning artifact already exists.
7. Use `obsidian-note-map-builder` only when a structured integration artifact already exists.
8. Use `obsidian-notes-from-map` only when a ready markdown map already exists.
9. Return only the action plan.

## Output format

```md
# Obsidian Action Plan: {{topic}}

## Task Type
- vault-profiling | research-integration | existing-knowledge-integration | theory-weaving | map-building | note-generation | practice-building | vault-patching

## Selected Skill
- {{skill-name}}

## Required Inputs
- {{input}}

## Planned Pipeline
1. {{step}}
2. {{step}}

## Next Output
- {{artifact}}
```
