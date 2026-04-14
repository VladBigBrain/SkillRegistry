# SkillRegistry Inventory

Реестр организован по двум объектам работы: `business-analysis` и `obsidian`. Каждый верхний раздел разбит по этим объектам, чтобы было проще видеть, с какой предметной областью работает конкретный артефакт.

## Верхний уровень

- `skills/` — skill-пакеты, сгруппированные по объектам.
- `agents/` — agent-манифесты, сгруппированные по объектам.
- `workflows/` — контейнеры под будущие workflow-артефакты по объектам.
- `schemas/` — контейнеры под будущие schema-артефакты по объектам.
- `evals/` — контейнеры под будущие evals по объектам.
- `runtime/` — runtime-манифесты, сгруппированные по объектам.

## Skills

### Business Analysis

- `skills/business-analysis/business-analysis-needs-requirements-md`
- `skills/business-analysis/business-analysis-stakeholders-from-business-requirements-md`
- `skills/business-analysis/business-analysis-use-case`
- `skills/business-analysis/business-analysis-user-story`

### Obsidian

- `skills/obsidian/obsidian-existing-knowledge-integrator`
- `skills/obsidian/obsidian-integration-planner`
- `skills/obsidian/obsidian-note-map-builder`
- `skills/obsidian/obsidian-notes-from-map`
- `skills/obsidian/obsidian-agent`
- `skills/obsidian/obsidian-practice-lab-builder`
- `skills/obsidian/obsidian-theory-weaver`
- `skills/obsidian/obsidian-vault-patcher`
- `skills/obsidian/obsidian-vault-profiler`

## Agents

### Business Analysis

- `agents/business-analysis/business-analysis-needs-requirements-md/agents/openai.yaml`
- `agents/business-analysis/business-analysis-stakeholders-from-business-requirements-md/agents/openai.yaml`
- `agents/business-analysis/business-analysis-use-case/agents/openai.yaml`
- `agents/business-analysis/business-analysis-user-story/agents/openai.yaml`

### Obsidian

- `agents/obsidian/.gitkeep`

## Runtime

### Business Analysis

- `runtime/business-analysis/business-analysis-needs-requirements-md/agents/openai.yaml`
- `runtime/business-analysis/business-analysis-stakeholders-from-business-requirements-md/agents/openai.yaml`
- `runtime/business-analysis/business-analysis-use-case/agents/openai.yaml`
- `runtime/business-analysis/business-analysis-user-story/agents/openai.yaml`

### Obsidian

- `runtime/obsidian/.gitkeep`

## Workflows

### Business Analysis

- `workflows/business-analysis/.gitkeep`

### Obsidian

- `workflows/obsidian/.gitkeep`

## Schemas

### Business Analysis

- `schemas/business-analysis/.gitkeep`

### Obsidian

- `schemas/obsidian/.gitkeep`

## Evals

### Business Analysis

- `evals/business-analysis/.gitkeep`

### Obsidian

- `evals/obsidian/.gitkeep`

## Counts

- `skills/business-analysis` — `4` skill directories, `4` files.
- `skills/obsidian` — `9` skill directories, `9` files.
- `agents/business-analysis` — `4` agent directories, `4` files.
- `agents/obsidian` — `1` placeholder file.
- `runtime/business-analysis` — `4` runtime manifests, `4` files.
- `runtime/obsidian` — `1` placeholder file.
- `workflows/` — `2` placeholder files.
- `schemas/` — `2` placeholder files.
- `evals/` — `2` placeholder files.

## Notes

- Полностью удалены `plugins-cache`, `vendor-imports`, `superpowers`, `.system` и несогласованные generic skills.
- Пустые объектные контейнеры сохранены через `.gitkeep`, чтобы структура по доменам жила в git даже до появления реальных workflow/schema/eval артефактов.
