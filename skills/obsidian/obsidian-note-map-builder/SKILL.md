---
name: obsidian-note-map-builder
description: Use when converting a structured integration result into a compact Obsidian topic map with Core, Components, and Advanced sections
---

# Note Map Builder

## Goal
Turn a structured plan into a small markdown topic map.

## Input
- Integration Plan or Existing Knowledge Integration
- Topic

## Rules
1. Use exactly three sections: Core, Components, Advanced.
2. Put 3 to 7 items in each section.
3. Use short names only.
4. Do not add descriptions.
5. Do not create notes.

## Output format

```md
# {{topic}}

## Core
- {{core-item}}

## Components
- {{component-item}}

## Advanced
- {{advanced-item}}
```
