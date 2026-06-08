# PEP 8 - Style Guide for Python Code (Summary)

## Indentation
- Use 4 spaces per indentation level.
- Continuation lines should align wrapped elements vertically using Python's implicit line joining inside parentheses, brackets and braces, or using a hanging indent.

## Maximum Line Length
- Limit all lines to a maximum of 79 characters.

## Binary Operators
- Should a line break before or after a binary operator? The preferred method is to break before the operator.

## Blank Lines
- Surround top-level function and class definitions with two blank lines.
- Method definitions inside a class are surrounded by a single blank line.

## Imports
- Imports should usually be on separate lines.
- Imports should be grouped in the following order:
    1. Standard library imports.
    2. Related third party imports.
    3. Local application/library specific imports.
- Absolute imports are recommended.

## String Quotes
- In Python, single-quoted strings and double-quoted strings are the same. Pick a rule and stick to it.

## Whitespace in Expressions and Statements
- Avoid extraneous whitespace in the following situations:
    - Immediately inside parentheses, brackets or braces.
    - Between a trailing comma and a following close parenthesis.
    - Immediately before a comma, semicolon, or colon.

## Naming Conventions
- Function and variable names should be lowercase, with words separated by underscores as necessary to improve readability (`snake_case`).
- Class names should normally use the `CapWords` convention.
- Constants should be written in all capital letters with underscores separating words.
