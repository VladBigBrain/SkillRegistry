# SkillRegistry

Репозиторий скиллов для работы с Codex от OpenAI.

Здесь хранятся доменно-организованные skills, agents, runtime-конфигурации и заготовки для workflows, schemas и evals, используемые для работы и расширения локального реестра Codex.

Пользовательские skills и связанные subagents вынесены в отдельный namespace `myskills/`.
Для `brainstorming` внутри `myskills` сохранён совместимый `.codex`-путь.
Vendor-артефакты вынесены в отдельный namespace `vendors/`, чтобы они не конфликтовали с локальными доменными skills и их runtime-структурой.
