![Run Tests](https://github.com/ravirocko315/importguard/actions/workflows/test.yml/badge.svg)

# importguard

Catch AI-hallucinated imports and function calls **before you run the code**.

LLMs like ChatGPT and Copilot often generate code that *looks* correct but calls functions or imports packages that don't actually exist. `importguard` scans your Python file and verifies every import and function call against what's actually installed — no guessing, no hardcoded lists.

![demo](demo.gif)

## Example
...