import ast

def extract_imports(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    return imports


def _resolve_chain(attribute_node):
    attrs = []
    current = attribute_node

    while isinstance(current, ast.Attribute):
        attrs.append(current.attr)
        current = current.value

    if isinstance(current, ast.Name):
        attrs.reverse()
        return current.id, attrs

    return None, None


def extract_calls(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
            root, attrs = _resolve_chain(node.func)
            if root is not None:
                calls.append({
                    "module": root,
                    "attrs": attrs,
                    "method": attrs[-1],
                    "line": node.lineno
                })
    return calls