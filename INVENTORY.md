# SkillRegistry Inventory

Реестр организован по двум объектам работы: `business-analysis` и `obsidian`. Каждый верхний раздел разбит по этим объектам, чтобы было проще видеть, с какой предметной областью работает конкретный артефакт.

## Верхний уровень

- `skills/` — skill-пакеты, сгруппированные по объектам.
- `agents/` — agent-манифесты, сгруппированные по объектам.
- `workflows/` — контейнеры под будущие workflow-артефакты по объектам.
- `schemas/` — контейнеры под будущие schema-артефакты по объектам.
- `evals/` — контейнеры под будущие evals по объектам.
- `runtime/` — runtime-манифесты, сгруппированные по объектам.
- `temp/` — персональный snapshot глобальных skills, вынесенный из `~/.codex/skills`.
- `myskills/` — изолированный namespace для пользовательских skills и subagents.
- `vendors/` — изолированный vendor namespace для внешних skills и subagents.

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

## MySkills

- `myskills/skills/brainstorming`
- `myskills/skills/business-discovery`
- `myskills/subagents/analyst`
- `myskills/subagents/business-discovery`
- `myskills/subagents/business-needs-requirements-md`
- `myskills/subagents/doc`
- `myskills/subagents/drawio`
- `myskills/subagents/figma`
- `myskills/subagents/figma-implement-design`
- `myskills/subagents/imagegen`
- `myskills/subagents/linear`
- `myskills/subagents/openai-docs`
- `myskills/subagents/pdf`
- `myskills/subagents/playwright`
- `myskills/subagents/reviewer`
- `myskills/subagents/screenshot`
- `myskills/subagents/spreadsheet`
- `myskills/subagents/stakeholders-from-business-requirements-md`
- `myskills/subagents/task-runner`
- `myskills/subagents/use-case`
- `myskills/subagents/user-story`

- `myskills/skills` — `2` пользовательских skill directories, `2` files `SKILL.md`.
- `myskills/subagents` — `19` пользовательских subagent directories, `19` files `agents/openai.yaml`.

## Temp

- `temp/skills` — `35` skill directories containing `SKILL.md`, это снимок прежнего глобального каталога `~/.codex/skills`.
- `temp/skills/.system` — системные personal skills, перенесённые из глобального каталога.
- `temp/skills/codex-primary-runtime` — runtime-oriented skills, перенесённые из глобального каталога.
- `temp/skills/skill-registry-catalog-installer` — личный каталогизатор, перенастроенный на `temp/skills` и plugin mirrors.

## Vendors

- `vendors/skills/system` — `5` vendor skill directories.
- `vendors/skills/superpowers` — `14` vendor skill directories.
- `vendors/skills/plugins-cache` — `59` vendor skill directories.
- `vendors/skills/tmp-plugins` — `237` vendor skill directories.
- `vendors/skills/vendor-imports` — `43` vendor skill directories.
- `vendors/subagents/system` — `5` vendor subagent manifests.
- `vendors/subagents/superpowers` — `0` nested `agents/openai.yaml` manifests, только именованные agent-ресурсы.
- `vendors/subagents/plugins-cache` — `15` vendor subagent manifests.
- `vendors/subagents/tmp-plugins` — `118` vendor subagent manifests.
- `vendors/subagents/vendor-imports` — `43` vendor subagent manifests.
- `vendors/` — `358` vendor skills и `181` vendor subagent resources суммарно.

## Notes

- Глобальный personal-каталог `~/.codex/skills` теперь может быть пустым; его рабочий snapshot сохранён в `temp/skills/`.
- Пользовательские `home` и `.codex` skill-артефакты убраны из внешнего каталога `agents` и перенесены в изолированный `myskills/`.
- `plugins-cache`, `vendor-imports`, `superpowers` и `.system` убраны из доменного ядра реестра и перенесены в изолированный `vendors/`.
- Пустые объектные контейнеры сохранены через `.gitkeep`, чтобы структура по доменам жила в git даже до появления реальных workflow/schema/eval артефактов.
