---
name: practice-lab-builder
description: Use when converting a theory pack into interactive Obsidian-linked practice with concept coverage, scenario reasoning, relationship mapping, and wrong-answer teaching feedback
---

# Practice Lab Builder

## Goal
Turn a theory pack into an interactive practice lab with generated `html + css + js` assets and explicit teaching feedback.

## Input
- Theory Weave
- Topic
- Optional related notes from the vault

## Rules
1. Generate mixed practice, not a single quiz type.
2. Include 36 concept-check questions.
3. Include 5 to 8 scenario tasks.
4. Include 3 to 5 relationship or analogy exercises.
5. Ensure every theory chunk appears in at least 2 questions.
6. Ensure every key relationship appears in at least 1 exercise.
7. Support both instant feedback and review mode.
8. Every wrong answer must explain the correct answer, the mistake, and what to review next.
9. Output the generated file list and the vault links used.

## Output format

```md
# Practice Lab: {{topic}}

## Exercises
- concept-check
- scenario-reasoning
- relationship-mapping

## Coverage
- 36 concept-check questions
- 5 to 8 scenario tasks
- 3 to 5 relationship or analogy exercises

## Feedback Modes
- instant feedback
- review mode

## Wrong Answer Feedback
- Correct answer: {{correct-answer}}
- Why: {{reason}}
- Your mistake: {{mistake}}
- Review next: [[{{note-to-review}}]]
- Related concept: [[{{related-note}}]]

## Vault Links Used
- [[{{note}}]]

## Generated Files
- index.html
- styles.css
- app.js
```
