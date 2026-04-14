---
name: obsidian-vault-patcher
description: Use when applying an approved Obsidian integration, theory, map, note, or linking plan back to vault markdown files with explicit safety boundaries
---

# Vault Patcher

## Goal
Apply approved structural changes to vault markdown files and report the result.

## Input
- Approved plan
- Target files
- Optional link changes

## Rules
1. Only apply approved changes.
2. Create notes, update notes, and add wikilinks only when the plan explicitly calls for them.
3. Do not merge unrelated notes.
4. Do not rewrite unrelated content.
5. Return a concise patch result summary after mutation.

## Output format

```md
# Vault Patch Result: {{topic}}

## Created
- {{path}}

## Updated
- {{path}}

## Linked
- [[{{source}}]] <-> [[{{target}}]]
```
