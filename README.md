## How it works

`importguard` parses a Python file with the built-in `ast` module; it does not run the file being checked. This prototype can inspect some direct calls, such as `requests.get()`, by importing the corresponding installed package. Importing a package can run its initialization code, so use this prototype in a trusted Python environment.

An import reported as missing may simply be a valid package that is not installed in the current environment.

## Current limitations

- Supports Python files only.
- Checks a limited form of direct calls, such as `requests.get()`.
- Does not reliably understand aliases, `from ... import ...`, chained calls, or methods on objects.
- A reported missing package is not proof that the package name is hallucinated.