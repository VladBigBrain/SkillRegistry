---
name: obsidian-vault-profiler
description: Use when inspecting an Obsidian vault for a topic to identify core notes, clusters, duplicate risks, missing areas, or anchor notes before planning changes
---

# Vault Profiler

## Goal
Inspect the vault for a topic and return a structural profile before planning or writing.

## Input
- Topic or question
- Optional folder scope
- Optional list of known notes

## Rules
1. Work read-only.
2. Prefer existing notes over invented structure.
3. Identify core notes, clusters, duplicate risks, missing areas, and anchor notes.
4. Keep the output structural and concise.
5. Do not create or rewrite notes.

## Output format

```md
# Vault Profile: {{topic}}

## Core Notes
- [[{{note}}]]

## Clusters
- {{cluster}}

## Duplicate Risks
- {{risk}}

## Missing Areas
- {{gap}}

## Anchor Notes
- [[{{anchor}}]]
```
