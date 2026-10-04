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


def extract_calls(file_path):
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())
    
    calls = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                if isinstance(node.func.value, ast.Name):
                    module_name = node.func.value.id
                    method_name = node.func.attr
                    line_number = node.lineno
                    calls.append({
                        "module": module_name,
                        "method": method_name,
                        "line": line_number
                    })
    
    return calls