# Vendors

Здесь лежит изолированный vendor namespace: внешние и системные skills, а также связанные с ними subagents, вынесенные из `agents`, чтобы не конфликтовать с локальным `home`-набором и доменной структурой `SkillRegistry`.

## Skills

- `vendors/skills/system` — системные skills из `skills/home/.system`
- `vendors/skills/superpowers` — superpowers skills
- `vendors/skills/plugins-cache` — skills из plugin cache
- `vendors/skills/tmp-plugins` — временные plugins и их метаданные
- `vendors/skills/vendor-imports` — vendor imports

## Subagents

- `vendors/subagents/system` — subagents для системных skills
- `vendors/subagents/superpowers` — subagents для superpowers
- `vendors/subagents/plugins-cache` — subagents из plugin cache
- `vendors/subagents/tmp-plugins` — subagents и plugin-структуры из tmp plugins
- `vendors/subagents/vendor-imports` — subagents из vendor imports

Это пространство хранится отдельно от доменных `skills/`, `agents/` и `runtime/`, поэтому vendor-артефакты не смешиваются с локальным реестром.
