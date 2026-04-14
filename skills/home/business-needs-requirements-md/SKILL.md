---
name: business-needs-requirements-md
description: Draft or rewrite a minimal business-analysis Markdown section for a product, module, or feature. Use when the user asks to create or update `бизнес-потребность.md`, `бизнес-требования.md`, `stakeholders/index.md`, and `business/index.md` together in one consistent traceable format, especially when each file must stay short, table-driven, and stakeholder tracing must come from business requirements.
---

# Business Needs and Requirements Markdown

## Goal
Produce a consistent analysis section with four files:
- `business/бизнес-потребность.md`
- `business/бизнес-требования.md`
- `business/index.md`
- `stakeholders/index.md`

## Output Contract
- Keep each file minimal.
- Do not add extra sections unless the user explicitly asks for them.
- Keep traceability explicit from business need to business requirements and from business requirements to stakeholders.
- Prefer rewriting the target files cleanly instead of appending mixed formats.

## File Contracts

### 1. `бизнес-потребность.md`
- Produce exactly one H1 title in the form `# Бизнес-потребность — <context>`.
- After the title, produce exactly one Markdown table.
- Default to one business need per file unless the user clearly states multiple independent business needs.

Use this schema:

```md
| Trace ID | Бизнес-потребность | Обоснование |
|---|---|---|
| `BN-XXX-001` | <business need> | <why the business needs it> |
```

### 2. `бизнес-требования.md`
- Produce exactly one H1 title in the form `# Бизнес-требования — <context>`.
- After the title, produce exactly one Markdown table.
- Keep one requirement per row.

Use this schema:

```md
| Trace ID | Бизнес-требование | Источник |
|---|---|---|
| `BR-XXX-001` | <business requirement> | `BN-XXX-001` |
```

### 3. `stakeholders/index.md`
- Produce exactly one H1 title in the form `# Стейкхолдеры — <context>`.
- After the title, produce exactly one Markdown table.
- Include only real business stakeholders: people, external roles, or business-facing support roles.
- Do not include modules, bounded contexts, services, APIs, or delivery teams as stakeholders.
- Every stakeholder row must be traceable to one or more `BR-*` rows.
- If a desired stakeholder cannot be traced to existing `BR-*`, first refine `бизнес-требования.md`, then add the stakeholder.

Use this schema:

```md
| Stakeholder ID | Стейкхолдер | Роль в контексте `<context>` | Ключевое ожидание | Источник |
|---|---|---|---|---|
| `SH-XXX-001` | <stakeholder> | <role> | <expectation> | `BR-XXX-001` |
```

### 4. `business/index.md`
- Produce a short navigation file for the same `business/` directory.
- Use exactly one H1 title in the form `# Бизнес-материалы — <context>`.
- Then list the files as short bullets with links.
- Keep descriptions short and navigation-oriented.

Default shape:

```md
# Бизнес-материалы — accounts

- [Бизнес-потребность](бизнес-потребность.md) — ключевая бизнес-потребность для общего модуля `account`.
- [Бизнес-требования](бизнес-требования.md) — бизнес-требования к общему модулю `account`.
```

## Writing Rules
- Write business need at outcome level, not as an API, service, endpoint, or implementation detail.
- Write business requirements as observable business rules or expected business capabilities.
- Derive stakeholders from business requirements, not from implementation topology.
- Keep all statements concise and product-facing.
- Convert solution-shaped user phrasing into business-facing wording while preserving intent.
- Keep tables atomic: one idea per row.

## Traceability Rules
- Use `BN-<CODE>-NNN` for business needs.
- Use `BR-<CODE>-NNN` for business requirements.
- Use `SH-<CODE>-NNN` for stakeholders.
- Derive `<CODE>` from the business context when it is obvious, for example `ACC` for `accounts`.
- Keep numbering sequential within each file starting from `001`.
- In `бизнес-требования.md`, every row must point to the source `BN-*` row in the `Источник` column.
- In `stakeholders/index.md`, every row must point to one or more `BR-*` rows in the `Источник` column.
- Reuse existing prefixes if the surrounding documents already define them.

## Workflow
1. Identify the business context name for the titles and trace-code prefix.
2. Write or refine the business need table first.
3. Derive the business requirements table from that need.
4. Derive stakeholders from the resulting business requirements.
5. If a stakeholder is clearly needed but has no source `BR-*`, refine the business requirements before finalizing stakeholders.
6. Create or refresh `business/index.md` so it links to the business files.
7. Check that the wording stays minimal and that the stakeholder rows can be traced back through `BR-*` to `BN-*`.

## Example
```md
# Бизнес-потребность — accounts

| Trace ID | Бизнес-потребность | Обоснование |
|---|---|---|
| `BN-ACC-001` | Пользователь должен один раз зарегистрироваться в продукте и затем использовать единый аккаунт во всех бизнес-контекстах продукта. | Исключает повторную регистрацию в разных частях продукта и создаёт единый клиентский идентификатор. |
```

```md
# Бизнес-требования — accounts

| Trace ID | Бизнес-требование | Источник |
|---|---|---|
| `BR-ACC-001` | В продукте должен существовать единый аккаунт клиента, общий для `exchange` и `market`. | `BN-ACC-001` |
| `BR-ACC-016` | Служба поддержки должна иметь возможность однозначно идентифицировать единый аккаунт клиента при разборе обращений, связанных с регистрацией и профилем. | `BN-ACC-001` |
```

```md
# Стейкхолдеры — accounts

| Stakeholder ID | Стейкхолдер | Роль в контексте `accounts` | Ключевое ожидание | Источник |
|---|---|---|---|---|
| `SH-ACC-001` | Клиент продукта | Один раз регистрируется в продукте и затем использует единый аккаунт в `exchange` и `market`. | Пройти одну регистрацию, получить единый `account_id` и иметь доступ к своему профилю. | `BR-ACC-002`, `BR-ACC-003`, `BR-ACC-010`, `BR-ACC-012` |
| `SH-ACC-002` | Служба поддержки | Разбирает обращения пользователей, связанные с регистрацией и профилем клиента. | Видеть единый клиентский контекст и однозначно понимать, какой аккаунт используется во всём продукте. | `BR-ACC-016` |
```
