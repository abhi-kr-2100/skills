---
name: improve-codebase
description: Randomly selects a Python file and provides a prompt to refactor it according to project or PEP 8 style guidelines. Use this skill when you want to proactively improve code quality and consistency in the codebase.
compatibility: Requires Python and uv
---

# Improve Codebase Skill

This skill helps you proactively improve the codebase by selecting a random file and providing a structured prompt to refactor it according to style guidelines.

## Workflow

1.  **Run the improvement script:**
    Use `uv run` to execute the selection script. This script will randomly select a Python file, locate the relevant style guidelines, and generate a prompt for you to follow.

    ```bash
    uv run skills/improve-codebase/scripts/improve_codebase.py
    ```

2.  **Follow the generated prompt:**
    The script outputs a "DIAGNOSTICS" section followed by a prompt. You should follow the instructions in the generated prompt exactly.

3.  **Refactor or leave unchanged:**
    If the selected file violates the style guidelines, apply the necessary changes. If the file already adheres to the guidelines, state that no changes are needed.

## Style Guide Discovery

The skill follows this priority for finding style guidelines:
1.  Searches for a `coding-guidelines/python/` directory anywhere in the project and uses all files within it.
2.  If not found, it falls back to an internal PEP 8 summary located at `skills/improve-codebase/assets/guides/python/pep8.md`.

## Scripts

- `scripts/improve_codebase.py`: The main script that performs file selection and prompt generation.
