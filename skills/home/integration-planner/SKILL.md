---
name: integration-planner
description: Use when integrating new research into an existing Obsidian vault and deciding what to create, update, connect, prioritize, or leave as a gap
---

# Integration Planner

## Goal
Convert new research into a vault integration plan.

## Input
- Research content
- Optional vault profile
- Optional existing notes

## Rules
1. Do not write notes.
2. Answer all five planning questions: what to create, what to update, how to connect it, what to prioritize, and what is missing.
3. Work structurally, not narratively.
4. Reuse existing notes when possible.
5. Return only the integration plan.

## Output format

```md
# Integration Plan: {{topic}}

## New Notes
- [[{{new-note}}]]

## Update Existing
- [[{{existing-note}}]]

## Links
- [[{{source}}]] -> {{relation}} -> [[{{target}}]]

## Priority
1. {{priority-item}}
2. {{priority-item}}

## Gaps
- {{gap}}
```
