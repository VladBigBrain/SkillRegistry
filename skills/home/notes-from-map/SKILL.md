---
name: notes-from-map
description: Use when turning a markdown topic map into note specs where each item becomes one note with sibling links and parent-category context
---

# Notes From Map

## Goal
Convert a topic map into note specs that preserve category context and sibling relationships.

## Input
- Markdown map with Core, Components, and Advanced sections

## Rules
1. Each map item becomes one note.
2. The note title must equal the map item.
3. All items from the same category go into links.
4. The parent category goes into context.
5. Return note specs, not explanations.

## Output format

```md
# {{note-title}}

## context
- {{parent-category}}

## links
- [[{{sibling-note}}]]

## body
- {{first-idea}}
```
