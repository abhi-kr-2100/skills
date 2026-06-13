---
name: improve-codebase
description: Randomly selects a Python file and a single coding guideline (from a pool of language-agnostic and Python-specific rules) and provides a prompt to refactor the file accordingly. Use this skill for incremental codebase improvements.
compatibility: Requires Python and uv
---

# Improve Codebase Skill

This skill helps you proactively improve the codebase by selecting a random file and a single specific guideline to apply. This focused approach allows for incremental and precise improvements.

## Workflow

1.  **Run the improvement script:**
    Use `uv run` to execute the selection script. This script will randomly select a Python file and a single style guideline from its internal pool, then generate a prompt for you to follow.

    ```bash
    uv run skills/improve-codebase/scripts/improve_codebase.py
    ```

2.  **Follow the generated prompt:**
    The script outputs a "DIAGNOSTICS" section followed by a prompt. You should follow the instructions in the generated prompt exactly.

3.  **Refactor or leave unchanged:**
    Compare the selected file against the specific guideline provided. If the file violates the guideline, refactor it. If it already adheres to it, state that no changes are needed.

## Guideline Pool

The skill selects one random guideline from a combined pool of:
- **Common Guidelines:** Language-agnostic principles like DRY, meaningful naming, and comment quality.
- **Python Guidelines:** Python-specific style rules (PEP 8).

## Scripts

- `scripts/improve_codebase.py`: The main script that performs file selection and prompt generation.
