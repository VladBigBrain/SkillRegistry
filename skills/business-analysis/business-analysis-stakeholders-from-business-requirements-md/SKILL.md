---
name: business-analysis-stakeholders-from-business-requirements-md
description: Draft or rewrite a stakeholder Markdown document from business requirements in a strict minimal format. Use when the user asks to create, refine, or format `stakeholders/index.md` for a product, module, or feature, especially when stakeholders must be derived from `BR-*` rows and must not include modules, APIs, bounded contexts, or delivery teams.
---

# Stakeholders from Business Requirements Markdown

## Goal
Produce a minimal `stakeholders/index.md` file derived from existing business requirements.

## Output Contract
- Produce exactly one H1 title in the form `# Стейкхолдеры — <context>`.
- After the title, produce exactly one Markdown table.
- Do not add extra sections unless the user explicitly asks for them.
- Derive every stakeholder from one or more existing `BR-*` rows.

## Table Schema
Use this exact schema:

```md
| Stakeholder ID | Стейкхолдер | Роль в контексте `<context>` | Ключевое ожидание | Источник |
|---|---|---|---|---|
| `SH-XXX-001` | <stakeholder> | <role> | <expectation> | `BR-XXX-001` |
```

## Inclusion Rules
- Include only real business stakeholders: people, external roles, or business-facing support roles.
- Do not include modules, bounded contexts, services, APIs, databases, queues, or technical components.
- Do not include product, delivery, or implementation teams unless the user explicitly defines them as business stakeholders.
- If the user proposes an item that is not a stakeholder, rewrite it as an integration consumer elsewhere or exclude it.

## Derivation Rules
- Start from `бизнес-требования.md`.
- Identify who is directly affected by the requirement, who depends on the result, or who uses the business outcome.
- Group multiple `BR-*` rows under one stakeholder when they describe the same business role.
- If a stakeholder cannot be traced to any `BR-*`, do not include it yet.
- If a clearly necessary stakeholder has no `BR-*` source, first refine the business requirements, then regenerate the stakeholder table.

## Writing Rules
- Keep the stakeholder name short and role-based.
- Keep the role column factual and scoped to the current context.
- Keep the expectation column business-facing and concise.
- Keep one stakeholder per row.

## Traceability Rules
- Use `SH-<CODE>-NNN`.
- Derive `<CODE>` from the business context when it is obvious, for example `ACC` for `accounts`.
- Keep numbering sequential within the file starting from `001`.
- Put one or more source `BR-*` identifiers in the `Источник` column.
- Reuse existing prefixes if the surrounding documents already define them.

## Workflow
1. Read the current `бизнес-требования.md`.
2. Filter out technical consumers and implementation actors.
3. Identify the real business stakeholders implied by the `BR-*` rows.
4. Write or rewrite `stakeholders/index.md` in the strict table format.
5. Check that every `SH-*` row traces back to at least one `BR-*` row.
6. If a stakeholder has no valid source requirement, fix the requirements first instead of guessing.

## Example
```md
# Стейкхолдеры — accounts

| Stakeholder ID | Стейкхолдер | Роль в контексте `accounts` | Ключевое ожидание | Источник |
|---|---|---|---|---|
| `SH-ACC-001` | Клиент продукта | Один раз регистрируется в продукте и затем использует единый аккаунт в `exchange` и `market`. | Пройти одну регистрацию, получить единый `account_id` и иметь доступ к своему профилю. | `BR-ACC-002`, `BR-ACC-003`, `BR-ACC-010`, `BR-ACC-012` |
| `SH-ACC-002` | Служба поддержки | Разбирает обращения пользователей, связанные с регистрацией и профилем клиента. | Видеть единый клиентский контекст и однозначно понимать, какой аккаунт используется во всём продукте. | `BR-ACC-016` |
```
