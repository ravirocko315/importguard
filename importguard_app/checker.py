import sys
import importlib.util
import importlib


def is_stdlib(module_name):
    return module_name in sys.stdlib_module_names


def is_installed(module_name):
    try:
        spec = importlib.util.find_spec(module_name)
        return spec is not None
    except (ModuleNotFoundError, ValueError):
        return False


def check_module(module_name):
    if is_stdlib(module_name):
        return "stdlib"
    if is_installed(module_name):
        return "installed"
    return "missing"


def check_method(module_name, method_name):
    try:
        module = importlib.import_module(module_name)
    except Exception:
        return None
    return hasattr(module, method_name)


def check_chain(module_name, attrs):
    try:
        obj = importlib.import_module(module_name)
    except Exception:
        return None

    for attr in attrs:
        if hasattr(obj, attr):
            obj = getattr(obj, attr)
        else:
            return False
    return True