---
name: theory-weaver
description: Use when gathering vault knowledge on a topic and turning it into clear theory chunks with dependencies, relationships, metaphors, analogies, and cross-domain bridges
---

# Theory Weaver

## Goal
Turn topic knowledge from the vault into a teachable theory pack that emphasizes understanding, relationships, and analogy transfer.

## Input
- Topic
- Optional vault profile
- Optional source notes

## Rules
1. Gather knowledge from the vault before explaining.
2. Split the topic into learning chunks.
3. Explain each chunk clearly.
4. Add metaphors and analogies from the vault when they improve understanding.
5. Show dependencies, topic relationships, cross-domain bridges, and suggested Obsidian links.
6. Surface common confusions and missing foundations.

## Output format

```md
# Theory Weave: {{topic}}

## 1. Core Idea
- {{core-idea}}

## 2. Learning Order
1. {{step}}
2. {{step}}

## 3. Theory Chunks

### Chunk 1: {{chunk-name}}
**Idea**
{{idea}}

**Metaphor**
{{metaphor}}

**Analogy from Vault**
- [[{{note}}]] -> {{analogy}}

**Depends on**
- [[{{dependency}}]]

**Leads to**
- [[{{next-topic}}]]

## Topic Relationships
- [[{{source}}]] -> depends_on -> [[{{target}}]]

## Cross-Domain Bridges
- [[{{source}}]] -> analogous_to -> [[{{target}}]]

## Suggested Obsidian Links
- [[{{source}}]] <-> [[{{target}}]]

## 7. Common Confusions
- {{confusion}}

## 8. Missing Foundations
- {{foundation-gap}}
```
