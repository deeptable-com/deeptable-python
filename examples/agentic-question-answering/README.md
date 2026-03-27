# Agentic Question Answering

This example compares three ways to answer the same spreadsheet question:

1. Directly from the original Excel workbook
2. From a DeepTable SQLite export
3. From a DeepTable CSV export folder

The same agent loop is used in each case. What changes is the tool surface:

- `excel` mode gives the model sheet-level search and range-reading tools
- `sqlite` mode gives the model a table overview plus SQL access
- `csv` mode loads the CSV folder into an in-memory SQLite database and exposes the same SQL tools

That makes it easy to compare the raw-workbook path with the structured-output path using the same question and the same model.

## Requirements

- `OPENAI_API_KEY`
- `DEEPTABLE_API_KEY` if you want to generate a fresh DeepTable structured sheet from a workbook with `convert_workbook_to_structured_sheet.py`

Install dependencies with `uv`:

```bash
uv sync
```

## Ask a question from a raw Excel workbook

```bash
uv run ask_question.py \
  --source excel \
  --excel-path /path/to/example.xlsx \
  --question "Which subscription-country pair has the highest revenue in 2025, and what cell contains that value?"
```

## Ask the same question from a DeepTable SQLite export

```bash
uv run ask_question.py \
  --source sqlite \
  --sqlite-path /path/to/example.sqlite \
  --question "Which subscription-country pair has the highest revenue in 2025, and what cell contains that value?"
```

## Ask the same question from a DeepTable CSV export

```bash
uv run ask_question.py \
  --source csv \
  --csv-dir /path/to/csv \
  --question "Which subscription-country pair has the highest revenue in 2025, and what cell contains that value?"
```

## Create a fresh DeepTable structured sheet with the DeepTable SDK

```bash
uv run convert_workbook_to_structured_sheet.py \
  --workbook-path /path/to/example.xlsx \
  --output-dir ./outputs \
  --formats sqlite csv
```

The script uploads the workbook, waits for processing to complete, downloads the SQLite database, and optionally exports a CSV folder from that SQLite database so the helper tables are preserved.

## Monorepo validation example

From this directory inside the DeepTable monorepo, these commands exercise the Acme example assets:

```bash
uv run ask_question.py \
  --source sqlite \
  --sqlite-path /workspaces/deeptable/examples/acme_subscriptions/structured_sheets_outputs/acme_subscriptions.sqlite \
  --question "Which subscription-country pair has the highest revenue in 2025, and what cell contains that value?"
```

```bash
uv run ask_question.py \
  --source csv \
  --csv-dir /workspaces/deeptable/examples/acme_subscriptions/structured_sheets_outputs/csv \
  --question "Which subscription-country pair has the highest revenue in 2025, and what cell contains that value?"
```

## Coding-agent prompt templates

If you want to compare this scripted example with a coding agent such as GitHub Copilot, Claude Code, or Codex, use the prompt templates in [AGENTS.md](./AGENTS.md).
