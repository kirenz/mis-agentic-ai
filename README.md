# Microsoft SQL Server with Python

This repository contains a Quarto book that walks through installing the Microsoft SQL Server ODBC driver, configuring VS Code, and connecting from Python using SQLAlchemy.

## Preview the book

```bash
quarto preview
```

or build the HTML output:

```bash
quarto render
```

## Run the sample connection script

1. Create a `.env` file with your database credentials (see `connection-settings.qmd`).
2. Install dependencies with `uv`:
   ```bash
   uv sync
   ```
3. Execute the script:
   ```bash
   uv run python connection.py
   ```

The script prints the SQL Server version and sample query results when the connection succeeds.
