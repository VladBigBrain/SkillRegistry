---
name: existing-knowledge-integrator
description: Use when reorganizing existing Obsidian notes on a topic into canonical notes, merge targets, updates, missing links, and explicit gaps
---

# Existing Knowledge Integrator

## Goal
Normalize existing topic knowledge already present in the vault without inventing unnecessary duplicates.

## Input
- Topic
- Existing notes for that topic
- Optional vault profile

## Rules
1. Work from existing notes first.
2. Identify canonical notes before suggesting new ones.
3. Show merge targets explicitly.
4. Separate missing links from true gaps.
5. Do not rewrite note bodies.

## Output format

```md
# Existing Knowledge Integration: {{topic}}

## Canonical Notes
- [[{{canonical-note}}]]

## Merge Into
- [[{{source}}]] -> [[{{target}}]]

## Update
- [[{{existing-note}}]]

## New Notes
- [[{{new-note}}]]

## Missing Links
- [[{{source}}]] -> [[{{target}}]]

## Gaps
- {{gap}}

## Priority
1. {{priority-item}}
2. {{priority-item}}
```
