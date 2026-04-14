# SkillRegistry Inventory

Репозиторий очищен от vendor-артефактов и `superpowers`. Оставлен только локальный набор навыков для бизнес-требований, use case / user story и Obsidian-процесса.

## Верхний уровень

- `skills/` — сохранённые локальные skill-пакеты.
- `agents/` — локальные agent-манифесты только для BA/UC/US.
- `workflows/` — контейнер под будущие локальные workflows.
- `schemas/` — контейнер под будущие локальные schemas.
- `evals/` — контейнер под будущие локальные evals.
- `runtime/` — runtime-манифесты для сохранённых локальных агентов.

## Skills Kept

- `skills/home/business-needs-requirements-md`
- `skills/home/stakeholders-from-business-requirements-md`
- `skills/home/use-case`
- `skills/home/user-story`
- `skills/home/existing-knowledge-integrator`
- `skills/home/integration-planner`
- `skills/home/note-map-builder`
- `skills/home/notes-from-map`
- `skills/home/obsidian-agent`
- `skills/home/practice-lab-builder`
- `skills/home/theory-weaver`
- `skills/home/vault-patcher`
- `skills/home/vault-profiler`

## Agents Kept

- `agents/home/business-needs-requirements-md/agents/openai.yaml`
- `agents/home/stakeholders-from-business-requirements-md/agents/openai.yaml`
- `agents/home/use-case/agents/openai.yaml`
- `agents/home/user-story/agents/openai.yaml`

## Runtime Kept

- `runtime/home/business-needs-requirements-md/agents/openai.yaml`
- `runtime/home/stakeholders-from-business-requirements-md/agents/openai.yaml`
- `runtime/home/use-case/agents/openai.yaml`
- `runtime/home/user-story/agents/openai.yaml`

## Counts

- `skills/` — `13` skill directories, `13` files total.
- `agents/` — `4` agent directories, `4` files total.
- `runtime/` — `4` runtime manifests, `4` files total.
- `workflows/` — `1` file (`.gitkeep`).
- `schemas/` — `1` file (`.gitkeep`).
- `evals/` — `1` file (`.gitkeep`).

## Notes

- Полностью удалены `plugins-cache`, `vendor-imports`, `superpowers`, `.system` и все несогласованные локальные generic skills.
- В `workflows/`, `schemas/`, `evals/` добавлены `.gitkeep`, чтобы пустые контейнеры сохранились в git.
