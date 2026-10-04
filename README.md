# importguard

Catch AI-hallucinated imports and function calls **before you run the code**.

LLMs like ChatGPT and Copilot often generate code that *looks* correct but calls functions or imports packages that don't actually exist. `importguard` scans your Python file and verifies every import and function call against what's actually installed — no guessing, no hardcoded lists.

## Example

\`\`\`python
import requests

response = requests.get("https://example.com")   # real
data = requests.get_jsonnn()                      # hallucinated
\`\`\`

\`\`\`bash
$ importguard check myfile.py

IMPORT CHECK
✓ requests: installed

CALL CHECK
✓ Line 3: requests.get()
✗ Line 4: requests.get_jsonnn() does not exist!
\`\`\`

## Install

\`\`\`bash
git clone https://github.com/YOUR_USERNAME/importguard
cd importguard
pip install -e .
\`\`\`

## Usage

\`\`\`bash
importguard check path/to/file.py
\`\`\`

## How it works

importguard parses your file using Python's built-in `ast` module (no code execution, fully safe), then checks each import against the standard library and installed packages, and verifies each method call using live introspection against the real module.

## Status

Early v0.1 — actively being built. Feedback and issues welcome.