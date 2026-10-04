from importguard_app.parser import extract_imports, extract_calls
from importguard_app.checker import check_module, check_method

imports = extract_imports("sample.py")
calls = extract_calls("sample.py")

print("=== IMPORT CHECK ===")
for module in imports:
    status = check_module(module)
    print(f"{module}: {status}")

print("\n=== CALL CHECK ===")
for call in calls:
    module = call["module"]
    method = call["method"]

    if check_module(module) in ("stdlib", "installed"):
        exists = check_method(module, method)
        if exists is False:
            print(f"[HALLUCINATION] Line {call['line']}: {module}.{method}() does not exist!")
        else:
            print(f"[OK] Line {call['line']}: {module}.{method}()")
    else:
        print(f"[CANT VERIFY] Line {call['line']}: {module} is not installed")